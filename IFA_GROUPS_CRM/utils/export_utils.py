import csv
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
import logging


def export_to_csv(queryset, fields, filename='output.csv'):
    """
    Export a Django queryset to a CSV file.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    writer = csv.writer(response)
    writer.writerow(fields)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in fields])

    return response


def export_to_pdf(template_path, context, filename='output.pdf'):
    """
    Export HTML content to a PDF file.
    """
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    try:
        template = get_template(template_path)
        html = template.render(context)
        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            logging.error("PDF generation failed")
            return HttpResponse("Error generating PDF.")
    except Exception as e:
        logging.exception("Unexpected error during PDF generation.")
        return HttpResponse("An error occurred during PDF generation.")

    return response
