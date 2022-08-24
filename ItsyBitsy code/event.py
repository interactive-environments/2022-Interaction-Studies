import time
import digitalio
import analogio

intervals = []
timeOuts = []
digital_sensors = {}
digital_events = []
analog_sensors = {}
analog_events = []
for_loops = []


class Timeout:

    def __init__(self, function, time_in_seconds):
        self.function = function
        self.execute_time = time.monotonic() + time_in_seconds

    def should_execute(self, current_time):
        if current_time >= self.execute_time:
            return True
        else:
            return False

    def execute(self):
        self.function()


class Interval:

    def __init__(self, function, time_in_seconds):
        self.function = function
        self.last_execution = time.monotonic()
        self.interval = time_in_seconds

    def should_execute(self, current_time):
        if current_time - self.last_execution >= self.interval:
            return True
        else:
            return False

    def execute(self):
        self.last_execution = time.monotonic()
        self.function()


class DigitalEvent:
    def __init__(self, sensor, event_type, func):
        self.function = func
        self.sensor = sensor
        self.sensor.direction = digitalio.Direction.INPUT
        self.event_type = event_type
        self.click = False
        self.switch = False

    def click_check(self):
        if not self.click and self.sensor.value:
            self.click = True
            self.function()
        if self.click and not self.sensor.value:
            self.click = False

    def change_check(self):
        if self.click != self.sensor.value:
            self.click = self.sensor.value
            self.function(self.click)

    def switch_check(self):
        if not self.click and self.sensor.value:
            self.click = True
            self.switch = not self.switch
            self.function(self.switch)
        if self.click and not self.sensor.value:
            self.click = False

    def check(self):
        if self.event_type == "click":
            self.click_check()
        elif self.event_type == "change":
            self.change_check()
        elif self.event_type == "switch":
            self.switch_check()


class AnalogEvent:
    def __init__(self, sensor, event_type, threshold, func, sensor_range=0):
        self.function = func
        self.sensor = sensor
        self.event_type = event_type
        self.value = self.sensor.value
        self.range = sensor_range
        self.threshold = threshold

    def get_value(self):
        if self.range > 0:
            return self.sensor.value / 65535 * self.range
        else:
            return self.sensor.value

    def above_check(self):
        if self.value < self.threshold <= self.get_value():
            self.value = self.get_value()
            self.function()
        elif self.value >= self.threshold > self.get_value():
            self.value = self.get_value()

    def below_check(self):
        if self.value > self.threshold >= self.get_value():
            self.value = self.get_value()
            self.function()
        elif self.value <= self.threshold < self.get_value():
            self.value = self.get_value()

    def change_check(self):
        if self.get_value() > self.value + self.threshold or self.get_value() < self.value - self.threshold:
            self.value = self.get_value()
            self.function(self.value)

    def check(self):
        if self.event_type == "above":
            self.above_check()
        if self.event_type == "below":
            self.below_check()
        if self.event_type == "change":
            self.change_check()


def digital_on(event_type, pin, func):
    if str(pin) in digital_sensors:
        sensor = digital_sensors[str(pin)]
    else:
        digital_sensors[str(pin)] = digitalio.DigitalInOut(pin)
        sensor = digital_sensors[str(pin)]
    d = DigitalEvent(sensor, event_type, func)
    digital_events.append(d)


def analog_on(event_typ, pin, func, threshold, sensor_range=0):
    if str(pin) in analog_sensors:
        sensor = analog_sensors[str(pin)]
    else:
        analog_sensors[str(pin)] = analogio.AnalogIn(pin)
        sensor = analog_sensors[str(pin)]

    a = AnalogEvent(sensor, event_typ, threshold, func, sensor_range)
    analog_events.append(a)


def set_timeout(function, time_in_seconds):
    t = Timeout(function, time_in_seconds)
    timeOuts.append(t)


def set_interval(function, time_in_seconds):
    i = Interval(function, time_in_seconds)
    intervals.append(i)
    return i


def stop_async_for(loop):
    if loop in for_loops:
        for_loops.remove(loop)


def async_for(iterator: [list, range], func, callback=0):
    if type(iterator) == range:
        l = list(iterator)
        l.reverse()
        item = (l, func, callback)
        for_loops.append(item)
    else:
        item = (iterator, func, callback)
        for_loops.append(item)
    return item


def clear_timers():
    timeOuts.clear()


def clear_intervals():
    intervals.clear()


def stop_interval(interval):
    if interval in intervals:
        intervals.remove(interval)


def event_loop(func=0):
    while True:
        current_time = time.monotonic()
        # Check all timeouts
        done = []
        for i in range(len(timeOuts)):
            timeout = timeOuts[i]
            if timeout.should_execute(current_time):
                timeout.execute()
                done.append(timeout)

        # remove timers that are done
        for t in done:
            timeOuts.remove(t)

        # Check all intervals
        for i in range(len(intervals)):
            try:
                interval = intervals[i]
                if interval.should_execute(current_time):
                    interval.execute()
            except IndexError:
                print("index doesnt exist")

        # Check all digital events
        for event in digital_events:
            event.check()

        # Check all analog events
        for event in analog_events:
            event.check()

        # Handle async for loops
        done = []
        for loop in for_loops:
            if len(loop[0]) > 0:
                item = loop[0].pop()
                loop[1](item)
            else:
                done.append(loop)

        for d in done:
            if d[2] != 0:
                d[2]()
            if d in for_loops:
                for_loops.remove(d)

        # execute user code
        if func != 0:
            func()
