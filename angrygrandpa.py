import getopt, random, sys, time

from soco import SoCo

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "v:z:", [ "volume=", "zone=" ])
  except getopt.GetoptError:
    fail()

  volume = None
  zone = None

  for o, a in opts:
    if o in ("-v", "--volume"):
      volume = a
    elif o in ("-z", "--zone"):
      zone = a
    else:
      fail()

  if volume is None or zone is None:
    fail()
  else:
    getangry(volume, SoCo(zone))

def getangry(volume, zone):
  while True:
    if zone.volume > volume:
      print "Decreasing volume from %s towards %s" % connection.volume, volume
      zone.volume -= 5
      time.sleep(30)
    else:
      # Sleep a long time so we don't flood the network
      sleep_minutes = random.randrange(3, 8)
      print "Everything's A-OK, checking again in %s minutes" % sleep_minutes
      time.sleep(sleep_minutes * 60)
  
def fail():
  usage()
  sys.exit(2)

def usage():
  print 'Usage: ' + sys.argv[0] + ' -v <volume> -z <ipaddr>'

if __name__ == "__main__":
  main(sys.argv[1:])
  
