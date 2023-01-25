import base64
from io import BytesIO
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.safestring import mark_safe 
from PIL import ImageOps
from PIL import Image as Im


class User(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    object = CustomUserManager()

    def __str__(self):
        return self.email

class Image(models.Model):
    title = models.CharField(max_length=20,null=False)
    photo = models.ImageField(upload_to='pics',null=False)
    data = []
    def __str__(self):
        return self.title
    
    def save(self): 
        super().save()
        temp = {}
        # create thumbnail

        img1 = Im.open(self.photo.path)
        
        img1.thumbnail((200,300))
        # creating buffer for thumbnail
        buffered_thumbnail = BytesIO()
        temp['title']= self.title+" thumbnail"
        img1.save(buffered_thumbnail, format="PNG")
        
        # conveting PIL Image to base64 string
        img_str_thumbnail = base64.b64encode(buffered_thumbnail.getvalue())
        img_base64_thumbnail = bytes("data:image/png;base64,", encoding='utf-8') + img_str_thumbnail
        img_base64_str_thumbnail = img_base64_thumbnail.decode("utf-8")
        temp['img']= img_base64_str_thumbnail
        self.data.append(temp)
        
        

        temp1 = {}
        # medium size image
        img2 = Im.open(self.photo.path)
        img2.resize((500,500))
        # creating buffer for medium
        
        buffered_medium = BytesIO()
        temp1['title']=self.title+" medium"
        img2.save(buffered_medium, format="PNG")
        # conveting PIL Image to base64 string
        img_str_medium = base64.b64encode(buffered_medium.getvalue())
        img_base64_medium = bytes("data:image/png;base64,", encoding='utf-8') + img_str_medium
        img_base64_str_medium = img_base64_medium.decode("utf-8")
        temp1['img']= img_base64_str_medium
        self.data.append(temp1)
        
        temp2 = {}
        # larger size image
        img3 = Im.open(self.photo.path)
        img3.resize((1024,768))
        
        # creating buffer for larger
        buffered_larger = BytesIO()
        temp2['title']=self.title+" larger"
        img3.save(buffered_larger, format="PNG")
        # conveting PIL Image to base64 string
        img_str_larger = base64.b64encode(buffered_larger.getvalue())
        img_base64_larger = bytes("data:image/png;base64,", encoding='utf-8') + img_str_larger
        img_base64_str_larger = img_base64_larger.decode("utf-8")
        temp2['img']= img_base64_str_larger
        self.data.append(temp2)
        
        temp3 = {}
        # grayscale Image
        # creating buffer for gray
        buffered_gray = BytesIO()
        gray = ImageOps.grayscale(img1)
        temp3['title']=self.title+" grayscale"
        gray.save(buffered_gray, format="PNG")
        # conveting PIL Image to base64 string
        img_str_grayscale = base64.b64encode(buffered_gray.getvalue())
        img_base64_grayscale = bytes("data:image/png;base64,", encoding='utf-8') + img_str_grayscale
        img_base64_str_grayscale = img_base64_grayscale.decode("utf-8")
        temp3['img']= img_base64_str_grayscale
        self.data.append(temp3)
        
        # print(img1,img2,img3,gray)
        
    
        
            
            
    
    

