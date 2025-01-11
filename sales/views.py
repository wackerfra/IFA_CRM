from django.shortcuts import render, get_object_or_404, redirect
from .models import SalesActivity
from .forms import SalesActivityForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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