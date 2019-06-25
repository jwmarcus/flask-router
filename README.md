Playing around with API's and Flask

Might be a good place to send some IOT data and kick off actions accordingly.

## Notes from building this project:

### Setting up the database with Alembic

To initialize the database via Alembic the first time. Initialize the db with `flask db init` then run `flask db migrate -m "devices"` and then the same for `datapoints`

Next, run `flask db upgrade` to do the actual db work

Any time you want to do some modifications to the models, rerun `flask db migrate -m "<object_names>"` and rerun `flask db upgrade`

### Working with data from the database

To get records from the database, refer to the SQLAlchemy documentation. Here are some examples:

```
datapoints = Datapoint.query.all()
for d in datapoints:
    print(p.device_id, p.value, p.timestamp)
```


TODO: Why do I want to use `db.relationship('User', backref='rewards')` again?
