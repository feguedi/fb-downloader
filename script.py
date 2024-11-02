import os
import sys
from time import sleep
from datetime import datetime, time
from urllib.parse import urlparse


def exec():
  try:
    now = datetime.now()
    fecha = f"{now.year}{now.month}{now.day}"
    hora = f"{now.hour}{minute}{now.second}"
    args = sys.argv
    print(f"# args {len(args)}")
    print(f"args {args}")

    if len(args) != 2:
      return False

    url = args[1]
    parsed = urlparse(url)
    os.system(f"mkdir {fecha}_{hora}")
    cmd = os.system(f"yt-dlp {url} --hls-use-mpegts -k -o /"{fecha}_{hora}/%(title).180s.%(ext)s/"")

    return cmd
  except:
    return False


if __name__ == '__main__':
  while True:
    try:
      resp = exec()

      if resp == False:
        break

      sleep(5)
    except IOError:
      print('An error occurred trying to read the file.')
      break
    except KeyboardInterrupt as ki:
      print("El usuario termino la ejecucion")
      break
    except ValueError:
      print("Valor incorrecto")
      break
    except:
      print("Error en la ejecucion")
      break
