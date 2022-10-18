from webbrowser import get
from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
def home_page(request):
    books = Book.objects.all()
    return render(request,'library/home.html', {'books':books})

def detail(request, book_id):
    book = get_object_or_404(Book,pk=book_id)
    return render(request,'library/detail.html',{'book':book})