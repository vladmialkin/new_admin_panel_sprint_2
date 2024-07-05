from django.urls import path

from .views import MoviesListApi, MovieDetailView

urlpatterns = [
    path('movies/', MoviesListApi.as_view()),
    path('movies/<uuid:pk>/', MovieDetailView.as_view()),
]
