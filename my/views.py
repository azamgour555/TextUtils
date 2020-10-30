
from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return render(request,"index.html")
def analyze(request):
    dtext=request.POST.get("text",'default')
    remp=request.POST.get("remp",'off')
    upper=request.POST.get('upper','off')
    exspace=request.POST.get('exspace','off')
    nlrem=request.POST.get('nlrem','off')

    if remp=='on':
        analyzed=''
        punc='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in dtext:
            if char not in punc:
                analyzed=analyzed + char
        dtext=analyzed


    if (upper=='on'):
        analyzed=''
        for char in dtext:
            analyzed=analyzed+char.upper()
        dtext=analyzed


    if(exspace=='on'):
        analyzed=''
        for index,char in enumerate(dtext):
            if not(dtext[index]==' ' and dtext[index+1]==' '):
                analyzed=analyzed+char


    if(nlrem=='on'):
        analyzed=''
        for char in dtext:
            if char!='\r' and char!='\n':
                analyzed=analyzed+char


    if(nlrem!='on' and exspace!='on' and upper!='on' and remp!='on'):
        pa={'purpose':'Error','analyzed_text':'Please Choose Atleast One Option'}
        return render(request, 'analyze.html', pa)




    par = {'purpose': 'Your Text Analyzed', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', par)


