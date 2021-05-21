#!/usr/bin/env python3

class Ritual:
	def __init__(self, invocation, penance, ingredients):
		self._invocation  = invocation
		self._penance     = penance
		self._ingredients = ingredients
		
	def summon(self, namedOne):
		print(f"You request to summon {namedOne}, if you are willing to pay the price.")
		print("Are you willing? [y/n]")
		
		n = input()
		if n.upper() not in ['Y', 'YES', 'N', 'NO']:
			print("Your request is denied. You offend with clumsy responses.")
		else:
			if n in ['Y', 'YES']:
				print(f"SUMMONING {namedOne}")
				print("....insert obscure occult symbols here......")
				self.awaken()
			else:
				print("The ground opens beneath you, and you are swallowed into a bottomless chasm.")
	
	def awaken(self):
		print("[STATUES CRUMBLING, EARTH CRACKING, TORCHES SIMULTANEOUSLY SNUFFED OUT, BLOOD RUNS THROUGH STONE CHANNELS]")
		print("[OTHER STANDARD RITUALISTIC STUFF HAPPENS]")
		
		
r = Ritual('git gud.', 'one recycled aluminum can', ['tofurkey', 'spatula', 'garden hose', 'can of spam'])

r.summon('Big Jimmy')

