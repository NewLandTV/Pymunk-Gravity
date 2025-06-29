import pyglet
import pymunk

from pymunk.pyglet_util import DrawOptions

# Window settings
window = pyglet.window.Window(1600, 900, "Gravity Simulation")

# Global variable settings
fps = 60
ballCount = 20
ballRadius = 60
gravityScale = -981
floorAngleA = 500
floorAngleB = 0
space = pymunk.Space()
drawOptions = DrawOptions()
space.gravity = (0, gravityScale)

# Floor
floor = pymunk.Body(body_type = pymunk.Body.STATIC)

floor.position = (0, 50)
floorShape = pymunk.Segment(floor, (0, floorAngleA), (window.width, floorAngleB), 1)
floorShape.elasticity = 1
floorShape.friction = 0.3

space.add(floor, floorShape)

# Ball
for i in range(0, ballCount):
    ball = pymunk.Body(1, 1)

    ball.position = (ballRadius * i * 2 + ballRadius, window.height - ballRadius)
    ballShape = pymunk.Circle(ball, ballRadius)
    ballShape.elasticity = 0.25
    ballShape.friction = 0.15

    space.add(ball, ballShape)

# Functions
def Update(deltaTime):
    window.clear()
    space.debug_draw(drawOptions)
    space.step(deltaTime)

pyglet.clock.schedule_interval(Update, 1.0 / fps)
pyglet.app.run()
