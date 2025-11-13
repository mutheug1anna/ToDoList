from django import template
from dashboard.models import DashboardStat

register = template.Library()

@register.simple_tag
def total_stats():
    """Return total number of dashboard stat records."""
    return DashboardStat.objects.count()

@register.simple_tag
def total_value_sum():
    """Return the sum of all values from DashboardStat."""
    return sum(stat.value for stat in DashboardStat.objects.all())

@register.simple_tag
def latest_stat():
    """Return the most recently added stat title (or placeholder if none)."""
    latest = DashboardStat.objects.order_by('-date_created').first()
    return latest.title if latest else "No stats yet"
