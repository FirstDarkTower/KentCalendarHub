from django.shortcuts import render, render_to_response
from django.template import RequestContext
from StudentSite.models import Calendar
from collections import OrderedDict

def index(request):
    context = RequestContext(request)
    context_list = dict(period_1_cals=Calendar.objects.filter(period=1))
    context_list["period_1_cals"] = remove_duplicates(context_list["period_1_cals"].order_by('class_title'))
    context_list["period_2_cals"] = remove_duplicates(Calendar.objects.filter(period = 2).order_by('class_title'))
    context_list["period_3_cals"] = remove_duplicates(Calendar.objects.filter(period = 3).order_by('class_title'))
    context_list["period_4_cals"] = remove_duplicates(Calendar.objects.filter(period = 4).order_by('class_title'))
    context_list["period_5_cals"] = remove_duplicates(Calendar.objects.filter(period = 5).order_by('class_title'))
    context_list["period_6_cals"] = remove_duplicates(Calendar.objects.filter(period = 6).order_by('class_title'))
    context_list["period_7_cals"] = remove_duplicates(Calendar.objects.filter(period = 7).order_by('class_title'))
    return render_to_response("StudentSite/index.html", context_list, context)

def get_teachers(class_name = "", period = 1):
    options = []
    if class_name and period:
        options = Calendar.objects.filter(class_title__istartswith=class_name, period = period )
    return options

def teacher_list(request):
    context = RequestContext(request)
    options = []
    class_name = ""
    period = 1
    if request.method == "GET":
        class_name = request.GET.get('class_name')
        period = request.GET.get('period')
    options = get_teachers(class_name, period)
    return render_to_response('StudentSite/option_list.html', {'options': options, 'field_title' : "Teacher:", 'period': period}, context)

def get_cal_key(class_name ="", period= 1, teacher_name = ""):
    key = ""
    if class_name and period and teacher_name:
        key = Calendar.objects.filter(class_title = class_name, period = period, teacher_name = teacher_name)[0].cal_id
    return key

def get_cal_id(request):
    context = RequestContext(request)
    class_name = ""
    period = 1
    teacher_name = ""
    if request.method == "GET":
        class_name = request.GET.get('class_name')
        period = request.GET.get('period')
        teacher_name = request.GET.get('teacher_name')

    key = get_cal_key(class_name, period, teacher_name)
    print "here"
    return render_to_response('StudentSite/single_box.html', {'key': key, 'field_title' : "ID:"}, context)

def remove_duplicates(list):
    new_list = []
    seen = set()
    for e in list:
        value = e.class_title
        if value not in seen:
            new_list.append(e)
            seen.add(value)

    return new_list
