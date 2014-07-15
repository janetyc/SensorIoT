from flask.ext.mongokit import MongoKit, Document
from datetime import datetime
from sensorapp import db, app

@db.register
class Device(Document):
    __database__ = app.config["DB_NAME"]
    __collection__ = "device"
    structure = {
        'name': unicode,
        'digit_pin_num': int,
        'analog_pin_num': int,
        'type': unicode,
        'location': unicode,
        'sensor_list': list,
        'actuator_list': list,
        'created_user':unicode,
        'created_time': datetime
    }
    required_fields = ['name', 'created_time']
    default_values = {'created_time': datetime.utcnow()}
    use_dot_notation = True

@db.register
class Sensor(Document):
    __database__ = app.config["DB_NAME"]
    __collection__ = "sensor"
    structure = {
        'name': unicode,
        'type': unicode,
        'digit_or_analog': unicode,
        'location': unicode,
        'ability': unicode,
        'at_device_id': unicode,
        'at_device_name': unicode,
        'at_pin': int,
        'created_user': unicode,
        'created_time': datetime
    }
    required_fields = ['name', 'created_time']
    default_values = {'created_time': datetime.utcnow()}
    use_dot_notation = True

@db.register
class Actuator(Document):
    __database__ = app.config["DB_NAME"]
    __collection__ = "actuator"
    structure = {
        'name': unicode,
        'type': unicode,
        'digit_or_analog': unicode,
        'location': unicode,
        'ability': unicode,
        'at_device_id': unicode,
        'at_device_name': unicode,
        'at_pin': int,
        'created_user': unicode,
        'created_time': datetime
    }
    required_fields = ['name', 'created_time']
    default_values = {'created_time': datetime.utcnow()}
    use_dot_notation = True

@db.register
class SensorData(Document):
    __database__ = app.config["DB_NAME"]
    __collection__ = "sensordata"
    structure = {
        'value': float,
        'from_sensor_id': unicode,
        'from_sensor_name': unicode,
        'sensing_time': datetime,
        'created_time': datetime
    }
    required_fields = ['value', 'from_sensor_name', 'sensing_time' ,'created_time']
    default_values = {'created_time': datetime.utcnow()}
    use_dot_notation = True


@db.register
class ActuatorData(Document):
    __database__ = app.config["DB_NAME"]
    __collection__ = "actuatordata"
    structure = {
        'value': float,
        'from_actuator_id': unicode,
        'from_actuator_name': unicode,
        'created_by': unicode,
        'acting_time': datetime,
        'created_time': datetime
    }
    required_fields = ['value', 'from_actuator_name', 'acting_time' ,'created_time']
    default_values = {'created_time': datetime.utcnow()}
    use_dot_notation = True


db.register([Device])
db.register([Sensor])
db.register([Actuator])
db.register([SensorData])
db.register([ActuatorData])

