#!/usr/bin/env python3

import sys
sys.setrecursionlimit(2 ** 30)

from memoized import memoized

def twovaluation(x):
  if x == 0: return 0
  y = x
  result = 0
  while not y&1:
    y //= 2
    result -= 1
  return result

# same as in https://cr.yp.to/papers.html#efd
# except that here we exclude negative r
def chain(m,n):
  assert m >= 3
  assert m&1
  assert n >= 0

  if n == 2 or ((n&1) and n <= m): 
    return [1,2]+list(range(3,m+1,2))

  if n == m+2:
    return chain(m,m)+[n]

  if n%6 == 1 and m+4 <= n and n <= 3*m-2:
    return chain(m,m)+[(2*n+4)//3,n]

  if n%6 == 3 and m+4 <= n and n <= 3*m:
    return chain(m,m)+[(2*n)//3,n]

  if n%6 == 5 and m+4 <= n and n <= 3*m-4:
    return chain(m,m)+[(2*n-4)//3,n]

  if n%4 == 0 and 4 <= n and n <= 2*m-2:
    return chain(m,m)+[n]

  if n&1:
    L = [(twovaluation(n-r),r) for r in range(1,m+1,2)]
    L.sort()
    _,r = L[0]
    return chain(m,n-r)+[n]
  return chain(m,n//2)+[n]

def chain_it(m,n):
  C = []

  while not (n == 2 or ((n&1) and n <= m)):
    assert m >= 3
    assert m&1
    assert n >= 0
    if n == m+2:
      C = [n] + C
      n = m
      continue
    if n%6 == 1 and m+4 <= n and n <= 3*m-2:
      C = [(2*n+4)//3,n] + C
      n = m
      continue
    if n%6 == 3 and m+4 <= n and n <= 3*m:
      C = [(2*n)//3,n] + C
      n = m
      continue
    if n%6 == 5 and m+4 <= n and n <= 3*m-4:
      C = [(2*n-4)//3,n] + C
      n = m
      continue
    if n%4 == 0 and 4 <= n and n <= 2*m-2:
      C = [n] + C
      n = m
      continue
    if n&1:
      L = [(twovaluation(n-r),r) for r in range(1,m+1,2)]
      L.sort()
      _,r = L[0]
      C = [n] + C
      n = n-r
      continue
    C = C + [n]
    n = n//2
  C.sort()
  C = [1,2]+list(range(3,m+1,2)) + C

  return C

def cost2(C):
  result = [0,0]
  for n in C:
    if n == 1:
      continue
    if n&1 == 0 and n//2 in C:
      result[1] += 1
    else:
      assert any(n-m in C for m in C)
      result[0] += 1
  return tuple(result)

def cost(C):
  result = cost2(C)
  return 10*result[0]+8*result[1]

@memoized
def chain2(n):
#   print("new prime = " + str(n.bit_length()))
  m = 3
  bestm = 3
  C = chain(m,n)
#  C = chain_it(m,n) 
  oldcost = cost(C)
  count = 0 
  while True:
    count += 1
    m += 2
    # if(m==145):
    #     print("")
    if 2*m > 3*bestm+10:
    #   print("bestm = " + str(bestm) + " cost = " + str(cost(C)))
    #   sys.stdout.flush()
      return C
    # C2 = chain_it(m,n)
    C2 = chain(m,n)
    newcost = cost(C2)
    # print(str(n.bit_length()) + " : " + str(count) + ": " + " m = " + str(m) + " cost = " + str(newcost), flush=True)    
    # sys.stdout.flush()
    # assert C3 == C2
    # print("cost = " + str(cost(C2)) + " 2*m = " + str(2*m) + " 3*best+10 = " + str(3*bestm+10))
    if newcost < oldcost:
      bestm = m
      C = C2
      oldcost = cost(C)
    
def code(C):
  C.sort()
  result = ''

  insn = []
  uses = {}

  for n in C:
    uses[n] = 0
    if n == 1:
      insn += [(1,'init',())]
      continue
    if n&1 == 0 and n//2 in C:
      rep = 1
      m = n//2
      while m&1 == 0 and m//2 in C:
        rep += 1
        m //= 2
      insn += [(n,'sq_rep',(m,-rep))]
      uses[m] += 1
      continue
    ok = False
    for m in C:
      if n-m in C:
        insn += [(n,'mul',(m,n-m))]
        uses[m] += 1
        uses[n-m] += 1
        ok = True
        break
    assert ok

  uses[max(C)] = 1

  decl = set() # registers declared
  regs = set() # currently used registers
  m2reg = {} # mapping m to register containing m

  for j in range(len(insn)):
    n,op,inputs = insn[j]

    clearregs = []

    for m in inputs:
      if m < 0: continue
      assert uses[m] >= 1
      uses[m] -= 1
      if uses[m] == 0:
        clearregs += [m]

    if uses[n] == 0: continue

    if len(clearregs) > 0:
      nreg = min(m2reg[m] for m in clearregs)
    else:
      nreg = 0
      while nreg in regs:
        nreg += 1

    if nreg not in decl:
      result += '  fp r%d;\n' % nreg
      decl.add(nreg)

    if op == 'init':
      assert len(inputs) == 0
    #   result += '  r%d = *x; // %d\n' % (nreg,n)
    #   result += '  r%d = *x;\n' % (nreg)
      result += '  fp_copy(r%d,x);\n' % (nreg)

    if op == 'sq_rep':
      assert len(inputs) == 2
      m,rep = inputs
      rep = -rep
      if nreg != m2reg[m]:
        result += '  fp_sqr(r%d,r%d);\n' % (nreg,m2reg[m])
        rep -= 1
      if rep > 0:
        if rep > 1:
          result += '  fp_sq1_rep(r%d,%d);\n' % (nreg,rep)
        else:
          result += '  fp_sq1(&r%d);\n' % (nreg)

    if op == 'mul':
      assert len(inputs) == 2
      m1,m2 = inputs
      if nreg == m2reg[m1]:
        # result += '  fp_mul2(&r%d,&r%d); // %d\n' % (nreg,m2reg[m2],n)
        result += '  fp_mul(r%d,r%d,r%d);\n' % (nreg,nreg,m2reg[m2])
      elif nreg == m2reg[m2]:
        # result += '  fp_mul2(&r%d,&r%d); // %d\n' % (nreg,m2reg[m1],n)
        result += '  fp_mul(r%d,r%d,r%d);\n' % (nreg,nreg,m2reg[m1])
      else:
        # result += '  fp_mul3(&r%d,&r%d,&r%d); // %d\n' % (nreg,m2reg[m1],m2reg[m2],n)
        result += '  fp_mul(r%d,r%d,r%d);\n' % (nreg,m2reg[m1],m2reg[m2])        

    for m in clearregs:
      regs.remove(m2reg[m])
      m2reg.pop(m)

    m2reg[n] = nreg
    regs.add(nreg)

  result += '  fp_copy(x,r%d);\n' % nreg
  return result
  
def main():
    print(chain2(51111173281739182739182798111111))

if __name__ == "__main__":
    main()  
