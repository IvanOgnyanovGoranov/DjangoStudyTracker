from django.shortcuts import render, redirect

MENU_ITEMS = [
    ('my_subjects', 'My Subjects'),
    ('add_subject', 'Add Subject'),
]

def home_page(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home_page.html', {'home_page_items': MENU_ITEMS})
