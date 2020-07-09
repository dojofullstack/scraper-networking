from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('networking/', csrf_exempt(views.IndexNetworking), name='IndexNetworking'),
    path('api/networking/', csrf_exempt(views.Networking), name='Networking'),
    path('api/file/', csrf_exempt(views.file_csv), name='file_csv')
]
