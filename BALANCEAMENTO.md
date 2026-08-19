# BALANCEAMENTO — Registro de Decisões

Todo desvio em relação às regras propostas no prompt original é documentado aqui, com: regra original, problema identificado, teste realizado, solução, motivo.

Scripts de apoio em `/tools/probability.py`.

---

## Fase 1 — Núcleo

### Decisão 1: Escala de Dificuldade — MANTIDA
- **Regra original:** 6/8/10/12/14/16/18+ (Muito fácil → Excepcional).
- **Teste realizado:** probabilidade de sucesso de 2d6+bônus para bônus de 0 a 10 contra cada dificuldade.
- **Resultado:** destreinado (bônus 0) tem 72% contra Muito Fácil e quase 0% contra Difícil+; especialista (bônus 5) tem 83% contra Normal mas só 8% contra Extremo; mestre (bônus 10) ainda falha ~8% contra Excepcional. Progressão de risco saudável em toda a faixa.
- **Solução:** nenhuma alteração necessária.

### Decisão 2: Bandas de Margem de Sucesso — ALTERADA
- **Regra original:** Falha crítica ≤ −5; Falha −4 a −1; Sucesso 0 a +3; Sucesso excepcional +4 a +6; Sucesso extraordinário ≥ +7.
- **Problema identificado:** em um teste "equilibrado" (bônus do personagem calibrado para ter ~50–60% de sucesso na dificuldade proposta), a margem só pode variar entre −5 e +5 (porque só a rolagem de 2d6, que vai de 2 a 12, varia — bônus e dificuldade são fixos no teste). Com o corte de Sucesso Extraordinário em +7, esse resultado se tornava **matematicamente impossível** em qualquer teste equilibrado, só ocorrendo quando o personagem já estava muito acima do desafio (situação onde o resultado já é irrelevante).
- **Teste realizado:** simulação da distribuição de margem para 5 confrontos bônus×dificuldade equilibrados (destreinado vs fácil, competente vs normal, especialista vs difícil, veterano vs muito difícil, mestre vs fácil/overkill). Com os cortes originais, "Sucesso extraordinário" deu 0% em 4 dos 5 casos equilibrados.
- **Solução:** bandas reduzidas e recentralizadas: Falha crítica ≤ −4; Falha −3 a −1; Sucesso 0 a +2; Sucesso excepcional +3; Sucesso extraordinário ≥ +4.
- **Motivo da mudança:** com o novo corte, todo teste equilibrado passa a ter chance real (8,3%) de gerar tanto Falha Crítica quanto Sucesso Extraordinário — simetria que dá emoção real à rolagem em qualquer nível de personagem, e não só em testes triviais.

### Decisão 3: Atributos 0–5 combinados com Perícias 0–5 — MANTIDA
- **Regra original:** atributos em escala 0 a 5.
- **Teste realizado:** bônus total (Atributo+Perícia) de 0 a 10 testado contra a escala de dificuldade (ver Decisão 1).
- **Resultado:** faixa de bônus gera diferenciação clara sem tornar dificuldades altas triviais nem baixas impossíveis para especialistas.
- **Solução:** nenhuma alteração necessária.

---

## Fase 2 — Combate

### Decisão 4: Fórmula de Vitalidade (10 + Vigor×2) — MANTIDA
- **Teste realizado:** simulação de combate (`/tools/combat_sim.py`) com milhares de repetições, cruzando bônus de ataque e dado de dano de arma contra Vitalidade/Defesa de um inimigo padrão (Vigor 2 → Vitalidade 14, Agilidade 2 → Defesa 10).
- **Resultado:** confronto equilibrado (bônus 5, espada 1d8) dura em média 3 rodadas; personagem fraco (bônus 2, faca) dura ~7,6 rodadas; personagem especializado (bônus 8) derruba em ~2,5 rodadas. Ritmo saudável para combate tático de 3 ações por rodada.
- **Solução:** nenhuma alteração.

