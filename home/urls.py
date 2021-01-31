from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name="home"),
    path('upload',views.upload,name="upload"),
    path('sellproduct',views.sellproduct,name="sellproduct"),
    path('cart/<int:pk>/', views.cart, name="cart"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('Like/',views.like_post,name="like_post"),
    path('accounts',views.accounts,name="account"),
    path('remove/<int:pk>/', views.remove, name="remove"),
    path('edit/<int:pk>/', views.edit, name="edit"),
    path('messages/<int:pk>/', views.messages, name="messages"),
    path('accountphone', views.accountphone, name="accountphone"),
    
  
     
]