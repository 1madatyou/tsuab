from modeltranslation.translator import register, TranslationOptions

from .models import (
    Manual, 
    DiplomaThesis, 
    
    EducationalMaterial,
    EducationalMaterialFile,
    EducationalMaterialLink
)


@register(Manual)
class ManualTranslationOptions(TranslationOptions):
    fields = ['title', 'author_surname', 'author_name', 'author_patronymic']


@register(DiplomaThesis)
class DiplomaThesisTranslationOptions(TranslationOptions):
    fields = ['title']


@register(EducationalMaterial)
class EducationalMaterialTranslationOptions(TranslationOptions):
    fields = ['title']


@register(EducationalMaterialFile)
class EducationalMaterialFileTranslationOptions(TranslationOptions):
    fields = ['title']


@register(EducationalMaterialLink)
class EducationalMaterialLinkTranslationOptions(TranslationOptions):
    fields = ['title']