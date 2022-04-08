from django import template
from flights.models import Flights

register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[int(i/2)].date
@register.filter
def index1(indexable, i):
    return indexable[int(i/2)].time
