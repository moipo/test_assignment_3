import requests
import jsonschema
from enum import Enum
import json
import pathlib
import os


SERVICE_URL = "http://127.0.0.1:8000/"

POST_SCHEMA = {
    "type": "object",
    "properties" : {
        "id":{"type": "number"},
        "title": {"type":"string"}
    },
    "required":["id"]
}

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Recieved status code is not equal to expected."
    WRONG_ELEMENT_COUNT = "Number of items is not equal to expected"


class Response:
    def  __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):

        if isinstance(self.response_json, list):
            for post in self.response_json:
                validate(post, schema)
        else:
            validate(self.response_json, schema)
        return self

    def assert_status_code(self, allowed_status_codes):
        if isinstance(allowed_status_codes, list):
            assert self.response_status in allowed_status_codes, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == allowed_status_codes, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self


def test_form_api():
    testing_dir = pathlib.Path(__file__).parent.parent.resolve()
    json_input_path = os.path.join(testing_dir,*["src", "input.json"])

    with open(json_input_path, "r") as f:
        json_input = json.load(f)
    # print(json_input)

    json_correct_ouput_path = os.path.join(testing_dir,*["src", "correct_output.json"])

    with open(json_correct_ouput_path, "r") as f:
        json_correct_output = json.load(f)
    # print(json_correct_output)

    for json_post_request, correct_response in zip(json_input["data"], json_correct_output["data"]):
        response = requests.post(url = SERVICE_URL, json = json_post_request)
        print(response.text, "  vs  ", correct_response)
        print("\n\n\n\n")

    # print(json_correct_output["data"][1])

    # response = requests.get(url = SERVICE_URL)
    # received_posts = response.json()
    # print(received_posts)
    #
    # assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT
    # r = Response(response)
    # r.assert_status_code(200).validate(POST_SCHEMA)



if __name__ == "__main__":
    print("works")
    test_form_api()
