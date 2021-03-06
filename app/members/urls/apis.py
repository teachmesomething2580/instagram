from django.urls import path

from members import apis

urlpatterns = [
    path('get_user_token/', apis.AuthTokenView.as_view()),
    path('profile/', apis.ProfileView.as_view()),
    path('profile/<int:pk>/', apis.ProfileView.as_view()),
]