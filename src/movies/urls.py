from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('result/(?P<movieTitle>\w{0,50})/$', views.result)
    path('<str:movieTitle>', views.result)
]
