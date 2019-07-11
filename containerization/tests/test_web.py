"""pytest tests for library"""

import base64
import json
import sys

import pytest
sys.path.append("../flask_app")

#flask app
from web import app

@pytest.fixture
def client():
    """Generic Flask application fixture"""

    app.testing = True
    return app.test_client()

@pytest.fixture
def aggregrate_client():
    """Flask application fixture that includes b64data"""

    app.testing = True
    with open("../ext/input.csv", "rb") as f:
        data = base64.b64encode(f.read()) 
    return app.test_client(), data

def test_root(client):
    """Tests that a redirect is in place for root"""

    # A GET request should return a 200
    res_get = client.get('/')
    assert res_get.status_code == 302

def test_favicon(client):
    """Test the Basics are working"""

    # A GET request should return a 200
    res_get = client.get('/favicon.ico')
    assert res_get.status_code == 200

    # A POST request should return a 405 (Not Allowed)
    res_post = client.post('/favicon.ico')
    assert res_post.status_code == 405

def test_api_groupbyops(aggregrate_client):
    """Test route /api/aggregate for every possible condition success/failure
    https://stackoverflow.com/questions/18263844/flask-and-werkzeug-testing-a-post-request-with-custom-headers

    """

    client, data = aggregrate_client
    url = "/api/npsum"
    
    #Verify other HTTP method than PUT returns 405
    res_get = client.get(url)
    assert res_get.status_code == 405

    #Verify wrong content-type return 415
    plain_text = 'plain/text'
    res_put_wrong_content_type = client.put(url, headers={'Content-Type': plain_text})
    failed_request_payload = json.loads(res_put_wrong_content_type.data)
    assert plain_text == failed_request_payload['content_type']
    assert res_put_wrong_content_type.status_code == 415

    #Verify wrong parameters/none parameters returns 400
    res_put_wrong_params = client.put(url, query_string={"column":"first_name", 
            "group_by":None}, headers={'Content-Type': 'application/json'})
    params_failed_request_payload = json.loads(res_put_wrong_params.data)
    assert None == params_failed_request_payload["group_by"]
    assert res_put_wrong_params.status_code == 400

    #Verify success condition
    success_res =  client.put(url, query_string={"column":"count", 
            "group_by":"last_name"}, headers={'Content-Type': 'application/json'}, data=data)
    assert success_res.status_code == 200
    assert {'eagle': 34, 'lee': 3, 'smith': 27} == json.loads(success_res.data)

    