import subprocess

import os

p = os.getcwd()

for i in os.walk('.'):
    for f in i[2]:
        if not f.endswith('.bmp'):
            continue
        print(f)
        subprocess.call(["magick", p+'/'+i[0] + '/'+f, p+'/'+i[0] + '/'+ f[:-4] + ".png"], stderr=subprocess.PIPE)
        


