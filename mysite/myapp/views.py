# myapp/views.py
from django.shortcuts import render


def data_view(request):
    return render(request, 'data.html')


def test_view(request):
    return render(request, 'test.html')


from django.shortcuts import render

# Create your views here.
