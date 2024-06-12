from django.shortcuts import render

# Create your views here.
def home(request):
    images, favourite_list = []
    return render(request, "home.html", {"images" : images, "favourite_list", favourite_list})
