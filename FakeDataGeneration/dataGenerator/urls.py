from typing import ValuesView
from django.conf.urls import url
from django.urls.resolvers import URLPattern
from dataGenerator import views

urlpatterns = [
    url(r'^datagenerator/$',views.dataGeneratorApi),
    url(r'^datagenerator/([0-9]+)$',views.dataGeneratorApi),
]