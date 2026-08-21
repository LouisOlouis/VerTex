# ALQUIMIA

A Alquimia é o ramo mais especializado do Crafting (`CRAFTING.md`) — em vez de transformar Componentes comuns em itens comuns, ela transforma matéria-prima rara e carregada de força elemental em **Essência Arcana**, e a Essência Arcana em poções, pergaminhos e artefatos. Este arquivo cobre a Alquimia inteira: como se extrai Essência, como se processa Essência em produto final, e como isso se conecta ao resto do sistema (Crafting, Magia, Downtime, Economia).

**Pré-requisito de mesa:** a Alquimia depende do módulo `MAGIA.md` estar ativo na campanha, porque todo o sistema gira em torno de gastar **Mana** — um recurso que só existe se esse módulo estiver em uso. Sem `MAGIA.md`, trate a Alquimia como ainda não disponível, do mesmo jeito que Classes que dependem de magia (Mago, Druida, Clérigo) viram conceito narrativo puro sem o módulo.

## 1. Quem pratica

Qualquer personagem com Mana pode praticar Alquimia — não é necessário ter Conexão Arcana, não é necessário pertencer a uma Classe específica. A Mana é o único portão de entrada, e ela já existe para qualquer personagem sob `MAGIA.md` (seção 2 daquele arquivo). Isso é uma diferença deliberada em relação à Conexão Arcana: enquanto conjurar exige um vínculo pessoal com um elemento, a Alquimia é técnica pura — um ofício que se aprende, não um dom que se desenvolve.

A Classe **Transmutador** (`CLASSES.md`) e a Raça **Homúnculo** (`RACAS.md`) foram desenhadas especificamente para recompensar quem investe nesse caminho, mas nenhuma delas é pré-requisito — são atalhos de otimização, não portas trancadas.

## 2. Os Dois Artefatos Centrais

### 2.1 Pedra Filosofal

A Pedra Filosofal é a estação de trabalho da Alquimia — o equivalente, em termos de regra, a um Kit especializado (`CRAFTING.md` §1, campo Ferramenta) que toda receita alquímica exige. Sem ela, nenhuma receita de Alquimia pode ser tentada.

- **Função:** processa Essência Arcana + Mana + uma condição/catalisador ambiental em um produto final (poção, pergaminho, Pedra Arcana, e assim por diante).
- **Custo de operação:** cada uso consome Mana do praticante, além dos custos normais de Materiais/Tempo/Dificuldade que qualquer receita de Crafting já exige.
- **Reutilizável:** ao contrário de um Componente consumido em uma receita comum, a Pedra Filosofal em si não se gasta em receitas do dia a dia (poções, pergaminhos) — ela é uma ferramenta permanente, como um Kit médico é permanente enquanto guarda usos.
- **Exceção — rituais de artefato:** em receitas de escala maior (criar uma Pedra Arcana para um Cajado, criar o Livro da Gula), a Pedra Filosofal deixa de ser reutilizável e é **consumida como componente do próprio ritual**. Essa é a linha que separa artesanato alquímico cotidiano de criação de artefato definitivo — ver seção 6.
- **Risco:** enquanto processa uma receita, a Pedra Filosofal fica fisicamente exposta. Se for destruída ou o processo for interrompido (combate, sabotagem, desastre) antes do fim, tudo que estava em processamento — Essência, Materiais adicionais e potencialmente a própria Pedra — se perde, seguindo a mesma lógica de "Falha Crítica" de `CRAFTING.md` §3. Isso é o custo real da Alquimia: ela **não gera Infecção Arcana** (é deliberadamente a via "segura" de tocar poder arcano, do mesmo jeito que Pergaminhos são a via segura de conjurar — `MAGIA.md` §3), mas não é uma via sem risco. O risco só é deslocado de "dentro do corpo" para "fora, no mundo".

### 2.2 Joia de Azoth

