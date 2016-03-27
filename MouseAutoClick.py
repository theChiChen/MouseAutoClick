# -*- coding: utf-8 -*-

import win32api, win32con, win32gui, time

# Get Mouse X Y
x,y=win32gui.GetCursorPos()
print("%s %s" %(x, y))


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


if __name__ == '__main__':
	while True:
		time.sleep(0.5)
		click(x,y)