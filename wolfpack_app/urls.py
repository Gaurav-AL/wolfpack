from django.urls import path,include
from . import views
from rest_framework_simplejwt import views as jwt_views
  
urlpatterns = [
    path('login', views.LoginView.as_view(), name ='login'),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    path('upload',views.uploadView,name='upload'),
    path('display',views.display,name ="display")
]
