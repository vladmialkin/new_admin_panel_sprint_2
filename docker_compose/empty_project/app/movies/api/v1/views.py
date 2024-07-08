from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView
from movies.models import FilmWork
from .mixins import MoviesApiMixin


class MovieDetailView(BaseDetailView):
    model = FilmWork
    http_method_names = ['get']

    def get_queryset(self, pk):
        try:
            return FilmWork.objects.get(pk=pk)
        except FilmWork.DoesNotExist:
            return None

    def get_context_data(self, pk, **kwargs):
        movie = self.get_queryset(pk=pk)
        context = {
            'id': movie.id,
            'title': movie.title,
            'description': movie.description,
            'creation_date': movie.creation_date,
            'rating': movie.rating,
            'type': movie.type,
        }
        return context

    def get(self, request, pk):
        try:
            context = self.get_context_data(pk=pk)
            return JsonResponse({'result': context})
        except FilmWork.DoesNotExist:
            return JsonResponse({'error': 'Movie not found'}, status=404)


class MoviesListApi(MoviesApiMixin, BaseListView):
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by
        )
        context = {
            'count': paginator.count,
            "total_pages": paginator.num_pages,
            "prev": page.has_previous(),
            "next": page.has_next(),
            'results': list(queryset),
        }
        return context

    def get_queryset(self):
        return FilmWork.objects.all().prefetch_related('genres').values('pk', 'title', 'description', 'genres')
