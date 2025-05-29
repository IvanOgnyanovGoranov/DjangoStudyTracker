from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from tracker.models import Subject
from django.urls import reverse
from django.template.loader import render_to_string

MENU_ITEMS = [
    ('manage_subjects', 'Manage Subjects'),
    ('start_studying',     'Start Studying'),
    ('view_stats',     'View Stats'),
]

def home_page(request):
    # Improve this part - make it dynamic
    url1 = reverse('manage_subjects')
    url2 = reverse('start_studying')
    url3 = reverse('view_stats')

    main_manu_options = (f'<ul>'
                         f'<li><a href="{url1}">Manage Subjects</a></li>'
                         f'<li><a href="{url2}">Start Studying</a></li>'
                         f'<li><a href="{url3}">View Stats</a></li>'
                         f'</ul>')
    return HttpResponse(main_manu_options)

def home_page_redirecting_numbers(request, home_page):
    max_choice = len(MENU_ITEMS)
    if not (1 <= home_page <= max_choice):
        return HttpResponseNotFound('This number is out of range!')

    view_name, _ = MENU_ITEMS[home_page - 1]
    url = reverse(view_name)
    return HttpResponseRedirect(url)
