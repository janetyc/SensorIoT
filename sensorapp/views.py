from flask import Blueprint, Flask, Response, request, render_template, redirect, url_for, jsonify
from datetime import datetime
from sensorapp import app, env
from sensorapp.dbquery import DBQuery

views = Blueprint('views', __name__, template_folder='templates')

@views.route('/')
def index():
    return render_template('index.html', output="hi")

@views.route('/dashboard')
def dashboard():
    devices = DBQuery().get_last_devices(5)
    sensors = DBQuery().get_last_sensors(5)
    actuators = DBQuery().get_last_actuators(5)
    sensor_data = DBQuery().get_last_sensor_data(5)
    actuator_data = DBQuery().get_last_actuator_data(5)
    data = {
        'devices': devices,
        'sensors': sensors,
        'actuators': actuators,
        'sensor_data': sensor_data,
        'actuator_data': actuator_data
    }
    return render_template('dashboard.html', data=data)

@views.route('/404')
def page_not_found():
    return render_template('404.html'), 404

@views.route('/400')
def bad_request():
    return render_template('400.html'), 400

#------ API ---------
@views.route('/add_device', methods=('GET','POST'))
def add_device():
    device_name = request.args.get('name', u'test_device')
    input = {
        'name': device_name,
        'digit_pin_num': int(request.args.get('digit_pin_num', u'14')),
        'analog_pin_num': int(request.args.get('analog_pin_num', u'6')),
        'type': request.args.get('type', u''),
        'location': request.args.get('location', u''),
        'sensor_list': request.args.get('sensor_list', u'').split('|'),
        'actuator_list': request.args.get('actuator_list', u'').split('|'),
        'created_user': request.args.get('created_user', u'')
    }

    device = DBQuery().get_device_by_name(device_name)
    if device:
        return jsonify(success=0, data="", error="DEVICE ALREADY EXIST!!")

    device_id = DBQuery().add_device(input)
    return jsonify(success=1, data=device_id)

@views.route('/add_sensor', methods=('GET', 'POST'))
def add_sensor():
    sensor_name = request.args.get('name', u'test_sensor')
    digit_or_analog = request.args.get('digit_or_analog', u'0')
    if digit_or_analog != "0":
        digit_or_analog = "1"

    input = {
        'name': sensor_name,
        'digit_or_analog': digit_or_analog,
        'type': request.args.get('type', u''),
        'location': request.args.get('location', u''),
        'ability': request.args.get('ability',u''),
        'at_device_id': request.args.get('at_device_id', u''),
        'at_device_name': request.args.get('at_device_name', u''),
        'at_pin': int(request.args.get('at_pin', u'0')),
        'created_user': request.args.get('created_user', u'')
    }

    sensor = DBQuery().get_sensor_by_name(sensor_name)
    if sensor:
        return jsonify(success=0, data="", error="SENSOR ALREADY EXIST!!")

    sensor_id = DBQuery().add_sensor(input)
    return jsonify(success=1, data=sensor_id)

@views.route('/add_actuator', methods=('GET', 'POST'))
def add_actuator():
    actuator_name = request.args.get('name', u'test_actuator')
    digit_or_analog = request.args.get('digit_or_analog', u'0')
    input = {
        'name': actuator_name,
        'digit_or_analog': digit_or_analog,
        'type': request.args.get('type', u''),
        'location': request.args.get('location', u''),
        'ability': request.args.get('ability',u''),
        'at_device_id': request.args.get('at_device_id', u''),
        'at_device_name': request.args.get('at_device_name', u''),
        'at_pin': int(request.args.get('at_pin', u'1')),
        'created_user': request.args.get('created_user', u'')
    }

    actuator = DBQuery().get_actuator_by_name(actuator_name)
    print actuator

    if actuator:
        return jsonify(success=0, data="", error="ACTUATOR ALREADY EXIST!!")

    actuator_id = DBQuery().add_actuator(input)
    return jsonify(success=1, data=actuator_id)


@views.route('/add_sensor_data', methods=('GET', 'POST'))
def add_sensor_data():
    value = float(request.args.get('value', u'0.0'))
    sensing_time = request.args.get('sensing_time', u'')
    sensor_name = request.args.get('sensor_name', u'')
    sensor_id = request.args.get('sensor_id', u'')

    if sensing_time == "":
        sensing_time_datetime = datetime.utcnow()
    else:
        sensing_time_datetime = datetime.strptime(sensing_time, '%Y-%m-%d_%H:%M:%S:%f')

    input = {
        'value': value,
        'from_sensor_id': sensor_id,
        'from_sensor_name': sensor_name, 
        'sensing_time': sensing_time_datetime,
    }

    sensor_data_id = DBQuery().add_sensor_data(input)

    return jsonify(success=1, data=sensor_data_id, time=sensing_time_datetime)

@views.route('/add_actuator_data', methods=('GET', 'POST'))
def add_actuator_data():
    value = float(request.args.get('value', u'0.0'))
    acting_time = request.args.get('acting_time', u'')
    actuator_name = request.args.get('actuator_name', u'')
    actuator_id = request.args.get('actuator_id', u'')

    if acting_time == "":
        acting_time_datetime = datetime.utcnow()
    else:
        acting_time_datetime = datetime.strptime(acting_time, '%Y-%m-%d_%H:%M:%S:%f')

    input = {
        'value': value,
        'from_actuator_id': actuator_id,
        'from_actuator_name': actuator_name,
        'acting_time': acting_time_datetime,
    }

    actuator_data_id = DBQuery().add_actuator_data(input)
    return jsonify(success=1, data=actuator_data_id)
