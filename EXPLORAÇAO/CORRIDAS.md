# CORRIDAS E PERSEGUIÇÕES

Uma corrida ou perseguição é dividida em **Trechos** — uma medida abstrata de distância, não metros exatos. Uma corrida curta tem 5 Trechos até a meta; uma perseguição longa pela cidade pode ter 10.

## 1. Estrutura da Rodada

Igual ao combate: **3 ações por rodada**, entre:

- **Acelerar** — teste de Agilidade + Pilotagem (ou Atletismo, se for corrida a pé/monstro montado) vs a Dificuldade do trecho atual (terreno, clima, tráfego). Aplica a Margem de Sucesso normalmente:

| Margem | Efeito |
|---|---|
| Falha crítica | Acidente: perde 1 Trecho e sofre uma Condição (Fraturado ou Sangrando, à escolha do Mestre conforme a cena) |
| Falha | Nenhum avanço |
| Sucesso | Avança 1 Trecho |
| Sucesso excepcional | Avança 2 Trechos |
| Sucesso extraordinário | Avança 3 Trechos |

- **Manobra Arriscada** — em vez de Acelerar, o piloto pode tentar um atalho ou manobra fora do previsto: mesma rolagem, mas a Dificuldade sobe 1 degrau na tabela (ex: Normal 10 vira Difícil 12) e o resultado de Sucesso Excepcional/Extraordinário concede +1 Trecho extra sobre a tabela acima. É a principal ferramenta de quem está atrás na corrida para tentar alcançar.
- **Ultrapassar** — só é possível contra um oponente no mesmo Trecho: teste opposto de Agilidade+Pilotagem. Quem vence assume a posição à frente; empate mantém a ordem.

**Perseguições com pontos de partida diferentes:** quando os competidores não começam lado a lado (uma fuga, não uma corrida formal), trate a posição de cada um separadamente e narre a distância entre eles como a diferença de Trechos acumulados — não uma posição absoluta na pista. Ultrapassar só se aplica quando essa diferença chega a 0.
- **Atacar** — usa as regras de `COMBATE.md` normalmente, com a Defesa do alvo ajustada por velocidade relativa: +2 se o alvo está 1 ou mais Trechos à frente ou atrás (mais difícil acertar algo em movimento relativo diferente).
- **Desviar de Obstáculo** — quando o Mestre coloca um obstáculo (tráfego, destroços, terreno ruim) em um Trecho, é preciso um teste extra (mesma Dificuldade do trecho) antes de poder Acelerar nele; falha aqui não custa Trecho, só a ação.
- **Reparar/Estabilizar** — usa Tecnologia ou Medicina (se for montaria viva) para remover 1 Condição adquirida na corrida, sem avançar.

## 2. Por que isso não é só "uma sequência de testes de Atletismo"

A Margem já usada em todo o sistema controla o ritmo (evita "sim/não" simples); a Manobra Arriscada dá ao competidor atrás uma ferramenta ativa de virada de jogo em vez de deixar a corrida decidida pelo bônus inicial; Ultrapassar e Atacar tornam a posição relativa relevante turno a turno, não só o total de Trechos.

**Validação:** simulado (`/tools/race_sim.py`) confronto entre bônus variados em uma corrida de 8 Trechos usando só a ação Acelerar (sem manobras arriscadas). Resultado: a corrida dura em média 4 a 6 rodadas, tempo compatível com uma cena de tensão sem se arrastar; mas confirma que, **sem a Manobra Arriscada**, a diferença de bônus decide o vencedor de forma quase determinística (91–100% de vitória para quem tem mais bônus). Isso confirma a necessidade da Manobra Arriscada como mecanismo de catch-up — ver `BALANCEAMENTO.md`.

## 3. Veículos e Montarias

| Tipo | Modificador | Traço |
|---|---|---|
| A pé | +0 | usa Atletismo |
| Montaria comum | +1 | usa Sobrevivência para controle sob estresse |
| Veículo terrestre comum | +2 | usa Tecnologia para reparos |
| Veículo/montaria de alta performance | +3 | Manobra Arriscada não sobe de degrau de Dificuldade (só a versão base) |

O modificador do veículo soma ao teste de Acelerar/Manobrar, mas **não substitui Agilidade/Pilotagem** — um piloto destreinado num veículo rápido ainda pode falhar.

## 4. Recursos e Vitória

Combustível/fôlego/energia é rastreado como um recurso simples: **3 usos** de Acelerar "forçado" (ação extra além das 3 normais, disponível 1x por corrida) antes de precisar de 1 rodada de recuperação sem avançar. Vitória: primeiro a alcançar o Trecho final; numa perseguição (não uma corrida até a meta), vitória é abrir distância de 3+ Trechos do perseguidor ou ser alcançado por ele.

---
*Próxima seção (Exploração e Conflitos Sociais) em `REGRAS.md`.*
