import os
import sys
from time import sleep


def exec():
  args = sys.argv
  print(f"# args {len(args)}")
  print(f"args {args}")

  if len(args) != 2:
    return False

  url = args[1]
  return url


if __name__ == '__main__':
  while True:
    try:
      resp = exec()

      if resp == False:
        break
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
