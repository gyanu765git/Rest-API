from django.urls import path
from basic_api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    
       path("api/", views.apiViewList.as_view()),
       path("api/<int:pk>/",views.apiViewDetail.as_view()),
         path('api/register/', views.RegisterAPI.as_view(), name='register'),
       path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
       path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
