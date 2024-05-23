from modeltranslation.translator import register, TranslationOptions

from .models import Manual, DiplomaThesis


@register(Manual)
class ManualTranslationOptions(TranslationOptions):
    fields = ['title', 'author_surname', 'author_name', 'author_patronymic']


@register(DiplomaThesis)
class DiplomaThesisTranslationOptions(TranslationOptions):
    fields = ['title']
