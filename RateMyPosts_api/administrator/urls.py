from . import views
from django.urls import path


urlpatterns = [
    path('post', views.postfun, name='post'),

]