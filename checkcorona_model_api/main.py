from flask import Flask, request, jsonify
from risk_calculator import risk

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

    # ask the model for risk analysis
    result = risk(2, 1, 2, "Argentina", "Chaco", 1, 0, 0, 0)

    return jsonify(risk= result['risk'],
                extended_risk= result['extended_results'],
                recomendations= 'Please, do wash your hand as much as you can, and stay home.',
                message_body=request.get_json()
                )

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
