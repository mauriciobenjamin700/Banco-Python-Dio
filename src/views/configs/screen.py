from screeninfo import get_monitors

monitor = get_monitors()[0]

WIDTH = 1280
HEIGHT = 720
X = (monitor.width // 2) - (WIDTH // 2)
Y = (monitor.height // 2) - (HEIGHT // 2)

del monitor

BACKGROUND_COLOR = "blue"
