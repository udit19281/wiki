from django.urls import path

from . import views
app_name="wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>",views.getpage,name="getpage"),
    path("wiki/<str:name>",views.getpage,name="getpage"),
    path("Search/",views.searchme,name="searchme"),
    path("create/",views.create,name="create"),
    
]
