from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

# to be changed to CBV's (class based views)
MENU_ITEMS = [
    ('my_subjects', 'My Subjects'),
    ('add_subject', 'Add Subject'),
]

def home_page(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home_page.html', {'home_page_items': MENU_ITEMS})
