from django.urls import path
from .views import RegisterView, LoginView, ProfileView
# from .views import LogoutView # optional


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    #"unfollow/<int:user_id>/", "follow/<int:user_id>"]
]