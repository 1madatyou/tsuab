from django.views import generic


class Contacts(generic.TemplateView):
    template_name = 'contacts/contacts.html'