from flask import Flask, request, jsonify

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

    # Here could be the call to the model made by Claire
    # data = model.calculateRisk(...)

    return jsonify(risk= "LOW",
                extended_risk= "The risk of infection id LOW",
                message_body=request.get_json()
                )
                
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
