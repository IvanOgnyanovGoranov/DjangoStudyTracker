from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from tracker.models import Subject
from django.urls import reverse
from django.template.loader import render_to_string

# to be changed to CBV's (class based views)
MENU_ITEMS = [
    ('manage_subjects', 'Manage Subjects'),
    ('start_studying',     'Start Studying'),
    ('view_stats',     'View Stats'),
]

def home_page(request):
    return render(request, 'home_page.html', {'home_page_items': MENU_ITEMS})

def home_page_redirecting_numbers(request, home_page):
    max_choice = len(MENU_ITEMS)
    if not (1 <= home_page <= max_choice):
        return HttpResponseNotFound('This number is out of range!')

    view_name, _ = MENU_ITEMS[home_page - 1]
    url = reverse(view_name)
    return HttpResponseRedirect(url)
