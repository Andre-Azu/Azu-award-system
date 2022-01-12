from django.urls import path
from . import views
from .views import CreateProfileView

urlpatterns=[
    path('', views.home, name="home"),
    path('signup/', views.Signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('createprofile/', CreateProfileView.as_view(), name="createprofile"),
    path('uploadproject/', views.uploadProject, name="uploadproject"),
    path('viewproect/<int:pk>/', views.viewProject, name="viewproject"),
    path('viewprofile/<int:pk>', views.viewProfile, name="viewprofile"),
] 