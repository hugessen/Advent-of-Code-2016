def find_adjacent_states(floors_state, elev):
	floor = elev['floor']
	
	
def will_irradiate(floors_state, elev):
	floor = elev['floor']
	if not elev['has_pair']: # Floor gens > Elev chips
		for chip in elev['chips']:
			if not chip in floors_state[floor]['gens']:
				return True
	if len(elev['gens']) is not 0: # Elev gens > Floor chips
		for chip in floors_state[floor]['chips']:
			if not chip in floors_state[floor]['gens'] and not chip in elev['gens']:
				return True # Floor chip gets KOd
	return False

def elev_safe(elev):
	if elev['chips'] == [] and elev['gens'] == []:
		return False
	if len(elev['chips']) == 2:
		return True
	if len(elev['chips']) == 1:
		if len(elev['gens']) == 0:
			return True
		if elev['chips'][0] == elev['gens'][0]:
			return True
		else:
			return False

def has_pair(elev):
	if len(elev['chips']) == 1 and len(elev['gens']) == 1 and elev['chips'][0] == elev['gens'][0]:
		return True
	return False

def state_hash(floors_state, elev):
	hsh = ''
	for floor in floors_state:
		for gen in floor['gens']:
			hsh += gen
		hsh += ' '
		for chip in floor['chips']:
			hsh += chip
		hsh += '\n'

floors = [
{gens:['S','P'], chips: ['S','P']},
{gens:['T','R','C'], chips: ['R','C']},
{gens:[], chips: ['T']},
{gens:[], chips: []} ]
elev = { floor: 0, gens: [], chips: [], has_pair: False }
visited_states = []