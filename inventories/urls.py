from django.conf.urls import url

from .views import index, sign_up, create_refuge

urlpatterns = [
    url(r'^sig-up/$', sign_up, name='sign-up'),
    url(r'^registrar/$', create_refuge, name='create-refuge'),
    url(r'^', index, name='index'),
]
