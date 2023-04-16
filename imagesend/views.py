from django.shortcuts import render,redirect
from .serializers import SendImageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import SendImage
from django.contrib.auth.decorators import login_required
import time
from django.contrib.auth import logout

def home(request):
    return render(request, "imagesend/index.html")


def web_three_auth(request):
    return render(request, "imagesend/login.html")

def view_images(request):
    img_data = SendImage.objects.all()
    return render(request, "imagesend/view_images.html", {'data': img_data})


# Create your views here.
@api_view(['POST'])
def post_alert(request):
    serializer = SendImageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    else:
        return "Error: Unable to process data!"

    return Response("Sucess")

@login_required
def user_logout(request):
    time.sleep(2) # waiting for 2 sec
    logout(request) # using django.contrib.auth.logout(), It takes an HttpRequest object and has no return value
    # messages.success(request,f'You are logged out successfully') # logout success msg
    return redirect('/api/login/') # redirect to login page



