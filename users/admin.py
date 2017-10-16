from django.contrib import admin
from .models import TaggedArticle as Tagged
from django.contrib.auth.admin import UserAdmin
from .models import TaggedArticle
from django.contrib.auth import get_user_model
User =  get_user_model()
admin.site.unregister(User)


class InlineTaggedArticle(admin.TabularInline):
    model = TaggedArticle


class CustomAdmin(UserAdmin):
    date_hierarchy = 'date_joined'
    inlines = [InlineTaggedArticle, ]
    list_display = list(UserAdmin.list_display) + ['totol_tagged_article']

    def totol_tagged_article(self, obj):
        return obj.tagging.all().count()

admin.site.register(User, CustomAdmin)


class TaggedArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    fields = ['category_fit', 'article', 'link', 'relevant_feedback', 'category', 'user', 'email']
    list_display = ['article_id', 'link', 'user', 'email']
    list_filter = ['user', 'email']
    model = Tagged


admin.site.register(Tagged, TaggedArticleAdmin)


