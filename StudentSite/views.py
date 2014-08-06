from django.shortcuts import render, render_to_response
from django.template import RequestContext
from StudentSite.models import Calendar

def index(request):
    context = RequestContext(request)
    context_list = dict(period_1_cals=Calendar.objects.filter(period=1))
    context_list["period_1_cals"] = context_list["period_1_cals"].order_by('class_title')
    context_list["period_2_cals"] = Calendar.objects.filter(period = 2).order_by('class_title')
    context_list["period_3_cals"] = Calendar.objects.filter(period = 3).order_by('class_title')
    context_list["period_4_cals"] = Calendar.objects.filter(period = 4).order_by('class_title')
    context_list["period_5_cals"] = Calendar.objects.filter(period = 5).order_by('class_title')
    context_list["period_6_cals"] = Calendar.objects.filter(period = 6).order_by('class_title')
    context_list["period_7_cals"] = Calendar.objects.filter(period = 7).order_by('class_title')

    return render_to_response("StudentSite/index.html", context_list, context)



