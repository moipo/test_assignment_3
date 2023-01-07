# test_assignment_3

Python version: 3.10


How to launch the project:

  1. run python3(py) manage.py runserver
  2. go to http://127.0.0.1:8000/

Or use docker:
  ...


In order to test the app by means of the script test_script.py , you need to firstly add the following code to settings.py :

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

After that just launch the script test_script.py from a different terminal.  
