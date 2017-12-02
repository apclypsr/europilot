#outputs array of image

from europilot.screen import Box
from europilot.train import generate_training_data, Config

class MyConfig(Config):
    # Screen area
    BOX = Box(0, 0, 500, 500)
    # Screen capture fps
    DEFAULT_FPS = 20

class GTD():
    def __init__(self):
        generate_training_data(config=MyConfig)


for i in range(400000):
    generate_training_data(config=MyConfig)
