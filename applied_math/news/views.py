from typing import Any

from django.views.generic import ListView, TemplateView
from django.shortcuts import redirect
from django.core.paginator import Paginator

from .models import News, NewsComment


class NewsList(ListView):
    template_name = "news/news_list.html"
    model = News
    context_object_name = "news"
    paginate_by = 6


class NewsDetail(TemplateView):
    template_name = "news/news_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        news_pk = self.kwargs.get("pk")
        news_obj = News.objects.get(pk=news_pk)

        # comments pagination
        news_comments = (
            news_obj.comments.filter(reply_to=None)
            .select_related("user")
            .prefetch_related("replies")
        )
        paginator = Paginator(news_comments, 10)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context.update(
            {
                "n": news_obj,
                "comments": page_obj,
                "count_of_comments": news_comments.count(),
                "paginator": paginator,
            }
        )

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        user = request.user
        news_obj = context.get("n")

        if "comment" in request.POST:
            comment_text = request.POST.get("comment")
            if len(comment_text) > 0:
                NewsComment.objects.create(
                    user=user,
                    news=news_obj,
                    text=comment_text,
                )
        elif "reply" in request.POST:
            reply_text = request.POST.get("reply")
            reply_to = NewsComment.objects.get(pk=request.POST.get("comment_id"))
            if len(reply_text) > 0:
                NewsComment.objects.create(
                    user=user, news=news_obj, text=reply_text, reply_to=reply_to
                )

        return redirect("news_detail", pk=news_obj.pk)
