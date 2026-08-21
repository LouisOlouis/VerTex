# REGRAS — Núcleo do Sistema

## 1. Mecânica Central

Todo teste segue a mesma fórmula, sem exceções:

**2d6 + Atributo + Perícia** vs **Dificuldade**

Some os dois dados, some o Atributo relevante, some a Perícia relevante. Se o total igualar ou superar a Dificuldade, o teste é bem-sucedido.

Não existem modificadores soltos, bônus situacionais numéricos ou penalidades acumuladas fora deste padrão — vantagens e desvantagens de situação se resolvem ajustando a Dificuldade (ver 1.3), nunca somando números extras ao resultado. Isso mantém o cálculo mental em uma única soma, sempre.

### 1.1 Perguntas que o jogador sempre consegue responder
- **O que eu rolo?** Sempre 2d6.
- **Qual atributo uso?** O Mestre define pela ação descrita (tabela de referência rápida no capítulo do Mestre).
- **Qual a dificuldade?** O Mestre declara antes da rolagem.
- **Se eu passar?** Veja a Margem de Sucesso (seção 3).
- **Se eu falhar?** Veja a Margem de Sucesso (seção 3) — falha sempre gera consequência, nunca "nada acontece".

### 1.2 Dificuldade

| Dificuldade | Classificação |
|---:|---|
| 6 | Muito fácil |
| 8 | Fácil |
| 10 | Normal |
| 12 | Difícil |
| 14 | Muito difícil |
| 16 | Extremo |
| 18+ | Excepcional |

### 1.3 Ajustando a Dificuldade por situação

Em vez de bônus/penalidades numéricas soltas, condições favoráveis ou desfavoráveis **sobem ou descem um degrau** na tabela de dificuldade (ex: Normal 10 → Fácil 8 com boa preparação; Normal 10 → Difícil 12 sob pressão de tempo). Isso preserva a regra de "uma soma só".

## 2. Margem de Sucesso

**Margem = (2d6 + Atributo + Perícia) − Dificuldade**

| Margem | Resultado |
|---:|---|
| −4 ou menos | Falha crítica |
| −3 a −1 | Falha |
| 0 a +2 | Sucesso |
| +3 | Sucesso excepcional |
| +4 ou mais | Sucesso extraordinário |


## 3. Atributos

Escala **0 a 5**. 0 = ausência/incapacidade notável, 1 = abaixo da média, 2 = média, 3 = acima da média, 4 = excelente, 5 = pico humano/limite raro.

| Atributo | Cobre |
|---|---|
| Força | potência física, carga, combate corporal |
| Agilidade | velocidade, coordenação, esquiva, acrobacia |
| Vigor | resistência física, recuperação |
| Intelecto | conhecimento, raciocínio, tecnologia |
| Percepção | sentidos, rastreamento, reação |
| Vontade | resistência mental, coragem, foco sobrenatural |


## 4. Perícias

Escala **0 a 5**, paralela aos Atributos.

| Nível | Significado |
|---:|---|
| 0 | Sem treino |
| 1 | Familiarizado |
| 2 | Treinado |
| 3 | Proficiente |
| 4 | Especialista |
| 5 | Referência (o melhor que existe) |

Perícias iniciais (12): Atletismo, Acrobacia, Combate, Furtividade, Pontaria, Investigação, Medicina, Tecnologia, Sobrevivência, Persuasão, Intimidação, Enganação.

A adição de mais pericias, ou niveis de conhecimento sobre elas(tambem valido para atributos), podem ser adicionadas para uma campanha mais interessante, todavia passar dos niveis normais tanto em pericia ou em atributos nescessitam de missões exclusivas de treinamento.

*(Custo de evolução, máximos por Pontos de Evolução e detalhamento de cada perícia entram na Fase 6 — Progressão — para manter os números coerentes com o restante do sistema antes de fixá-los.)*

## 5. Estatísticas Derivadas

| Estatística | Fórmula |
|---|---|
| Vitalidade | 10 + Vigor × 2 |
| Defesa | 8 + Agilidade |
| Iniciativa | 2d6 + Agilidade + Percepção (rolada 1x por combate) |
| Movimento | 6 + Agilidade (metros por ação de mover) |
| Capacidade de carga | 5 + Força (espaços de inventário) |

