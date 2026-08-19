import random

def roll2d6():
    return random.randint(1,6)+random.randint(1,6)

def simulate(bonus, trials=20000):
    exposures_list=[]
    for _ in range(trials):
        nivel=0
        exposures=0
        while nivel<6 and exposures<200:
            exposures+=1
            dif = 8+nivel  # resistir fica mais dificil conforme o nivel sobe
            total = roll2d6()+bonus
            if total<dif:
                nivel+=1
        exposures_list.append(exposures)
    return sum(exposures_list)/len(exposures_list)

for bonus in [1,3,5,7]:
    r = simulate(bonus)
    print(f"bonus resistencia {bonus}: media de {r:.1f} exposicoes ate Transformacao (nivel 6)")

print("\n--- Versão 2: dificuldade fixa por exposição (não escala com o nível) ---")
def simulate_fixed(bonus, dif=10, trials=20000):
    exposures_list=[]
    for _ in range(trials):
        nivel=0
        exposures=0
        while nivel<6 and exposures<200:
            exposures+=1
            total = roll2d6()+bonus
            if total<dif:
                nivel+=1
            else:
                # sucesso: chance de recuperar 1 nivel via tratamento leve, simulando jogo real
                pass
        exposures_list.append(exposures)
    return sum(exposures_list)/len(exposures_list)

for bonus in [1,3,5,7]:
    r = simulate_fixed(bonus)
    print(f"bonus {bonus}: media de {r:.1f} exposicoes ate Transformacao (dificuldade fixa 10)")

print("\n--- Versão 3: dificuldade cresce devagar (8 + nivel//2) ---")
def simulate_slow(bonus, trials=20000):
    exposures_list=[]
    for _ in range(trials):
        nivel=0
        exposures=0
        while nivel<6 and exposures<200:
            exposures+=1
            dif = 8 + nivel//2
            total = roll2d6()+bonus
            if total<dif:
                nivel+=1
        exposures_list.append(exposures)
    return sum(exposures_list)/len(exposures_list)

for bonus in [1,3,5,7]:
    r = simulate_slow(bonus)
    print(f"bonus {bonus}: media de {r:.1f} exposicoes ate Transformacao (crescimento lento)")
