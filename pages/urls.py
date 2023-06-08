from django.urls import path
from .views import HomeView, AboutView, homeView  # , ContactView, LoginView, LogoutView, SignUpView
from django.views.generic import RedirectView

urlpatterns = [
    # path('', RedirectView.as_view(pattern_name='home', permanent=False)),
    # path('', HomeView.as_view()),
    # path('', HomeView.as_view(), name='home'),
    path('', homeView, name='home'),
    path('about/', AboutView.as_view(), name='about'),

]
