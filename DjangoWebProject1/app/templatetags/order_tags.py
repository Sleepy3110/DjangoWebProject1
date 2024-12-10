from django import template

register = template.Library()

@register.filter
def sum_total_price(items):
    return sum(item.price * item.quantity for item in items)

