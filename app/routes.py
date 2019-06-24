from flask import request
from app import app, db
from app.models import Device, Datapoint

# Enable the ability to call "flask shell" and get an automatic
# database and "Device" and "Datapoint" objects to work with.
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
        datapoints = Datapoint.query.all()
        d_arr = []
        for d in datapoints:
            d_arr.append(d.value)
        return str(d_arr)
