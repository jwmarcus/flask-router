from flask import request, jsonify, render_template
from app import app, db
from app.models import Device, DeviceSchema, Datapoint, DatapointSchema

# Enable the ability to call "flask shell" and get an automatic
# database and "Device" and "Datapoint" objects to work with.
@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Device": Device, "Datapoint": Datapoint}


@app.route("/")
def index():
    return render_template('index.html', title="Index")

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


@app.route("/api/data/<mac_addr>/", methods=["POST"])
def create_datapoint(mac_addr):
    device_id = create_device_id_from_mac_addr(mac_addr).json["response"]

    datapoint = Datapoint(
        device_id=device_id,
        key=request.form["key"],
        value=request.form["value"],
        type=request.form["type"],
    )
    db.session.add(datapoint)
    db.session.commit()

    return jsonify(
        status="OK", code=200, messages=["INFO: Datapoint added"], response=[]
    )


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


@app.route("/api/devices/id/<mac_addr>/", methods=["GET"])
def get_device_id_from_mac_addr(mac_addr):
    device = Device.query.filter_by(mac_addr=mac_addr).first()
    schema = DeviceSchema()
    device_id = 0 if device is None else schema.dump(device).data["id"]
    return jsonify(status="OK", code=200, messages=[], response=device_id)


@app.route("/api/devices/id/<mac_addr>/", methods=["POST"])
def create_device_id_from_mac_addr(mac_addr):
    device_id = get_device_id_from_mac_addr(mac_addr).json["response"]
    message = "INFO: Existing device found (id={})".format(device_id)

    if device_id is 0:
        new_device = Device(mac_addr=mac_addr)
        db.session.add(new_device)
        db.session.commit()

        # Requery Devices now that a new record was added
        device_id = get_device_id_from_mac_addr(mac_addr).json["response"]
        message = "INFO: New device created [{}]".format(device_id)

    return jsonify(status="OK", code=200, messages=[message], response=device_id)
