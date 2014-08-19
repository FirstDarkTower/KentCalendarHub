from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext


def index(request):
    context = RequestContext(request)

    return render_to_response('CollabCheckout/index.html', context);