*(Capacidade de carga pode ser modificada com itens de inventario, como mochilas que nao geram peso)*

*(Defesa usa a mesma escala da tabela de Dificuldade (seção 1.2) — um Mestre já sabe ler "Defesa 10" como "Normal", sem tabela nova para decorar.)*

## 6. Sorte

Todo personagem começa com **3 pontos de Sorte**, gastos um de cada vez para:

- **Rerrolar o pior dos dois dados** de um teste que acabou de fazer (o outro dado é mantido). Só pode ser usada depois de ver o resultado, antes de aplicar a Margem.

- **Reduzir uma consequência de falha em um degrau** (ex: transformar Falha Crítica em Falha simples).

- **Alterar um pequeno detalhe plausível da cena** (a porta estava destrancada, havia uma corda ali, o guarda tinha acabado de sair) — sujeito à aprovação do Mestre quanto à plausibilidade.

Sorte se recupera apenas entre sessões (1 ponto) ou por decisão do Mestre em momentos marcantes — nunca durante o mesmo confronto em que foi gasta.

## 7. Determinação

**Determinação inicial = 3 + Vontade**.

 Determinação é a vontade de continuar — ativa Habilidades Especiais, resiste a  Condições mentais (Amedrontado, Atordoado) ou fisicas(Fraturas, euxaustao e ferimentos) e permite agir além do limite normal quando Incapacitado (ver `COMBATE.md`).

| Uso | Custo |
|---|---|
| Ativar uma Habilidade Especial | conforme definido na habilidade (1 a 3 pontos) |
| Resistir automaticamente a uma Condição mental por 1 rodada | 1 ponto |
| Agir uma vez estando Incapacitado | 2 pontos |

Determinação se recupera com descanso curto (1 ponto a cada cena de respiro) e totalmente ao fim de um arco narrativo — mais devagar que Sorte, mas sem exigir esperar a próxima sessão.

So e possivel resistir a condiçoes fisicas sendo da raça Humano (ver `RACAS.md`)

Agir incapacitado ou com condiçoes fisicas usando determinação nao significa imortalidade, significa apenas ignorar a dor, voce ainda sofre dano e pode morrer

## 8. Condições

Cada condição tem causa, efeito, duração e forma de remoção próprias — nenhuma duplica o papel de outra.

| Condição | Causa típica | Efeito | Remoção |
|---|---|---|---|
| Sangrando | dano perfurante/cortante grave | perde 1 Vitalidade no início de cada turno; **escala** (+1 de perda) a cada ação física realizada enquanto sangrando | teste de Medicina (Dificuldade 8) ou 1 rodada de repouso total |
| Queimando | fogo, ácido | dano fixo (1d4) no início de cada turno por 3 rodadas, não escala | apagar (ação + Dificuldade 8) encerra antes do prazo |
| Envenenado | veneno, picada, gás | níveis 1–3 acumuláveis; mais detalher no final da pagina | teste de Vigor (Dificuldade igual a 8+nível) ou antídoto |
| Fraturado | dano grave em combate (Gravemente Ferido + acerto crítico contra) | −2 em testes físicos e Movimento reduzido pela metade; **não causa dano contínuo** (diferencia de Sangrando/Queimando) | tratamento médico prolongado (fora de cena) ou magia/tecnologia específica |
| Atordoado | atordoamento, choque | perde a próxima ação; efeito único, não acumula | termina automaticamente no início do próximo turno do personagem |
| Exausto | esforço extremo, falta de descanso | níveis acumuláveis; cada nível dá −1 em testes físicos e reduz 1 ação disponível por rodada ao chegar no nível 3 | descanso adequado remove 1 nível por vez |
| Amedrontado | ameaça, horror, sobrenatural | não pode se aproximar voluntariamente da fonte do medo; para agir contra ela, requer teste de Vontade (Dificuldade 10) ou gastar 1 Determinação | passa a fonte do medo sair de cena, ou teste de Vontade bem-sucedido |
| Infectado | ver `INFECCAO.md` | ver `INFECCAO.md` | ver `INFECCAO.md` |
| Amaldiçoado | ver `MALDICOES.md` (Fase 4) | ver `MALDICOES.md` | ver `MALDICOES.md` |

