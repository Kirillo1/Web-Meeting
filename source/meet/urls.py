from django.urls import path

from .views import index

app_name = 'meet'

urlpatterns = [
    path('', index, name='index')
]
