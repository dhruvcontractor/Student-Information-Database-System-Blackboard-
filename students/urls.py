from django.urls import path, include

from django.contrib.auth import views as auth_views
from . import views

app_name = 'students'
urlpatterns = [
    path(r'',include(tf_urls)),
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('update/<int:pk>/', views.ProfileUpdate.as_view(), name='update'),
    path('profile/', views.ProfileFormView.as_view(), name='profile'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]
