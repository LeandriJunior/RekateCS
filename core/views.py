from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class HomeView(View):
    def get(self, request):
        response = {'message': 'Hello World! Saraiva é viado'}

        return JsonResponse(response, status=200, safe=False)