from rest_framework.views import APIView
from rest_framework.response import Response
from tinydb import TinyDB, Query
from .utils import get_type
import json


class FormAPIView(APIView):
    def post(self, request):
        db = TinyDB("db.json")
        Form = Query()
        data = request.data

        #get all the templates with at least 1 same field name
        templates = []
        for key in data.keys():
            for template in db.search(getattr(Form, f'{key}').matches("[aZ]*")):
                if template not in templates:
                    templates.append(template)

        templates_that_fit = []

        #filter the templates until the appopriate one is found
        data["name"] = "some_name"
        fields_set = set(data.keys())
        for template in templates:
            if set(template.keys()).issubset(fields_set):
                was_no_break = True
                for key in template.keys():
                    if get_type(template[key])==get_type(data[key]):
                        continue
                    else:
                        was_no_break = False
                        break
                if was_no_break: templates_that_fit.append(template)

        if templates_that_fit:
            max_length = 0
            fits_the_most = None
            for template in templates_that_fit:
                if len(template) > max_length:
                    max_length = len(template)
                    fits_the_most = template
            return Response(fits_the_most.get("name"))

        del data["name"]

        #send the field types
        for key,value in data.items():
            data[key] = get_type(value)
        return Response(data)
