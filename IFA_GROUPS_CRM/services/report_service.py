def filter_reports(reports, report_type=None, start_date=None, end_date=None):
    """
    Filter reports based on type, start date, and end date.
    """
    if report_type:
        reports = reports.filter(report_type=report_type)
    if start_date:
        reports = reports.filter(generated_at__gte=start_date)
    if end_date:
        reports = reports.filter(generated_at__lte=end_date)
    return reports


def generate_report_description(report_type):
    """
    Generates content for different types of reports.
    """
    if report_type == 'booking_summary':
        from bookings.models import Booking
        return "\n".join(
            [
                f"Operator: {booking.operator.name}, Guests: {booking.number_of_guests}, Check-in: {booking.check_in}, Check-out: {booking.check_out}"
                for booking in Booking.objects.all()]
        )

    elif report_type == 'sales_summary':
        from sales.models import SalesActivity
        return "\n".join(
            [f"Title: {sale.title}, Operator: {sale.operator.name}, Date: {sale.activity_date}, Status: {sale.status}"
             for sale in SalesActivity.objects.all()]
        )

    return "No description available."
