from django.views import View

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound


class MainView(View):
    def get(self, request):
        return render(request, 'tours/index.html')


class DepartureView(View):
    def get(self, request, departure):
        return render(request, 'tours/departure.html')


class TourView(View):
    def get(self, request, id):
        return render(request, 'tours/tour.html')


def custom_handler_404(request, exception):
    return HttpResponseNotFound(request, '<h1>Page not found</h1>')


def custom_handler_500(request):
    return HttpResponseNotFound(request, '<h1>Error</h1>')