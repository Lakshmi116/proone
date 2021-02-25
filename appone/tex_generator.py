from pathlib import Path
import os

def createTextFile(name,rollno,stream,branch,minor,college,email,iitgmail,mobileno,linkedin,education,projects,techskills,keyCourses,por,achievements):
    BASE_DIR = Path(__file__).resolve().parent.parent
    appone_dir = Path(__file__).resolve().parent
    print(BASE_DIR)
    print(appone_dir)
    base_file_path = os.path.join(BASE_DIR,"base.txt")
    test_file_path = os.path.join(BASE_DIR,"test.tex")
    print(base_file_path)
    print(test_file_path)
    readfile = open(str(base_file_path),"rt")
    writefile=open(str(test_file_path),"w")

    lines=readfile.readlines()

    #write some static code
    for i in range(0,91):
        writefile.write(lines[i])

    #Heading Dynamic Code
    #if Minor is there 
    if (minor!=""):
        writefile.write(r"\textbf{\huge "+name+r"}\\")
        writefile.write("\n")
        writefile.write(r"{Roll No. "+rollno+r"}&\href{mailto:"+email+r"}{ "+email+r"}\\")
        writefile.write("\n")
        writefile.write(r"{"+stream+r". -"+branch+r"}& Mobile : "+mobileno+r"\\")
        writefile.write("\n")
        writefile.write(r"{Minor in "+minor+r"}&\href{mailto:"+iitgmail+r"}{ "+iitgmail+r"}\\")
        writefile.write("\n")
        writefile.write(r"{"+college+r"} & \href{https://www."+linkedin+r"/}{"+linkedin+r"}")
        writefile.write("\n")
    #else
    else:
        writefile.write(r"\textbf{\huge "+name+r"}\\")
        writefile.write("\n")
        writefile.write(r"{Roll No. "+rollno+r"}&\href{mailto:"+email+r"}{ "+email+r"}\\")
        writefile.write("\n")
        writefile.write(r"{"+stream+r". -"+branch+r"}& Mobile : "+mobileno+r"\\")
        writefile.write("\n")
        writefile.write(r"{"+college+r"}&\href{mailto:"+iitgmail+r"}{ "+iitgmail+r"}\\")
        writefile.write("\n")
        writefile.write(r"{} & \href{https://www."+linkedin+r"/}{"+linkedin+r"}")
        writefile.write("\n")

    #write some static code
    for i in range(96,112):
        writefile.write(lines[i])

    #Education Dynamic code
    #education=[["d1","c1","p1","y1"],["d2","c2","p2","y2"],["d3","c3","p3","y3"]]
    for sublist in education:
        if(sublist[0]!=""):
            writefile.write(r"\hline "+sublist[0] +r"& "+sublist[1]+ r"& "+sublist[2] +r"& "+sublist[3] +r"\\")
            writefile.write("\n")
   
    #write some static code
    for i in range(115,128):
        writefile.write(lines[i])

    #Projects Dynamic code
    #projects=[["title1","club1","desc1","link1","date1"],["title2","club2","desc2","link2","date2"],["title3","club3","desc3","link3","date3"],["title4","club4","desc4","link4","date4"]]
    for sublist in projects:
        if(sublist[0]!=""):
            writefile.write(r"\resumeSubheading{"+sublist[0]+r"}{"+sublist[4]+r"}{"+sublist[1]+r"}{\href{"+sublist[3]+r"}{\textit{\small "+sublist[3]+r"   }}}")
            writefile.write("\n")
            writefile.write(r"\begin{itemize}")
            writefile.write("\n")
            writefile.write(r"\item "+sublist[2])
            writefile.write("\n")
            writefile.write(r" \end{itemize}")
            writefile.write("\n")
            writefile.write(r"\vspace{2pt}")
            writefile.write("\n")
            writefile.write("\n")
    
    #write some static code
    for i in range(151,164):
        writefile.write(lines[i])

    #Technical Skills Dynamic code
    #techskills=["pllang","webtech","dbms","os","miscell","otherskills"]
    if(techskills[0]!=""):
        writefile.write(r"\resumeSubItem{Programming Languages}{"+techskills[0]+r"}")
        writefile.write("\n")
    if(techskills[1]!=""):
        writefile.write(r"\resumeSubItem{Web Technologies}{"+techskills[1]+r"}")
        writefile.write("\n")
    if(techskills[2]!=""):
        writefile.write(r"\resumeSubItem{DBMS}{"+techskills[2]+r"}")
        writefile.write("\n")
    if(techskills[3]!=""):
        writefile.write(r"\resumeSubItem{OS}{"+techskills[3]+r"}")
        writefile.write("\n")
    if(techskills[4]!=""):
        writefile.write(r"\resumeSubItem{Miscelleneous}{"+techskills[4]+r"}")
        writefile.write("\n")
    if(techskills[5]!=""):
        writefile.write(r"\resumeSubItem{Other Skills}{"+techskills[5]+r"}")
        writefile.write("\n")
    
    #write some static code
    for i in range(170,186):
        writefile.write(lines[i])

    #Key courses Dynamic code
    # keyCourses=["ma101","webd101","cpp110"]
    for course in keyCourses:
        if(course!=""):
            writefile.write(r"\item "+course)
            writefile.write("\n")
    
    #write some static code
    for i in range(194,208):
        writefile.write(lines[i])

    #POR Dynamic code
    #por=[["title1","desc1"],["title2","desc2"],["title3","desc3"],["title4","desc4"]]
    for sublist in por:
        if(sublist[0]!=""):
            writefile.write(r"\resumeSubItem{"+sublist[0]+r"}")
            writefile.write("\n")
            writefile.write(r"{\vspace{-7pt}")
            writefile.write("\n")
            writefile.write(r"\begin{itemize}")
            writefile.write("\n")
            writefile.write(r"\item "+sublist[1])
            writefile.write("\n")
            writefile.write(r"\end{itemize} }")
            writefile.write("\n")
            writefile.write("\n")
    
    #write some static code
    for i in range(231,244):
        writefile.write(lines[i])

    #Achievements Dynamic code
    #achievements=[["title1","desc1"],["title2","desc2"],["title3","desc3"],["title4","desc4"],["title5","desc5"],["title6","desc6"]]
    for sublist in achievements:
        if(sublist[0]!=""):
            writefile.write(r"\resumeSubItem{"+sublist[0]+r"}{"+sublist[1]+r"}")
            writefile.write("\n")
    
    #write some static code
    for i in range(250,256):
        writefile.write(lines[i])


createTextFile(name="Nikitha",rollno="190102052",stream="Btech",branch="ECE",minor="CSE",college="IITG",
              email="nikithareddy@gmail.com",iitgmail="m.nikitha@iitg.ac.in",mobileno="9848670705",
              linkedin="linkedin.com/in/nikitha2309",
              education=[["d1","c1","p1","y1"],["d2","c2","p2","y2"],["","","",""]],
              projects=[["title1","club1","desc1","link1","date1"],["title2","club2","desc2","link2","date2"],["title3","club3","desc3","link3","date3"],["title4","club4","desc4","link4","date4"]],
              techskills=["pllang","webtech","dbms","os","miscell","otherskills"],
              keyCourses=["ma101","webd101","cpp110"],
              por=[["title1","desc1"],["title2","desc2"],["title3","desc3"],["title4","desc4"]],
              achievements=[["title1","desc1"],["title2","desc2"],["title3","desc3"],["title4","desc4"],["title5","desc5"],["title6","desc6"]])
