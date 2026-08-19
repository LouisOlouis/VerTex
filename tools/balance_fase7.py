import random
def roll2d6(): return random.randint(1,6)+random.randint(1,6)
def roll_die(n): return random.randint(1,n)

def fight(pj_bonus, pj_vit, pj_def, pj_dmg, pj_armor,
          e_bonus, e_vit, e_def, e_dmg, trials=15000):
    wins=0; rounds_total=0; dmg_dealt_total=0
    for _ in range(trials):
        v=pj_vit; ev=e_vit; rounds=0; dmg_dealt=0
        while v>0 and ev>0 and rounds<40:
            rounds+=1
            for _ in range(2):
                if roll2d6()+pj_bonus>=e_def:
                    d=roll_die(pj_dmg); ev-=d; dmg_dealt+=d
                if ev<=0: break
            if ev<=0: break
            if roll2d6()+e_bonus>=pj_def:
                v-=max(0,roll_die(e_dmg)-pj_armor)
        rounds_total+=rounds; dmg_dealt_total+=dmg_dealt
        if v>0 and ev<=0: wins+=1
    return wins/trials, rounds_total/trials, dmg_dealt_total/trials

perfis = [
    ("Fraco     (bonus2, vit12, def9,  armor0, dano1d6)", 2,12,9,6,0),
    ("Medio     (bonus5, vit14, def10, armor1, dano1d8)", 5,14,10,8,1),
    ("Especial. (bonus7, vit16, def11, armor1, dano1d10)",7,16,11,10,1),
    ("Otimizado (bonus8, vit18, def12, armor2, dano1d10)",8,18,12,10,2),
]
print("vs Inimigo Padrao Nivel2 (bonus5, vit14, def10, dano1d8)")
print(f"{'perfil':52}{'vitoria':>10}{'rodadas':>10}{'dano causado':>14}")
for name,b,vit,de,dmg,ar in perfis:
    w,r,d = fight(b,vit,de,dmg,ar, 5,14,10,8)
    print(f"{name:52}{w*100:>9.1f}%{r:>10.1f}{d:>14.1f}")
