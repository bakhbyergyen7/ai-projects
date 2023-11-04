from random import random

TRIALS = 10**6

evidence = 0
query = 0
pall = []
pdenomall = []
joint_observed = 0
pjointall = []

for trial in range(1, TRIALS + 1):
    randA, randB, randC, randD = (random() for i in range(4))
    A = (randA < 1/2)
    if A:
        B = (randB < 1)
        C = (randC < 1)
    else:
        B = (randB < 1/2)
        C = (randC < 1/2)

    if B and C:
        D = (randD < 1)
    elif B and not C:
        D = (randD < 1/2)
    elif not B and C:
        D = (randD < 1/2)
    else:
        D = (randD < 0)

    if D:
        evidence += 1
        if A:
            query += 1
        p = query/evidence
        pall.append(p)
    pdenom = evidence/trial
    pdenomall.append(pdenom)

print("P(A | D) ~=", pall[-1])

import matplotlib.pyplot as plt

plt.plot(pall)
plt.plot(pdenomall)