from django.urls import path
from .views import index, login, login_view, course_view
urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('courses/', course_view, name='courses'),
]
