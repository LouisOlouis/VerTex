# INFECÇÃO

A Infecção é rastreada como um **Nível de 0 a 6**, igual para todo personagem, independente de origem narrativa (mordida, gás, ritual, artefato corrompido — o Mestre define a fonte).

| Nível | Estado |
|---:|---|
| 0 | Saudável |
| 1 | Exposto |
| 2 | Contaminado |
| 3 | Infectado |
| 4 | Degradado |
| 5 | Crítico |
| 6 | Transformação |

## 1. Adquirir e Resistir

Uma exposição (contato com a fonte de Infecção) gera um teste de **Vigor** (exposição física) ou **Vontade** (exposição sobrenatural/mental) contra a **Dificuldade da fonte**, usando a mesma tabela de Dificuldade já usada em todo o sistema (`REGRAS.md`, seção 1.2) — uma fonte "fraca" é Dificuldade 8, uma "extrema" é 16+. Falha aumenta o Nível de Infecção em 1. Falha crítica (Margem ≤ −4) aumenta em 2.

**Por que a Dificuldade não escala automaticamente com o Nível atual:** testamos essa alternativa (`/tools/infection_sim.py`) e ela cria dois problemas — ou o crescimento é rápido demais para personagens fracos e quase impossível para os fortes (achatando a decisão em "construa Vigor/Vontade alto e ignore a mecânica"), ou fica lento demais para todos. Usar a Dificuldade da fonte (decidida pelo Mestre por cena, igual a qualquer outro teste) é mais simples, mais consistente com o resto do sistema e devolve ao Mestre o controle de ritmo — ver `BALANCEAMENTO.md`.

## 2. Sintomas e Efeitos por Nível

| Nível | Sintomas visíveis | Efeito mecânico (penalidade) | Dádiva disponível (opcional) |
|---:|---|---|---|
| 0 Saudável | nenhum | nenhum | — |
| 1 Exposto | nenhum ainda | nenhum | — |
| 2 Contaminado | veias escurecidas, olhos alterados | −1 em Vigor e Vontade | 1 Habilidade Especial de Infecção "menor" (ex: sentidos aguçados) |
| 3 Infectado | sintomas visíveis a qualquer um | −1 em todos os testes | dádiva de nível 2 se intensifica |
| 4 Degradado | deformações leves, comportamento errático sob estresse | −2 em todos os testes | dádiva poderosa, com custo passivo (ex: −2 na Vitalidade máxima) |
| 5 Crítico | transformação física parcial | −3 em todos os testes; a cada cena, teste de Vontade (Dificuldade 12) ou age contra a vontade do jogador por 1 ação | dádiva de combate poderosa, mas o personagem pode ferir aliados sob perda de controle |
| 6 Transformação | — | o personagem passa ao controle do Mestre (torna-se NPC) até ser curado, contido ou passar por uma condição narrativa especial definida pela campanha | poder total da Infecção, sem limitação de jogador |

## 3. A decisão central: aceitar ou remover

A partir do Nível 2, ao subir de nível o jogador escolhe:

- **Aceitar a dádiva** daquele nível: ganha o benefício mecânico imediatamente, mas o Nível de Infecção nunca pode ser reduzido abaixo deste ponto por tratamento comum (só por Artefato ou ritual específico da campanha).
- **Recusar a dádiva**: não ganha o benefício, mas mantém a Infecção totalmente reversível por tratamento.

Essa escolha é o núcleo de risco/recompensa pedido: poder imediato e permanente vs. reversibilidade total.

## 4. Diminuir (Tratamento)

| Nível atual | Tratamento necessário | Teste |
|---:|---|---|
| 1 | repouso e cuidado básico | Medicina, Dificuldade 8 |
| 2–3 | tratamento prolongado (1 cena de downtime) | Medicina, Dificuldade 12 |
| 4–5 | recurso raro (antídoto, ritual) definido pela campanha | Medicina ou Vontade, Dificuldade 14, + o recurso |
| 6 | não removível por tratamento comum | requer solução narrativa específica da campanha |

Tratamento bem-sucedido reduz 1 Nível. Dádivas aceitas (seção 3) não são desfeitas mesmo com a redução do Nível — o personagem mantém a marca permanente daquele estágio.

## 5. Consequências Narrativas

Personagens em Nível 3+ são reconhecíveis por NPCs comuns (medo, rejeição, caça). Nível 5+ pode atrair atenção de organizações ou entidades ligadas à origem da Infecção — deixado para o Mestre da campanha definir.

## 6. Infecção Arcana *(se `MAGIA.md` estiver em uso)*

Quem usa Conexão Arcana tem uma trilha de Infecção **separada** desta, com a mesma estrutura de 6 Níveis, mas causada por falha crítica ao canalizar um Arcano em vez de exposição comum. Ver `MAGIA.md` §5.

---
*Wagurita, Maldições e Artefatos — incluindo sua interação com a Infecção — em `MALDICOES.md`.*
