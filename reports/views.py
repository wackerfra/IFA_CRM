from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required

from .models import Report
from .forms import ReportForm
from IFA_GROUPS_CRM.services.report_service import filter_reports, generate_report_description
from IFA_GROUPS_CRM.utils.export_utils import export_to_csv, export_to_pdf
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


@login_required
def admin_only_view(request):
    """
    Example view accessible only to admin users.
    """
    if not request.user.is_staff:  # Check if the user is an admin
        return HttpResponseForbidden("You do not have permission to access this page.")

    # Admin-only business logic here
    return render(request, 'admin_only_page.html')


@login_required
def normal_user_view(request):
    """
    Example view accessible to normal users (and admin users).
    """
    return render(request, 'normal_user_page.html')

@login_required
def report_list(request):
    """
    Displays a paginated and filterable list of reports.
    """
    reports = Report.objects.all()
    report_type = request.GET.get('report_type', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    page = request.GET.get('page', 1)

    # Filter reports
    reports = filter_reports(reports, report_type, start_date, end_date)

    # Paginate reports
    paginator = Paginator(reports, 10)  # 10 reports per page
    reports = paginator.get_page(page)

    return render(request, 'reports/report_list.html', {'reports': reports})


@login_required
def report_detail(request, pk):
    """
    Displays the details of a specific report with optional data filtering.
    """
    report = get_object_or_404(Report, pk=pk)
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    filtered_data = []

    # Dynamically fetch related data based on report type
    if report.report_type == 'booking_summary':
        from bookings.models import Booking  # Avoid circular import
        filtered_data = Booking.objects.all()
        if start_date:
            filtered_data = filtered_data.filter(check_in__gte=start_date)
        if end_date:
            filtered_data = filtered_data.filter(check_out__lte=end_date)

    elif report.report_type == 'sales_summary':
        from sales.models import SalesActivity  # Avoid circular import
        filtered_data = SalesActivity.objects.all()
        if start_date:
            filtered_data = filtered_data.filter(activity_date__gte=start_date)
        if end_date:
            filtered_data = filtered_data.filter(activity_date__lte=end_date)

    return render(request, 'reports/report_detail.html', {'report': report, 'filtered_data': filtered_data})


@login_required
@permission_required('reports.change_report', raise_exception=True)
def report_update(request, pk):
    """
    Updates a specific report.
    """
    report = get_object_or_404(Report, pk=pk)

    if request.method == "POST":
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm(instance=report)

    return render(request, 'reports/report_form.html', {'form': form})


@login_required
@permission_required('reports.delete_report', raise_exception=True)
def report_delete(request, pk):
    """
    Deletes a specific report.
    """
    report = get_object_or_404(Report, pk=pk)

    if request.method == "POST":
        report.delete()
        return redirect('report_list')

    return render(request, 'reports/report_confirm_delete.html', {'report': report})


@login_required
@permission_required('reports.add_report', raise_exception=True)
def report_create(request):
    """
    Creates and saves a new report based on user input.
    """
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)

            # Generate report content dynamically
            report.description = generate_report_description(report.report_type)
            report.save()

            return redirect('report_list')
    else:
        form = ReportForm()

    return render(request, 'reports/report_form.html', {'form': form})


@login_required
def report_export_csv(request):
    """
    Exports reports as a CSV file.
    """
    fields = ['name', 'report_type', 'generated_at', 'description']
    return export_to_csv(Report.objects.all(), fields, filename="reports.csv")


@login_required
def report_export_pdf(request):
    """
    Exports reports as a PDF file.
    """
    reports = Report.objects.all()
    template_path = 'reports/report_pdf_template.html'
    context = {'reports': reports}
    return export_to_pdf(template_path, context, filename="reports.pdf")
