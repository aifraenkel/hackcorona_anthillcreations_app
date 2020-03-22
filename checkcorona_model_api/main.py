from flask import Flask, request, jsonify
from risk_calculator import risk
from recomendation_calculator import recomendations

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/')
def default():
    """Return a friendly HTTP greeting."""
    return 'Anthill Creations - HackCorona - Covid19 diagnostics and recomendations api'

@app.route('/infection_risk', methods = ['POST'])
def postJsonHandler(): 

    # Parse json body, validate if the request has all the required values

    # relatives ages 0:less than 50, 1:between 50 and 65, 2: more than 65
    relatives_ages = 0
    # relatives with pre-existent disease 0:no, 1:yes
    relatives_existent_disease = 1
    # relatives smoking history 0:no, 1:yes
    relatives_habits = 0


    # ask the model for risk analysis
    result = risk(2, 1, 2, "Brazil", "Sao Paulo", 1, 0, 0, 0)

    return jsonify(risk= result['risk'],
                extended_risk= result['extended_results'],
                recomendations= recomendations(result['risk'], relatives_ages, relatives_existent_disease, relatives_habits),
                message_body=request.get_json()
                )

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
