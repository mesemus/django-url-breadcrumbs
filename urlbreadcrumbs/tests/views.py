# encoding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext


def simple_view(request, template):
    return render_to_response(template, {}, context_instance=RequestContext(request))


def simple_view_with_arg(request, template, pk):
    return render_to_response(template, {'pk': pk}, context_instance=RequestContext(request))
