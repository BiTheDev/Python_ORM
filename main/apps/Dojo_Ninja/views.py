from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from time import strftime
import random
from . import models
def index(request):

    return HttpResponse('Hello')