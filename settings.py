class Settings:
    """ A class to store all settings for Alien Invasion. """

    def __init__(self):
        """" Initialize the game's settings. """
        # Screen settings
        self.screen_width = 1500
        self.screen_height = 750
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (100, 100, 255)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
