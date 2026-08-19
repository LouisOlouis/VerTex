import random

def roll2d6():
    return random.randint(1,6)+random.randint(1,6)

def margin_result(total, dif):
    m = total-dif
    if m<=-4: return -1  # falha critica: acidente, perde posicao
    if m<=-1: return 0   # falha: sem avanco
    if m<=2: return 1    # sucesso
    if m==3: return 2    # excepcional
    return 3             # extraordinario

def simulate_race(bonusA, bonusB, dif=10, meta=8, trials=20000):
    winsA=0; rounds_list=[]
    for _ in range(trials):
        posA=0; posB=0; rounds=0
        while posA<meta and posB<meta and rounds<60:
            rounds+=1
            posA = max(0, posA + margin_result(roll2d6()+bonusA, dif))
            if posA>=meta: break
            posB = max(0, posB + margin_result(roll2d6()+bonusB, dif))
        rounds_list.append(rounds)
        if posA>=meta and posB<meta: winsA+=1
        elif posA>=meta and posB>=meta: winsA+=0.5
    return winsA/trials, sum(rounds_list)/len(rounds_list)

print(f"{'confronto':40}{'vitoria A':>12}{'rodadas media':>16}")
tests=[
    ("empate (5 vs 5)",5,5),
    ("competente vs fraco (5 vs 2)",5,2),
    ("especialista vs competente (7 vs 5)",7,5),
    ("especialista vs fraco (7 vs 2)",7,2),
]
for name,a,b in tests:
    wa, rr = simulate_race(a,b)
    print(f"{name:40}{wa*100:>11.1f}%{rr:>16.1f}")
