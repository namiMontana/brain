from django.db import models
from django.contrib.auth.models import User
from article.models import Article
from django.utils import timezone

choices = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('not sure', 'Not Sure'),
)


class TaggedArticle(models.Model):
    user = models.ForeignKey(User, related_name='tagging')
    email = models.EmailField(max_length=255)
    category_fit = models.CharField(choices=choices, max_length=255)
    article = models.ForeignKey(Article, related_name='articles')
    link = models.URLField(max_length=255,)
    relevant_feedback = models.TextField(blank=True)
    category = models.CharField(max_length=255,)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
