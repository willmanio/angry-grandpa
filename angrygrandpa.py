import getopt, random, sys, time

from soco import SoCo

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "v:z:", [ "volume=", "zone=" ])
  except getopt.GetoptError:
    fail()

  volume_limit = None
  zone = None

  for o, a in opts:
    if o in ("-v", "--volume"):
      volume_limit = int(a)
    elif o in ("-z", "--zone"):
      zone = a
    else:
      fail()

  if volume_limit is None or zone is None:
    fail()
  else:
    getangry(volume_limit, SoCo(zone))

def getangry(volume_limit, zone):
  while True:
    if zone.volume > volume_limit:
      new_volume = max(0, zone.volume - 5)
      print "Decreasing volume from {0} to {1}".format(zone.volume, new_volume)
      zone.volume = new_volume
      time.sleep(30)
    else:
      # Sleep a long time so we don't flood the network
      sleep_minutes = random.randrange(2,5)
      print "Everything's A-OK, checking again in {0} minutes".format(sleep_minutes)
      time.sleep(sleep_minutes * 60)
  
def fail():
  usage()
  sys.exit(2)

def usage():
  print "Usage: {0} -v <volume> -z <ipaddr>".format(sys.argv[0])

if __name__ == "__main__":
  main(sys.argv[1:])
  
