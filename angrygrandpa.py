import getopt, sys, time

from soco import SoCo

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "z:", [ "zone=" ])
  except getopt.GetoptError:
    fail()

  zone = None

  for o, a in opts:
    if o in ("-z", "--zone"):
      zone = a
    else:
      fail()

  if zone is None:
    fail()
  else:
    getangry(SoCo(zone))

def getangry(connection):
  while True:
    if connection.volume > 75:
      print "Decreasing volume from %s" % connection.volume
      connection.volume -= 5
    else:
      print "Everything's A-OK!"
    time.sleep(10)
  
def fail():
  usage()
  sys.exit(2)

def usage():
  print 'Usage: ' + sys.argv[0] + ' -z <ipaddr>'

if __name__ == "__main__":
  main(sys.argv[1:])
  
