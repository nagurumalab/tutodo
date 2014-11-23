from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

class Tasks(restful.Resource):
    def get(self):
        return "All Task"

api.add_resource(Task,'/tasks')

if __name__ == '__main__':
    app.run(debug=True)
