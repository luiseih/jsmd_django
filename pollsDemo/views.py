from django.http import HttpResponse


def index(request):
    return HttpResponse("hello, world. You are at the polls demo index.")
