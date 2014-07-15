import bson
from datetime import datetime, timedelta

from sensorapp.models import Device, Sensor, Actuator
from sensorapp.models import SensorData, ActuatorData
from sensorapp import db

class DBQuery(object):
    def add_device(self, input):
        device = Device()
        device.name = input['name']
        device.digit_pin_num = input['digit_pin_num']
        device.analog_pin_num = input['analog_pin_num']
        device.type = input['type']
        device.location = input['location']
        device.sensor_list = input['sensor_list']
        device.actuator_list = input['actuator_list']
        device.created_user = input['created_user']
        device.created_time = datetime.utcnow()
        device_id = db.device.insert(device)
        return str(device_id)

    def get_last_devices(self, count=10):
        query = db.Device.find().sort("created_time", -1).limit(count)
        result = [q for q in query]

        if len(result):
            return result
        else:
            return []

    def get_device_by_id(self, device_id):
        if type(device_id) == str and isValidObjectId(device_id):
            device = db.Device.get_from_id(bson.ObjectId(device_id))
            return device
        else:
            return None
    
    def get_device_by_name(self, name):
        device = db.Device.find({"name": name}).limit(1)
        result = [d for d in device]
            
        if len(result):
            return result[0]
        else:
            return None

    def add_sensor(self, input):
        sensor = Sensor()
        sensor.name = input['name']
        sensor.type = input['type']
        sensor.digit_or_analog = input['digit_or_analog']
        sensor.location = input['location']
        sensor.ability = input['ability']
        sensor.at_device_id = input['at_device_id']
        sensor.at_device_name = input['at_device_name']
        sensor.at_pin = input['at_pin']
        sensor.created_user = input['created_user']
        sensor.created_time = datetime.utcnow()
        sensor_id = db.sensor.insert(sensor)
        return str(sensor_id)

    def get_sensor_by_name(self, name):
        sensor = db.Sensor.find({"name": name}).limit(1)
        result = [s for s in sensor]

        if len(result):
            return result[0]
        else:
            return None

    def get_last_sensors(self, count=10):
        query = db.Sensor.find().sort("created_time", -1).limit(count)
        result = [q for q in query]

        if len(result):
            return result
        else:
            return []

    def add_actuator(self, input):
        actuator = Actuator()
        actuator.name = input['name']
        actuator.type = input['type']
        actuator.digit_or_analog = input['digit_or_analog']
        actuator.location = input['location']
        actuator.ability = input['ability']
        actuator.at_device_id = input['at_device_id']
        actuator.at_device_name =input['at_device_name']
        actuator.at_pin =input['at_pin']
        actuator.created_user = input['created_user']
        actuator.created_time = datetime.utcnow()
        actuator_id = db.actuator.insert(actuator)
        return str(actuator_id)


    def get_actuator_by_name(self, name):
        actuator = db.Actuator.find({"name": name}).limit(1)
        result = [a for a in actuator]

        if len(result):
            return result[0]
        else:
            return None

    def get_last_actuators(self, count=10):
        query = db.Actuator.find().sort("created_time", -1).limit(count)
        result = [q for q in query]

        if len(result):
            return result
        else:
            return []

    def add_sensor_data(self, input):
        data = SensorData()
        data.value = input['value']
        data.from_sensor_id = input['from_sensor_id']
        data.from_sensor_name = input['from_sensor_name']
        data.sensing_time = input['sensing_time']
        data.created_time = datetime.utcnow()
        data_id = db.sensordata.insert(data)
        return str(data_id)

    def get_last_sensor_data(self, count=10):
        query = db.SensorData.find().sort("created_time", -1).limit(count)
        result = [q for q in query]

        if len(result):
            return result
        else:
            return []

    def add_actuator_data(self, input):
        data = ActuatorData()
        data.value = input['value']
        data.from_sensor_id = input['from_actuator_id']
        data.from_sensor_name = input['from_actuator_name']
        data.sensing_time = input['acting_time']
        data.created_time = datetime.utcnow()
        data_id = db.actuatordata.insert(data)
        return str(data_id)

    def get_last_actuator_data(self, count=10):
        query = db.ActuatorData.find().sort("created_time", -1).limit(count)
        result = [q for q in query]

        if len(result):
            return result
        else:
            return []


def isValidObjectId(self, obj_id):
    try:
        id = bson.ObjectId(obj_id)
        return True
    except bson.errors.InvalidId:
        return False
