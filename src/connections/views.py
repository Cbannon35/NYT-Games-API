from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    # print("hello ?")
    return render(request, 'home.html')

@login_required
def restricted_view(request):
    # Your view logic for authenticated users
    # return render(request, 'restricted_template.html')
    return HttpResponse("You are authenticated")

# or

def some_protected_view(request):
    if request.user.is_authenticated:
        # Your view logic for authenticated users
        return render(request, 'protected_template.html')
    else:
        # Return a forbidden response for unauthenticated users
        return HttpResponseForbidden("You don't have permission to access this page.")