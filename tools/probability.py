import itertools
from collections import Counter

# distribuição 2d6
rolls = [a+b for a in range(1,7) for b in range(1,7)]
dist = Counter(rolls)
total = 36

def p_at_least(target):
    return sum(c for v,c in dist.items() if v>=target)/total

# bônus = atributo(0-5) + pericia(0-5) -> 0 a 10
difficulties = [6,8,10,12,14,16,18]
bonuses = {
    "destreinado (0)":0,
    "iniciante (1)":1,
    "competente (3)":3,
    "especialista (5)":5,
    "veterano (7)":7,
    "mestre (10)":10,
}

print(f"{'Bônus':18}", *[f"D{d:>3}" for d in difficulties])
for name,b in bonuses.items():
    row=[]
    for d in difficulties:
        need = d-b
        p = p_at_least(need) if need<=12 else 0.0
        row.append(f"{p*100:5.1f}%")
    print(f"{name:18}", *row)

print("\n--- Margem: bandas para diversos confrontos bônus x dificuldade ---")
bands = [(-999,-5,"Falha crítica"),(-4,-1,"Falha"),(0,3,"Sucesso"),(4,6,"Sucesso excepcional"),(7,999,"Sucesso extraordinário")]

def band_dist(bonus, difficulty):
    counts = {name:0 for _,_,name in bands}
    for roll,c in dist.items():
        margin = roll+bonus-difficulty
        for lo,hi,name in bands:
            if lo<=margin<=hi:
                counts[name]+=c
                break
    return {k: v/total*100 for k,v in counts.items()}

# testar confrontos "equilibrados" (chance de sucesso ~40-70%) e um "mestre vs fácil"
tests = [
    ("destreinado vs facil(8)", 0, 8),
    ("competente vs normal(10)", 3, 10),
    ("especialista vs dificil(12)", 5, 12),
    ("veterano vs muito dificil(14)", 7, 14),
    ("mestre vs facil(8) [overkill]", 10, 8),
]
for name,b,d in tests:
    r = band_dist(b,d)
    print(name, {k: f"{v:.0f}%" for k,v in r.items()})

print("\n--- Bandas de margem REVISADAS ---")
bands2 = [(-999,-4,"Falha crítica"),(-3,-1,"Falha"),(0,2,"Sucesso"),(3,3,"Sucesso excepcional"),(4,999,"Sucesso extraordinário")]
def band_dist2(bonus, difficulty):
    counts = {name:0 for _,_,name in bands2}
    for roll,c in dist.items():
        margin = roll+bonus-difficulty
        for lo,hi,name in bands2:
            if lo<=margin<=hi:
                counts[name]+=c
                break
    return {k: round(v/total*100,1) for k,v in counts.items()}
for name,b,d in tests:
    print(name, band_dist2(b,d))
