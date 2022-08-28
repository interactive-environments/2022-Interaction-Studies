import time
import board
import p9813

pin_clk = board.D13
pin_data = board.D10
num_leds = 1
leds = p9813.P9813(pin_clk, pin_data, num_leds)

leds.fill((0, 0, 0))
leds.write()

def behaveDayNoCompany(energy):
    leds.fill((0, 0, 55+(energy*5)))
    leds.write()
    return

def behaveDayCompany(energy):
    leds.fill((0, 0, 100+(energy*15)))
    leds.write()
    return

def behaveNightNoCompany(energy):
    leds.fill((0, 55+(energy*5), 0))
    leds.write()
    return

def behaveNightCompany(energy):
    leds.fill((0, 100+(energy*15), 0))
    leds.write()
    return

def behaveInvitinglyBeautiful(energy):
    leds.fill((255, 255, 255))
    leds.write()
    return

