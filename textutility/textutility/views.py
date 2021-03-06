#i have created this file---abdul moiz
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html")
    
def analyze(request):
    #get the text
    djtext=request.GET.get('text','default')
    #check checkbox values
    removepunc = request.GET.get('removepuctuation','off')
    fullcaps= request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcount=request.GET.get('charcount','off')
   #check which check box is on
    if removepunc == "on":
        punctuation='''!@#$%^&*()_+|\{}[]:;"'<,>.?/'''
    # analyze the text
        analyzed=""
        for char in djtext:
            if char not in punctuation:
                analyzed=(analyzed+char)
        params={'purpose':'Removed punctuation', 'analyzed_text':analyzed}
        return render(request,'analyze.html', params)
    elif(fullcaps == "on"):
    # analyze the text
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'change to Uppercase', 'analyzed_text':analyzed}  
        return render(request,'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n":
                analyzed=analyzed+char
        params={'purpose':'removed new lines', 'analyzed_text':analyzed}  
        return render(request,'analyze.html', params)
    elif(extraspaceremover =="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed=analyzed+char

        params={'purpose':'removed new lines', 'analyzed_text':analyzed}  
        return render(request,'analyze.html', params)   
    elif(charcount=="on"):
        analyzed=len(djtext)
        params={'purpose':'character count', 'analyzed_text':analyzed}
        return render(request,'analyze.html', params)            
    else:
        return HttpResponse("Error")     
#def capitalizefirst(request):
    #return HttpResponse("capitalizefirst")
#def newlineremove(request):
    #return HttpResponse("newlineremove")
#def spaceremove(request):
   # return HttpResponse("spaceremove")
#def charactercount(request):
    #return HttpResponse("charactercount")                   