Playing around with API's and Flask

Might be a good place to send some IOT data and kick off actions accordingly.

## Notes from building this project:

### Setting up the database with Alembic

To initialize the database via Alembic the first time. Initialize the db with `flask db init` then run `flask db migrate -m "devices"` and then the same for `datapoints`

Next, run `flask db upgrade` to do the actual db work

Any time you want to do some modifications to the models, rerun `flask db migrate -m "<object_names>"` and rerun `flask db upgrade`

### Working with data from the database

Bootstrap the database using these commands in your favorite sql tool:

```
INSERT INTO device ('id') VALUES (1);

INSERT INTO datapoint (device_id, mac_addr, field, value, type) VALUES (1, '123456', 'TEMP', '72.9', 'INT');
INSERT INTO datapoint (device_id, mac_addr, field, value, type) VALUES (1, '123456', 'TEMP', '73.1', 'INT');
INSERT INTO datapoint (device_id, mac_addr, field, value, type) VALUES (1, '123456', 'TEMP', '74.2', 'INT');
INSERT INTO datapoint (device_id, mac_addr, field, value, type) VALUES (1, '123456', 'TEMP', '72.1', 'INT');
```

To get records from the database, refer to the SQLAlchemy documentation. Here are some examples:

```
datapoints = Datapoint.query.all()
for d in datapoints:
    print(p.device_id, p.value, p.timestamp)
```




TODO: Why do I want to use `db.relationship('User', backref='rewards')` again?

## Thoughts on the API

### Things I want to get from the API

- get all measurements for a device_id
- get all measurements for a macaddr
- get all measurements of a type
- get all measurements matching a field
- everything above but just latest n measurements
- get some time parameters

get routes:

- /all routes:
- /device/<device_id>/all
- /macaddr/<macaddr>/all
- /type/<measurement_type>/all
- /field/<field_type>/all
- /<same_as_above>/<variable>/latest/<optional_n>

### Things I want to put on the API

- @device_id - what is the self-reported device name
- @macaddr - the mac address it came from
- @field - the name of the piece of data
- @value - str, we can cast it otherwise
- @type - to tell us what that string represents
- @createtime - when was the measurement taken
- @timestamp - when was the measurement recorded
