#!/usr/bin/env python
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from gpiozero import MotionSensor
import time
import subprocess

from app import app
from light_driver import LightDriver

light_driver = LightDriver()

pir = MotionSensor(app.config['PIR'])
alarm_duration = app.config['ALARM_DURATION']
radio_duration = app.config['RADIO_DURATION']
alarm_file = app.config['ALARM_FILE_NAME']
alarm_duration_seconds = (alarm_duration * 60)
radio_duration_seconds = (radio_duration * 60)

print("")
print("Alarm Duration %s" %alarm_duration_seconds)
print("PIR Pin %s" %pir)
print("")

"""
Play Obnoxious Alarm Sound
"""
def main():
    print("Started Motion Detection")
    light_driver.on()
    cmd = ['mpc', 'stop']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    cmd = ['mpc', 'update']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    cmd = ['mpc', 'clear']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    # You will need the alarm file in the respective folder of your system for mpc to be able to add it
    cmd = ['mpc', 'add', alarm_file]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    cmd = ['mpc', 'play']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    print("Started Alarm")
    ( pir.wait_for_motion() or time.sleep(alarm_duration_seconds))
    print("Motion Detected")
    cmd = ['mpc', 'stop']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    light_driver.off()
    time.sleep(5)
    # After playing the alarm turn on the radio for given time
    cmd = ['mpc', 'update']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    cmd = ['mpc', 'clear']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    cmd = ['mpc', 'add', 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    cmd = ['mpc', 'play']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    print("Playing Radio")
    time.sleep(radio_duration_seconds)
    cmd = ['mpc', 'stop']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    print("Stop Radio")


if __name__ == "__main__":
    main()
