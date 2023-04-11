from django.urls import path

from .views import index, create_meet

app_name = 'meet'

urlpatterns = [
    path('', index, name='index'),
    path('create_meet/', create_meet, name='create_meet')
]