A Joia de Azoth é um inventário portátil dedicado a Essência Arcana — funciona para Essência da mesma forma que um espaço de inventário comum funciona para Componentes (`REGRAS.md` §5 e §12), só que especializado e evolutivo.

- **Custo de acesso:** item raro e caro (ver `ECONOMIA.md` §3 para preço de referência) — normalmente algo que um personagem inicial não começa possuindo, e sim conquista ao longo da campanha.
- **Extração:** ao consumir, dentro da Joia, um item de raridade **Raro** (`CRAFTING.md` §2 — o único tier acima de Incomum no sistema) vinculado a um Arcano, o item é convertido em unidades de Essência Arcana daquele Arcano. Como o item bruto consumido é sempre Raro, e itens Raros "quase nunca são comprados — normalmente um gancho de aventura" (`CRAFTING.md` §2), a extração de Essência está estruturalmente amarrada à exploração e às missões, não à economia comum. Ver a tabela de exemplos na seção 4.
- **Rendimento:** cada item Raro consumido rende **3 unidades de Essência** daquele Arcano — o mesmo múltiplo já usado para Componentes Comuns em `CRAFTING.md` §2 ("1 espaço = 3 unidades"), reaproveitando a mesma proporção em vez de inventar uma nova. Não existe grau ou pureza adicional: a quantidade é a única variável.
- **Capacidade e evolução:** a Joia começa com espaço limitado. Ela só expande sua capacidade ao atingir a capacidade máxima **simultaneamente em 5 ou mais tipos diferentes de Essência**. Esse gatilho aumenta a cada evolução subsequente (a próxima expansão exige um número maior de tipos cheios ao mesmo tempo). Isso significa que a Joia recompensa **diversidade de prática**, não volume de uso: um alquimista que só extrai Essência de Fogo, por mais que processe, nunca a faz evoluir sozinho — ele precisa deliberadamente explorar Arcanos diferentes.

### 2.3 Rota alternativa: Frasco + Moedor

Um praticante sem Joia de Azoth ainda extrai Essência, através de duas etapas manuais em vez de uma etapa automática:

1. **Frasco** — guarda a matéria-prima Rara extraída, um item por Frasco (mesma lógica de "não empilha" dos Componentes Raros, `CRAFTING.md` §2).
2. **Moedor** — ferramenta separada que decompõe o conteúdo do Frasco em Essência Arcana utilizável (mesmo rendimento de 3 unidades por item, seção 2.2).

Essa rota é acessível a qualquer alquimista iniciante — Frascos e Moedores são baratos (`ECONOMIA.md` §3) — mas, ao contrário da Joia de Azoth, **não escala**: não ganha capacidade ou eficiência com o uso. É a opção de entrada; a Joia é o investimento de longo prazo. Nenhuma das duas é "pior" — são dois pontos diferentes da mesma curva de investimento.

## 3. Estrutura de uma Receita de Alquimia

Uma receita de Alquimia usa exatamente os mesmos campos de uma receita de Crafting comum (`CRAFTING.md` §1), com três diferenças específicas do ramo:

| Campo | Em Crafting comum | Em Alquimia |
|---|---|---|
| Perícia | Medicina, Tecnologia ou Sobrevivência | as mesmas três — a receita define qual (Medicina para a maioria das poções, Tecnologia para Pedras Arcanas e artefatos, Sobrevivência quando a receita usa material bruto colhido em campo) |
| Materiais | Componentes por tier (Comum/Incomum/Raro) | unidades de **Essência Arcana**, por Arcano e quantidade — extraídas antes, pela Joia de Azoth ou por Frasco+Moedor |
| Ferramenta | um Kit específico | a **Pedra Filosofal**, sempre — sem ela, a receita é impossível (não existe versão "improvisada" de Alquimia, ao contrário de outros Kits) |
| Tempo | Trecho / Cena / Bloco de Downtime | normalmente 1 Cena (poções simples) a 1 Bloco de Downtime (receitas maiores) — ver `DOWNTIME.md` |
| Dificuldade | tabela central (`REGRAS.md` §1.2) | a mesma tabela, mas cada receita de Alquimia também define uma **condição/catalisador** obrigatória (ex: uma fogueira acesa) — sem ela, a receita não pode nem ser tentada, do mesmo jeito que Ferramenta ausente em Crafting comum |
| **Custo adicional exclusivo de Alquimia** | não existe | **Mana**, gasta pela Pedra Filosofal além de qualquer outro custo |
| Resultado no Sucesso | item produzido | poção, pergaminho ou artefato produzido |
| Resultado na Falha | Comuns/Incomuns preservados, Raros perdidos numa Falha Crítica | igual — mas como Alquimia só usa Essência (já extraída de um Raro), uma Falha Crítica na Pedra Filosofal significa perder a Essência já investida, não o item Raro original (que já virou Essência antes) |

