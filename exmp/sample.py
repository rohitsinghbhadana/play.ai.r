# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:16:50 2017

@author: bhadana
"""

import os
import cv2
import numpy as np
from mss.windows import MSS as mss
from matplotlib import pyplot as plt
import pyautogui
pyautogui.PAUSE = 1

#global Declerations
sct = mss()

def takeScreenShot():

  filename = sct.shot(mon=2)
  print(filename)

def findTemplateinImage(template, image, method):
#  img2 = image.copy()
  w, h = template.shape[::-1]

#  img = img2.copy()
  method = eval(method)

  # Apply template Matching
  result = cv2.matchTemplate(image,template,method)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

  # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
  if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
  else:
    top_left = max_loc
  bottom_right = (top_left[0] + w, top_left[1] + h)

  cv2.rectangle(image,top_left, bottom_right, (255,255,255), 2)

  print("click location is y=", (top_left[1] + h/2) , " x =", (top_left[0] + w/2))

  plt.figure(figsize=(20,10),dpi=80, facecolor='w', edgecolor='k')
  plt.subplot(121),plt.imshow(result,cmap = 'gray')
  plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
  plt.subplot(122),plt.imshow(image,cmap = 'gray')
  plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
  plt.suptitle(method)

  plt.show()
  return ((top_left[0] + w/2),(top_left[1] + h/2))



image = cv2.imread('monitor-2.png',0)
template = cv2.imread('run.jpg',0)
(x,y) = findTemplateinImage(template, image, 'cv2.TM_SQDIFF_NORMED')
print ("mouse click at x=", x , " y=",y)
pyautogui.click(x=x,y=y)
