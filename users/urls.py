from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from article import urls as article_detail

urlpatterns = [
   url(r'^dashboard/$', views.Dashboard.as_view(), name='dashboard'),
   url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
   url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
   url(r'^login/', auth_views.login, name='login'),
   url(r'^profile/$', views.Profile.as_view(), name='profile'),
   url(r'^tagging/(?P<cat>(?=.*\S).+)/$', views.Tagging.as_view(), name='tagging'),
   url(r'^article/tag/$', views.TagView.as_view(), name='tagged'),
   url(r'^article/', include(article_detail)),
   url('^', include('django.contrib.auth.urls')),
]