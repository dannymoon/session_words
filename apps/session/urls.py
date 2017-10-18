from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'left', views.left),
    url(r'right', views.right)
]