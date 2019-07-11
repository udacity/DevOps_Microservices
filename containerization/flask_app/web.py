import os
import base64
import sys
from io import BytesIO

from flask import Flask
from flask import send_from_directory
from flask import request
from flask_api import status
from flasgger import Swagger
from flask import redirect
from flask import jsonify

from sensible.loginit import logger
from nlib import csvops
from nlib import utils

log = logger(__name__)

app = Flask(__name__)
Swagger(app)

def _b64decode_helper(request_object):
    """Returns base64 decoded data and size of encoded data"""

    size=sys.getsizeof(request_object.data)
    decode_msg = "Decoding data of size: {size}".format(size=size)
    log.info(decode_msg)
    decoded_data = BytesIO(base64.b64decode(request.data))
    return decoded_data, size

@app.route("/")
def home():
    """/ Route will redirect to API Docs: /apidocs"""

    return redirect("/apidocs")


@app.route("/favicon.ico")
def favicon():
    """The Favicon"""

    return send_from_directory(os.path.join(app.root_path, 'static'),
                    'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/api/funcs', methods = ['GET'])
def list_apply_funcs():
    """Return a list of appliable functions


        GET /api/funcs
        ---
        responses:
            200:
                description: Returns list of appliable functions.


    """

    appliable_list = utils.appliable_functions()
    return jsonify({"funcs":appliable_list})


@app.route('/api/<groupbyop>', methods = ['PUT'])
def csv_aggregate_columns(groupbyop):
    """Aggregate column in an uploaded csv
    
    ---
        consumes:  application/json
        parameters:
            -   in: path
                name:  Appliable Function (i.e.  npsum, npmedian)
                type:  string
                required: true
                description:  appliable function, which must be registered (check /api/funcs)
            -   in: query
                name: column
                type: string
                description:  The column to process in an aggregation
                required:  True
            -   in: query    
                name: group_by
                type: string
                description:  The column to group_by in an aggregation
                required:  True
            -   in: header
                name:  Content-Type
                type:  string
                description:  Requires "Content-Type:application/json" to be set
                required:  True
            -   in: body
                name: payload
                type:  string
                description:  base64 encoded csv file
                required: True

        responses:
            200:
                description: Returns an aggregated CSV.

    """

    #TO DO?:  Make this into a helper function
    #Return 415 if not valid content type
    content_type = request.headers.get('Content-Type')
    content_type_log_msg = "Content-Type is set to:  {content_type}".\
        format(content_type=content_type)
    log.info(content_type_log_msg)
    if not content_type == "application/json":
        wrong_method_log_msg =\
             "Wrong Content-Type in request: {content_type} sent, but requires application/json".\
            format(content_type=content_type)
        log.info(wrong_method_log_msg)
        return jsonify({"content_type": content_type, 
                "error_msg": wrong_method_log_msg}), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE

    #Parse Query Parameters and Retrieve Values
    query_string = request.query_string
    query_string_msg = "Request Query String: {query_string}".format(query_string=query_string)
    log.info(query_string_msg)
    column = request.args.get("column")
    group_by = request.args.get("group_by")
    
    #Query Parameter logging and handling
    query_parameters_log_msg = "column: [{column}] and group_by: [{group_by}] Query Parameter values".\
        format(column=column, group_by=group_by) 
    log.info(query_parameters_log_msg)
    if not column or not group_by:
        error_msg = "Query Parameter column or group_by not set"
        log.info(error_msg)
        return jsonify({"column": column, "group_by": group_by, 
                "error_msg": error_msg}), status.HTTP_400_BAD_REQUEST

    #Load Plugins and grab correct one
    plugins = utils.plugins_map()
    appliable_func = plugins[groupbyop]

    #TO DO?:  Add some additional error handling (invalid column name, etc)
    #Unpack data and operate on it
    data,_ = _b64decode_helper(request)
    #Returns Pandas Series
    res = csvops.group_by_operations(data, 
        groupby_column_name=group_by, apply_column_name=column, func=appliable_func)
    log.info(res)
    return res.to_json(), status.HTTP_200_OK


if __name__ == "__main__": # pragma: no cover
    log.info("START Flask")
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
    log.info("SHUTDOWN Flask")