import random

class SmartSensor:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.readings = []
        self.alert_count = 0
    def simulate(self, n):
            for i in range(1,n+1):
                temp = random.uniform(18.0, 45.0)
                self.readings.append(temp)
                if temp > 35:
                    self.alert_count += 1
    def get_status(self):
        if self.alert_count > 3:
            return "CRITICAL"
        elif self.alert_count > 0:
            return "WARNING"
        else:
            return "NORMAL"
    def summary(self):
         return f"{self.name} | {self.room} | Readings: {len(self.readings)} | Max: {max(self.readings) if self.readings else 0} | Alerts: {self.alert_count} | Status: {self.get_status()}"
    
class MonitoringSystem:
    def __init__(self):
        self.sensors = []
    def add_sensor(self, sensor):
        self.sensors.append(sensor)
    def run(self, n):
        for sensor in self.sensors:
            sensor.simulate(n)
    def hottest_room(self):
        hottest = None
        max_temp = 0
        for sensor in self.sensors:
            if sensor.readings:
                sensor_max = max(sensor.readings)
                if sensor_max > max_temp:
                    max_temp = sensor_max
                    hottest = sensor.room
        return hottest
    def critical_sensors(self):
        return [sensor for sensor in self.sensors if sensor.get_status() == "CRITICAL"]
    def report(self):
        text = "=== ROOM MONITOR SYSTEM REPORT ===\n"
        for sensor in self.sensors:
            text += sensor.summary() + "\n"
        text += f"\nHottest Room: {self.hottest_room()}\n"
        text += f"Critical Sensors: {', '.join([s.room for s in self.critical_sensors()])}\n"
        text += "=================================="
        return text
system = MonitoringSystem()
sensor1 = SmartSensor("TempSensor1", "Living Room")
sensor2 = SmartSensor("TempSensor2", "Bedroom")
sensor3 = SmartSensor("TempSensor3", "Kitchen")
sensor4 = SmartSensor("TempSensor5", "Garage")
sensor5 = SmartSensor("TempSensor6", "Bathroom")
system.add_sensor(sensor1)
system.add_sensor(sensor2)
system.add_sensor(sensor3)
system.add_sensor(sensor4)  
system.add_sensor(sensor5)
system.run(20)
print(system.report())
report = system.report()
print(report)

with open("monitor_report.txt", "w") as f:
    f.write(report)

print("Report saved to monitor_report.txt")