from django.urls import path
from basic_api import views

urlpatterns = [
    
       path("api/", views.apiViewList),
       path("api/<int:pk>/",views.apiViewDetail),
]
