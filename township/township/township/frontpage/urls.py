from django.conf.urls import url
from . import views

app_name = 'township.frontpage'
urlpatterns = [
    url(r'^$', views.welcome, name='index'),
]