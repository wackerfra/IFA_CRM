from django.shortcuts import render, get_object_or_404, redirect
from .models import SalesActivity, HotelSeason, Hotel
from .forms import SalesActivityForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import HotelSeasonPricing
from datetime import date, datetime


import csv
@login_required
# def sales_list(request):
#     activities = SalesActivity.objects.all()  # Fetch all sales activities.
#     return render(request, 'sales/sales_list.html', {'activities': activities})
def sales_list(request):
    sales = SalesActivity.objects.all()
    return render(request, 'sales/sales_list.html', {'sales': sales})

@login_required
def sales_detail(request, pk):
    sale = get_object_or_404(SalesActivity, pk=pk)
    return render(request, 'sales/sales_detail.html', {'sale': sale})

@login_required
def sales_create(request):
    if request.method == 'POST':
        form = SalesActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_list')
    else:
        form = SalesActivityForm()
    return render(request, 'sales/sales_form.html', {'form': form})


@login_required
def sales_update(request, pk):
    activity = get_object_or_404(SalesActivity, pk=pk)
    if request.method == 'POST':
        form = SalesActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('sales_list')
    else:
        form = SalesActivityForm(instance=activity)
    return render(request, 'sales/sales_form.html', {'form': form})


@login_required
def sales_delete(request, pk):
    activity = get_object_or_404(SalesActivity, pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('sales_list')
    return render(request, 'sales/sales_confirm_delete.html', {'activity': activity})


@login_required
def export_sales_csv(request):
    sales = SalesActivity.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sales_activities.csv"'

    writer = csv.writer(response)
    writer.writerow(['Activity Date', 'Description', 'Status', 'Next Follow-up', 'Follow-up Due'])
    for sale in sales:
        writer.writerow([sale.activity_date, sale.description, sale.get_status_display(), sale.next_follow_up, sale.follow_up_due])

    return response

@login_required
def hotel_pricing_view(request, hotel_id):
    # Get the hotel or return a 404 if it doesn't exist
    hotel = get_object_or_404(Hotel, id=hotel_id)

    # Get today's date
    today = date.today()

    # Query all seasons greater than or equal to today for the hotel
    upcoming_seasons = hotel.seasons.filter(start_date__gte=today).order_by('start_date')  # Sorted by start_date

    return render(request, 'sales/hotel_pricing.html', {
        'hotel': hotel,
        'upcoming_seasons': upcoming_seasons,
    })

@login_required
def hotel_overview(request):
    # Retrieve all hotels for the dropdown filter
    hotels = Hotel.objects.all()

    # Get filters from query parameters
    selected_hotel_id = request.GET.get('hotel')  # Hotel ID from dropdown
    selected_date = request.GET.get('date')  # Date from input field

    # Start with all seasons
    filtered_seasons = HotelSeason.objects.all()

    # Apply hotel filter if selected
    if selected_hotel_id:
        filtered_seasons = filtered_seasons.filter(hotel_id=selected_hotel_id)

    # Apply date filter if provided
    if selected_date:
        try:
            filter_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            filtered_seasons = filtered_seasons.filter(start_date__lte=filter_date, end_date__gte=filter_date)
        except ValueError:
            # Handle invalid date
            pass

    context = {
        'hotels': hotels,
        'filtered_seasons': filtered_seasons,
        'selected_hotel_id': selected_hotel_id,
        'selected_date': selected_date,
    }
    return render(request, 'sales/hotel_overview.html', context)



