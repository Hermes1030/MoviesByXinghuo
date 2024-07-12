from django.shortcuts import render

from PythonDemo.SparkPythondemo import UseSpark


# Create your views here.
def index(request):
    # process
    if request.method == 'GET':
        return render(request, 'index.html')
    # print(request.POST.get("content"))
    result = UseSpark(request.POST.get("content"))
    return render(request, 'index.html', {"data": result})
