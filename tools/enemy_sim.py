import random
def roll2d6(): return random.randint(1,6)+random.randint(1,6)
def roll_die(n): return random.randint(1,n)

def pj_survives_vs_group(pj_bonus, pj_vit, pj_def, pj_dmg_die, pj_armor,
                          n_enemies, e_bonus, e_dmg_die, e_vit, e_def, trials=8000):
    pj_wins=0
    for _ in range(trials):
        vit=pj_vit
        enemies=[e_vit]*n_enemies
        rounds=0
        while vit>0 and any(v>0 for v in enemies) and rounds<40:
            rounds+=1
            # PJ ataca 2x (2 acoes), foca 1 inimigo vivo por vez
            for _ in range(2):
                alive=[i for i,v in enumerate(enemies) if v>0]
                if not alive: break
                tgt=alive[0]
                if roll2d6()+pj_bonus>=e_def:
                    enemies[tgt]-=roll_die(pj_dmg_die)
            # inimigos vivos atacam, 1 acao cada
            for i,v in enumerate(enemies):
                if v>0:
                    if roll2d6()+e_bonus>=pj_def:
                        vit-=max(0,roll_die(e_dmg_die)-pj_armor)
            if vit<=0: break
        if vit>0 and not any(v>0 for v in enemies):
            pj_wins+=1
    return pj_wins/trials

print("PJ medio (bonus5, vit14, def10, espada1d8, armor1) vs grupo de minions Nivel1 (bonus4, def9, vit11, 1d6):")
for n in [1,2,3,4,5]:
    p = pj_survives_vs_group(5,14,10,8,1, n, 4, 6, 11, 9)
    print(f"  {n} minion(s): {p*100:.1f}% de vitoria do PJ")
