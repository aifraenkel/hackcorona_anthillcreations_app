from flask import Flask, request, jsonify
from risk_calculator import risk
from recomendation_calculator import recomendations
from bot_message_parser import *

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/')
def default():
    """Return a friendly HTTP greeting."""
    return 'Anthill Creations - HackCorona - Covid19 diagnostics and recomendations api'

@app.route('/infection_risk', methods = ['POST'])
def postJsonHandler(): 

    survey_dict = request.json['parameters']
    print(survey_dict)

    # Parse json body, validate if the request has all the required values
    arguments = ['agegroup', 'geo-country' ,'hasPreexistConditions',
                    'exposureType','hasFever','hasSymptoms', 'smokeHistory','geo-state']

    try:
        all_feature_present = [True if key in survey_dict else False for idx, key in enumerate(arguments) ]
        missing_arg = [arguments[idx] for idx, key in enumerate(all_feature_present) if not all_feature_present[idx]]
    except Exception as e:
        return jsonify(risk= "NA",
                extended_risk= "NA",
                StatusCode=500,
                error=str(e),
                message_body=survey_dict
                )
    
    if False in all_feature_present:
        return jsonify(risk= "NA",
                extended_risk= "NA",
                StatusCode=404,
                error="Essential arguments {} missing".format(','.join(missing_arg)),
                message_body= request.json['parameters']
                )

    age_brackets = parseAgeBrackets(survey_dict['agegroup'])
    existing_disorder = parseExistingDisorder(survey_dict['hasPreexistConditions'])
    smoking_history = parseSmokingHistory(survey_dict['smokeHistory'])
    country = survey_dict['geo-country']
    state = survey_dict['geo-state']
    exposed_to_virus = parseExposureToVirus(survey_dict['exposureType'])
    exposed_to_risk_country = isCountryRisky(country)
    has_fever = parseHasFever(survey_dict['hasFever'])
    has_related_symptoms = parseHasRelatedDiseases(survey_dict['hasSymptoms'])

    # relatives ages 0:less than 50, 1:between 50 and 65, 2: more than 65
    relatives_ages = 0
    # relatives with pre-existent disease 0:no, 1:yes
    relatives_existent_disease = 1
    # relatives smoking history 0:no, 1:yes
    relatives_habits = 0

    # ask the model for risk analysis
    result = risk(age_brackets, existing_disorder, smoking_history, country, state, exposed_to_virus, exposed_to_risk_country, has_fever, has_related_symptoms)

    return jsonify(risk= result['risk'],
                extended_risk= result['extended_results'],
                recomendations= recomendations(result['risk'], relatives_ages, relatives_existent_disease, relatives_habits),
                message_body= request.json['parameters']
                )

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
