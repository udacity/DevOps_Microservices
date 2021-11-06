import json
import wikipedia

# prints when function loads
print('Loading function')


def lambda_handler(event, context):
    ''' Wikipedia page summarizer.
        :param event: a request with a wikipedia "entity" that has page information
        :return: a response that contains the first sentence of a wikipedia page,
            the response is JSON formatted.'''
    
    # check that the request has some input body
    if 'body' in event:
        event = json.loads(event["body"])
    
    # get the wikipedia "entity" from the body of the request
    entity = event["entity"]
    # res = wikipedia.summary(entity, sentences=1) # first sentence, result
    BAD_REQUEST_STATUS = 400
    ALL_GOOD_STATUS = 200 
    # Exception handling
    try:
        res = wikipedia.summary(entity, sentences=1) # first sentence, result
        statusCode = ALL_GOOD_STATUS
    except wikipedia.exceptions.PageError:
        res= "\nThis word does not exist!\n"
        statusCode = BAD_REQUEST_STATUS
    except wikipedia.exceptions.DisambiguationError: 
        statusCode = BAD_REQUEST_STATUS
        res = "\nThere are multiple references to this word!\n"
    except:
        statusCode = BAD_REQUEST_STATUS
        res = "\nSorry, Cannot Handle this request!\n"

    # print statements
    print(f"context: {context}, event: {event}")
    print(f"Response from wikipedia API: {res}")
    
    # format the response as JSON and return the result
    response = {
        "statusCode": statusCode, 
        "headers": { "Content-type": "application/json" },
        "body": json.dumps({"message": res})
    }
    
    return response
