from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScopeShip


class ArticleScopeShipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter_topics = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                counter_topics += 1

        if counter_topics == 0:
            raise ValidationError('Выберите основной раздел статьи')
        if counter_topics > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleScopeShipInline(admin.TabularInline):
    model = ArticleScopeShip
    formset = ArticleScopeShipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # list_display для контроля, какие поля отображаются на странице списка изменений администратора.
    list_display = ('title', 'published_at')

    inlines = [ArticleScopeShipInline]

    # # настроить заголовок столбца
    # def published_tag(self):
    #     return ', '.join([tag.topic for tag in self.scopes.all()[:3]])
    #
    # published_tag.short_description = 'Темы'


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass

