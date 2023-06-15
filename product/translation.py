from modeltranslation.translator import translator, TranslationOptions
from .models import BaseItem

class BaseItemTranslationOptions(TranslationOptions):
    fields = '__all__'

translator.register(BaseItem, BaseItemTranslationOptions)
