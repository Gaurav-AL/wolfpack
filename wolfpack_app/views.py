from django.shortcuts import render,redirect
from .models import User,Image
from rest_framework.response import Response
from rest_framework.views import APIView
from PIL import Image as Im
from PIL import ImageOps
from .serializers import ImageUploadForm,UserSerializer
from django.conf.global_settings import MEDIA_URL

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
  
  
class LoginView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Authentication Successfull'}
        return Response(content)



    
def uploadView(request): 
    form = ImageUploadForm(request.POST, request.FILES)                                     
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
            form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

    
def display(request):
    print(Image.data)
    context={
        'data':Image.data
    }  
    return render(request,'display.html',context)


