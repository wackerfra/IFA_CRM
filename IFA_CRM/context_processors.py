from datetime import datetime


def current_year(request):
    """Adds the current year to the template context."""
    return {
        'year': datetime.now().year,
    }
