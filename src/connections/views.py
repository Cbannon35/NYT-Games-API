from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # print("hello ?")
    return render(request, 'home.html')