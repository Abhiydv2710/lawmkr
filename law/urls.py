from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .views import home,category,bookmark
from .import views
urlpatterns = [
    path('',home),
    path('category/<slug:url>',category),
    path('searchbar/',views.searchbar, name="searchbar"),
    path('bookmark/', views.bookmark, name="bookmark"),

]
