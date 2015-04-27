import soco

""" Prints something """
for zone in soco.discover():
  print zone.player_name
