from flask import request, jsonify
from app import app, db
from app.models import Device, DeviceSchema, Datapoint, DatapointSchema

# Enable the ability to call "flask shell" and get an automatic
# database and "Device" and "Datapoint" objects to work with.
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Device": Device, "Datapoint": Datapoint}


@app.route("/")
def hello_world():
    return jsonify(
        status="OK", code=200, messages=[], response=[{"message": "Hello there!"}]
    )


@app.errorhandler(404)
def handle_404(error):
    return jsonify(status="ERROR", code=404, messages=[str(error)], response=[])


# Datapoint routes
@app.route("/api/data/", methods=["GET"])
def get_datapoints():
    datapoints = Datapoint.query.all()
    schema = DatapointSchema(many=True)

    return jsonify(
        status="OK", code=200, messages=[], response=schema.dump(datapoints).data
    )


@app.route("/api/data/filter/<filter_key>/<filter_val>/", methods=["GET"])
def get_datapoints_by_filter(filter_key, filter_val):
    if filter_key not in dir(Datapoint):
        return jsonify(
            status="ERROR",
            code=400,
            response=[],
            messages=["Filter request is invalid. Check that key exists."],
        )
    datapoints = Datapoint.query.filter_by(**{filter_key: filter_val}).all()
    schema = DatapointSchema(many=True)

    return jsonify(
        status="OK", code=200, messages=[], response=schema.dump(datapoints).data
    )


@app.route("/api/data/<int:device_id>/", methods=["POST"])
def post_datapoint(device_id):
    datapoint = Datapoint(
        mac_addr=request.form["mac_addr"],
        field=request.form["field"],
        value=request.form["value"],
        type=request.form["type"],
    )
    db.session.add(datapoint)
    db.session.commit()

    return jsonify()


# Device routes
@app.route("/api/devices/", methods=["GET"])
@app.route("/api/devices/<int:device_id>/", methods=["GET"])
def get_devices(device_id=None):
    devices = (
        Device.query.all()
        if device_id is None
        else Device.query.filter_by(id=device_id).first()
    )
    schema = DeviceSchema(many=(device_id is None))

    return jsonify(
        status="OK", code=200, messages=[], response=schema.dump(devices).data
    )
