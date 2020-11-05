from django.views import View
from django.shortcuts import render


class MainView(View):
    def get(self, request):
        return render(request, './tours/index.html')


class DepartureClass(View):
    def get(self, request):
        return render(request, './tours/departure.html')


class TourView(View):
    def get(self, request):
        return render(request, './tours/tour.html')
