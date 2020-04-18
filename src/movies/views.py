from django.shortcuts import render, redirect

def index(request):
    if(request.method == "POST"):
        return redirect(result, movieTitle = request.POST['movieTitle'])
    return render(request, 'index.html')

def result(request, movieTitle):
    context = {
        'title': movieTitle,
    }
    return render(request, 'result.html', context=context)
