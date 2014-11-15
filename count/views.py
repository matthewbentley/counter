from django.http import HttpResponse
from count.models import Inc

# Create your views here.

def hi(request):
    try:
        inc = Inc.objects.all()[0]
        inc.number += 1
        inc.save()
    except IndexError:
        inc = Inc(number=0)
        inc.save()

    return HttpResponse(inc.number)