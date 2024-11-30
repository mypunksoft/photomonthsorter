import os
from exif import Image
from glob import glob
fils = glob(os.path.join('./', '*.jpg'))
kol = len(fils)
for i in range(kol):
  with open(fils[i], "rb") as pl:
    image = Image(pl)
    mes = image.datetime_original[5:7]
  if os.path.isdir(mes):
    os.rename(f'{fils[i]}', f'./{mes}/{fils[i]}')
  else:
    os.mkdir(mes)
    os.rename(f'{fils[i]}', f'./{mes}/{fils[i]}')
