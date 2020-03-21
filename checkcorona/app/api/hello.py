"""
Hello API route handlers

"""
from flask import jsonify

from . import api


@api.route('/hello/<name>')
def hellow(name):
    return jsonify(dict(hello=name))


from flask import Flask
from flask import request

  
@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'
  
app = Flask(__name__)