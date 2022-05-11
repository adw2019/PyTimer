import sys
import pyglet

window = pyglet.window.Window(fullscreen=True)

COUNTDOWN = int(sys.argv[1])

class Timer(object):
    def __init__(self):
        self.start = '%s:00' % COUNTDOWN
        self.label = pyglet.text.Label(self.start, font_size=360,
                                        x = window.width/2, y=window.height//2,
                                        anchor_x = 'center', anchor_y = 'center')
        self.reset()

    def reset(self):
        self.time = COUNTDOWN * 60
        self.running = False
        self.label.tex  = self.start
        self.label.color = (255,255,255,255)

    def update(self, dt):
        if self.running:
            self.time -= dt
            m, s = divmod(self.time, 60)
            self.label.text = '%02d:%02d' % (m, s)
            if m < 1:
                self.label.color = (180, 0, 0, 255)
            if m < 0:
                self.running = False
                self.label.text = 'Tiden er ute!'

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        if timer.running:
            timer.running = False
        else:
            timer.running = True
    elif symbol == pyglet.window.key.ESCAPE:
        window.close()

@window.event
def on_draw():
    window.clear()
    timer.label.draw()

timer = Timer()
pyglet.clock.schedule_interval(timer.update, 1)
pyglet.app.run()