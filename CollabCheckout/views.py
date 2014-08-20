from datetime import date
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext
from CollabCheckout.forms import RoomSlotForm
from CollabCheckout.models import RoomSlot


def index(request):
    context = RequestContext(request)
    return render_to_response('CollabCheckout/index.html', context);

def get_periods(dateText = ""):
    periods = [dict(number="None", text="None")]
    date_array = str(dateText).split("/")
    d = date(int(date_array[2]), int(date_array[0]), int(date_array[1])).isoformat()
    day_type = RoomSlot.objects.filter(date=d)[0].day_type
    period_0 = dict(number=0, text="Before school")
    period_1 = dict(number=1, text="Period 1")
    period_2 = dict(number=1, text="Period 2")
    period_3 = dict(number=1, text="Period 3")
    period_4 = dict(number=1, text="Period 4")
    period_5 = dict(number=1, text="Period 5")
    period_6 = dict(number=1, text="Period 6")
    period_7 = dict(number=1, text="Period 7")
    period_8 = dict(number=1, text="After school: 3:30-4:30")
    period_9 = dict(number=1, text="After school: 4:30-5:30")
    period_10 = dict(number=1, text="First half of lunch")
    period_11 = dict(number=1, text="Second half of lunch")
    if day_type == "A":
        periods = [period_0, period_1, period_3, period_4, period_6, period_7, period_8, period_9, period_10, period_11]
    elif day_type == "B":
        periods = [period_0, period_1, period_2, period_4, period_5, period_7, period_8, period_9, period_10, period_11]
    elif day_type == "C":
        periods = [period_0, period_1, period_2, period_3, period_5, period_6, period_8, period_9, period_10, period_11]
    elif day_type == "D":
        periods = [period_0, period_2, period_3, period_4, period_6, period_7, period_8, period_9, period_10, period_11]
    elif day_type == "E":
        periods = [period_0, period_1, period_3, period_4, period_5, period_7, period_8, period_9, period_10, period_11]
    elif day_type == "F":
        periods = [period_0, period_1, period_2, period_4, period_5, period_6, period_8, period_9, period_10, period_11]
    elif day_type == "G":
        periods = [period_0, period_2, period_3, period_5, period_6, period_7, period_8, period_9, period_10, period_11]
    return periods

def period_list(request):
    context = RequestContext(request)
    if request.method == "GET":
        dateText = request.GET.get('dateText')
    periods = get_periods(dateText)
    context_list = dict(periods = periods)
    return render_to_response('CollabCheckout/period_list.html', context_list, context)

def checkout(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = RoomSlotForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            #form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return HttpResponse("It worked")
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = RoomSlotForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('CollabCheckout/checkout.html', {'form': form}, context)

def get_room_list(period, dateText):
    rooms = []
    date_array = str(dateText).split("/")
    d = date(int(date_array[2]), int(date_array[0]), int(date_array[1])).isoformat()
    rooms = RoomSlot.objects.filter(period=period, date=d, reserved=False)

    return rooms;


def room_list(request):
    context = RequestContext(request)
    if request.method == "GET":
        dateText = request.GET.get('dateText')
        period = request.GET.get('period')
    periods = get_room_list(period, dateText)
    context_list = dict(periods = periods)
    return render_to_response('CollabCheckout/period_list.html', context_list, context)