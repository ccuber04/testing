import win32api
import time

def move_mouse():
    while True:
        # Get current mouse position
        current_x, current_y = win32api.GetCursorPos()

        # Move the mouse by 1 pixel and back to simulate movement
        win32api.SetCursorPos((current_x + 1, current_y + 1))
        time.sleep(0.1)
        win32api.SetCursorPos((current_x, current_y))

        # Wait for 5 minutes
        time.sleep(300)

if __name__ == "__main__":
    move_mouse()
