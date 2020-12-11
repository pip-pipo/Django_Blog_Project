from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path("about/",views.about, name="/about/"),
    path('contact/',views.contact, name="/contact/"),
    path('dasboard/',views.dasboard, name="/dasboard/"),
    path('login/',views.user_login, name="/login/"),
    path('signup/',views.user_signup, name="/signup/"),
    path('logout/',views.user_logout, name="/logout/"),
    path('abbnewpost/',views.addnewpost,name="/addnewpost/"),
    path('updatePost/',views.updatePost,name="/updatePost/"),
# i was i dynamic url 
# problem was url autenticated not captater 
]
