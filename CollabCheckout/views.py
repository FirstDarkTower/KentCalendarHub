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
    periods = []
    date_array = str(dateText).split("/")
    d = date(int(date_array[2]), int(date_array[0]), int(date_array[1])).isoformat()
    day_type = RoomSlot.objects.filter(date=d)[0].day_type
    print day_type
    period_0 = dict(number=1, text="Period 1")
    period_1 = dict(number=1, text="Period 1")
    period_2 = dict(number=1, text="Period 1")
    period_3 = dict(number=1, text="Period 1")
    period_4 = dict(number=1, text="Period 1")
    period_5 = dict(number=1, text="Period 1")
    period_6 = dict(number=1, text="Period 1")
    period_7 = dict(number=1, text="Period 1")
    period_8 = dict(number=1, text="Period 1")
    period_9 = dict(number=1, text="Period 1")
    period_10 = dict(number=1, text="Period 1")
    period_11 = dict(number=1, text="Period 1")
    if day_type == "A":
        periods = [1, 3, 4, 6, 7]
    elif day_type == "B":
        periods = [2, 4, 5, 7, 1]
    elif day_type == "C":
        periods = [3, 5, 6, 1, 2]
    elif day_type == "D":
        periods = [4, 6, 7, 2, 3]
    elif day_type == "E":
        periods = [5, 7, 1, 3, 4]
    elif day_type == "F":
        periods = [6, 1, 2, 4, 5]
    elif day_type == "G":
        periods = [7, 2, 3, 5, 6]
    periods.sort()
    return periods

def period_list(request):
    context = RequestContext(request)
    if request.method == "GET":
        dateText = request.GET.get('dateText')
    periods = get_periods(dateText)
    print periods
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
