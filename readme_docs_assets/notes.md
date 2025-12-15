# Creating a new app

To create the About app:

    Firstly, we would type: python3 manage.py startapp about.
    We will need to:
        Add view code to views.py
        Translate our ERD into code in models.py
        Add the model to the admin site in admin.py
        We will also need to create a templates/about directory and an about.html template in there
        Finally, we will need to create a urls.py file and wire up our view with a URL

When we create our new about app, we will need to do the following:

    In the settings.py file, we will need to add 'about' to the INSTALLED_APPS list.
    Import our about.urls to the project-level urls.py with a URL  called about/.
    We'll need to create an about_url variable in base.html like we did with the home_url, and add a link to the navigation section of base.html.
