Playing around with API's and Flask

Might be a good place to send some IOT data and kick off actions accordingly.

## Notes from building this project:

### Setting up the database with Alembic

To initialize the database via Alembic the first time, run `flask db migrate -m "devices"` and then the same for `datapoints`

Next, run `flask db upgrade` to do the actual db work

### Working with data from the database

To get records from the database, refer to the SQLAlchemy documentation. Here are some examples:

```
datapoints = Datapoint.query.all()
for d in datapoints:
    print(p.device_id, p.value, p.timestamp)
```
