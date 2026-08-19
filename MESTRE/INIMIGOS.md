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

## Catálogo — 30 Inimigos

Organizados por papel narrativo (Comuns/Especializados/Sobrenaturais/Elites/Chefes) — a **Categoria** mecânica (Minion/Padrão/Elite/Chefe, `REGRAS.md` §13) é uma coluna própria, porque um inimigo "temático sobrenatural" pode ter estatística de Minion ou Elite conforme o desafio pretendido.

### Comuns (10) — ameaças mundanas, Nível 1

| Nome | Categoria | Nível | Vitalidade | Defesa | Ataque | Dano | Resistência | Fraqueza | Comportamento |
|---|---|---:|---:|---:|---:|---|---|---|---|
| Assaltante | Minion | 1 | 11 | 9 | +4 | 1d6 | — | Intimidação | Foge abaixo de 25% |
| Vira-lata Selvagem | Minion | 1 | 11 | 9 | +4 | 1d4 | — | Alto ruído (assusta) | Sempre em grupo de 2+ |
| Ladrão Oportunista | Minion | 1 | 11 | 9 | +4 | 1d6 (faca) | — | Percepção alta do alvo | Rouba e foge, evita briga |
| Bêbado Violento | Minion | 1 | 11 | 9 | +4 | 1d4 | — | Persuasão | Ataca sem tática, alvo aleatório |
| Guarda Desatento | Padrão | 1 | 11 | 9 | +4 | 1d6 (pistola) | — | Furtividade | Soa alarme se detectar alguém |
| Catador de Sucata | Minion | 1 | 11 | 9 | +4 | 1d6 (machado improvisado) | — | Tecnologia (negociar por peças) | Foge com o que roubou |
| Corvo Gigante | Minion | 1 | 11 | 9 | +4 | 1d4 (bicada) | — | Alcance longo | Ataca de surpresa e recua |
| Rato Gigante | Minion | 1 | 11 | 9 | +4 | 1d4 | transmite Envenenado Nível 1 no acerto | Fogo | Sempre em bando |
| Fanático de Rua | Padrão | 1 | 11 | 9 | +4 | 1d8 (espada) | — | Persuasão | Ataca sem recuar, grita ameaças |
| Guarda de Caravana | Padrão | 1 | 11 | 9 | +4 | 1d8 (rifle) | — | Cobertura | Protege a carga antes de perseguir |

### Especializados (8) — treinados, equipados, com tática, Nível 2–3

| Nome | Categoria | Nível | Vitalidade | Defesa | Ataque | Dano | Resistência | Fraqueza | Comportamento |
|---|---|---:|---:|---:|---:|---|---|---|---|
| Batedor | Padrão | 2 | 14 | 10 | +5 | 1d8 (rifle) | — | Furtividade contra ele | Prioriza alvos Feridos |
| Franco-atirador | Padrão | 2 | 14 | 10 | +5 | 1d10 (rifle, longo alcance) | — | Aproximação rápida | Mantém distância, reposiciona após atirar |
| Guarda Corporativo Blindado | Padrão | 2 | 14 | 10 | +5 | 1d8 (pistola) | Redução 1 (armadura leve) | Fogo/explosivos | Avança em formação |
| Especialista em Armadilhas | Padrão | 2 | 14 | 10 | +5 | 1d6 (faca) | — | Percepção alta | Prepara o terreno antes do combate (`CRAFTING.md`) |
| Mercenário | Padrão | 3 | 17 | 11 | +6 | 1d10 | — | — | Foca o alvo mais perigoso primeiro |
| Batedor Motorizado | Padrão | 2 | 14 | 10 | +5 | 1d8 | — | Terreno fechado | Usa Manobra Arriscada quando em desvantagem (`CORRIDAS.md`) |
| Negociador Armado | Padrão | 2 | 14 | 10 | +5 | 1d8 | — | Persuasão | Tenta negociar antes de lutar |
| Infiltrador Furtivo | Padrão | 3 | 17 | 11 | +6 | 1d6 (faca) | — | Percepção alta (revela Oculto) | Ataca a partir de Oculto (`REGRAS.md` §17), foge se Detectado |

### Sobrenaturais (6) — Infecção e Arcano

