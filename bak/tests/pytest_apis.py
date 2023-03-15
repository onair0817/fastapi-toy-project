import json
import requests


def test_process_document():
    # Prepare the input document
    input_document = {"type": "contract", "description": "Sample Contract", "page": 1}

    # Convert the input document to a JSON string
    input_json = json.dumps(input_document)

    # Call the endpoint
    response = requests.post(
        "http://localhost:8001/document/ocr",
        data=input_json,
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200

    # Check the response
    response_json = response.json()
    assert response_json["type"] == "contract"
    assert response_json["description"] == "Sample Contract"
    assert response_json["page"] == 1
    assert "ocr" in response_json
    assert "key_value" in response_json


# import pytest
# import requests


# url = "http://localhost:8001/document/ocr"


# def test_process_document_success():
#     data = {
#         "type": "contract",
#         "description": "test contract",
#         "page": 1,
#     }

#     response = requests.post(url, json=data)
#     assert response.status_code == 200
#     response_json = response.json()
#     assert response_json["type"] == "contract"
#     assert response_json["description"] == "test contract"
#     assert response_json["page"] == 1
#     assert "ocr" in response_json
#     assert response_json["key_value"] == 1


# def test_process_document_without_description():
#     data = {
#         "type": "contract",
#         "page": 1,
#     }
#     response = requests.post(url, json=data)
#     assert response.status_code == 200
#     response_json = response.json()
#     assert response_json["type"] == "contract"
#     assert response_json["description"] is None
#     assert response_json["page"] == 1
#     assert "ocr" in response_json
#     assert response_json["key_value"] == 1


# def test_process_document_invalid_type():
#     data = {
#         "type": "invalid",
#         "description": "test invalid",
#         "page": 1,
#     }
#     response = requests.post(url, json=data)
#     assert response.status_code == 200
#     response_json = response.json()
#     assert response_json["type"] == "invalid"
#     assert response_json["description"] == "test invalid"
#     assert response_json["page"] == 1
#     assert "ocr" in response_json
#     assert response_json["key_value"] is None


# def test_process_document_missing_required_field():
#     data = {
#         "description": "test missing required field",
#         "page": 1,
#     }
#     response = client.post("/document/ocr", json=data)
#     assert response.status_code == 400


# def test_process_document_page_negative_value():
#     data = {
#         "type": "contract",
#         "description": "test negative page value",
#         "page": -1,
#     }
#     response = requests.post(url, json=data)
#     assert response.status_code == 400


# def test_process_document_page_zero_value():
#     data = {
#         "type": "contract",
#         "description": "test zero page value",
#         "page": 0,
#     }
#     response = requests.post(url, json=data)
#     assert response.status_code == 400


# def test_process_document_page_non_integer_value():
#     data = {
#         "type": "contract",
#         "description": "test non-integer page value",
#         "page": 1.5,
#     }
#     response = requests.post(url, json=data)
#     assert response.status_code == 400


# def test_process_document_missing_type():
#     data = {
#         "description": "test missing type",
#         "page": 1,
#     }
#     response = requests.post(url, json=data)
#     assert response.status_code == 400


# def test_process_document_type_not_enum_value():
#     data = {
#         "type": "not_valid_type",
#         "description": "test not valid type",
#         "page": 1,
#     }
#     response = requests.post(url, json=data)
#     assert response.status_code == 400


# def test_process_document_missing_page():
#     data = {
#         "type": "contract",
#         "description": "test missing page",
#     }
#     response = requests.post(url, json=data)
#     assert response.status_code == 400


# def test_process_document_valid():
#     data = {
#         "type": "contract",
#         "description": "test valid contract",
#         "page": 1,
#     }
#     response = requests.post(url, json=data)
#     assert response.status_code == 200
#     response_data = json.loads(response.content)
#     assert response_data["type"] == "contract"
#     assert response_data["description"] == "test valid contract"
#     assert response_data["page"] == 1
#     assert "ocr" in response_data
#     assert response_data["key_value"] == 1


# @pytest.fixture
# def document():
#     return {"type": "a", "seq": ["a", "b", "c"]}
