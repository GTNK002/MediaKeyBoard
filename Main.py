from pynput.keyboard import Key, Listener, Controller
Keyboard = Controller()


def on_press(key):
    if key == Key.print_screen:
        Keyboard.press(Key.media_volume_mute)
    elif key == Key.scroll_lock:
        Keyboard.press(Key.media_volume_down)
    elif key == Key.pause:
        Keyboard.press(Key.media_volume_up)


with Listener(on_press=on_press) as listener:
    listener.join()
