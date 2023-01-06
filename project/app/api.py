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
            print(set(template.keys()) , " in ", fields_set)
            if set(template.keys()).issubset(fields_set):
                print("is_subset")
                print("\n DATA TYPE COMPARISON:")
                for key in template.keys():
                    print(f"{get_type(template[key])}=={get_type(data[key])}")
                    if get_type(template[key])==get_type(data[key]):
                        continue
                    else:
                        break
                return Response(template)


        for key,value in data.items():
            data[key] = get_type(value)
        return Response(data)
