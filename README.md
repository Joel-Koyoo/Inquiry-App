# [Django REST framework][docs]


**Awesome web-browsable Web APIs.**

Full documentation for the project is available at [https://www.django-rest-framework.org/][docs].


# HOW TO RUN THE APPLICATION

Here is how to make the appplication run on your PC


    create a virtual environment (virtualenv venv)
    pip install -r requirements.txt
    python manage.py makemigrations authentication
    python manage.py migrate authentication
    python manage.py makemigrations ReviewApp
    python manage.py migrate authentication
    python manage.py migrate 
    
That's it, we're done!

    ./manage.py runserver

You can now open the API in your browser at `http://127.0.0.1:8000/`.
