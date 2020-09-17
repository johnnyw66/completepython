# pip install pyglet
import pyglet
from pyglet.window import key



window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.RIGHT:
        print('The right arrow key was pressed.')
    elif symbol == key.UP:
        print('The up arrow key was pressed.')
    elif symbol == key.DOWN:
        print('The down arrow key was pressed.')
    elif symbol == key.SPACE:
        print('The space arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')

@window.event
def on_draw():
    window.clear()
    label.draw()


pyglet.app.run()