| Nome | Categoria | Nível | Vitalidade | Defesa | Ataque | Dano | Resistência | Fraqueza | Comportamento |
|---|---|---:|---:|---:|---:|---|---|---|---|
| Cão de Guarda Infectado | Minion | 1 | 11 | 9 | +4 | 1d6 | Envenenado | Fogo | Ataca sempre o mais próximo |
| Contaminado (Infecção Nível 3) | Padrão | 2 | 14 | 10 | +5 | 1d8 | Sangrando | Água benta/ritual | Errático — 50% de chance de atacar o aliado mais próximo |
| Enxame Contaminado | Minion | 2 | 14 | 10 | +5 | 1d6 (mordidas múltiplas) | Furtividade contra ele (barulhento) | Fogo em área | Sempre em grupo de 3+, nunca sozinho |
| Espectro Amaldiçoado | Padrão | 3 | 17 | 11 | +6 | 1d10 (toque gélido, ignora Redução de dano física) | metade do dano físico comum | Luz/Fé (Persuasão religiosa) | Persegue só quem carrega a maldição de origem (`MALDICOES.md`) |
| Aberração (Infecção Nível 4) | Elite | 4 | 30\* | 12 | +7 | 1d12 | Físico comum | Fogo/Queimando | Ignora Amedrontado |
| Arauto do Arcano (Infecção Arcana Nível 6) | Elite | 5 | 35\* | 13 | +8 | 2d8 (efeito do Arcano) | conforme o Arcano (`MAGIA.md` §6) | oposto elemental do Arcano | Ataca com o domínio do Arcano em vez de combate direto |

### Elites (4) — ameaças significativas solo

| Nome | Categoria | Nível | Vitalidade | Defesa | Ataque | Dano | Resistência | Fraqueza | Habilidade | Comportamento |
|---|---|---:|---:|---:|---:|---|---|---|---|---|
| Mercenário Veterano | Elite | 3 | 26\* | 11 | +6 | 1d10 | — | — | — | Usa Manobra Defender quando Ferido |
| Capitão de Milícia | Elite | 3 | 26\* | 11 | +6 | 1d10 (espada+escudo) | Redução 1 | Persuasão (covardia oculta) | **Grito de Comando** (Ativa): concede o bônus de Ajudar a até 2 aliados na mesma ação | Lidera Minions; foge se ficar sozinho |
| Caçador de Recompensas | Elite | 4 | 30\* | 12 | +7 | 1d12 (arma pesada) | — | Furtividade (rastreia por som/cheiro; cego a quem está Oculto) | **Mira Calculada** (Ativa, 1 uso/cena): ignora cobertura parcial no próximo ataque | Nunca desiste do alvo contratado |
| Colosso Blindado | Elite | 5 | 35\* | 13 | +8 | 2d8 | Redução 3 (blindagem) | Explosivos/ataques concentrados | — | Avança lento e direto; ignora Amedrontado e Atordoado |

\* Vitalidade já com o bônus de Elite (+50%) aplicado.

### Chefes (2) — clímax de arco, usando `COMBATE.md` §10

**Líder da Seita** — Chefe, Nível 3, Vitalidade 34\*\*, Defesa 11, Ataque +6, Dano 1d10 + Habilidade, Resistência Persuasão, Fraqueza Vontade baixa em aliados, 5 ações/rodada.
- **Fase 1 (100–66% Vit):** combate normal, prioriza o alvo com menor Defesa.
- **Fase 2 (65–33% Vit) — Convocação:** uma vez ao entrar nesta fase, convoca 1–2 Contaminados (ver Sobrenaturais).
- **Fase 3 (<33% Vit) — Fúria Ritualística:** ataques causam +2 de dano, mas perde 1 ação por rodada (total 4); foge com 1 aliado se restar sozinho.

**O Devorador** — Chefe, Nível 5, Vitalidade 46\*\*, Defesa 13, Ataque +8, Dano 2d8 + Habilidade, Resistência Físico comum, Fraqueza Fogo/Luz, 5 ações/rodada.
- **Fase 1 (100–66% Vit):** ataques físicos padrão.
- **Fase 2 (65–33% Vit) — Mudança de Arena:** o ambiente passa a gerar um Perigo Ambiental (`REGRAS.md` §9): teste de Vigor Dificuldade 12 por rodada ou +1 exposição de Infecção.
- **Fase 3 (<33% Vit) — Transformação:** ganha a Habilidade Especial **Última Fome** (ativa 1x): ataque em área — todos na cena sofrem 1d8 de dano e um teste de resistência à Infecção Dificuldade 14 (`INFECCAO.md` §1).

\*\* Vitalidade já com o bônus de Chefe (+100%) aplicado.

## Referência rápida de encontro (1 PJ médio)

| Minions Nível 1 enfrentados | Chance de vitória do PJ |
|---:|---:|
| 1 | ~100% (trivial) |
| 2 | ~95% (fácil) |
| 3 | ~54% (equilibrado/difícil) |
| 4 | ~11% (perigoso) |
| 5 | ~1% (quase certamente letal) |

Para grupos de PJs, multiplique o número de minions proporcionalmente ao número de personagens, mantendo a proporção de dificuldade desejada (ex: 3 PJs → use a linha "3 por PJ" como referência de "equilibrado" = 9 minions, ajustando para baixo se o grupo tiver curador ou grande vantagem de Defesa).

---
*Ver `MESTRE.md` para o processo completo de montar um encontro, e `COMBATE.md` §10 para as ferramentas de Fase/Convocação/Transformação usadas pelos Chefes acima.*
