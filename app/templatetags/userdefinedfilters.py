from django import template

register=template.Library()

def swap(value):
    return value.swapcase()

def counting(value,arg):
    return value.count(arg)

def remove(value,arg):
    return value.replace(arg,'')

register.filter('swapping',swap)
register.filter('counting',counting)
register.filter('remove',remove)