import sys

n = int(input().strip())
genes = input().strip().split(' ')
health = map(int, input().strip().split(' '))
s = int(input().strip())


class dna_determine(object):
    def __init__(self):
        self.lists = {}
        self.i = []


def d(n, lists):
    for i in range(len(lists)):
        f(lists[i][0], lists[i][1], n)
    for k in n.lists:
        if len(n.lists[k]) > 1: n_l = dna_determine(); d(n_l, n.lists[k]); n.lists[k] = [n_l, None]


def func_search(i, x, n):
    if len(x) >= 1:
        if x[0] not in n.lists:
            n.lists[x[0]] = [[i, x[1:]]]
        else:
            n.lists[x[0]].append([i, x[1:]])
    else:
        n.i.append(i)


def do_ac(d, di, k, s_m):
    if k.i:
        for ki in k.i:
            if start <= ki <= end: s_m += health[ki]
    if di < len(d) and d[di] in k.lists:
        if len(k.lists[d[di]]) == 1:
            ti, ts = k.lists[d[i]][0][0], k.lists[d[di]][0][1]
            if (i + 1 + len(ts) <= len(d) and d[i:i + 1 + len(ts)] == d[di] + ts and start <= ti <= end):
                s_m += health[ti]
        else:
            nr2.append(k.lists[d[di]][0])
    return s_m


rt = dna_determine()
d(rt, [[i, genes[i]] for i in range(len(genes))])
MAX, MIN = -1000000000000000000000, 1000000000000000000000

for a0 in range(s):
    start, end, d = input().strip().split(' ')
    start, end, d = [int(start), int(end), str(d)]
    s_m, nr1 = 0, []
    for i in range(len(d)):
        nr2 = []
        s_m = do_ac(d, i, rt, s_m)
        for k in nr1:
            s_m = do_ac(d, i, k, s_m)
        nr1 = nr2
    for k in nr1:
        s_m = do_ac(d, len(d), k, s_m)
    MAX, MIN = max(s_m, MAX), min(s_m, MIN)
print(str(MIN) + ' ' + str(MAX))






#################################
from math import inf
from bisect import bisect_left as bLeft, bisect_right as bRight
from collections import defaultdict

# ------------------------------------------------------------------------------
def getHealth(seq, first, last, largest):
  h, ls = 0, len(seq)
  for f in range(ls):
    for j in range(1, largest+1):
      if f+j > ls: break
      sub = seq[f:f+j]
      if sub not in subs: break
      if sub not in gMap: continue
      ids, hs = gMap[sub]
      h += hs[bRight(ids, last)]-hs[bLeft(ids, first)]
  return h

# ------------------------------------------------------------------------------
howGenes = int(input())
genes = input().rstrip().split()
healths = list(map(int, input().rstrip().split()))
howStrands = int(input())
gMap = defaultdict(lambda: [[], [0]])
subs = set()
for id, gene in enumerate(genes):
  gMap[gene][0].append(id)
  for j in range(1, min(len(gene), 500)+1): subs.add(gene[:j])
for v in gMap.values():
  for i, ix in enumerate(v[0]): v[1].append(v[1][i]+healths[ix])

# ------------------------------------------------------------------------------
largest = max(list(map(len, genes)))
hMin, hMax = inf, 0
for _ in range(howStrands):
  firstLastd = input().split()
  first = int(firstLastd[0])
  last = int(firstLastd[1])
  strand = firstLastd[2]
  h = getHealth(strand, first, last, largest)
  hMin, hMax = min(hMin, h), max(hMax, h)
print(hMin, hMax)