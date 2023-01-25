# Serializers define the API representation.
from rest_framework import  serializers
from .models import User,Image
from django import forms

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'photo']



    
    

    
