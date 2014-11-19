from django.shortcuts import render, render_to_response
from django.template import RequestContext
from twisted.protocols.ftp import REQ_ACTN_ABRTD_FILE_UNAVAIL
from StudentSite.models import Calendar
from collections import OrderedDict

def index(request):
    context = RequestContext(request)
    context_list = dict(period_1_cals=Calendar.objects.filter(period=1, school="US"))
    context_list["period_1_cals"] = remove_duplicates(context_list["period_1_cals"].order_by('class_title'))
    context_list["period_2_cals"] = remove_duplicates(Calendar.objects.filter(period = 2, school="US").order_by('class_title'))
    context_list["period_3_cals"] = remove_duplicates(Calendar.objects.filter(period = 3, school="US").order_by('class_title'))
    context_list["period_4_cals"] = remove_duplicates(Calendar.objects.filter(period = 4, school="US").order_by('class_title'))
    context_list["period_5_cals"] = remove_duplicates(Calendar.objects.filter(period = 5, school="US").order_by('class_title'))
    context_list["period_6_cals"] = remove_duplicates(Calendar.objects.filter(period = 6, school="US").order_by('class_title'))
    context_list["period_7_cals"] = remove_duplicates(Calendar.objects.filter(period = 7, school="US").order_by('class_title'))
    return render_to_response("StudentSite/index.html", context_list, context)

def get_teachers(class_name = "", period = 1):
    options = []
    if class_name and period:
        options = Calendar.objects.filter(class_title=class_name, period = period )
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
    id = "period"+period+"teacher"
    if class_name.find("6th") > -1:
        sixth_class = class_name.split("6th ")[1].lower();
        if sixth_class == "science" or sixth_class == 'math':
            id = sixth_class +"teacher"
        elif sixth_class == 'language arts':
            id = 'langartsteacher'
        else:
            id = 'socstudteacher'
    return render_to_response('StudentSite/option_list.html', {'options': options, 'field_title' : "Teacher:", 'id': id}, context)

def get_cal_key(class_name ="", period= 1, teacher_name = ""):
    key = ""
    if class_name and period and teacher_name:
        key = Calendar.objects.filter(class_title = class_name, period = period, teacher_name = teacher_name)[0].cal_id
    elif class_name and period == "8":
        key = Calendar.objects.filter(class_title = class_name, period = period)[0].cal_id
    elif class_name and period == "10":
        key = Calendar.objects.filter(class_title = class_name, period = period)[0].cal_id
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

def ms_page(request):
    context = RequestContext(request)
    context_list = dict(period_1_cals=Calendar.objects.filter(period=1, school__in=[7,8]))
    context_list["period_1_cals"] = remove_duplicates(context_list["period_1_cals"].order_by('class_title'))
    context_list["period_2_cals"] = remove_duplicates(Calendar.objects.filter(period = 2, school__in=[7, 8]).order_by('class_title'))
    context_list["period_3_cals"] = remove_duplicates(Calendar.objects.filter(period = 3, school__in=[7, 8]).order_by('class_title'))
    context_list["period_4_cals"] = remove_duplicates(Calendar.objects.filter(period = 4, school__in=[7, 8]).order_by('class_title'))
    context_list["period_5_cals"] = remove_duplicates(Calendar.objects.filter(period = 5, school__in=[7, 8]).order_by('class_title'))
    context_list["period_6_cals"] = remove_duplicates(Calendar.objects.filter(period = 6, school__in=[7, 8]).order_by('class_title'))
    return render_to_response("StudentSite/ms_page.html", context_list, context)

def sixth_page(request):
    context = RequestContext(request)
    context_list = dict(science=remove_period_duplicates(Calendar.objects.filter(class_title__contains="Science", school=6).order_by('period')))
    context_list["math"] = remove_period_duplicates(Calendar.objects.filter(class_title__contains="Math", school=6).order_by('period'))
    context_list["homeroom"] = Calendar.objects.filter(class_title__contains="Homeroom", school=6).order_by('teacher_name')
    context_list["langarts"] = remove_period_duplicates(Calendar.objects.filter(class_title__contains="Language Arts", school=6).order_by('period'))
    context_list["socstud"] = remove_period_duplicates(Calendar.objects.filter(class_title__contains="Social Studies", school=6).order_by('period'))
    context_list["rotation"] = ["1", "2", "3", "4"]

    return render_to_response("StudentSite/sixth.html", context_list, context)


def remove_period_duplicates(list):
    new_list = []
    seen = set()
    for e in list:
        value = e.period
        if value not in seen:
            new_list.append(e)
            seen.add(value)

    return new_list


def get_sixth_rotations(rotation_number):
    options = []
    if rotation_number:
        options = Calendar.objects.filter(school = 6, class_title__in=["6th Latin Language Arts", "6th Physical Education", "6th Writing Skills", "6th Arts Rotation", "6th Latin"], period=rotation_number)
    return options

def sixth_rotations(request):
    context = RequestContext(request)
    options = []
    rotation = 1
    if request.method == "GET":
        rotation = request.GET.get('rotation')
    options = get_sixth_rotations(rotation)

    return render_to_response('StudentSite/sixth_rotations.html', {'options': options}, context)


def other_calendars(request):
    context = RequestContext(request)
    context_list = dict(other_cals=Calendar.objects.filter(school='other'))
    context_list["electivesyear"] = Calendar.objects.filter(school="ELEC", semester='14-15').order_by('class_title')
    context_list["electivesS1"] = Calendar.objects.filter(school="ELEC", semester='S1').order_by('class_title')
    context_list["electivesS2"] = Calendar.objects.filter(school="ELEC", semester='S2').order_by('class_title')
    return render_to_response('StudentSite/other_calendars.html', context_list, context)
