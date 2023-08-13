import time

import pyautogui
from directkeys import *
import datetime


def tap_key(key):
    PressKey(key)
    time.sleep(0.2)
    ReleaseKey(key)


if __name__ == '__main__':
    Throttle = -100
    for _ in reversed(range(5)):
        print("starting in %s sec..." % _)
        time.sleep(1)
    start_time = datetime.datetime.now()
    print('start time: %s' % start_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-5])
    with open(r"sense_data\action.csv", "w+") as f:
        f.write('datetime,throttle\n')
        while True:
            speeding = pyautogui.locateOnScreen('speeding.png', confidence=0.8, region=(253, 960, 454, 998))
            current_time = datetime.datetime.now()
            difference = current_time - start_time
            elapsed_time = difference.total_seconds()
            now = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-5]
            if elapsed_time > 600:
                break
            if speeding is None:
                if Throttle < 100:
                    # accelerate
                    Throttle += 10
                    tap_key(A)
                    f.writelines('%s,%i\n' % (now, Throttle))
                else:
                    f.writelines('%s,%i\n' % (now, Throttle))
            else:
                if Throttle > -100:
                    # decelerate
                    Throttle -= 10
                    tap_key(D)
                    f.writelines('%s,%i\n' % (now, Throttle))
                else:
                    f.writelines('%s,%i\n' % (now, Throttle))
    print('end time: %s' % now)