Ou seja: **teste 2d6 + Atributo + Perícia (Medicina/Tecnologia/Sobrevivência) vs Dificuldade da receita**, exatamente como qualquer Fabricação — só que além de gastar Essência e ocupar a Pedra Filosofal por um tempo, o praticante também paga Mana, e precisa estar no lugar/condição certos.

### Tabela de Margem (idêntica a `CRAFTING.md` §3)

| Margem | Resultado |
|---|---|
| Falha crítica | nada produzido; a Essência investida na receita é perdida |
| Falha | nada produzido; a Essência é preservada, pode tentar de novo (novo gasto de Tempo e Mana) |
| Sucesso | item produzido normalmente |
| Sucesso Excepcional/Extraordinário | item produzido + efeito ampliado (mesma lógica de bônus de `CRAFTING.md` §3), à escolha do jogador |

## 4. Essências Arcanas — como se consegue cada uma

Cada Essência Arcana corresponde a um dos 12 Arcanos definidos em `MAGIA.md` §6. Como todo material-fonte precisa ser Raro (seção 2.2), cada Essência está amarrada a um gancho de aventura temático — a tabela abaixo dá um ponto de partida para cada Arcano; o Mestre pode (e deve) adaptar os nomes à sua própria campanha, mantendo a mesma lógica de "material Raro, específico, normalmente ligado a uma missão".

| Arcano | Exemplo de material Raro | Onde normalmente se encontra |
|---|---|---|
| Fogo | Coração de Salamandra Ígnea | no núcleo de um vulcão adormecido, ou guardado por uma criatura de fogo |
| Água | Pérola de Maré Viva | formada apenas durante uma tempestade específica, em mar aberto |
| Terra | Núcleo de Granito Vivo | cresce lentamente ao redor de algo enterrado — leva décadas para se formar |
| Ar/Vento | Pena de Ave-do-Trovão | de uma criatura que nunca pousa, avistada apenas em tempestades |
| Gelo | Fragmento de Geleira Eterna | de uma geleira que nunca derrete, mesmo sob calor extremo |
| Eletricidade | Núcleo de Elemental Capturado | condensado no momento exato de uma tempestade elétrica |
| Luz | Lágrima Cristalizada | de um ser ou lugar associado à pureza/revelação, formada em um momento de grande verdade |
| Escuridão | Fragmento de Sombra Persistente | uma sombra que se recusa a desaparecer mesmo sob luz direta |
| Natureza | Semente da Árvore-Mãe | de uma árvore ancestral, guardada havia gerações |
| Metal | Minério que Nunca Enferruja | extraído de uma jazida com história própria, geralmente disputada |
| Sangue | Sangue de Pacto Rompido | ainda quente, de um vínculo mágico desfeito à força |
| Espírito | Relicário de Última Lembrança | carrega a memória final de alguém que morreu com algo inacabado |

> Esses exemplos existem para dar ao Mestre um ponto de partida narrativo — eles não têm efeito mecânico próprio além de "ser Raro e vinculado a um Arcano". A extração em si (seção 2.2) já define o rendimento (3 unidades de Essência por item).

