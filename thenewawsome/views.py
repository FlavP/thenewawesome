from django.http import HttpResponse

import random

def hello_world(request):
    return HttpResponse("Hello World")

def root_page(request):
    return HttpResponse("Hello from the root page")

def random_number(request, max_rand=100):
    random_number = random.randrange(0, int(max_rand))
    msg = "Random Number Between 0 and %s : %d"