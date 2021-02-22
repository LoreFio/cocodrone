#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:06:49 2021

@author: lauragalvezjimenez
"""

from djitellopy import tello
from time import sleep
import time
import cv2


def my_movement(drone, velocity, stime):
    drone.send_rc_control(velocity[0],velocity[1],velocity[2],velocity[3])
    sleep(stime)


STIME = 2
drone = tello.Tello()
drone.connect()

print(drone.get_battery())

drone.streamon()

drone.takeoff()

start = time.time()

count=0
while abs(time.time()-start)<30:
    drone.rotate_clockwise(20)
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    
    #my_movement(drone, [0,10,0,0], STIME)
    #my_movement(drone, [0,0,0,90], STIME)
    #my_movement(drone, [0,10,0,0], STIME)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    count+=1

drone.land()
drone.streamoff()
print(count)
