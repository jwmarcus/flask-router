from flask import request, jsonify
from app import app, db
from app.models import Device, DeviceSchema, Datapoint, DatapointSchema

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
        datapoints = Datapoint.query.filter_by(device_id=device_id).all()
        datapoint_schema = DatapointSchema(many=True)
        output = datapoint_schema.dump(datapoints).data
        return jsonify({'result': output})
