from datetime import datetime
from app import db
from marshmallow import Schema, fields

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datapoints = db.relationship('Datapoint')

    def __repr__(self):
        return '<Device {}>'.format(self.id)

# class DeviceSchema(Schema):
#     id = fields.Int(dump_only=True)
#     # TODO:
#     # datapoints

class Datapoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    key = db.Column(db.String(256))
    value = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Datapoint {}>'.format(self.id)
