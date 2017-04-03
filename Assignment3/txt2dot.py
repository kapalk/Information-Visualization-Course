import sys

nodes = {}
edges = []
cnt = 1

for x in open(sys.argv[1]):
	[a, b] = x.strip().split(';')
	if not a in nodes:
		nodes[a] = cnt
		cnt = cnt + 1
	if not b in nodes:
		nodes[b] = cnt
		cnt = cnt + 1
	edges.append([nodes[a], nodes[b]])

print 'graph {'
for n in nodes.keys():
	print 'n%d [label = "%s"];' % (nodes[n], n)
for e in edges:
	print 'n%d -- n%d;' % (e[0], e[1]);
	
print '}'
