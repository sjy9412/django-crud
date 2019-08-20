from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/',views.create),
    path('<int:article_pk>',views.detail),
]