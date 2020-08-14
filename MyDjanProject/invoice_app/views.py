from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.


def home_page(request:HttpRequest):
    name = request.GET.get("name")
    context = {"name": name, "time": str(datetime.now())}
    return render(request, "index.html", context = context)


def ping(request:HttpRequest):
    #return HttpResponse("Hello world!")

    now = datetime.now()
    return JsonResponse({"message": "hello world"
                            , "current_time": str(now)})