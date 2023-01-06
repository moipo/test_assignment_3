from rest_framework.views import APIView
from rest_framework.response import Response
from tinydb import TinyDB, Query
from .utils import get_type
import json


class FormAPIView(APIView):
    def post(self, request):
        db = TinyDB("db.json")
        print(db.all())
        Form = Query()
        data = request.data



        templates = []
        for key in data.keys():
            templates.extend(db.search(getattr(Form, f'{key}').matches("[aZ]*")))
        templates = list(frozenset(templates))

        print("TEMPLATES:" )
        for template in templates:
            print(template)
        print()
        # answers = []
        fields_set = set(data.keys())
        for template in templates:
            print(set(template.keys()) , " in ", fields_set)
            if set(template.keys()).issubset(fields_set):
                print("is_subset")
                for key in template.keys():
                    if get_type(template[key])==type(data[key]):
                        continue
                    else:
                        break
                    return Response(template)



        #performance optimization :
        # template_set = set()
        # # get all the templates with at least 1 matching name
        # for key in data.keys():
        #     template_set.update([str(i) for i in (db.search(getattr(Form, f'{key}').matches("[aZ]*")))])
        #
        #
        # print(template_set)
        #
        # for possible_template_str in template_set:
        #     possbile_template = json.loads(possible_template_str) #json
        #     for field_name, value in possible_tempate:
        #         if field_name in data.keys() and type(value)==type(data.get(field_name)):
        #             continue
        #         else:
        #             break
        #         print("answer")


                # print(field_name, value)


        # print(db.search(Form.field_name_4.matches("[aZ]*")))
        # var = "field_name_4"
        # print(db.search(getattr(Form, f'{var}').matches("[aZ]*")))
        return Response({"something":"something"})
