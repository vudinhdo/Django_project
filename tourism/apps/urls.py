from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('destination/', views.destination, name="destination"),
    path('destination/destination_single/<int:id>/', views.dSingle, name="dSingle"),
    path('hotel/', views.hotel, name="hotel"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('blog/', views.blogs, name="blog"),
    path('blog-single/<int:blog_id>/', views.blog_single, name="blog_single"),
    path("login_view/", views.login_view, name="login_view"),
    path("register/", views.register_user, name="register_user"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout_view, name="logout"),
    path("blog/<int:blog_id>/<int:user_id>/add-comment/", views.add_Comment, name="add_Comment"),
]
