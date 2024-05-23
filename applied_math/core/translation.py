from modeltranslation.translator import register, TranslationOptions

from materials.models import Manual, DiplomaThesis
from news.models import News


@register(Manual)
class ManualTranslationOptions(TranslationOptions):
    fields = ['title', 'author_surname', 'author_name', 'author_patronymic']


@register(DiplomaThesis)
class DiplomaThesisTranslationOptions(TranslationOptions):
    fields = ['title']


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ['title', 'text']
