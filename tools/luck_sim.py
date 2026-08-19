import itertools
from collections import Counter

def p_success_normal(need):
    c=0
    for a in range(1,7):
        for b in range(1,7):
            if a+b>=need: c+=1
    return c/36

def p_success_reroll_lowest(need):
    # joga 2d6, se falhar, pode escolher rerrolar o dado mais baixo uma vez (gasta 1 Sorte)
    total=0; succ=0
    for a in range(1,7):
        for b in range(1,7):
            total+=1
            s = a+b
            if s>=need:
                succ+=1
                continue
            # falhou: tenta usar sorte, rerrola o menor dos dois dados
            lo = min(a,b); hi = max(a,b)
            # probabilidade de sucesso apos rerrolar o dado baixo
            p_after = sum(1 for x in range(1,7) if hi+x>=need)/6
            succ += p_after
    return succ/total

print(f"{'need':>5}{'sem sorte':>12}{'com sorte (rerrola pior dado)':>32}{'ganho':>10}")
for need in range(4,14):
    p0 = p_success_normal(need)
    p1 = p_success_reroll_lowest(need)
    print(f"{need:>5}{p0*100:>11.1f}%{p1*100:>31.1f}%{(p1-p0)*100:>9.1f}pp")
