from django.conf.urls import url
from apps.user.views import RegistroUsuario,UserAPI

urlpatterns = [
    # Examples:
    # url(r'^$', 'refugio.views.home', name='home'),
    url(r'^registrar/',RegistroUsuario.as_view(),name = 'registrar' ),
    url(r'^api',UserAPI.as_view(),name='api')
]
