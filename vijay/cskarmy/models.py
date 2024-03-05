from django.db import models
from django.contrib import admin
class text_book(models. Model):
    Barcode=models.IntegerField(primary_Key="Barcode");
    book_Title=models.charField(max_length=20);
    lesson_no=models.IntegerField();
    Author=models.charField(max_length=20);
    phone_No=models.IntegerField();
class text_bookAdmin(admin.ModelAdmin):
    list_display=("Barcode", "book_Title", "lesson_no", "Author","phone_No");