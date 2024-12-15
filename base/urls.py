from django.urls import path
from . import views

urlpatterns = [
    # base:
    path("", views.home, name="home"),
    path("profile/<str:pk>/", views.user_profile, name="user-profile"),
    # auth:
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("signup/", views.signup_user, name="signup"),
    # rooms:
    path("room/<str:pk>/", views.room, name="room"),
    path("topics/", views.topics_page, name="topics"),
    path("activity/", views.activity_page, name="activity"),
    path("create-room/", views.create_room, name="create-room"),
    path("update-room/<str:pk>/", views.update_room, name="update-room"),
    path("delete-room/<str:pk>/", views.delete_room, name="delete-room"),
    # users:
    path("delete-message/<str:pk>/", views.delete_message, name="delete-message"),
    path("update-user/", views.update_user, name="update-user"),
]
