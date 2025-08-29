# https://www.youtube.com/watch?v=rw4s4M3hFfs

blocks = [
	{
		"gym": False,
		"school": True,
		"store": False
	},
	{
		"gym": True,
		"school": False,
		"store": False
	},
	{
		"gym": True,
		"school": True,
		"store": False
	},
	{
		"gym": False,
		"school": True,
		"store": False
	},
	{
		"gym": False,
		"school": True,
		"store": True
	}
]

vectors = [
    ["gym", "school", "store"], 3,
    ["store"], 4,
    ["gym", "store"], 3,
    ['school'], 0
]

# very slow implementation
def brute_force():
    def min_distance(block_index: int, req: str): # O(len(blocks))
        if blocks[block_index][req] == True:
            return 0
        di = 1
        while block_index - di > -1 or block_index + di < len(blocks):
            l, r = block_index - di, block_index + di
            if l > -1 and blocks[l][req] == True:
                break
            if r < len(blocks) and blocks[r][req] == True:
                break
            di += 1
        return di

    index = -1
    minmax_distance = len(blocks)
    for block_idx in range(len(blocks)): # O(len(req) * len(blocks) * len(blocks))
        distance = max(min_distance(block_idx, r) for r in reqs)
        if distance < minmax_distance:
            minmax_distance = distance
            index = block_idx
    return index

for i in range(0, len(vectors), 2):
    reqs = vectors[i]
    expected = vectors[i + 1]
    returned = brute_force()
    print(f'block index {returned}')
    assert expected == returned, f'for {reqs} expected {expected}, but returned {returned}'
