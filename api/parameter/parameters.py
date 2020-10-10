import _thread

from flask import request
from flask_restful import Resource

from api.parameter.generating_random_temperatures import set_random_temperatures
from api.parameter.set_parameters import set_parameters, get_parameters as ret_parameters
from api.pvs.log_pv import log_pvs_to_database
from database_config.config import mycursor, mydb


class Parameters(Resource):
    def get(self):
        return ret_parameters()

    def post(self):
        data = request.json['data']

        threshold, powerph, volume, mole , time = int(data['threshold']), int(data['powerph']), \
                                           int(data['volume']), int(data['mole']) , int(data['time'])

        sql = "INSERT INTO ParametersLogs (threshold, volume , mole , powerph , time ) VALUES (%s, %s , %s , %s , %s)"

        val = (
        threshold, volume, mole, powerph, time )

        mycursor.execute(sql, val)
        mydb.commit()

        set_parameters(threshold, powerph, volume, mole)

        _thread.start_new_thread(set_random_temperatures, ("Generating-Random-Temperatures", 2,))
        _thread.start_new_thread(log_pvs_to_database, ("Log-Pvs-Database", 4,))

        return 'set successfully'
