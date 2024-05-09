from django.urls import path

from home import views

urlpatterns = [
    path("",views.index,name="index"),
    path("about",views.aboutus,name="aboutus"),
    path('search/', views.search_results, name='search_results'),
]
