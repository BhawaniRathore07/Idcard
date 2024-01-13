from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index ),
    path('books/',views.books ),
    path('notes/',views.notes ),
    path('previous-year-paper/',views.previous_year_paper ),
    ]