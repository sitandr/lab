import subprocess

import os

p = os.getcwd()

for i in os.walk(p):
    path =  i[0] + '/'
    for f in i[2]:
        if not f.endswith('.jpg'):
            continue

        f = path+f

        subprocess.call(["magick", f, f, "-strip", "-interlace", "Plane", "-gaussian-blur", "0.05", "-quality", "85%"], stderr=subprocess.PIPE)
