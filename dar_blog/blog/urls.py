from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('main/', main, name='main'),
    path('registration/', register_user, name='registration'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('test/', show_test_page, name='test'),
    path('write_post/', write_post, name='write_post'),
    path('add_category/', add_category, name='add_category'),
    path('detail_category/<int:pk>', detail_category, name='detail_category'),
    path('show_music/', show_music, name='show_music'),
    path('analytics/', analytics, name='analytics')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

