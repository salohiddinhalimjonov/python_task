from modeltranslation.translator import translator, TranslationOptions
from apps.category.models import Category


class CategoryTranslationOptions(TranslationOptions):
    fields = ["title"]

translator.register(Category, CategoryTranslationOptions)