### Decisão 5: Defesa = 8 + Agilidade — MANTIDA (nova fórmula, não estava explícita no prompt original)
- **Motivo:** o prompt pedia Defesa como estatística derivada sem fórmula fixa. Optei por alinhá-la à mesma escala da tabela de Dificuldade (6 a 18+) para que o Mestre não precise decorar uma escala numérica separada — "Defesa 10" já significa "Normal" na tabela que ele usa para tudo mais.
- **Teste realizado:** mesma simulação da Decisão 4, variando Defesa de 8 a 13 (Agilidade 0–5). Resultados consistentes com o ritmo desejado em toda a faixa.

### Decisão 6: Tabela de dano das armas — MANTIDA, com uma adição
- **Regra original:** tabela de dano (Soco 1d4 até Arma pesada 1d12) sem custos associados.
- **Problema identificado:** na simulação, "Arma pesada" (1d12) derrubava o inimigo padrão em 2,1 rodadas contra 3 rodadas da Espada (1d8), sem nenhuma desvantagem mecânica — ou seja, não havia razão para escolher uma arma mais fraca.
- **Solução:** os valores de dano foram mantidos, mas Arma Pesada agora ocupa 2 espaços de inventário e exige recarga a cada 3 usos (ver `COMBATE.md` e futura `EQUIPAMENTOS.md`), criando um trade-off real de poder vs. praticidade em vez de mudar os dados de dano.
- **Motivo da mudança:** resolver o desbalanceamento sem mexer na identidade das armas (que já "sentem" certas na escala de dado), preservando a regra 33 ("altere só o necessário").

### Decisão 7: Ataques de oportunidade — REMOVIDOS do sistema base
- **Regra original:** item 8 pedia a regra "caso realmente sejam necessários".
- **Análise:** o papel de desincentivar movimento livre já é cumprido pela ação de Defender e pela vulnerabilidade natural de gastar ação em vez de atacar. Adicionar a regra geraria mais rolagens sem gerar decisões novas (violaria a Restrição de Design, item 34).
- **Solução:** regra base não inclui ataques de oportunidade; fica disponível como efeito pontual de habilidades específicas na Fase 3.

---

## Fase 3 — Sorte, Determinação, Habilidades, Condições

### Decisão 8: Mecanismo de gasto de Sorte — DEFINIDO (regra original só dava a ideia geral)
- **Teste realizado:** simulação (`/tools/luck_sim.py`) comparando chance de sucesso normal vs. "rerrolar o pior dos dois dados" para todas as dificuldades de teste (2 a 13).
- **Resultado:** o ganho é maior exatamente nos testes de risco médio (+22 a +26 pontos percentuais quando a chance base está entre 40–60%) e cai para quase zero nos extremos — Sorte nunca garante sucesso (nunca chega a 100%) nem é inútil em testes difíceis.
- **Solução:** Sorte implementada como "rerrolar o pior dado, depois de ver o resultado, antes de aplicar a Margem". Recuperação limitada a entre sessões, para não permitir spam dentro do mesmo confronto.

### Decisão 9: Determinação inicial = 3 + Vontade — NOVA FÓRMULA (não estava no prompt original)
- **Motivo:** o prompt pedia "quantidade inicial" sem propor valor. Optei por ligar à Vontade (mesmo papel narrativo: força de vontade) em vez de um valor fixo igual para todos, para que a especialização em Vontade tenha peso mecânico real — hoje Vontade só era usada em testes sociais/sobrenaturais pontuais.
- **Solução:** 3 + Vontade (faixa 3 a 8), recuperação parcial em descanso curto, total ao fim de arco narrativo — deliberadamente mais lenta que Sorte para preservar a diferença de função entre os dois recursos.

### Decisão 10: Habilidades — regras anti-quebra formalizadas
- **Motivo:** o prompt pede apenas "crie regras para impedir habilidades quebradas" sem especificar quais. Formalizei 5 regras de auditoria (não substituir rolagem por sucesso automático, teto de bônus atrelado ao Atributo, proibição de ignorar Defesa/Vitalidade/Dificuldade por completo, duração obrigatória em Ativas/Especiais, não-empilhamento de efeitos idênticos) para que qualquer habilidade futura (Infecção, Maldições, Wagurita) possa ser auditada objetivamente, em vez de caso a caso.

