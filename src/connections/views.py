from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

def home(request):
    # print("hello ?")
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        if request.get('username') and request.get('password'):
            # Authenticate the user
            # ...
            # Redirect to a success page.
            return HttpResponse("You are authenticated")
        else:
            # Return an 'invalid login' error message.
            return HttpResponse("Invalid login")
    elif request.method == 'GET':
        return render(request, 'login.html')

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
        return HttpResponseForbidden("You don't have permission to access this page")