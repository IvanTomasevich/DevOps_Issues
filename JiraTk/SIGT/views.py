from django.shortcuts import render

# Create your views here.


def sigt_view(request):
    return render(request, "sigt.html", {})
