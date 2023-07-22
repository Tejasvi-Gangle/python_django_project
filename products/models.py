from django.db import models

# Create your models here.

class Review(models.Model):
    Name=models.CharField(max_length=300)
    Title=models.CharField(max_length=500)
    
    Description=models.TextField(max_length=10000,blank=True)
    Created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now=True)

class Contact(models.Model):
    Name=models.CharField(max_length=300)
    Mobile=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255)
    General_Enquiry=models.TextField(max_length=10000)
    Created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now=True)

