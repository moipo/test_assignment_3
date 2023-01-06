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

        templates = []
        for key in data.keys():
            for template in db.search(getattr(Form, f'{key}').matches("[aZ]*")):
                if template not in templates:
                    templates.append(template)

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
                if was_no_break: return Response(template.get("name"))

        for key,value in data.items():
            data[key] = get_type(value)
        return Response(data)
