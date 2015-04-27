# angry-grandpa
Stabilizes Sonos volume across time

Do you have a Sonos player at work? Does a rude coworker insist on playing _Where Da Hood At?_ at 9:30 AM on full volume?

Show your coworkers who's boss with angry-grandpa. This sweet little jimmy will slowly and periodically decrease your Sonos
player's volume to a provided threshold. Just keep it running in the background and enjoy working in (near-) silence.

angry-grandpa runs in Vagrant VM with a public IP address, which should help prevent detection. To further cloak itself, angry-grandpa
also randomizes the check-in delay when the volume is at an acceptable level.

## Running angry-grandpa
- `vagrant up`
- `cd /vagrant`
- `python angrygrandpa.py`
