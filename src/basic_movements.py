#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:28:21 2021

@author: lauragalvezjimenez
"""

from djitellopy import tello
from time import sleep


def my_movement(drone, velocity, stime):
    drone.send_rc_control(velocity[0],velocity[1],velocity[2],velocity[3])
    sleep(stime)

STIME = 2
drone = tello.Tello()
drone.connect()

print(drone.get_battery())

drone.takeoff()

my_movement(drone, [0,10,0,0], STIME)
my_movement(drone, [0,0,0,90], STIME)
my_movement(drone, [0,10,0,0], STIME)


drone.land()
