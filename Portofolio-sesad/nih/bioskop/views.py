from django.shortcuts import render,redirect
#from django.contrib import messages
#from bioskop.models import Contact,Blogs,Internship
# Create your views here.
def home(request):
    return render(request,'home.html')



