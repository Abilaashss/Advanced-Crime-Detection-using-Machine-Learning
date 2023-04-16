from django.urls import path, include, re_path
from .views import post_alert,home, view_images, web_three_auth, user_logout
urlpatterns = [
   path('',home, name="home"),
   path('view-images/', view_images, name="view_images"),
   path('images/', post_alert, name='post_alert'),
   path('login/' , web_three_auth, name="login"),
   path('logout/', user_logout, name="logout")
]

