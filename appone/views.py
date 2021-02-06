from django.shortcuts import render
from django_tex.shortcuts import render_to_pdf
from django_tex.core import compile_template_to_pdf
from django.shortcuts import redirect
import os

# Create your views here.
def index(request):
    index_dict = {
        'insert_me':'text in index inserted!',
    }
    if(request.method == "POST"):
        os.system("cd")
        os.system("pdflatex test.tex")
        os.system("move test.pdf ./static/pdfs")
        return redirect('/page1/')
    return render(request,'index/index.html',context =index_dict)
def page1(request):
    my_dict = {}
    return render(request,'page1/page1.html',context = my_dict)
    
def page2(request):
    page2_dict = {
        'insert_me':'text in page2 inserted!',
    }    
    return render(request,'page2/page2.html',context=page2_dict)
