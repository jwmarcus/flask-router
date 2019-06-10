from app import app
from flask import request

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/log/<device_id>', methods=['GET', 'POST'])
def log(device_id):
    if request.method == 'POST':
        return '{}\'s endpoint sent data'.format(device_id)
    else:
        return '{}\'s endpoint requested data'.format(device_id)
