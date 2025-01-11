# services/report_service.py
def filter_reports(reports, report_type=None, start_date=None, end_date=None):
    if report_type:
        reports = reports.filter(report_type=report_type)
    if start_date:
        reports = reports.filter(generated_at__gte=start_date)
    if end_date:
        reports = reports.filter(generated_at__lte=end_date)
    return reports