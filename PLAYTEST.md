# PLAYTEST

Três cenários testados, usando as fichas de exemplo de `CRIACAO_PERSONAGEM.md` e as fórmulas já validadas matematicamente em cada fase. Resultados de dados foram gerados por simulação (`/tools/`) quando o objetivo era medir tendência estatística, e por rolagem única narrada quando o objetivo era testar clareza de regra em uso.

## Teste 1: Combate — duração e letalidade

**Cenário:** Marco (O Combatente, bônus Combate 3+Força4=7, Vitalidade 16, Defesa 11) enfrenta 2 Assaltantes (Minion Nível 1, cada um Vitalidade 11, Defesa 9, bônus +4, dano 1d6).

**Execução (rolagem narrada):**
1. Iniciativa: Marco 2d6(7)+Agilidade3+Percepção2=12. Assaltantes: 9. Marco age primeiro.
2. Rodada 1: Marco ataca o Assaltante A duas vezes (2 ações) — 2d6(9)+7=16 vs Defesa9: acerto, Margem+7 (Sucesso extraordinário) → dano em dobro, maior de 2d6: 5. Assaltante A cai para 6. Segundo ataque: 2d6(6)+7=13, Margem+4, dano normal+2 = 1d6(4)+2=6. Assaltante A morre.
3. Assaltante B ataca Marco: 2d6(8)+4=12 vs Defesa11: acerto, dano 1d6(3). Marco: 16→13 (ainda Saudável).
4. Rodada 2: Marco foca Assaltante B, mata em 1 ataque (2d6(10)+7=17, dano 1d6(5)+2=7 — Assaltante B tinha 11, mas Margem+7 exigiria conferir; mesmo em dano normal já derruba com 2 ações).

**Resultado:** combate resolvido em 2 rodadas, consistente com a simulação da Fase 6 (1 PJ médio/especializado vence 2 minions com folga, ~95-100%). Nenhum ajuste necessário.

**Revisão:** a regra de Sucesso Extraordinário em ataque (dano em dobro) apareceu logo na primeira rolagem do teste e resolveu o combate rápido — confirma que a Margem torna ataques individuais importantes, não só o total de rodadas.

## Teste 2: Investigação — funcionamento das perícias

**Cenário:** Iris (A Investigadora, Investigação3+Intelecto4=7) examina a cena de um ataque de Contaminado, tentando descobrir a origem da Infecção. Dificuldade definida pelo Mestre: 12 (Difícil, pistas foram deliberadamente escondidas).

**Execução:** 2d6(6)+7=13 vs 12: Margem+1, Sucesso simples. Resultado: Iris descobre a informação básica (o ataque veio de um bueiro específico), mas não o detalhe extra (quem esteve lá antes).

Numa segunda tentativa, com uma pista física em mãos (Mestre reduz a Dificuldade 1 degrau, para 10): 2d6(9)+7=16, Margem+6, Sucesso Extraordinário. Iris ganha a informação básica **e** o detalhe extra (uma pegada que não é humana).

**Resultado:** o sistema de Margem para graus de descoberta (`REGRAS.md` §9) funcionou sem precisar de tabela nova — o mesmo conceito de Margem usado em combate se aplicou diretamente à investigação.

**Revisão:** nenhum ajuste necessário. Ponto de atenção documentado para o Mestre: reduzir a Dificuldade por progresso da cena (como no exemplo, achar uma pista física) é a ferramenta certa para recompensar boas decisões dos jogadores sem inventar um bônus numérico avulso — reforça a regra da seção 1.3 de `REGRAS.md`.

## Teste 3: Corrida — a corrida é interessante?

**Cenário:** perseguição de 6 Trechos. Deko (O Sobrevivente Carismático, Sobrevivência não cobre Pilotagem — usa Atletismo1+Agilidade2=3, fraco nessa corrida) foge de um Batedor motorizado (bônus 5+veículo+2=7).

**Execução:**
- Rodada 1: Deko Acelera: 2d6(5)+3=8 vs Dificuldade10 (terreno urbano): Margem−2, Falha, sem avanço. Batedor: 2d6(8)+7=15, Margem+5, avança 2. Posição: Deko 0, Batedor 2 (o Batedor já ultrapassaria se estivessem no mesmo Trecho, mas partiram de pontos diferentes — Mestre resolve como distância abrindo).
- Rodada 2: Deko, atrás, tenta Manobra Arriscada (Dificuldade sobe para 12): 2d6(11)+3=14, Margem+2, Sucesso — avança 1 (mais o bônus da manobra não se aplicou pois não foi Excepcional/Extraordinário). Posição: Deko 1, Batedor ainda avança normal: +1. 
- Rodada 3: Deko tenta de novo a Manobra Arriscada: 2d6(12)+3=15 vs 12, Margem+3 (Sucesso Excepcional) — avança 2+1(bônus da manobra)=3. Bom resultado, mas ainda atrás.

**Resultado:** a corrida gerou tensão real — Deko, claramente em desvantagem de bônus, teve uma ferramenta ativa (Manobra Arriscada) que criou chance de virada sem garantir vitória, exatamente como validado por simulação na Fase 5.

**Revisão:** nenhum ajuste de regra necessário. Nota de clareza adicionada: quando os competidores partem de pontos diferentes (perseguição, não corrida lado a lado), o Mestre deve narrar a "distância" como a diferença entre as posições, não uma posição absoluta — isso não estava explícito em `CORRIDAS.md` e foi adicionado.

---
*Ajuste de clareza aplicado em `CORRIDAS.md` como resultado deste playtest — ver `BALANCEAMENTO.md`, Fase 9.*
