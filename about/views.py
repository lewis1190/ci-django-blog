from django.shortcuts import render
from .models import About
from django.contrib import messages
from .forms import CollaborateRequestForm

# Create your views here.


def about_me(request):
    """
    Display the About page.

    **Template:**

    :template:`about/about.html`
    """
    about = About.objects.all().order_by("-updated_on").first()

    if request.method == "POST":
        collaborate_form = CollaborateRequestForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save(commit=True)
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )

    collaborate_form = CollaborateRequestForm()
    return render(
        request, "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        })