Caso esteja envenenado o player sofre debuff na capacidade maxima de vitalidade
| Nivel de envenenamento | debuff | observaçao |
|---|---|---|
| 1 | -10% de vitalidade maxima e -1 em todos os testes | pode ser removida de forma natural com o teste de vigor(Dificuldade igual a 8+nível)|
| 2 | -25% de vitalidade maxima e -2 em todos os testes | cada teste de vigor desce um nivel de envenenamento |
| 3 | -50% de vitalidade maxima e -3 em todos os testes | impossivel ser diminuida com teste de vigor, obrigatorio o uso de antidotos, a cada 1 rodada gera atordoamento, testes de vigor servem para impedir o atordoamento na proxima rodada|

Mais de 5+força atordoamentos seguidos leva a Incapacitaçao.
Incapacitados com envenenamento de nivel 3 morrem de 1 a 2 dias.

**Nota de consistência:** ao contrário das demais linhas desta tabela, Infectado e Amaldiçoado não são uma condição única com um efeito fixo — são **categorias** que apontam para sistemas próprios de múltiplos estágios (Infecção tem 6 Níveis; cada Maldição é uma ficha independente). Estão listadas aqui só para deixar claro que fazem parte da mesma família de "estados alterados" do personagem, não para sugerir que têm um efeito simples como Atordoado ou Exausto.

**Nota de consistência:** Sangrando, Queimando e Envenenado poderiam parecer redundantes (todos causam dano ao longo do tempo) — por isso cada um tem um mecanismo de escalada/remoção diferente: Sangrando pune ação física, Queimando é previsível e temporário, Envenenado ataca a capacidade geral do personagem em vez de só Vitalidade. Fraturado foi deliberadamente desenhado **sem** dano contínuo, para não ser uma quarta variação da mesma ideia.

---

## 9. Exploração

Viagens são medidas em **Trechos de Viagem** (mesma unidade abstrata das Corridas, `CORRIDAS.md` — reaproveitar o conceito evita criar uma escala de distância nova). A cada Trecho:

1. **Teste de Sobrevivência** (Dificuldade definida por clima/terreno: 8 fácil, 10 normal, 12+ hostil) consome 1 unidade de Suprimentos do grupo (ver Equipamentos) em caso de falha; em caso de sucesso, consome normalmente sem perdas extras.
2. **Teste de Percepção** (Dificuldade 10, feito por quem estiver de vigia) determina se o grupo nota um encontro ou perigo antes dele acontecer.

### Perigos Ambientais
Tratados como um "ataque" do ambiente: teste de Vigor ou Agilidade (conforme a natureza do perigo) vs a Dificuldade do perigo. Falha aplica uma Condição já existente (Exausto, Fraturado, Queimando) — nenhuma Condição nova exclusiva de exploração.

### Descoberta e Investigação
Teste de Investigação vs Dificuldade definida pelo Mestre, usando a Margem para controlar quanto é revelado:

| Margem | Resultado |
|---|---|
| Falha | nada encontrado, sem custo adicional |
| Sucesso | a informação básica é revelada |
| Sucesso excepcional/extraordinário | revela também um detalhe extra (pista para outra cena, vantagem tática) |

Isso reaproveita a Margem central em vez de criar uma tabela de "graus de descoberta" separada.

**Por que não é uma simulação detalhada:** o sistema não rastreia comida/água por refeição, nem clima hora a hora — cada Trecho representa um segmento narrativo relevante (meio dia, um bioma, uma etapa da jornada), suficiente para decisões significativas sem virar contabilidade.

## 10. Conflitos Sociais

Toda perícia social (Persuasão, Intimidação, Enganação) usa a mesma fórmula central contra uma nova estatística derivada:

**Resistência Social = 8 + Vontade** 
(mesma lógica de Defesa = 8 + Agilidade, seção 5).

### Quando rolar

**Só existe teste quando o resultado é incerto e importa para a cena.** Três casos dispensam rolagem:
- O pedido é trivial ou o NPC já está inclinado a aceitar → sucesso automático, sem gastar tempo de mesa.
- O pedido é impossível dentro da personalidade/interesses do NPC → falha automática, o Mestre narra a recusa.
- Não há consequência real em caso de falha → não há por que rolar, apenas narre.

