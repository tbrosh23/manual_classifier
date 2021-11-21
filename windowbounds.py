import win32gui

def callback(hwnd, extra):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    window_text = win32gui.GetWindowText(hwnd)
    if "Calc" in window_text:
        print("Window %s:" % window_text)
        print("\tLocation: (%d, %d)" % (x, y))
        print("\t    Size: (%d, %d)" % (w, h))

def main():
    win32gui.EnumWindows(callback, None)

if __name__ == '__main__':
    main()