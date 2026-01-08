from config import *


class PowerSystem:
    def __init__(self):
        self.current_power = TOTAL_POWER
        self.max_power = TOTAL_POWER
        self.is_power_out = False

    def drain_power(self, dt, camera_active=False, left_door_closed=False,
                    right_door_closed=False, left_light_on=False, right_light_on=False):
        """Drain power based on active systems"""
        if self.is_power_out:
            return

        drain_rate = POWER_DRAIN_BASE

        if camera_active:
            drain_rate += POWER_DRAIN_CAMERA
        if left_door_closed:
            drain_rate += POWER_DRAIN_DOOR
        if right_door_closed:
            drain_rate += POWER_DRAIN_DOOR
        if left_light_on:
            drain_rate += POWER_DRAIN_LIGHT
        if right_light_on:
            drain_rate += POWER_DRAIN_LIGHT

        self.current_power -= drain_rate * dt

        if self.current_power <= 0:
            self.current_power = 0
            self.is_power_out = True

    def get_power_percentage(self):
        return (self.current_power / self.max_power) * 100

    def get_power_bar_color(self):
        percentage = self.get_power_percentage()
        if percentage > 50:
            return GREEN
        elif percentage > 25:
            return YELLOW
        else:
            return RED
