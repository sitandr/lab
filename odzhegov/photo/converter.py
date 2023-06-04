import subprocess

import os

p = os.getcwd()

for i in os.walk(p):
    path =  i[0] + '/'
    for f in i[2]:
        if not f.endswith('.bmp'):
            continue

        f2 = path + f[:-4] + '.png'
        f = path+f

        if os.path.isfile(f2):
            subprocess.call(["pngquant", f2, "-o", f2, "-f", "--quality=65-80"], stderr=subprocess.PIPE)
            continue
        print("Progress")
        subprocess.call(["magick", f, f2], stderr=subprocess.PIPE)
        


