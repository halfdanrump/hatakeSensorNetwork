from flask import Flask
flapp = Flask('sensor_api')


### Use Twitter Bootstrap
from flask_bootstrap import Bootstrap
Bootstrap(flapp)

### Restify the app
from flask.ext import restful
rest_api = restful.Api(flapp)



### Adds websocket to app
#from flask.ext.socketio import SocketIO
#socketio = SocketIO(flapp)

### Before importing other modules, import and setup run configuration
from app import conf
flapp.config.update(conf.module_config)




from satoyama import database, models

### Import modules containing statements that must be executed when the webapp is started (such as adding routes for the REST api)
import resources

@flapp.teardown_appcontext
def shutdown_session(exception=None):
    database.db_session.remove()
