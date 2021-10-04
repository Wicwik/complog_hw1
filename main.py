# Author: Robert Belanec
# Choose and uncomment a sample test or specify vertices (numbers), edges (pairs of vertices) and colors (letters) 

# TEST1
vertices = [1, 2, 3, 4]
edges = [(1,2), (2,3), (3,4), (1,4)]
colors = ['a', 'b', 'c']

# TEST2
# vertices = [1, 2, 3, 4]
# edges = [(1,2), (3,4)]
# colors = ['a', 'b']

# TEST3
# vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# edges = [(1,2), (1,5), (1,6), (2,3), (2,6), (3,4), (3,6), (3,7), (4,7), (5,6), (5,8), (6,7), (6,8), (6,9), (7,9), (8,9)]
# colors = ['a', 'b', 'c']

# TEST4
# vertices = [1, 2, 3, 4]
# edges = [(1,2), (2,3), (3,4), (1,4)]
# colors = ['a', 'b', 'c', 'd']

# TEST5
# vertices = [1, 2, 3]
# edges = [(1,2), (2,3), (3,4), (1,4)]
# colors = ['a', 'b', 'c']

# TEST6
# vertices = [1, 2]
# edges = [(1,2)]
# colors = ['a']


output_file = 'output.txt'

f = open(output_file, 'w')

# remove invalid edges
to_remove = []
for e in edges:
	if e[0] not in vertices or e[1] not in vertices:
		to_remove.append((e[0], e[1]))

for e in to_remove:
	edges.remove(e)

# representing edges
to_found = edges.copy();
not_edges = []
for v in vertices:
	for vv in vertices:
		if v != vv and (v, vv) in to_found:
			f.write('edge({0},{1})\n'.format(v, vv))
			to_found.remove((v, vv))
		
		elif (v != vv) and (v, vv) not in edges and (vv, v) not in edges and (v, vv) not in not_edges and (vv, v) not in not_edges:
			f.write('-edge({0},{1})\n'.format(v, vv))
			not_edges.append((v, vv))

f.write('\n')

# every vertex must be colored
for v in vertices:
	for c in colors:
		if c == colors[-1]:
			f.write('color({0},{1})\n'.format(v, c))
		else:
			f.write('color({0},{1}) '.format(v, c))

f.write('\n')

# one vertex can't have two colors
for v in vertices:
	tried = []
	for c in colors:
		for cc in colors:
			if cc != c and (cc, c) not in tried and (c, cc) not in tried:
				tried.append((c,cc))
				f.write('-color({0},{1}) -color({0},{2})\n'.format(v, c, cc))

f.write('\n')

# neighbours cant have the same color
for e in edges:
	for c in colors:
		f.write('-color({0},{1}) -edge({0},{2}) -color({2},{1})\n'.format(e[0], c, e[1]))
	f.write('\n')

f.close()

print('[INFO] Output has been written to {0}'.format(output_file))
		