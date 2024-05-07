from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_POST


@require_POST
def delete_error_message(_: HttpRequest) -> HttpResponse:
    return HttpResponse("")
