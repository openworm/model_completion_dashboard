from __future__ import absolute_import
from __future__ import print_function
from django import template

register = template.Library()

@register.filter
def lookup(value, arg):
    print(arg)
    x,y=arg.split(',')
    print(x,y)
    # if x.isdigit() and y.isdigit():
    #     if (int(x),int(y)) in value.keys():
    #         return value[int(x),int(y)]
    # 
