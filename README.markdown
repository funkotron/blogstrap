# Blogstrap

> A simple blog engine on Django using Twitter's Bootstrap.


Use Django's admin interface to create posts, pages, tags and social profile links. All post text is in *markdown* and so the requirements include Django 1.2+ and python-markdown.  

### Installation guide 

1. Change any settings in the settings.py file including SITE_META.site
1. Run `python manage.py syncdb` to create a database.
1. Run `python manage.py runserver` to run on port 8000
1. Visit `http://localhost:8000/site-admin` in your browser
1. Create a new post / tag / social profile
1. Result
