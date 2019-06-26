from datetime import datetime
from app import db, ma

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datapoints = db.relationship('Datapoint')

    def __repr__(self):
        return '<Device {}>'.format(self.id)

class Datapoint(db.Model):
    id = db.Column(db.Integer, primary_key=True) # db_id
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    mac_addr = db.Column(db.String(24))
    field = db.Column(db.String(256))
    value = db.Column(db.String(256))
    type = db.Column(db.String(256))
    # create_time is when the measurement was taken
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    # timestamp is when the record was created in the database
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Datapoint {}>'.format(self.id)

class DeviceSchema(ma.ModelSchema):
    class Meta:
        model = Device

class DatapointSchema(ma.ModelSchema):
    class Meta:
        model = Datapoint
