from django.urls import path
from . import views

app_name = 'apriori'
urlpatterns=[
    path('', views.apriori_v , name='apriori_v'),
    ]