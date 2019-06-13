from flask import request
from app import app, db
from app.models import Device, Datapoint

# not sure this belongs here, but wha-hey!
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Device': Device, 'Datapoint': Datapoint}

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/log/<device_id>', methods=['GET', 'POST'])
def log(device_id):
    if request.method == 'POST':
        return '{}\'s endpoint sent data'.format(device_id)
    else:
        return '{}\'s endpoint requested data'.format(device_id)
