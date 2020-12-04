# This is my view file
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'homepage.html')

def analyzed(request):
    djinputtext=request.GET.get('inputtext','default')
    analyzed_text=""
    purpose=""

    # Removing Punctuation
    if(request.GET.get('removepunc','off') == "on"):
        purpose="Remove Punctuations"
        punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
        for char in djinputtext:
            if char  not in punctuations:
                analyzed_text=analyzed_text+char
    
    # Remove Extra Space
    elif(request.GET.get('removeextraspace','off')== "on"):
        purpose="Remove Extra Space"
        for index,char in enumerate(djinputtext):
            if char==' ' and djinputtext[index+1]==' ':
                pass
            else:
                analyzed_text=analyzed_text+char
    # Remove New Line
    elif(request.GET.get('removenewline','off') == 'on'):
        purpose="Remove New Line"
        for char in djinputtext:
            if char != "\n":
                analyzed_text=analyzed_text+char
    # Capitalize All letter
    elif(request.GET.get('fullcaps','off') == 'on'):
        purpose="Capitalize all Letter"
        for char in djinputtext:
            analyzed_text=analyzed_text+char.upper()
    # Count Number of char
    elif(request.GET.get('charcount','off') == 'on'):
        purpose="Number of char"
        counter=0
        for char in djinputtext:
            counter=counter+1
        analyzed_text="Total number of character are "+str(counter)
        
    else:
        purpose="Choose what you want to do"
    params={'purpose':purpose,'result':analyzed_text}
    return render(request,'analyzed.html',params)