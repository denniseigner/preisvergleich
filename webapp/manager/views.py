from django.http import HttpResponse


def index() -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")
