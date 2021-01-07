import pigpio
import time

pi = pigpio.pi()

RED_PIN = 17
GREEN_PIN = 24
BLUE_PIN = 22

def set_color(red, green, blue, seconds=0.1):
    pi.set_PWM_dutycycle(RED_PIN, red)
    pi.set_PWM_dutycycle(GREEN_PIN, green)
    pi.set_PWM_dutycycle(BLUE_PIN, blue)
    print("RGB:", red, green, blue)
    time.sleep(seconds)
    
set_color(0, 0, 0)

while True:
    set_color(255, 0, 0)
    set_color(255, 165, 0)
    set_color(0, 255, 0)
    set_color(0, 255, 165)
    set_color(0, 0, 255)
    set_color(75, 0, 130)
    set_color(128, 0, 128)
    set_color(0, 0, 0)
       
pi.stop()
