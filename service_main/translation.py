from modeltranslation.translator import translator, TranslationOptions
from service_main.models.products import *

from service_main.models.profile import *
from service_main.models.general import *

class ChoiceTypeTranslationOptions(TranslationOptions):
    fields = ('name',)

class ChoiceTranslationOptions(TranslationOptions):
    fields = ('value',)

translator.register(ChoiceType, ChoiceTypeTranslationOptions)
translator.register(Choice, ChoiceTranslationOptions)