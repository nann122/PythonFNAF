import random
from config import *


class Animatronic:
    def __init__(self, name, start_location):
        self.name = name
        self.current_location = start_location
        self.aggression = 1
        self.move_timer = 0
        self.move_interval = random.uniform(3, 8)
        self.is_active = False

    def update(self, dt, night_number, power_level):
        """Update animatronic behavior"""
        self.move_timer += dt

        # Increase aggression based on night and power level
        effective_aggression = self.aggression * (1 + night_number * 0.3)
        if power_level < 20:
            effective_aggression *= 1.5

        if self.move_timer >= self.move_interval / effective_aggression:
            self.attempt_move()
            self.move_timer = 0
            self.move_interval = random.uniform(2, 6)

    def attempt_move(self):
        """Attempt to move to next location"""
        if random.random() < 0.3:  # 30% chance to move
            self.move_to_next_location()

    def move_to_next_location(self):
        """Override in subclasses"""
        pass


class Freddy(Animatronic):
    def __init__(self):
        super().__init__("freddy", "show_stage")
        self.path = ["show_stage", "dining_area", "east_hall", "right_door"]
        self.path_index = 0

    def move_to_next_location(self):
        if self.path_index < len(self.path) - 1:
            self.path_index += 1
            self.current_location = self.path[self.path_index]


class Bonnie(Animatronic):
    def __init__(self):
        super().__init__("bonnie", "show_stage")
        self.path = ["show_stage", "dining_area", "backstage", "supply_closet", "west_hall", "left_door"]
        self.path_index = 0

    def move_to_next_location(self):
        if self.path_index < len(self.path) - 1:
            self.path_index += 1
            self.current_location = self.path[self.path_index]


class Chica(Animatronic):
    def __init__(self):
        super().__init__("chica", "show_stage")
        self.path = ["show_stage", "dining_area", "kitchen", "east_hall", "right_door"]
        self.path_index = 0

    def move_to_next_location(self):
        if self.path_index < len(self.path) - 1:
            self.path_index += 1
            self.current_location = self.path[self.path_index]


class Foxy(Animatronic):
    def __init__(self):
        super().__init__("foxy", "pirate_cove")
        self.curtain_state = "closed"  # closed, peeking, gone
        self.camera_check_timer = 0
        self.run_phase = 0  # 0: in cove, 1: running, 2: at door

    def update(self, dt, night_number, power_level, camera_on_foxy=False):
        super().update(dt, night_number, power_level)

        if not camera_on_foxy:
            self.camera_check_timer += dt
        else:
            self.camera_check_timer = 0

        # Foxy becomes more aggressive if not watched
        if self.camera_check_timer > 5 and self.run_phase == 0:
            self.start_running()

    def start_running(self):
        self.run_phase = 1
        self.current_location = "west_hall"
        # Will reach door in 2-3 seconds

    def move_to_next_location(self):
        if self.run_phase == 1:
            self.run_phase = 2
            self.current_location = "left_door"


class AIDirector:
    def __init__(self):
        self.animatronics = {
            'freddy': Freddy(),
            'bonnie': Bonnie(),
            'chica': Chica(),
            'foxy': Foxy()
        }

    def update(self, dt, night_number, power_level, camera_system):
        """Update all animatronics"""
        foxy_being_watched = camera_system.current_camera == "pirate_cove"

        for name, animatronic in self.animatronics.items():
            if name == "foxy":
                animatronic.update(dt, night_number, power_level, foxy_being_watched)
            else:
                animatronic.update(dt, night_number, power_level)

    def get_animatronic_at_door(self, side):
        """Check if any animatronic is at specified door"""
        door_location = f"{side}_door"
        for animatronic in self.animatronics.values():
            if animatronic.current_location == door_location:
                return animatronic
        return None

    def get_animatronics_at_location(self, location):
        """Get all animatronics at a specific location"""
        return [a for a in self.animatronics.values() if a.current_location == location]
