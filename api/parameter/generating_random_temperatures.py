import random
import time

from epics_db.pv_objects import thermometer_1, thermometer_2, thermometer_3

temperature_mid_value = 700
temperature_bound = 200
delay = 1


def set_random_temperatures(ll, ll1):
    while True:
        time.sleep(delay)

        thermometer_1.put(value=random.randint(temperature_mid_value - (temperature_bound / 2),
                                               temperature_mid_value + (temperature_bound / 2)))

        thermometer_2.put(value=random.randint(temperature_mid_value - (temperature_bound / 2),
                                               temperature_mid_value + (temperature_bound / 2)))

        thermometer_3.put(value=random.randint(temperature_mid_value - (temperature_bound / 2),
                                               temperature_mid_value + (temperature_bound / 2)))
