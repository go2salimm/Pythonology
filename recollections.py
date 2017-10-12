from collections import defaultdict, Counter, OrderedDict, deque
import json

colours = (
    ('Salim', 'Yellow'),
    ('Adam', 'Blue'),
    ('Omar', 'Green'),
    ('Adam', 'Black'),
    ('Salim', 'Red'),
    ('Jacob', 'Silver'),
)

favcolors = defaultdict(list)

for name, colour in colours:
    favcolors[name].append(colour)

print type(colours)
print favcolors



sd = {}
#sd['colors']['favorite'] = "blue"

tree = lambda : defaultdict(tree)
print type(tree)
sd = tree()
sd['colors']['favorite'] = "blue"
print json.dumps(sd)


coloursOrder = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in coloursOrder.items():
    print (key, value)

print coloursOrder
print coloursOrder["Green"]


favs = Counter( name for name, colour in colours)
print favs

with open('/tmp/wifi-U4GzeR.log', 'rb') as f:
    line_count = Counter(f)

f.close
print line_count


d = deque()
d.append('5')
d.append('2')
d.append('9')
print len(d)

print d[0]
print d[-1]
print d