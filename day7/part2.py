
import re
import sys

class GATE:
    def __init__(self, *args):
        array = list(args)
        self.op = array.pop(0)
        self.args = array
        self.result = None

    def opNOT(self):
        x = self.args[0]
        if isinstance(x, int):
            x &= 0xffff
            self.result = ~x
            self.result &= 0xffff
        return self.result

    def opANDOR(self):
        x = self.args[0]
        y = self.args[1]
        if isinstance(x, int) and isinstance(y, int):
            x &= 0xffff
            y &= 0xffff
            if self.op == 'AND':
                self.result = x & y
            elif self.op == 'OR':
                self.result = x | y
            else:
                # should never get here!
                raise Exception('ERROR in opANDOR')
            self.result &= 0xffff
        return self.result

    def opSHIFT(self):
        x = self.args[0]
        if isinstance(x, int):
            x &= 0xffff
            if self.op == 'LSHIFT':
                self.result = x << self.args[1]
            elif self.op == 'RSHIFT':
                self.result = x >> self.args[1]
            else:
                # should never get here!
                raise Exception('ERROR in opSHIFT')
            self.result &= 0xffff
        return self.result

    def __call__(self):
        execute = {
            'NOT': self.opNOT,
            'AND': self.opANDOR,
            'OR': self.opANDOR,
            'LSHIFT': self.opSHIFT,
            'RSHIFT': self.opSHIFT
        }
        return execute[self.op]()

    def __str__(self):
        return "{}{}".format(self.op, str(tuple(self.args)))

wires = dict()
toResolve = []
ops = [ "AND", "OR", "NOT", "LSHIFT", "RSHIFT" ]

with open(sys.argv[1]) as f:
    for line in f:
        op, dest = line.strip().split(' -> ')
        toResolve.append(dest)
        array = op.split(' ')
        for i, s in enumerate(array):
            try:
                # try to resolve any numeric signals to 16-bit values
                array[i] = int(s) & 0xffff
            except:
                pass
            # move instruction to index 0
            if s in ops:
                array.pop(i)
                array.insert(0, s)
        # we have either a signal or wire
        if len(array) == 1:
            if isinstance(array[0], int):
                toResolve.pop(-1)
            wires.setdefault(dest, array[0])
        else:
            wires.setdefault(dest, GATE(*array))

def resolve(w):
    v = wires[w]

    # already resolved
    if isinstance(v, int):
        #print(w,'SIGNAL',str(v))
        return v
    
    # wire reference
    if isinstance(v, str):
        #print(w,'WIRE',str(v))
        return resolve(v)
    
    # gate output
    if isinstance(v, GATE):
        #print(w,'GATE',str(v))
        value = v()
        # gate is already resolved
        if isinstance(value, int):
            return value
        # resolve the gate inputs
        for i, a in enumerate(v.args):
            if isinstance(a, str):
                v.args[i] = resolve(a)
        # return the gate output
        return v()
    
    print('WTF!')
    raise Exception('ERROR in resolve', w, str(v), type(v))

# override 'b' with the value of 'a' from part1
wires['b'] = 46065

while toResolve:
    w = toResolve.pop(0)
    #print(len(toResolve),w)
    wires[w] = resolve(w)

for w in sorted(wires):
    print('{}: {}'.format(w, str(wires[w])))
