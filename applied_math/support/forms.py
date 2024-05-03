from django import forms

from .models import SupportTicket


class SupportTicketForm(forms.ModelForm):
    """Форма для модели обращения в поддержку"""
    class Meta: 
        model = SupportTicket
        fields = ['user_name', 'user_email', 'subject', 'text']