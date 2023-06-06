from . import views
from django.urls import path


urlpatterns = [
    path("post", views.create_post, name="post"),
    path("tag", views.tagfun, name="tag"),
    path("statistics", views.statisticsfun, name="statistics"),
    path("tagList", views.viewTags_fun, name="tagList"),
    path("getImages", views.get_images, name="getImages"),

]
