import requests
from enum import Enum
import json
import pathlib
import os

SERVICE_URL = "http://127.0.0.1:8000/get_form"

class ErrorMessages(Enum):
    WRONG_STATUS_CODE = "Recieved status code is not equal to expected."
    WRONG_JSON = "Json output is not equal to expected"

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
            assert self.response_status in allowed_status_codes, ErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == allowed_status_codes, ErrorMessages.WRONG_STATUS_CODE.value
        return self

    def validate(self, correct_response):
        assert self.response_json == correct_response, str(self.response_json) +  ErrorMessages.WRONG_JSON.value
        return self


def test_form_api():

    testing_dir = pathlib.Path(__file__).parent.parent.resolve()

    json_input_path = os.path.join(testing_dir,*["src", "input.json"])
    with open(json_input_path, "r") as f:
        json_input = json.load(f)

    json_correct_ouput_path = os.path.join(testing_dir,*["src", "correct_output.json"])
    with open(json_correct_ouput_path, "r") as f:
        json_correct_output = json.load(f)

    for json_post_request, correct_response in zip(json_input["data"], json_correct_output["data"]):
        response = requests.post(url = SERVICE_URL, json = json_post_request)
        r = Response(response)
        r.assert_status_code(200).validate(correct_response)


if __name__ == "__main__":
    test_form_api()
    print("All test were passed")