### Decisão 11: Condições — Fraturado sem dano contínuo
- **Problema identificado:** Sangrando, Queimando, Envenenado e uma leitura ingênua de Fraturado poderiam todos virar "dano por rodada com nome diferente" — redundância que o prompt pede para evitar (item 11).
- **Solução:** Fraturado ficou definido como penalidade de capacidade (testes físicos e Movimento), sem nenhum componente de dano contínuo, diferenciando-o claramente das outras três condições, que por sua vez diferem entre si pelo *mecanismo* de dano contínuo (escalada por ação, duração fixa, ou ataque à capacidade geral em vez de à Vitalidade).

---

## Fase 4 — Infecção, Maldições, Artefatos, Wagurita

### Decisão 12: Dificuldade de resistência à Infecção — NÃO escala automaticamente com o Nível
- **Regra original:** implícita — "crie regras completas para adquirir, resistir, aumentar, diminuir".
- **Teste realizado:** simulação (`/tools/infection_sim.py`) de três abordagens — dificuldade crescendo 1 ponto por nível, dificuldade fixa, e dificuldade crescendo devagar (metade do nível). Em todas, um personagem com bônus de resistência alto (Vigor/Vontade 5, bônus 7) levava mais de 170 exposições em média para chegar à Transformação, contra ~9 de um personagem fraco (bônus 1) na pior curva.
- **Problema identificado:** qualquer fórmula de dificuldade automática cria uma disparidade extrema entre builds, tornando a Infecção irrelevante para personagens especializados em resistência e brutal para os demais — o oposto de "decisões reais" pedido no item 15.
- **Solução:** a Dificuldade do teste de resistência é definida pela **fonte da exposição** (usando a mesma tabela de Dificuldade central do sistema, já familiar ao Mestre), exatamente como qualquer outro teste — não por uma fórmula automática ligada ao Nível atual do personagem.
- **Motivo da mudança:** devolve ao Mestre o controle de ritmo por cena (uma fonte fraca é Dificuldade 8, uma extrema é 16+), evita a matemática degenerada encontrada nas três curvas testadas, e mantém a Infecção consistente com a filosofia do resto do sistema (Dificuldade sempre contextual, nunca uma fórmula própria isolada).

### Decisão 13: Estrutura de Maldições e Artefatos — campos padronizados
- **Motivo:** o prompt já define quais campos cada maldição/artefato deve ter; a decisão de design foi reaproveitar a escala de penalidade −1/−2/−3 (já usada em Condições e Ferimentos) em vez de inventar uma nova escala numérica, e reaproveitar as regras anti-quebra de `HABILIDADES.md` para o "Poder" de Artefatos — reduz a quantidade de sistemas numéricos paralelos que o Mestre precisa lembrar.

### Decisão 14: Wagurita — estrutura sem lore
- Conforme instrução explícita do prompt, nenhum detalhe de história foi inventado. A estrutura mecânica reaproveita integralmente os sistemas de Habilidades, Infecção e Maldições já validados, para que a Wagurita não exija uma mecânica exclusiva quando a campanha definir seu conteúdo.

---

## Fase 5 — Corridas, Exploração, Conflitos Sociais

### Decisão 15: Corridas precisam de Manobra Arriscada como mecanismo de catch-up
- **Teste realizado:** simulação (`/tools/race_sim.py`) de uma corrida de 8 Trechos usando só a ação básica de Acelerar.
- **Problema identificado:** sem alternativa, a diferença de bônus decidia a corrida quase sempre (91–100% de vitória para o lado com mais bônus), o que contraria o item 19 ("mecanicamente interessante", não decidida de antemão).
- **Solução:** adicionada a ação Manobra Arriscada (mesmo teste, Dificuldade um degrau acima, recompensa maior na Margem alta) como ferramenta ativa do competidor atrás, dando ao jogador uma decisão real (arriscar para tentar alcançar) em vez de aceitar passivamente o resultado.

### Decisão 16: Exploração e Conflitos Sociais reaproveitam mecânicas já existentes
- **Motivo:** os itens 20 e 21 pedem explicitamente para não transformar essas áreas em simulação detalhada ou rolagem constante. Em vez de criar sistemas numéricos novos, Exploração reaproveita a unidade "Trecho" de `CORRIDAS.md` e a Margem central para graus de descoberta; Conflitos Sociais reaproveita a fórmula de Defesa (virando "Resistência Social = 8 + Vontade") e a estrutura de "corrida de pontos" para negociações estendidas. Isso mantém o número de sistemas distintos que o Mestre precisa lembrar o menor possível, sem perder profundidade.

