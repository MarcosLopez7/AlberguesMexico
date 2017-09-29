from django.conf.urls import url

from .views import create_refuge, index, sign_in, sign_out, sign_up, CreateRefugeAPIView, CreatePostAPIView

urlpatterns = [
    url(r'^sig-up/$', sign_up, name='sign-up'),
    url(r'^sign-in/$', sign_in, name='sign-in'),
    url(r'^sign-out/$', sign_out, name='sign-out'),
    url(r'^registrar/$', create_refuge, name='create-refuge'),
    url(r'^create-refuge/$', CreateRefugeAPIView.as_view(), name='create-refuge-api'),
    url(r'^create-post/$', CreatePostAPIView.as_view(), name='create-post-api'),
    url(r'^', index, name='index'),
]
