from django.shortcuts import render
import os
from django.http import HttpResponse



# folder_path = os.getcwd()+"/ClassCentral/templates"

# for filename in os.listdir(folder_path):
#     if filename.endswith('html'):
#         if not filename.split('.')[0].endswith('_'):
#             new_filename = filename.split(".")[0] + '_' + ".html"
#             os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))


def index(request):
    return render(request,'index.html')

def myview(request,s1):
    return render(request,request.path.replace('/','_')+'.html')

def myview2(request,s1,s2):
    return render(request,request.path.replace('/','_')+'.html')

def myview3(request,s1,s2,s3):
    return render(request,request.path.replace('/','_')+'.html')