## 5. Fabricando com a Pedra Filosofal

Toda receita de Alquimia processada na Pedra Filosofal define, além dos campos da seção 3: **qual condição/catalisador** o ambiente precisa oferecer, **qual combinação de Essências** (Arcano + quantidade), e **quanto Mana** custa. Para manter os números coerentes com o resto do sistema, a Alquimia reaproveita a mesma progressão de Dificuldade/Custo de Mana já usada para os Círculos de Pergaminho (`MAGIA.md` §3) — um "Tier" de poção alquímica é, na prática, do mesmo peso que um Círculo de Pergaminho.

### Tabela de Tiers

| Tier | Dificuldade | Custo de Mana | Unidades de Essência por Arcano exigido |
|---:|---:|---:|---:|
| 1 | 8 | 2 | 1 |
| 2 | 10 | 3 | 2 |
| 3 | 12 | 5 | 3 |
| 4 | 14 | 7 | 4 |
| 5 | 16 | 10 | 5 |

### Exemplos de Receita

| Nome | Tier | Catalisador | Essências | Perícia | Resultado |
|---|---:|---|---|---|---|
| Bálsamo Calmante | 1 | água corrente | 1 unidade de Água | Medicina | remove 1 Nível de Exausto |
| Poção de Resistência a Fogo | 2 | fogueira acesa | 2 de Fogo + 2 de Gelo | Medicina | ignora dano da Condição Queimando por 1 cena |
| Elixir de Fôlego Prolongado | 3 | imersão em água parada | 3 de Água + 3 de Ar/Vento | Sobrevivência | respira debaixo d'água por 1 cena |
| Tônico de Regeneração Acelerada | 4 | luz do sol direta ao meio-dia | 4 de Luz + 4 de Natureza | Medicina | recupera Vitalidade adicional no próximo Descanso Longo |
| Elixir de Pele de Pedra | 5 | contato direto com rocha exposta | 5 de Terra + 5 de Metal | Tecnologia | reduz dano recebido em 2 por 1 cena, cumulativo com Armadura |

> Como em `CRAFTING.md` §5, estes são exemplos, não um catálogo fechado — o Mestre pode criar qualquer receita nova seguindo a mesma tabela de Tiers, mantendo a regra de equilíbrio de `CRAFTING.md` §5: uma poção fabricada nunca deve ser estritamente melhor que o equivalente comprado pelo mesmo custo de espaço/investimento.

## 6. Rituais de Artefato

Diferente das receitas do dia a dia (seção 5), alguns produtos consomem a própria Pedra Filosofal (e às vezes a Joia de Azoth) como componente do ritual, não como ferramenta reutilizável. Isso marca a fronteira entre artesanato cotidiano e criação de artefato definitivo:

- **Pedra Arcana** (núcleo obrigatório de um Cajado) — consome 1 Pedra Filosofal inteira + 8 unidades de Essência de um único Arcano. Ver `MAGIA.md`, seção sobre Cajados, para as regras completas de uso.
- **Livro da Gula** — consome 1 Pedra Filosofal + 1 Joia de Azoth, ambas permanentemente, além de muito Papel Arcano e Couro de Dragão. Ver `MALDICOES.md` para a ficha completa do artefato.

Esses rituais normalmente não são "receitas de mesa" no sentido de Downtime comum — são ganchos de aventura por si só, com Dificuldade e consequências definidas pelo Mestre caso a caso, seguindo o mesmo princípio de `CRAFTING.md` §2 para Componentes Raros: "quase nunca comprado, normalmente um gancho de aventura".

---
*Ver `CRAFTING.md` para a estrutura geral de Fabricação, `MAGIA.md` para Pergaminhos e Cajados, `MALDICOES.md` para o Livro da Gula, `ECONOMIA.md` para preços da Pedra Filosofal/Joia de Azoth/Frasco/Moedor, e `DOWNTIME.md` para encaixar Alquimia em um Bloco de tempo entre aventuras.*
