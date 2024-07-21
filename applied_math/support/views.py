from django.http import HttpResponse
from django.views.generic import FormView, TemplateView

from .forms import SupportTicketForm


class Support(FormView):
    template_name = "support/support.html"
    form_class = SupportTicketForm
    success_url = "done"

    def form_valid(self, form) -> HttpResponse:
        form.save()
        return super().form_valid(form)


class SupportDone(TemplateView):
    template_name = "support/support_done.html"
