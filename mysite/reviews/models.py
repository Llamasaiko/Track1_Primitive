from __future__ import unicode_literals

from django.db import models


# class Book(models.Model):
#     HARDCOVER = 1
#     PAPERBACK = 2
#     EBOOK = 3
#     BOOK_TYPES = (
#         (HARDCOVER, 'Hardcover'),
#         (PAPERBACK, 'Paperback'),
#         (EBOOK, 'E-book'),
#     )
#     title = models.CharField(max_length=50)
#     publication_date = models.DateField(blank=True, null=True)
#     author = models.CharField(max_length=30, blank=True)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     pages = models.IntegerField(blank=True, null=True)
#     book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES, blank=True, null=True)

class Review_Entity(models.Model):
    rid = models.IntegerField(primary_key=True, serialize=False, blank=False, null=False)
#    hid = models.IntegerField(blank=False, null=True)
    hid = models.ForeignKey('Hotel_Entity', on_delete=models.CASCADE,blank=False,null=True)
    Review_Date = models.CharField(max_length=15)
    Reviewer_Nationality = models.CharField(max_length=50)
    Positive_Review = models.TextField(max_length=2000)
    Negative_Review = models.TextField(max_length=2000)
    Review_Total_Positive_Word_Counts = models.IntegerField(blank=True, null=True)
    Review_Total_Negative_Word_Counts = models.IntegerField(blank=True, null=True)
    Total_Number_of_Reviews_Reviewer_Has_Given = models.IntegerField(blank=True, null=True)
    Reviewer_Score = models.DecimalField(max_digits=3,decimal_places=1,blank=True, null=True)
    Tags = models.TextField(blank=True, null=True)
class Hotel_Entity(models.Model):
    Hotel_Name = models.CharField(max_length=100,blank=True,null=True)
    Hotel_Address = models.CharField(max_length=200,blank=True,null=True)
    lat = models.DecimalField(max_digits=10,decimal_places=7,blank=True,null=True)
    lng = models.DecimalField(max_digits=10,decimal_places=7,blank=True,null=True)
    Average_Score = models.DecimalField(max_digits=3,decimal_places=1,blank=True,null=True)
    Total_Number_of_Reviews = models.IntegerField(blank=True,null=True)
    Additional_Number_of_Scoring = models.IntegerField(blank=True,null=True)
    hid = models.IntegerField(primary_key=True,serialize=False)