# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for project."""
    return render(request, 'Sign_up/index.html')
