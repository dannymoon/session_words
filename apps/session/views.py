
from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
# Create your views here.
def index(request):
    return render(request, 'session/index.html')

def left(request):
    if request.method == "POST":
        if 'all_inputs' not in request.session:
            request.session['all_inputs'] = []
        else:
            request.session['all_inputs'] = request.session['all_inputs']
        temp = {'word':request.POST['textbox'],'color':request.POST['color'],'font':request.POST['Big'], 'time':strftime("%Y-%m-%d %H:%M:%S", gmtime())}
        request.session['all_inputs'].append(temp)
    	return redirect("/")
    else:
    	return redirect("/")

def right(request):
    print "aoijfoijfoij"
    request.session['all_inputs'] = []
    return redirect("/")