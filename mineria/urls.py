"""mineria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from apps.index.views import index_v
from apps.apriori.views import apriori_v
from apps.pearson.views import pearson_v
from apps.similitudes.views import similitudes_v
from apps.clustering.views import clustering_v
from apps.regresion.views import regresion_v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_v, name='index'),
    path('apriori',include('apps.apriori.urls',namespace='apriori')),
    path('pearson',pearson_v),
    path('similitudes',similitudes_v),
    path('clustering',clustering_v),
    path('regresion',regresion_v),
]
