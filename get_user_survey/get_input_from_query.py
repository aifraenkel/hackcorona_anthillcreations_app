import json
import uuid
import datetime

def gather_response(, query_string, statusCode):
    response = {"headers": {"Content-Type": "application/json",
                        },
                "statusCode": statusCode,
                "body":json.dumps({"message":"""Incorrect inputs for the {}!""".format(query_string)})}

def get_survey_inputs(request):

    request_json = request.get_json()
    if request.args and 'queryStringParameters' in request.args:

        query_strings = event['queryStringParameters']
        try:
            age = int(query_strings['age'])
        except:
            return gather_response('age', 500)

        try:
            has_disorder = int(query_strings['has_disorder'])
        except:
            return gather_response('has_disorder', 500)

        try:
            disorders = query_strings['disorder'].replace(' ','').splits(',')
        except:
            return gather_response('disorders', 500)
        
        try:
            is_smoker = query_strings['is_smoker']
        except:
            return gather_response('is_smoker', 500)

        try:
            been_to_redzone = int(query_strings['been_to_redzone'])
        except:
            return gather_response('been_to_redzone', 500)

        try:
            has_symtoms = int(query_strings['has_symtoms'])
        except:
            return gather_response('has_symtoms', 500)
        
        return '.'.join([str(value) for value in [age, has_disorder, disorders, is_smoker, been_to_redzone, has_symtoms]])