### Reputação e Relações

Cada personagem tem uma Reputação de −3 a +3 com NPCs ou facções recorrentes, que **ajusta a Dificuldade dos testes sociais com aquele NPC/facção em 1 ponto por grau** (Reputação +2 = Dificuldade 2 pontos mais baixa; −2 = 2 pontos mais alta). Isso substitui a necessidade de recalcular relações a cada cena — é só consultar o número.

### Negociação (conflito social estendido)

Quando o resultado de uma negociação importante não é binário (ex: fechar um contrato, evitar uma guerra entre facções), use uma versão estendida: cada lado tenta acumular 3 "Pontos de Acordo" antes do outro, com testes alternados de Persuasão/Intimidação/Enganação vs Resistência Social do oponente — mesma estrutura de Margem (sucesso = +1 ponto, excepcional = +2, extraordinário = +3, falha crítica = o oponente ganha 1 ponto).

## 11. Progressão

Personagens evoluem gastando **Pontos de Evolução (PE)**, concedidos pelo Mestre ao fim de sessões ou marcos narrativos (referência: 3 a 5 PE por sessão — ver `MESTRE.md`).

| Melhoria | Custo |
|---|---|
| Atributo: subir 1 nível | 2 × o novo nível (ex: 0→1 custa 2, 4→5 custa 10) |
| Perícia: subir 1 nível | 1 × o novo nível (ex: 0→1 custa 1, 4→5 custa 5) |
| Habilidade Passiva nova | 3 PE |
| Habilidade Ativa nova | 5 PE |
| Habilidade Especial nova | 8 PE |
| Especialização (bônus +1 restrito a um uso específico de uma perícia, ex: "Investigação em cenas de crime") | 4 PE |

Custo de Atributo é sempre mais caro que o de Perícia equivalente — de propósito: Atributos afetam múltiplas coisas ao mesmo tempo (Vigor sozinho afeta Vitalidade, resistência à Infecção e testes físicos), então custam mais para não tornar "maximizar um Atributo" estritamente superior a diversificar Perícias.


## 12. Equipamentos

Inventário por **espaços**, não peso exato. Capacidade de carga = 5 + Força (seção 5).

| Categoria | Espaços | Efeito |
|---|---:|---|
| Arma leve (soco, faca) | 0–1 | ver `COMBATE.md` |
| Arma padrão (espada, machado, pistola, rifle) | 1 | ver `COMBATE.md` |
| Arma pesada | 2 | ver `COMBATE.md` (recarrega a cada 3 usos) |
| Armadura leve | 1 | reduz dano recebido em 1 |
| Armadura média | 2 | reduz dano recebido em 2; −1 em testes de Agilidade |
| Armadura pesada | 3 | reduz dano recebido em 3; −2 em testes de Agilidade e Movimento −1 |
| Kit médico | 1 | 3 usos; cada uso facilita 1 teste de Medicina em 1 degrau de Dificuldade |
| Ferramenta especializada | 1 | +1 em um teste de Perícia específica (não empilha com outra ferramenta igual) |
| Equipamento de exploração (corda, barraca, kit de sobrevivência) | 1 cada | reduz em 1 degrau a Dificuldade do teste de Sobrevivência correspondente (`REGRAS.md`, seção 9) |

Armadura é a única fonte de redução de dano no sistema — evita empilhar reduções de fontes diferentes (Habilidades já não podem duplicar efeitos idênticos, ver `HABILIDADES.md`).

## 13. Criação Rápida de Inimigos

Inimigos são definidos por um único número, o **Nível** (1 a 5+), que gera todas as estatísticas base:

| Nível | Vitalidade | Defesa | Bônus de Ataque | Dano |
|---:|---:|---:|---:|---|
| 1 | 11 | 9 | +4 | 1d6 |
| 2 | 14 | 10 | +5 | 1d8 |
| 3 | 17 | 11 | +6 | 1d10 |
| 4 | 20 | 12 | +7 | 1d12 |
| 5 | 23 | 13 | +8 | 2d8 |

