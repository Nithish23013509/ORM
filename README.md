# Ex02 Django ORM Web Application
## Date: 05.03.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![WhatsApp Image 2024-03-05 at 11 41 09_73543bef](https://github.com/Nithish23013509/ORM/assets/149038138/9cae506a-185f-408b-9fd1-10f2fbb822f9)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
from django.db import models
from django.contrib import admin
class Text_Book(models.Model):
    Barcode=models.IntegerField(primary_key="Barcode");
    Book_Title=models.CharField(max_length=25);
    Author_Name=models.CharField(max_length=25);
    Author_email=models.EmailField();
    DoP=models.DateField();
    Pages=models.IntegerField();
class Text_BookAdmin(admin.ModelAdmin):
    list_display=("Barcode","Book_Title","Author_Name","Author_email","DoP","Pages");

from django.contrib import admin
from .models import Text_Book,Text_BookAdmin
admin.site.register(Text_Book,Text_BookAdmin)
```

## OUTPUT


![WhatsApp Image 2024-03-05 at 11 25 08_909142ca](https://github.com/Nithish23013509/ORM/assets/149038138/8ecf40fc-f57f-4b29-b925-86267c766d7f)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
