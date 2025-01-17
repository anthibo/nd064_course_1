from flask import Flask
import json
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
        response  = json.dumps({
        "result": "Okay- healthy"
    }),
    status = 200,
    mimetype = 'application/json'

        
    )
    
    
     
    return response


@app.route("/metrics")
def metrics():
    response = app.response_class(
        response  = json.dumps({
        "User-Count": 140,
        "Active-Users":23

    }),
    status = 200,
    mimetype = 'application/json'

        
    )
    app.logger.info('metrics request successfull')
    return response
    
    
     
    return response

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
