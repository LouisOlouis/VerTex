import random

def roll2d6():
    return random.randint(1,6)+random.randint(1,6)

def roll_die(n):
    return random.randint(1,n)

WEAPONS = {
    "Soco": (4,0),
    "Faca": (6,0),
    "Espada": (8,0),
    "Machado": (10,0),
    "Pistola": (8,0),
    "Rifle": (10,0),
    "Arma pesada": (12,0),
}

def vitalidade(vigor):
    return 10 + vigor*2

def defesa(agilidade):
    return 8 + agilidade

def simulate_fight(atk_bonus, dmg_die, def_target, vit_target, armor, atk_actions=2, trials=20000):
    rounds_list=[]
    for _ in range(trials):
        vit=vit_target
        rounds=0
        while vit>0 and rounds<50:
            rounds+=1
            for _ in range(atk_actions):
                total = roll2d6()+atk_bonus
                if total>=def_target:
                    dmg = max(0, roll_die(dmg_die)-armor)
                    vit-=dmg
                if vit<=0: break
        rounds_list.append(rounds)
    return sum(rounds_list)/len(rounds_list)

print(f"{'cenário':45}{'rodadas médias p/ derrotar'}")
cenarios = [
    ("PJ médio (bonus5, espada1d8) vs inimigo médio (def10,vit14,armor1)", 5, 8, 10, 14, 1),
    ("PJ fraco (bonus2, faca1d6) vs inimigo médio (def10,vit14,armor1)", 2, 6, 10, 14, 1),
    ("PJ especializado (bonus8, espada1d8) vs inimigo médio (def10,vit14,armor1)", 8, 8, 10, 14, 1),
    ("PJ médio (bonus5, rifle1d10) vs inimigo blindado (def10,vit18,armor3)", 5, 10, 10, 18, 3),
    ("PJ médio (bonus5, arma pesada1d12) vs inimigo médio (def10,vit14,armor1)", 5, 12, 10, 14, 1),
]
for name, ab, dd, dt, vt, ar in cenarios:
    r = simulate_fight(ab, dd, dt, vt, ar)
    print(f"{name:70}{r:.2f}")
