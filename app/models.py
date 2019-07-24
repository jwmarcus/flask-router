from datetime import datetime
from app import db, ma


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datapoints = db.relationship("Datapoint")
    mac_addr = db.Column(db.String(24))

    def __repr__(self):
        return "<Device {}, mac_addr {}>".format(self.id, self.mac_addr)


class Datapoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # db_id
    device_id = db.Column(db.Integer, db.ForeignKey("device.id"))
    key = db.Column(db.String(256))
    value = db.Column(db.String(256))
    type = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Datapoint {}>".format(self.id)


class DeviceSchema(ma.ModelSchema):
    class Meta:
        model = Device
        include_fk = True


class DatapointSchema(ma.ModelSchema):
    class Meta:
        model = Datapoint
        include_fk = True
