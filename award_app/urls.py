from django.urls import path
from . import views
from .views import CreateProfileView

urlpatterns=[
    path('home', views.home, name="home"),
    path('', views.Signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.Signup, name="logout"),
    path('createprofile/', CreateProfileView.as_view(), name="createprofile"),
    path('uploadproject/', views.uploadProject, name="uploadproject"),
    path('viewproect/<int:pk>/', views.viewProject, name="viewproject"),
    path('viewprofile/<int:pk>', views.viewProfile, name="viewprofile"),
    path('searchprojects/', views.searchProject, name="search_results"),
] 