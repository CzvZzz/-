class Settings():
    #设置存储
    def __init__(self):
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (240, 255, 255)

        self.ship_speed=2

        self.bullet_speed_factor = 1
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