---

## Fase 6 — Progressão, Equipamentos, Inimigos, Mestre

### Decisão 17: Custo de Atributo maior que Perícia — por desenho, não por teste isolado
- **Motivo:** cada Atributo já afeta múltiplas estatísticas derivadas (Vigor → Vitalidade + resistência à Infecção + testes; Agilidade → Defesa + Movimento + Corridas), enquanto uma Perícia afeta só os testes daquela perícia. Custo maior (2×nível vs 1×nível) compensa esse alcance maior, evitando que "só subir Atributo" seja estritamente melhor que diversificar.
- **Teste realizado:** comparação de custo total para levar um combo Atributo+Perícia a 5/5 (45 PE) contra levar dois combos a 3/3 (36 PE) — confirma que ambas as rotas custam de forma comparável, criando escolha real entre profundidade e amplitude.

### Decisão 18: Fórmulas de criação rápida de inimigos — derivadas das fórmulas já validadas de PJ
- **Motivo:** em vez de criar uma escala nova para inimigos, a Vitalidade (8+Nível×3) e Defesa (8+Nível) foram calibradas para que um inimigo "Nível 2" caia próximo do "inimigo médio" (Vitalidade 14, Defesa 10) já usado e validado na simulação de combate da Fase 2 — nenhuma matemática nova precisou ser inventada, só extrapolada de forma consistente.
- **Teste realizado:** simulação (`/tools/enemy_sim.py`) de 1 PJ médio contra grupos de 1 a 5 minions Nível 1, gerando a tabela de referência de encontro usada em `INIMIGOS.md` e `MESTRE.md`.

---

## Fase 7 — Balanceamento Consolidado

Todas as decisões de 1 a 18 (Fases 1–6) já foram validadas individualmente à medida que cada sistema foi criado. A Fase 7 fecha o requisito do item 26: comparar os 4 perfis de personagem (fraco, médio, especializado, otimizado) em um cenário comum.

### Decisão 19: Comparação dos 4 perfis em combate — validada, com um ajuste na orientação ao Mestre
- **Teste realizado:** simulação (`/tools/balance_fase7.py`) dos 4 perfis contra o mesmo inimigo Padrão Nível 2 (Vitalidade 14, Defesa 10, bônus 5, dano 1d8 — a referência usada desde a Fase 2).
- **Resultado:**

| Perfil | Vitória | Rodadas médias | Dano causado (médio) |
|---|---:|---:|---:|
| Fraco (bônus 2) | 26,8% | 3,2 | 9,3 |
| Médio (bônus 5) | 98,1% | 2,4 | 16,2 |
| Especializado (bônus 7) | 100,0% | 1,8 | 17,0 |
| Otimizado (bônus 8) | 100,0% | 1,8 | 17,0 |

- **Achado 1 — retornos decrescentes confirmados:** Especializado e Otimizado empatam estatisticamente. Depois de um certo ponto (~bônus 7 contra Defesa 10), gastar mais PE em combate não aumenta a taxa de vitória — o PE extra só compensa em Dificuldades mais altas (ver tabela de probabilidade da Fase 1) ou em outros pilares. Isso confirma que **não existe combinação obrigatória** para "vencer o jogo": o teto de utilidade prática satura antes do teto numérico (bônus 10), abrindo espaço real para builds diversificados sem penalidade de desempenho em combates normais.
- **Achado 2 — problema de calibração de encontro, não de regra:** um personagem recém-criado (bônus 2, ainda sem PE gastos) perde a maioria das vezes contra um inimigo Padrão Nível 2. Isso não é um defeito das regras de combate (já validadas na Fase 2) — é uma questão de **calibração do Mestre**: um inimigo Nível 2 não deveria ser o encontro padrão para um grupo recém-criado.
- **Solução:** adicionada a orientação "Nível do inimigo Padrão ≈ bônus total do PJ ÷ 2" em `MESTRE.md`, para que a escolha do Nível do inimigo acompanhe a evolução do grupo ao longo da campanha, em vez de um valor fixo.
- **Nota de escopo:** o perfil "Otimizado" (bônus 8, Vitalidade 18, Defesa 12) **não é alcançável na criação de personagem** — o array fixo (`CRIACAO_PERSONAGEM.md`) limita o bônus inicial máximo a 7 (Atributo 4 + Perícia 3). Ele representa um personagem várias sessões depois, com PE já investidos. Isso é intencional e reforça a Decisão 17: mesmo gastando PE extra além do "Especializado", o ganho em combate já saturou — o retorno real daquele investimento aparece em outros pilares ou em Dificuldades mais altas, não em vencer combates padrão com mais facilidade.

