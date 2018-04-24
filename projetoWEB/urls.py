"""projetoWEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from loja import views as loja_views
from contatos import views as contatos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loja_views.home, name='home'),
    path('sobre/', loja_views.sobre, name='sobre'),
    #path('listaPorCategoria/<int:id>', loja_views.listaPorCategoria, name='listaPorCategoria'),
    path('perfil/', loja_views.perfilUsuario, name='perfil'),
    path('contatos/', contatos_views.contatos, name='contatos'),
    path('accounts/', include('allauth.urls')),
    url(r'^listaPorCategoria/(?P<pk>\d+)/$', loja_views.listaPorCategoria, name='listaPorCategoria')
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
