import random

def foo(x,y,z):
    return x**3 + 0*y**2 + 0*z

def fitness(x,y,z):
    ans = foo(x,y,z)

    if ans == 0:
        return 99999
    else:
        return abs(1/ans)

solution = []
for s in range(10000):
    solution.append( (random.uniform(0,1000),
                     random.uniform(0,10000),
                     random.uniform(0,10000)))

for i in range(5):

    rankedsolution = []
    for s in solution:
        rankedsolution.append((fitness(s[0],s[1],s[2]),s) )
    rankedsolution.sort()
    rankedsolution.reverse()

    print(f'== Gen {i} best solution ===')
    print(rankedsolution[0])

    #if rankedsolution[0][0] > 999:
     #   break

    bestsolution = rankedsolution[:100]
    elements = []

    for s in bestsolution:
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])

    newGen = []
    for i in range(1000):
        e1 = random.choice(elements) * random.uniform(0.99,1.01)
        e2 = random.choice(elements) * random.uniform(0.99,1.01)
        e3 = random.choice(elements) * random.uniform(0.99,1.01)

        newGen.append((e1,e2,e3))

    solution = newGen