Fórmulas: Vitalidade = 8 + Nível×3; Defesa = 8 + Nível; Bônus de Ataque = Nível+3.

**Categorias** (multiplicam o Nível base sem precisar recalcular tudo):
- **Bicho/Minion:** usa a tabela normalmente, mas aparece em grupo.
- **Padrão:** usa a tabela normalmente, sozinho ou em duplas.
- **Elite:** Vitalidade +50%, ganha 1 Habilidade (`HABILIDADES.md`).
- **Chefe:** Vitalidade +100%, 2 ações extras por rodada (total 5), ganha 1 a 2 Habilidades.

Cada inimigo ainda precisa de Nome, Categoria, Resistências/Fraquezas (ex: resistente a Queimando, fraco contra Furtividade) e Comportamento (1 linha: "ataca o alvo mais fraco", "foge abaixo de 25% de Vitalidade") — ver exemplos em `INIMIGOS.md`.


## 14. Módulos Opcionais

Três sistemas adicionais, cada um independente e opcional — a campanha usa nenhum, um, dois ou os três juntos, sem alterar nada do núcleo acima:

| Módulo | O que adiciona | Arquivo |
|---|---|---|
| Magia | uma 13ª Perícia (Conjuração), o recurso Mana, e duas formas de conjurar — Pergaminhos (seguros, mas fixos) e Conexão Arcana (livre, mas arriscada) | `MAGIA.md` |
| Classes | arquétipos tradicionais de RPG (Guerreiro, Mago, Ladino etc.) que empacotam Atributo Principal, Perícias e a Habilidade inicial — sem somar pontos além do que a criação já dá | `CLASSES.md` |
| Raças | povos jogáveis (Humano, Elfo, Anão, Orc etc.) que deslocam 1 ponto entre dois Atributos e concedem uma Habilidade Única — também sem somar pontos | `RACAS.md` |

Classes e Raças compartilham um eixo de progressão próprio: a **Habilidade Única** de cada uma evolui em 3 Estágios, e os Estágios 2 e 3 não custam PE — desbloqueiam completando uma Missão de Classe/Origem, guiada pelo Mestre (`MESTRE.md` §10).

## 15. Tempo e Descanso

Três escalas de tempo cobrem tudo que o sistema precisa medir — nenhuma exige contar minutos:

| Escala | Duração narrativa | Uso |
|---|---|---|
| Ação | ~alguns segundos | combate, corridas (3 ações/rodada) |
| Cena | minutos a ~1 hora | investigação, conflito social, perseguição completa |
| Trecho / Descanso / Sessão | ver abaixo | exploração, recuperação, downtime |

### Descanso Curto
Uma pausa de alguns minutos a ~1 hora dentro da mesma cena ou logo após ela (respirar, fazer curativo de campo, reorganizar o grupo). Recupera:
- **1 ponto de Determinação** (`REGRAS.md` §7).
- **Metade do Mana atual até o máximo**, arredondado para cima, se `MAGIA.md` estiver em uso (`MAGIA.md` §2).
- Não recupera Vitalidade nem Sorte.

### Descanso Longo
Uma noite de sono ou pausa segura equivalente (acampamento, hospedagem). Recupera:
- **Vitalidade até o máximo** (ver "Recuperação de Vitalidade" abaixo).
- **Determinação até o máximo**.
- **Mana até o máximo**, se aplicável.
- Remove **1 Nível de Exausto**.
- Não recupera Sorte (ver §6) nem reduz Infecção/Maldições — esses seguem suas próprias regras de tratamento.

Um Descanso Longo só se completa se não for interrompido por um encontro que force ação — interrupção deixa as recuperações pela metade (arredondando para cima), a critério do Mestre.

### Recuperação de Vitalidade
Fora de tratamento médico (que age em cena, ver `COMBATE.md` §8), a Vitalidade se recupera:
- **Descanso Longo:** recupera totalmente.
- **Downtime/tempo entre aventuras:** recupera totalmente, mesmo sem Descanso Longo formal.
- **Sem descanso** (ex: marcha forçada): não recupera sozinha — só por Medicina, item ou habilidade.

