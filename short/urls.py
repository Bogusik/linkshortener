from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('<str:link_hash>', views.redirector),
    path('link/<str:link>', views.link, name='link')
]
