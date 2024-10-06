import os
import pandas as pd

def mymath(x, y, w, h):
    center_x = (x + w // 2)/1111
    center_y = (y + h // 2)/2363
    c=x/1111
    d=y/2363
    return center_x,center_y,c,d