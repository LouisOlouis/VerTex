# CRAFTING

Sistema modular: estrutura fixa + poucos exemplos, não um catálogo de centenas de receitas. Um Mestre pode criar qualquer receita nova seguindo o mesmo modelo.

## 1. Estrutura de uma Receita

Toda receita tem os mesmos campos:

| Campo | Descrição |
|---|---|
| Perícia | Medicina, Tecnologia ou Sobrevivência (as três cobrem praticamente qualquer fabricação; o Mestre pode liberar outra em casos específicos) |
| Materiais | quantidade de **Componentes** por tier (Comum/Incomum/Raro — seção 2) |
| Ferramenta | qual kit é exigido (`EQUIPAMENTOS.md`) — sem ele, Dificuldade +2 degraus ou impossível, a critério do Mestre |
| Tempo | 1 Trecho (em campo), 1 Cena (com ferramenta e local adequado) ou 1 Bloco de Downtime (`DOWNTIME.md`) |
| Dificuldade | usa a tabela central (`REGRAS.md` §1.2) |
| Resultado no Sucesso | o item é produzido |
| Resultado na Falha | Componentes Comuns/Incomuns não se perdem (podem tentar de novo); Componentes Raros se perdem numa Falha Crítica |

## 2. Componentes

Materiais são abstraídos em 3 tiers, ocupando espaço de inventário como qualquer item (`REGRAS.md` §12):

| Tier | Espaços | Como se consegue |
|---|---:|---|
| Comum | 1 = 3 unidades | comprado (5 Créditos/unidade) ou coletado em Exploração (`REGRAS.md` §9, Descoberta) |
| Incomum | 1 = 1 unidade | comprado (25 Créditos) ou recompensa específica de missão |
| Raro | ocupa 1 espaço por unidade, não empilha | quase nunca comprado — normalmente um gancho de aventura |

## 3. Fabricar

**Teste:** 2d6 + Atributo relevante + Perícia (Medicina/Tecnologia/Sobrevivência) vs a Dificuldade da receita.

| Margem | Resultado |
|---|---|
| Falha crítica | nada produzido; Componentes Raros usados na receita são perdidos |
| Falha | nada produzido; Componentes Comuns/Incomuns preservados, pode tentar de novo (novo gasto de Tempo) |
| Sucesso | item produzido normalmente |
| Sucesso Excepcional/Extraordinário | item produzido + 1 unidade extra de Componente Comum "sobra" do processo, ou o Tempo gasto é reduzido pela metade (à escolha do jogador) |

## 4. Exemplos de Receita

| Nome | Perícia | Materiais | Ferramenta | Tempo | Dificuldade | Resultado |
|---|---|---|---|---|---|---|
| Antídoto caseiro | Medicina | 2 Comuns | Kit médico | 1 Cena | 10 | 1 Antídoto (`EQUIPAMENTOS.md`) |
| Kit médico improvisado | Medicina | 3 Comuns | — | 1 Trecho | 12 | Kit médico com 1 uso (em vez de 3) |
| Ferramenta especializada improvisada | Tecnologia | 2 Comuns + 1 Incomum | Kit de arrombamento ou similar | 1 Cena | 12 | Ferramenta especializada temporária (1 cena de duração) |
| Armadilha de campo | Sobrevivência | 2 Comuns | — | 1 Trecho | 10 | 1 uso: primeiro inimigo a passar sofre um teste de Agilidade (Dificuldade 10) ou fica Caído (`COMBATE.md` §9) |
| Munição improvisada | Tecnologia | 1 Comum | — | 1 Trecho | 10 | 1 carga extra para Pistola ou Rifle (`ECONOMIA.md` §3) |

## 5. Criando uma Receita Nova

Siga a tabela da seção 1. Regras de equilíbrio:
- Nunca produza um efeito que as regras anti-quebra de `HABILIDADES.md` §2 proibiriam numa Habilidade (sem sucesso automático, sem ignorar Defesa/Vitalidade/Dificuldade por completo).
- Um item fabricado nunca deve ser estritamente melhor que o equivalente comprado (`EQUIPAMENTOS.md`) pelo mesmo custo de espaço — fabricar existe para dar acesso quando comprar não é possível (campo, embargo, item raro), não para ser sempre a opção ótima.

---
*Ver `DOWNTIME.md` para encaixar Fabricação em um Bloco de tempo entre aventuras, e `ECONOMIA.md` para preços de Componentes.*