---

## Fase 8 — Playtest

Três cenários jogados (`PLAYTEST.md`): Combate (Marco vs 2 Assaltantes), Investigação (Iris examinando uma cena), Corrida (Deko fugindo de um Batedor). Nenhum dos três exigiu alteração de regra — os três confirmaram, em jogo real, os números já validados por simulação nas fases anteriores. Um único ajuste de **clareza** (não de regra) foi identificado e aplicado: `CORRIDAS.md` não deixava explícito como tratar perseguições onde os competidores partem de pontos diferentes (em vez de lado a lado) — adicionado um parágrafo explicando que a distância entre eles é a diferença de Trechos, e que Ultrapassar só se aplica quando essa diferença chega a 0.

## Fase 9 — Auditoria de Consistência

Revisão de todos os arquivos em busca dos problemas listados no item 29. Encontrados e corrigidos:

| # | Problema encontrado | Onde | Correção |
|---|---|---|---|
| 1 | `COMBATE.md` listava a tabela de dano das armas sem cabeçalho de seção (erro de edição), e não referenciava o catálogo estendido de `EQUIPAMENTOS.md` | `COMBATE.md` §5 | heading restaurado + linha de referência cruzada para `EQUIPAMENTOS.md` |
| 2 | Tabela de Condições (`REGRAS.md` §8) listava "Infectado" e "Amaldiçoado" como se fossem condições simples de efeito único, quando na verdade são sistemas próprios de múltiplos estágios | `REGRAS.md` §8 | nota de consistência explicando a diferença |
| 3 | `CORRIDAS.md` não cobria o caso de perseguições com pontos de partida diferentes (achado no Teste 3 do Playtest) | `CORRIDAS.md` §1 | parágrafo de esclarecimento adicionado |
| 4 | Perfil "Otimizado" da Fase 7 poderia ser lido como alcançável na criação de personagem, mas exige PE de progressão | `BALANCEAMENTO.md`, Decisão 19 | nota de escopo adicionada (acima) |

**Verificações sem problema encontrado:** custos de Habilidades (todas têm custo definido, `HABILIDADES.md`), soma dos arrays de Atributos e Perícias dos 3 personagens de exemplo (todos batem com o total permitido), fórmulas de estatísticas derivadas aplicadas nos exemplos (Vitalidade/Defesa/Determinação conferem com os Atributos declarados), referências cruzadas entre arquivos (`REGRAS.md` → `COMBATE.md`, `HABILIDADES.md`, `INFECCAO.md`, `MALDICOES.md`, `CORRIDAS.md`, `EQUIPAMENTOS.md`, `MESTRE.md`, `INIMIGOS.md` — todas apontam para conteúdo que de fato existe).

---

## Fase 10 — Módulos Opcionais: Magia, Classes, Raças

### Decisão 20: Magia reaproveita Dificuldade, Margem e Infecção em vez de sistemas novos
- **Teste realizado:** simulação (`/tools/magic_sim.py`) do dano médio por ponto de Foco gasto em cada Círculo, comparado ao dano por ação das armas já validadas em `COMBATE.md`.
- **Resultado:** dano por Foco ficou estável (~1,6–1,8) em todos os Círculos; feitiços de Círculo alto (2d10, 3d10) superam o dano de qualquer arma por ativação, mas o Foco total (4–14) permite só 1–2 conjurações desse porte por cena de descanso — magia vira "burst" limitado contra o dano sustentado e ilimitado das armas, sem uma opção dominar a outra.
- **Solução:** tabela de Círculos calibrada com esses custos; falha crítica ao conjurar gera uma exposição à Infecção (reaproveitando `INFECCAO.md` em vez de inventar uma penalidade de magia exclusiva), e a Dificuldade de cada Círculo usa a tabela central de Dificuldade — nenhuma escala numérica nova para o Mestre aprender.

