from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from api.parameter.parameters import Parameters
from api.parameter.log_parameters import LogParameters
from api.pvs.log_pv import log_pvs_to_database
from api.pvs.live_log import LiveLog
from api.pvs.pv import PV
import _thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'

CORS(app)
api = Api(app)

api.add_resource(Parameters, '/parameters', endpoint='parameters')
api.add_resource(LogParameters, '/log/parameters', endpoint='log_parameters')
api.add_resource(PV, '/pv', endpoint='pv')
api.add_resource(LiveLog, '/live_log', endpoint='live_log')

if __name__ == "__main__":
    app.run(debug=True, port=1234)
