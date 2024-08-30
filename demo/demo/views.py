from django.shortcuts import render, redirect, HttpResponse
from demo.middleware import MyMiddleware

import phonenumbers
from django.shortcuts import render, redirect
import re
from phonenumbers import carrier

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, "index.html")