### Sorte e Determinação (recapitulação)
Sorte só se recupera entre sessões ou por decisão do Mestre em momentos marcantes (§6) — nunca por Descanso. Determinação segue a tabela acima (§7 detalha os usos).

## 16. Estabilização e Morte

Regras completas de Ferimentos, Incapacitação e Morte estão em `COMBATE.md` §6 e §8 (dependem de dano recebido em combate, então ficam junto das regras de ataque). Esta seção fixa os termos usados em qualquer contexto, dentro ou fora de combate:

| Estado | Gatilho | Pode agir? |
|---|---|---|
| Saudável / Ferido / Gravemente Ferido | Vitalidade acima de 0 | Sim, com as penalidades de `COMBATE.md` §6 |
| Incapacitado | Vitalidade 0 ou menos | Não, exceto gastando Determinação (`REGRAS.md` §7) |
| Moribundo | Incapacitado e não estabilizado | Testes de Vigor por rodada (`COMBATE.md` §8) |
| Morto | Vitalidade ≤ −máximo | Não — permanente |

**Estabilizar** (fora ou dentro de combate) é sempre um teste de Medicina, Dificuldade 8, feito por outro personagem em 1 ação. Sucesso trava a Vitalidade do alvo no valor atual (não sobe nem desce) até receber tratamento maior; falha não piora nada, só consome a ação.

## 17. Furtividade

Toda tentativa de agir sem ser notado — dentro ou fora de combate — usa a mesma escala de três estados:

| Estado | Significado |
|---|---|
| Oculto | ninguém hostil sabe da presença do personagem naquele local |
| Suspeito | algo foi notado (som, vulto, rastro), mas ninguém confirmou o quê ou onde |
| Detectado | a posição do personagem é conhecida |

**Ficar Oculto:** teste de Furtividade vs a Percepção+Investigação de quem poderia notar (Dificuldade = 8 + a maior Percepção relevante na cena). Sucesso mantém Oculto.

**De Oculto para Suspeito:** qualquer ação barulhenta, ou uma falha simples no teste de Furtividade, degrada 1 grau (Oculto→Suspeito), não direto para Detectado — dá ao Mestre espaço para tensão antes da revelação.

**De Suspeito para Detectado:** uma falha crítica no teste de Furtividade, ou uma ação que exponha o personagem diretamente (atacar, falar alto, luz direta), leva a Detectado.

**Voltar a Oculto:** só é possível saindo do campo de percepção de quem detectou (linha de visão/audição quebrada por pelo menos 1 ação) e passando novamente pelo teste de Ficar Oculto — não existe "esconder-se instantaneamente" de quem já está olhando.

**Ataque a partir de Oculto:** o primeiro ataque feito a partir do estado Oculto contra um alvo que não sabe da presença do atacante é automaticamente um Sucesso Extraordinário na Margem de acerto (`COMBATE.md` §3), sem precisar rolar o ataque — só a Furtividade que garantiu o Oculto já foi o teste relevante. Depois desse ataque, o atacante passa a Detectado por quem foi atingido (mas pode continuar Oculto para outros alvos que não notaram).

## 18. Ajuda e Intervenção

A ação **Ajudar** (`COMBATE.md` §1) não é exclusiva de combate: fora de cena, qualquer personagem pode gastar uma ação relevante para dar **+1 no próximo teste de um aliado**, desde que a ajuda seja plausível na ficção (não é possível "ajudar" em algo que só uma pessoa fisicamente consegue fazer, como se espremer por um vão estreito).

**Intervir** contra um teste de um NPC ou obstáculo (ex: atrapalhar quem está tentando escapar, distrair um guarda) usa a mesma lógica: um teste oposto ou uma ação que force o alvo a repetir o teste em 1 degrau de Dificuldade mais difícil, à critério do Mestre — nunca cancela o teste do alvo automaticamente (regra anti-quebra de `HABILIDADES.md` §2 se aplica igualmente aqui: nenhum efeito gera sucesso/falha automática de terceiros).

Ajuda e Intervenção **não empilham** entre múltiplos ajudantes no mesmo teste — o bônus máximo por teste é +1, não importa quantos personagens ajudem (evita que um grupo grande torne qualquer teste trivial).

---

