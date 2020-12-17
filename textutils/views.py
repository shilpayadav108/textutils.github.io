from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def about(request):
    return HttpResponse("about")

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    


    # print(removepunc)
    # print(djtext)
    if removepunc == "on":
        # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_-'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params = {'purpose':'Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
    # analyze the text
        # return render(request, 'analyze.html', params)


    if(fullcaps == "on"):
        # analyzed = djtext
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose':'Change to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)



    if(newlineremover == "on"):
        # analyzed = djtext
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose':'Removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)


    if(extraspaceremover == "on"):
        # analyzed = djtext
        analyzed = ""
        for index, char in enumerate(djtext):
            if  not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose':'Removed extra spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Please select any operation and try again")
    # else:
    #     return HttpResponse("Error")
    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")