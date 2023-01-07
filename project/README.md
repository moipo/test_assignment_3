# test_assignment_3

Python version: 3.10


How to launch the project:

  1. run python3(py) manage.py runserver
  2. go to http://127.0.0.1:8000/get_form

Or use docker:
  ...


In order to test the app by means of the script testing/tests/test_form_api.py , you need to firstly add the following code to settings.py :

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

After that, just launch the script test_script.py from a different terminal either by pytest with a command pytest -s -v testing/tests/* , or simpy by launching the script test_form_api.py
