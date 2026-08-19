# INIMIGOS

Regras de criação em `REGRAS.md`, seção 13. Este arquivo traz o catálogo pronto para uso e o modelo de ficha.

## Ficha de Inimigo (modelo)

- **Nome:**
- **Categoria:** Minion / Padrão / Elite / Chefe
- **Nível:** 1–5
- **Vitalidade / Defesa / Bônus de Ataque / Dano:** (da tabela em `REGRAS.md` §13, ajustada pela Categoria)
- **Movimento:** igual à tabela de PJs (`REGRAS.md` §5) para a mesma faixa de Agilidade equivalente ao Nível
- **Resistências:** tipos de dano ou Condição que este inimigo reduz ou ignora
- **Fraquezas:** o oposto — o que o afeta com mais força
- **Habilidades:** 0 (Minion/Padrão) a 2 (Chefe), usando o formato de `HABILIDADES.md`
- **Comportamento:** 1 linha, ex: "ataca sempre o alvo mais próximo", "foge abaixo de 25% de Vitalidade", "prioriza alvos Feridos"

## Catálogo Inicial

| Nome | Categoria | Nível | Vitalidade | Defesa | Ataque | Dano | Resistência | Fraqueza | Comportamento |
|---|---|---:|---:|---:|---:|---|---|---|---|
| Assaltante | Minion | 1 | 11 | 9 | +4 | 1d6 | — | Intimidação | Foge abaixo de 25% |
| Cão de guarda infectado | Minion | 1 | 11 | 9 | +4 | 1d6 | Envenenado | Fogo | Ataca sempre o mais próximo |
| Batedor | Padrão | 2 | 14 | 10 | +5 | 1d8 (rifle) | — | Furtividade contra ele | Prioriza alvos Feridos |
| Contaminado (Infecção Nível 3) | Padrão | 2 | 14 | 10 | +5 | 1d8 | Sangrando | Água benta/ritual | Errático — 50% de chance de atacar aliado mais próximo |
| Mercenário veterano | Elite | 3 | 26* | 11 | +6 | 1d10 | — | — | Usa Manobra Defender quando Ferido |
| Aberração Nível 4 (Infecção) | Elite | 4 | 30* | 12 | +7 | 1d12 | Físico comum | Fogo/Queimando | Ignora Amedrontado |
| Líder da seita (Chefe) | Chefe | 3 | 34** | 11 | +6 | 1d10 + Habilidade | Persuasão | Vontade baixa em aliados | 5 ações/rodada; foge com 1 aliado se restar sozinho |

\* Vitalidade já com o bônus de Elite (+50%) aplicado. \*\* Vitalidade já com o bônus de Chefe (+100%) aplicado.

## Referência rápida de encontro (1 PJ médio)

Validado por simulação (`/tools/enemy_sim.py`):

| Minions Nível 1 enfrentados | Chance de vitória do PJ |
|---:|---:|
| 1 | ~100% (trivial) |
| 2 | ~95% (fácil) |
| 3 | ~54% (equilibrado/difícil) |
| 4 | ~11% (perigoso) |
| 5 | ~1% (quase certamente letal) |

Para grupos de PJs, multiplique o número de minions proporcionalmente ao número de personagens, mantendo a proporção de dificuldade desejada (ex: 3 PJs → use a linha "3 por PJ" como referência de "equilibrado" = 9 minions, ajustando para baixo se o grupo tiver curador ou grande vantagem de Defesa).

---
*Ver `MESTRE.md` para o processo completo de montar um encontro.*