### Decisão 21: Classes não somam poder, só empacotam escolhas
- **Motivo:** adicionar Classes sobre um sistema já validado como livre (`CRIACAO_PERSONAGEM.md`) criaria risco de dar mais pontos efetivos a quem escolhe uma Classe do que a quem monta o personagem manualmente. Resolvido tornando a Classe um atalho que só direciona o Atributo Principal, as Perícias e a única Habilidade que todo personagem já recebe — nunca uma habilidade ou pontos extras.

### Decisão 22: Raças deslocam pontos, não somam
- **Motivo:** mesma lógica da Decisão 21. Cada Raça desloca exatamente 1 ponto entre dois Atributos (soma do array continua 15) e concede um traço qualitativo (nunca um bônus numérico livre, para não conflitar com as regras anti-quebra de `HABILIDADES.md`). A única exceção (Nível de Infecção inicial em "Enraizado na Infecção") vem com o mesmo custo que qualquer personagem pagaria para chegar lá jogando, para não pular a progressão de graça.

### Nota de escopo
Os três módulos eram opcionais e não modificam nenhuma regra central já validada nas Fases 1–9, nem invalidam os 3 personagens de exemplo de `CRIACAO_PERSONAGEM.md`.

## Fase 10 (revisão) — Magia com Pergaminhos/Conexão Arcana, Habilidades Únicas com progressão por Missão

Louis pediu uma revisão do módulo de Magia (duas formas de uso — Pergaminho vs Conexão Arcana — e uma "Infecção Arcana" separada da Infecção comum) e a adição de Habilidades Únicas em 3 Estágios para Classes e Raças, evoluindo por Missão em vez de só por PE. `MAGIA.md`, `CLASSES.md` e `RACAS.md` foram consolidados em um único arquivo, `MAGIA_CLASSES_RACAS.md`.

### Decisão 23: Infecção Arcana como trilha separada, reaproveitando a estrutura de `INFECCAO.md`
- **Motivo:** em vez de criar uma mecânica de corrupção mágica do zero, a Infecção Arcana usa exatamente os mesmos 6 Níveis, dádivas e regras de tratamento já validados para a Infecção comum — só troca os sintomas/dádivas pelo Arcano específico. Isso cumpre o pedido de Louis (falha crítica com Conexão Arcana = "alma e corpo fraquejaram perante o elemento") sem duplicar um sistema já testado.
- **Ajuste em relação ao pedido original:** Pergaminhos foram deliberadamente isentos de Infecção Arcana (conforme Louis pediu) — falha crítica com Pergaminho destrói o item em vez de arriscar o personagem, criando a assimetria risco/segurança entre as duas formas de magia.

### Decisão 24: "Domínio" ligado à Vontade, com recompensa mecânica em troca de perda de controle
- **Motivo:** Louis descreveu que mente fraca pode ser dominada pelo Arcano, "não necessariamente algo ruim". Formalizado como: a partir do Nível 3 de Infecção Arcana, falhar em um teste de Vontade (Dificuldade 8+Nível) faz o Arcano influenciar uma decisão da cena, mas concede +2 no próximo teste alinhado com essa influência — perda de controle narrativo trocada por vantagem mecânica, em vez de ser só uma penalidade.

### Decisão 25: Mana cresce com o uso, não só com Atributos
- **Motivo:** pedido direto de Louis ("quanto mais magia em geral você usa, mais mana você tem"). Implementado como um contador de Usos Mágicos Acumulados (Pergaminho ou Conexão Arcana, sucesso ou falha) que soma +1 ao Mana máximo a cada 8 usos, até um teto de +5 — rende progressão ao longo de uma campanha inteira sem inflacionar o número indefinidamente.

