from django.shortcuts import render
from django_tex.shortcuts import render_to_pdf
from django_tex.core import compile_template_to_pdf
from django.shortcuts import redirect
from appone.tex_generator import createTextFile
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
def index(request):
    index_dict = {
        'insert_me':'text in index inserted!',
    }
    if(request.method == "POST"):
        """
        createTextFile(name="Nikitha",rollno="190102052",stream="Btech",branch="ECE",minor="CSE",college="IITG",
              email="nikithareddy@gmail.com",iitgmail="m.nikitha@iitg.ac.in",mobileno="9848670705",
              linkedin="linkedin.com/in/nikitha2309",
              education=[["d1","c1","p1","y1"],["d2","c2","p2","y2"],["","","",""]],
              projects=[["title1","club1","desc1","link1","date1"],["title2","club2","desc2","link2","date2"],["title3","club3","desc3","link3","date3"],["title4","club4","desc4","link4","date4"]],
              techskills=["pllang","webtech","dbms","os","miscell","otherskills"],
              keyCourses=["ma101","webd101","cpp110"],
              por=[["title1","desc1"],["title2","desc2"],["title3","desc3"],["title4","desc4"]],
              achievements=[["title1","desc1"],["title2","desc2"],["title3","desc3"],["title4","desc4"],["title5","desc5"],["title6","desc6"]]) 
            """    

        #os.system("pdflatex test.tex")
        #os.system("move test.pdf ./static/pdfs")
        os.system("cd ./..")
        os.system("python new.py")
        os.system("pdflatex latexFile.tex")
        os.system("move latexFile.pdf ./static/pdfs")
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
