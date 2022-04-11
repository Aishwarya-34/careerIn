# File Name: views.py
# Description: This file handles the display of the homepage

# Imported Libraries
import os
from django.shortcuts import render, redirect
from django.conf import settings
from ast import literal_eval
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, FileResponse, Http404
from django.db import IntegrityError
from web_application.app_core.models import Resume
from web_application.app_core.forms import ResumeModelForm
from django.contrib import messages
from django.views.generic import CreateView, TemplateView, ListView
from django.urls import reverse_lazy

def homepage(request):
     return render(request, 'homepage.html', {})
 
# Resume form created here
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('resume')
        resumes_data = []

        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeModelForm
    return render(request, 'upload_resume.html',
        {'form': form})


def resume_list(request):
    resumes = Resume.objects.all()
    with open("web_application/app_core/static/myfile.txt", "r") as rf:
        internships = rf.read()

    # First get the industry user added   -> resumes[len(resumes)-1].industry

    # Second -> Call API from backend (Address = http://127.0.0.1:5000/?industry= +${}) 
    # fetch(URL)  ->
    #  Get this format = [{
        #     "company": "AIA Chicago",
        #     "link": "https://www.indeed.com/cmp/Aia-Group-Limited",
        #     "title": "All levels - product architecture + design"
        # }]
    # response.Internship
    # internships = response.Internship
    return render(request, 'resume_list.html',
        {'resumes': resumes, 'internships' : internships })

def delete_resume(request, pk):
    if request.method == 'POST':
        resume = Resume.objects.get(pk=pk)
        resume.delete()
    return redirect('resume_list')


from django.http import HttpResponse

def read_file(request):
    f = open('myfile.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")

# Set up for later, when search results have been returned
#def search_results():
    #template_name = 'search_results.html'