### Decisão 26: Habilidades Únicas de Classe/Raça em 3 Estágios, gatilho é narrativo (Missão), não PE
- **Motivo:** pedido direto de Louis. Para não abrir uma segunda economia de progressão paralela a PE (o que quebraria a Decisão 17, custo de Atributo vs Perícia), os Estágios 2 e 3 não têm custo em PE — são desbloqueados só por completar uma Missão de Classe/Origem (arco narrativo definido pelo Mestre). Isso mantém a progressão numérica (PE) e a progressão narrativa (Missões) como eixos separados que não competem pelo mesmo orçamento.

---

## Fase 10 (revisão 2) — Separação em arquivos, Classes/Raças tradicionais, adaptação do resto do sistema

Louis pediu: arquivos separados para Magia, Classes e Raças (em vez do arquivo único da revisão anterior); mais exemplos de Arcanos; Classes e Raças em uma visão mais tradicional de RPG (guerreiro/mago/ladino, elfos/anões/orcs); e adaptação dos outros documentos às novidades.

### Decisão 27: Voltar a 3 arquivos separados
- **Motivo:** pedido direto de Louis. `MAGIA_CLASSES_RACAS.md` foi removido; o conteúdo foi dividido de volta em `MAGIA.md`, `CLASSES.md` e `RACAS.md`, mantendo os cross-references entre eles (cada um aponta para os outros dois quando relevante) para não perder a coerência que a versão única tinha.

### Decisão 28: Arcanos expandidos de 6 para 12
- Adicionados: Ar/Vento, Luz, Natureza, Metal, Sangue, Espírito — cobrindo arquétipos tradicionais de RPG que dependem de magia elemental/esotérica (druida → Natureza, clérigo → Luz, necromante/sangue → Sangue/Espírito) sem exigir um sistema novo: todos usam a mesma estrutura de Domínio/Sintoma/Traço de Domínio já validada.

### Decisão 29: Classes reformuladas como arquétipos tradicionais de RPG
- **Motivo:** pedido direto de Louis. Trocado o conjunto anterior (Guerreiro/Atirador/Ladino/Curandeiro/Sobrevivente/Carismático/Conjurador) por 9 classes no molde clássico: Guerreiro, Bárbaro, Patrulheiro, Ladino, Clérigo, Mago, Druida, Bardo, Paladino — Mago/Druida/Clérigo já vêm com um gancho mecânico para `MAGIA.md` (Pergaminho com desconto, Conexão Arcana grátis, ou ambos), sem que isso represente pontos extras (mesma regra da Decisão 21: Classe empacota escolha, não soma poder).

### Decisão 30: Raças tradicionais (Elfo, Anão, Orc, Halfling, Meio-Elfo) substituindo as genéricas
- **Motivo:** pedido direto de Louis. Mantidas as duas raças ligadas à ambientação já estabelecida (Tocado pelo Arcano, Enraizado na Infecção) porque continuam úteis e não competem com o pedido — as novas raças tradicionais foram adicionadas ao lado delas, não no lugar. Todas seguem a mesma regra de deslocamento de Atributo (+1/−1, soma sempre 15) e Habilidade Única qualitativa da Decisão 22.

### Decisão 31: Documentos existentes adaptados para referenciar os módulos
- `REGRAS.md` ganhou uma seção 14 (Módulos Opcionais) resumindo os três e apontando para os arquivos certos.
- `CRIACAO_PERSONAGEM.md` ganhou um passo 1.1 (Raça e Classe) e notas nos passos 2–4 sobre como eles se encaixam no fluxo já existente, sem mudar a contagem de pontos.
- `FICHA.md` ganhou campos de Raça/Classe, uma 13ª linha de Perícia (Conjuração), um bloco de Magia (Mana, Conexões Arcanas, Infecção Arcana) e um rastreador de Missões de Classe/Origem.
- `INFECCAO.md` ganhou uma seção 6 curta apontando para a Infecção Arcana, para quem ler esse arquivo isoladamente não achar estranho a menção em `MAGIA.md`.
- `MESTRE.md` ganhou uma seção 10 explicando como montar uma Missão de Classe/Origem (o gatilho de progressão dos Estágios 2 e 3).
- `EQUIPAMENTOS.md` ganhou uma linha para Pergaminhos no catálogo de itens.

---
*Fases seguintes acrescentam decisões abaixo desta linha, na ordem em que forem tomadas.*
