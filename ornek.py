from flask import Flask, request

from flask_restful import Api, Resource

import pandas as pd

import requests





app = Flask(__name__)

api = Api(app)



class Math(Resource):

   def get(self, operation, expression):

       url = f"https://newton.now.sh/api/v2/{operation}/{expression}"



       response = requests.get(url)

       data = response.json()

       return {'data' : data}, 200





api.add_resource(Math, "/math/<string:operation>/<string:expression>")




if __name__ == '__main__':

   app.run(host="0.0.0.0", port=5005)

   app.run()