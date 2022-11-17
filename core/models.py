from django.db import models


# Create your models here.
# Category, Partner, Author, Book, BookLoan
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    recommended_age = models.CharField(max_length=100, blank=False, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)


class Book(models.Model):
    name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Partner(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    dni = models.CharField(max_length=8, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(max_length=300, blank=False, null=False, default='')
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    book = models.ManyToManyField(Book, through='BookLoan', blank=True)


class BookLoan(models.Model):
    status = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
