# RAÇAS (Módulo Opcional)

Por padrão todo personagem é um humano comum. Este módulo entra se a campanha tiver espaço para povos e ancestralidades diferentes — desde o elenco clássico de RPG (elfos, anões, orcs) até algo específico da sua ambientação. Ver também `MAGIA.md` (algumas raças começam com afinidade arcana) e `INFECCAO.md` (uma raça nasce da própria Infecção).

## 1. Como funciona

Cada Raça faz duas coisas, sempre juntas, para manter o total de pontos do personagem igual ao de qualquer outro:

1. **Desloca 1 ponto** entre dois Atributos do array já distribuído (+1 em um, −1 em outro — a soma continua 15, `CRIACAO_PERSONAGEM.md` §2).
2. Concede uma **Habilidade Única de Raça**, em 3 Estágios, como as Classes (`CLASSES.md` §3).

## 2. Raças

### Humano
Sem talento inato dominante — mas versátil o bastante para compensar.
- **Deslocamento:** nenhum
- **Habilidade (Estágio 1) — Adaptável:** +1 Perícia extra na criação (7 pontos em vez de 6)
- Sem restrição

### Elfo
Longevo, gracioso, com afinidade natural para o arcano.
- **Deslocamento:** Agilidade +1 / Força −1
- **Habilidade (Estágio 1) — Sentidos Élficos:** nunca é surpreendido em ambientes naturais; se `MAGIA.md` estiver ativo, começa com Nível de Conexão 1 em 1 Arcano à escolha
- **Restrição:** −1 em testes de Força relacionados a carga/quebra (ex: arrombar algo à força)

### Anão
Resistente, teimoso, ligado à tradição e ao trabalho manual.
- **Deslocamento:** Vigor +1 / Agilidade −1
- **Habilidade (Estágio 1) — Sangue de Pedra:** ignora o primeiro Nível de Exausto ou Envenenado adquirido em uma cena
- **Restrição:** Movimento −1 (passo mais curto e pesado)

### Orc
Força bruta e resistência à dor — mais temido do que ouvido.
- **Deslocamento:** Força +1 / Intelecto −1
- **Habilidade (Estágio 1) — Fúria Contida:** enquanto Ferido ou Gravemente Ferido, ganha +1 de dano corpo a corpo
- **Restrição:** −1 em testes de Enganação (expressões e intenções são difíceis de disfarçar)

### Pequenino (Halfling)
Pequeno, ágil, difícil de notar e mais difícil ainda de acertar.
- **Deslocamento:** Agilidade +1 / Vigor −1
- **Habilidade (Estágio 1) — Sortudo:** 1 ponto de Sorte adicional (4 no total em vez de 3)
- **Restrição:** Capacidade de carga −1 espaço

### Meio-Elfo
Não totalmente de nenhum dos dois mundos — e por isso confortável em muitos.
- **Deslocamento:** Percepção +1 / Vontade −1
- **Habilidade (Estágio 1) — Entre Dois Mundos:** pode escolher a Habilidade de Estágio 1 de Elfo **ou** de Humano no lugar da própria, no momento da criação
- Sem restrição adicional

### Tocado pelo Arcano *(requer módulo `MAGIA.md`)*
Nascido com um Arcano já latente na alma, antes mesmo de aprender a controlá-lo.
- **Deslocamento:** Vontade +1 / Força −1
- **Habilidade (Estágio 1) — Afinidade:** começa com Nível de Conexão Arcana 1 em 1 Arcano à escolha, de graça
- **Restrição:** a Infecção Arcana daquele Arcano nunca cai abaixo do Nível 1 por tratamento comum

### Enraizado na Infecção *(usa `INFECCAO.md`)*
Sobreviveu a uma exposição severa antes mesmo da história começar — e carrega isso no corpo.
- **Deslocamento:** Vigor +1 / Agilidade −1
- **Habilidade (Estágio 1) — Sangue Contaminado:** começa a campanha com 1 Dádiva de Infecção Nível 2 já aceita
- **Restrição:** começa com Nível de Infecção 2, não removível abaixo disso (mesmo custo que qualquer personagem pagaria chegando lá jogando)

## 3. Progressão da Habilidade Única (por Missão)

Mesma estrutura das Classes (`CLASSES.md` §3): Estágio 2 exige 1 Missão de Origem, Estágio 3 exige uma 2ª Missão mais significativa. Como criar uma Missão de Origem: ver `MESTRE.md` §10.

**Exemplo de progressão** — Sangue de Pedra (Anão): Estágio 1 ignora o 1º Nível de Exausto/Envenenado da cena; Estágio 2 (após a Missão) passa a ignorar até o 2º Nível; Estágio 3 (2ª Missão) também reduz em 1 Nível qualquer Condição física adquirida em combate (não zera, só reduz o pior golpe).

## 4. Criando uma Raça nova

| Campo | Regra |
|---|---|
| Nome | livre |
| Deslocamento de Atributo | +1 em um, −1 em outro (nunca sem compensação) |
| Habilidade Única, Estágio 1 | qualitativa, nunca um bônus numérico livre — segue `HABILIDADES.md` §2 |
| Restrição | algo que essa Raça tem mais dificuldade em fazer, equilibrando a Habilidade |

## 5. Compatibilidade

Raça, Classe e Magia são três módulos independentes — qualquer combinação funciona, porque nenhum dos três soma pontos além do que a criação de personagem já define.
