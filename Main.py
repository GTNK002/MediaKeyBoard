from pynput.keyboard import Key, Listener, Controller
import pystray
import PIL.Image

"""
Libraries to install
  pynput
  pystary
Don't forget to add Icon.png in Directory
"""

image = PIL.Image.open("Icon.png")
Keyboard = Controller()
out = 0  # print out False


def printf(var):
    if out == 1:
        print(var)


def ks():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def on_clicked(icon, item):
    if str(item) == "Start":
        printf("Start")
        ks()


aIcon = pystray.Icon("Icon", image, menu=pystray.Menu(pystray.MenuItem("Start", on_clicked)))


def on_press(key):
    printf('{0} pressed'.format(
        key))


def on_release(key):
    printf('{0} release'.format(
        key))
    if key == Key.esc:
        aIcon.stop()
        return False
    elif key == Key.print_screen:
        Keyboard.press(Key.media_volume_mute)
    elif key == Key.scroll_lock:
        Keyboard.press(Key.media_volume_down)
    elif key == Key.pause:
        Keyboard.press(Key.media_volume_up)


aIcon.run()
