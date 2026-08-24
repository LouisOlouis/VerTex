# MAGIA (Módulo Opcional)

Este é um módulo — só entra na mesa se a campanha usar magia além (ou em vez) da Infecção. Reaproveita a mecânica central em vez de criar um sistema numérico paralelo. Ver também `CLASSES.md` (Mago, Druida, Clérigo e o Transmutador se apoiam neste sistema) e `RACAS.md` (algumas raças começam com afinidade arcana, incluindo o Homúnculo).

Existem **três formas** de usar magia, com uma tensão diferente cada uma:

- **Pergaminhos** — magia aprendida/técnica: segura, mas rígida e descartável.
- **Conexão Arcana** — magia vivida/espiritual: flexível, mas arriscada para corpo e mente.
- **Cajados** *(seção 7)* — não são uma terceira forma de conjurar por conta própria, mas um catalisador que potencializa a Conexão Arcana de quem já a possui.

Todas gastam do mesmo recurso: **Mana**. A produção de Pergaminhos e a criação de Cajados usam, além disso, o sistema de Alquimia (`ALQUIMIA.md`).

## 1. Nova Perícia: Conjuração

13ª Perícia, só relevante se este módulo estiver em uso. Escala 0–5, igual às demais (`REGRAS.md` §4).

## 2. Mana

**Mana = 4 + Intelecto + Vontade** (faixa 4 a 14).

**Quanto mais magia você usa, mais Mana você tem:** todo uso de magia — Pergaminho ou Conexão Arcana, dando certo ou errado — soma 1 **Uso Mágico Acumulado** (permanente, não zera). A cada **8 Usos Mágicos Acumulados**, o Mana máximo sobe **+1**, até um teto de **+5** (o crescimento para em 40 usos acumulados — o suficiente para acompanhar uma campanha inteira sem inflacionar o número para sempre).

Mana se recupera pela metade (arredondado para cima) em um descanso curto, e por completo em um descanso longo.

## 3. Pergaminhos

Um Pergaminho contém **um único feitiço fixo, sem variações de no maximo 5 usos** — "Pergaminho de Bola de Fogo" faz bola de fogo, nada mais. É um item consumível (1 espaço de inventário, `EQUIPAMENTOS.md`).

**Teste para usar:** 2d6 + Intelecto + Conjuração vs Dificuldade do Pergaminho.

| Círculo do Pergaminho | Dificuldade | Custo de Mana | Dado de efeito | usos |
|---:|---:|---:|---|---|
| 1 | 8 | 2 | 1d6 | 5 |
| 2 | 10 | 3 | 1d10 | 3 |
| 3 | 12 | 5 | 2d8 | 2 |
| 4 | 14 | 7 | 2d10 | 2 |
| 5 | 16 | 10 | 3d10 | 1 |

Resultado pela Margem (`REGRAS.md` §2):

| Margem | Efeito | O que acontece com o Pergaminho |
|---|---|---|
| Falha crítica | nada acontece | **destruído** — se desfaz sem efeito; o Mana não é gasto |
| Falha | nada acontece | intacto — pode tentar de novo depois |
| Sucesso | efeito normal | **1 de uso** |
| Sucesso excepcional | efeito ampliado (+2 no dado) | 1 de uso |
| Sucesso extraordinário | efeito ampliado (dado em dobro, usa o maior) | nao sofre dano de uso |

**Por que Falha Crítica não causa Infecção Arcana:** um Pergaminho já fez o trabalho difícil de estabilizar o feitiço antes de chegar às suas mãos — o risco foi pago por quem o escreveu, não por quem o usa. É isso que torna Pergaminhos a forma "segura" de fazer magia: previsíveis, descartáveis, sem risco pessoal, ao custo de nunca fazerem nada além do que já vêm prontos para fazer.

### 3.1 Produção de Pergaminhos *(requer `ALQUIMIA.md`)*

Um Pergaminho não nasce pronto — alguém o produz, gastando o mesmo aparato de `ALQUIMIA.md`, mais um teste de conjuração de verdade. O processo tem duas etapas bem separadas:

**Etapa 1 — Preparar o suporte.** Uma folha de **Papel Arcano** (o mesmo material usado no ritual do Livro da Gula, `MALDICOES.md`) é imbuída com Mana através de um teste de Conjuração puro: **2d6 + Intelecto + Conjuração vs Dificuldade 10**. Essa etapa não usa Arcanismo nem Alquimia — qualquer conjurador pode preparar Papel Arcano imbuído em série, mesmo sem nunca ter tocado em Essência Arcana. O resultado é um Papel Arcano pronto para receber um feitiço.

**Etapa 2 — Gravar o feitiço.** Isso já usa o aparato completo de Alquimia:

1. Formar um círculo com as Essências Arcanas correspondentes ao Arcano do feitiço desejado, na mesma quantidade exigida pelo Círculo do Pergaminho (ver tabela abaixo).
2. Posicionar a Pedra Filosofal no centro do círculo (uso reutilizável — a Pedra não é consumida nesta etapa).
3. O conjurador tenta o feitiço normalmente por **Conexão Arcana** (`MAGIA.md` §4: 2d6 + Vontade + Nível de Conexão vs a Dificuldade do Círculo desejado), mas aponta o efeito para a Pedra Filosofal em vez de liberá-lo na cena — a Pedra intercepta e captura o resultado.
4. No clímax, as Essências do círculo se espalham pelo ambiente (a descarga visual do poder sendo liberado) e o Papel Arcano queima — é o próprio ato de queimar que grava o feitiço nele.

| Círculo do Pergaminho | Dificuldade da conjuração | Essência exigida (por Arcano do feitiço) |
|---:|---:|---:|
| 1 | 10 | 1 unidade |
| 2 | 12 | 2 unidades |
| 3 | 14 | 3 unidades |
| 4 | 16 | 4 unidades |
| 5 | 18+ | 5 unidades |

O resultado da conjuração na Etapa 2 segue a Margem normal de Conexão Arcana (`MAGIA.md` §4): Falha destrói o círculo de Essências sem produzir nada (papel intacto, pode tentar de novo); Falha Crítica não gera Infecção Arcana aqui (a Pedra Filosofal absorve o choque no lugar do corpo do conjurador — mesma lógica de risco físico de `ALQUIMIA.md` §2.1), mas destrói tanto as Essências quanto o papel; Sucesso produz o Pergaminho com as estatísticas normais de seu Círculo (`MAGIA.md` §3); Sucesso Excepcional/Extraordinário produz o Pergaminho com 1 uso extra.

Um Pergaminho produzido dessa forma é **idêntico** a um comprado (`ECONOMIA.md` §3) — Alquimia é uma via de acesso alternativa, não uma versão superior, seguindo a mesma regra de equilíbrio de `CRAFTING.md` §5.

## 4. Conexão Arcana

Um personagem pode se conectar com um **Arcano** (um elemento ou força — lista completa na seção 6). A Conexão tem um **Nível (0 a 5)** por Arcano, comprado com PE (mesmo custo de Perícia: 1×novo nível — `REGRAS.md` §11), independente para cada Arcano que o personagem desenvolver.

Uma pessoa comum so pode se conectar com no maximo 2 arcanos.

**Com um Arcano conectado, você pode tentar fazer o que quiser dentro do domínio daquele elemento** — não existe lista fixa de feitiços. A única barreira real é o Nível de Conexão, que limita o quão ambicioso o efeito pode ser:

| Nível de Conexão | Dificuldade máxima que pode tentar | Escopo típico |
|---:|---:|---|
| 0 | — | nenhuma conexão, não pode usar esse Arcano |
| 1 | 10 (Normal) | efeitos pequenos e pessoais (uma fagulha, esfriar algo, uma corrente fraca) |
| 2 | 12 (Difícil) | efeitos de combate simples (dano direto, empurrar, um pequeno alcance) |
| 3 | 14 (Muito difícil) | efeitos de área (congelar uma sala, um tremor localizado, uma nuvem de escuridão) |
| 4 | 16 (Extremo) | efeitos de grande escala (uma tempestade, um terremoto, apagar a luz de uma região) |
| 5 | 18+ (Excepcional) | efeitos quase absolutos dentro do domínio do elemento — mudam a cena de forma permanente |

**Teste:** 2d6 + Vontade + Nível de Conexão (daquele Arcano) vs a Dificuldade que o Mestre define para o efeito pedido — o jogador descreve o que quer fazer, o Mestre decide o quão ambicioso isso é dentro da tabela acima, e nunca mais que o Nível de Conexão permite tentar.

**Custo de Mana:** segue a mesma escala dos Pergaminhos pela Dificuldade escolhida (8→2, 10→3, 12→5, 14→7, 16→10, 18+→14 Mana).

Resultado pela Margem: igual à tabela de Pergaminhos (Sucesso = efeito pedido; Excepcional = ampliado; Extraordinário = ampliado maior) — **exceto na Falha Crítica**, que não destrói nada material, mas custa muito mais caro (seção 5).

## 5. Infecção Arcana

Falha Crítica usando Conexão Arcana significa que **a alma e o corpo do personagem fraquejaram diante do elemento**. Isso gera (ou aumenta) a **Infecção Arcana** — uma trilha separada da Infecção comum (`INFECCAO.md`), usando exatamente a mesma estrutura de 6 Níveis, dádivas e tratamento, só que com sintomas e dádivas descritos pelo Arcano específico (seção 6).

A partir do nivel 1 de infecçao arcana o infectado passa a ter sonhos onde pode  ceder/faquejar perante ao arcano, ou negar sua natureza
ceder ao arcano aumenta 1 nivel de infecçao


| Nível | Estado |
|---:|---|
| 0 | Saudável |
| 1 | Exposto ao Arcano |
| 2 | Marcado |
| 3 | Permeado |
| 4 | Consumido |
| 5 | Dominado |
| 6 | Transcendência (ou Ruína) Arcana |

As regras de aceitar dádiva vs. tratar (`INFECCAO.md` §3–4) valem exatamente iguais aqui.

**Domínio (mente fraca é influenciada, não necessariamente para pior):** a partir do Nível 3 de Infecção Arcana, o infectado começa a ouvir a voz do arcano o influenciando, toda vez que o personagem usa aquele Arcano, ele faz um teste de Vontade (Dificuldade 8+Nível). Falha significa que o Arcano influencia uma decisão importante da cena — o jogador ainda decide a ação, mas ela precisa se alinhar com a natureza do elemento (ver "Traço de Domínio" na seção 6). Em troca, o personagem ganha **+2 no próximo teste que seguir esse comportamento**.

No nivel 6 o personagem se torna um arauto do arcano

## 6. Arcanos

| Arcano | Domínio (o que permite) | Sintoma da Infecção Arcana | Traço de Domínio (se a Vontade falha) |
|---|---|---|---|
| Fogo | calor, combustão, luz intensa | pele rachada, brilho sob a pele em momentos de estresse | impulsividade e agressividade — ataca ou confronta antes de negociar |
| Água | fluidez, pressão, maré | pele sempre úmida, voz com eco leve | evita confronto direto, mesmo quando lutar seria mais seguro |
| Terra | solidez, peso, crescimento | pele endurecendo em pequenas placas | teimosia — recusa recuar ou mudar de plano mesmo com nova informação |
| Ar/Vento | movimento, som, respiração | voz carregada por um eco de vento, passos silenciosos demais | inquietação — dificuldade em ficar parado ou manter um plano de longo prazo |
| Gelo | frio, imobilização, preservação | extremidades frias ao toque, hálito visível mesmo em ambiente quente | frieza calculista — prioriza a missão/sobrevivência sobre laços pessoais |
| Eletricidade | velocidade, impulso, choque | pequenos arcos voltaicos involuntários quando emocionado | age por impulso, decisões rápidas demais, dificuldade em esperar |
| Luz | revelação, cura, purificação | os olhos brilham fracamente no escuro | intolerância — insiste em expor segredos ou confrontar mentiras, mesmo quando seria mais sábio deixar quieto |
| Escuridão | ocultamento, silêncio, o desconhecido | a sombra do personagem se move com leve atraso | isolamento — evita pedir ajuda ou revelar informação mesmo quando seria útil |
| Natureza | crescimento, decomposição, instinto animal | pele com textura de casca ou escama em pontos pequenos | instinto acima da razão — reage como um animal encurralado a ameaças, mesmo sociais |
| Metal | dureza, condução, precisão | veias com brilho metálico visíveis sob pele fina | frieza mecânica — trata problemas como quebra-cabeças a resolver, ignora o peso emocional da situação |
| Sangue | vida, cura, corrupção | massas de carne crescendo onde nao deveriam | possessividade — prioriza proteger quem já é próximo, mesmo à custa de estranhos que precisariam de ajuda |

A lista acima é um ponto de partida — a campanha pode renomear, adicionar ou remover Arcanos livremente, mantendo a mesma estrutura (Domínio + Sintoma + Traço de Domínio).

## 7. Cajados *(módulo opcional — requer Conexão Arcana e `ALQUIMIA.md`)*

Um Cajado é um catalisador físico que amplia e direciona o poder de um conjurador com Conexão Arcana — a terceira via de interação com Magia deste sistema, ao lado de Pergaminhos e Conexão Arcana pura, mas que não funciona sozinha: ela **potencializa** a Conexão Arcana, não a substitui.

### 7.1 Componentes obrigatórios

- **Cabo:** a base física do Cajado, fabricada via Crafting comum (`CRAFTING.md`). Melhor material de Componente usado no Cabo, melhor o Cajado — controla a magnitude do bônus (ver exemplos em `EQUIPAMENTOS.md`).
- **Pedra Arcana:** o núcleo obrigatório, criado por um ritual de Alquimia que consome 1 Pedra Filosofal inteira e 8 unidades de Essência de um único Arcano (`ALQUIMIA.md` §6). Cada Pedra Arcana contém exatamente **um** Arcano — não existe Pedra Arcana híbrida.
- **Adornos (opcionais):** decorações agregadas ao Cajado (penas, presas, cristais) concedem bônus temáticos adicionais, mas **só fazem efeito se forem do mesmo Arcano da Pedra Arcana** do Cajado — um adorno de Arcano diferente permanece puramente decorativo, sem reforçar nem misturar.

### 7.2 Regras de uso

- Um Cajado só funciona se o portador tiver **Conexão Arcana com o Arcano da sua Pedra Arcana** (`MAGIA.md` §4). Sem essa Conexão, o Cajado não tem efeito mecânico algum — é só um bastão bem trabalhado.
- Com a Conexão correta, o Cajado é **obrigatório** para tentar efeitos de Nível de Conexão 4 ou 5 (Dificuldade 16+ na tabela de `MAGIA.md` §4) daquele Arcano — sem ele, esses efeitos são impossíveis de tentar, a critério do Mestre, seguindo a mesma lógica de Ferramenta ausente em `CRAFTING.md` §1.
- Em qualquer Nível de Conexão, o Cajado concede um bônus numérico ao teste de Conexão Arcana (ver tabela de exemplos em `EQUIPAMENTOS.md` — Cabo Comum: +1; Cabo Incomum: +1 e −1 no custo de Mana; Cabo Raro: +2 e −2 no custo de Mana), por ajudar no direcionamento de Mana — esse bônus segue a mesma regra de "Ferramenta especializada" já usada em `REGRAS.md` §12, não empilha com outro Cajado do mesmo Arcano.

### 7.3 Escada de investimento

| Situação | Efeito |
|---|---|
| Sem Conexão Arcana no Arcano da Pedra | nenhum efeito — o Cajado é só estética |
| Com Conexão, sem Cajado | conjura normalmente até Nível de Conexão 3 (Dificuldade até 14) |
| Com Conexão + Cajado | bônus no teste em qualquer Nível, conforme o Cabo (§7.2) |
| Nível de Conexão 4–5 (Dificuldade 16+) | o Cajado deixa de ser bônus opcional e vira requisito |

## 8. Regras Anti-Quebra

Pergaminhos, Conexão Arcana e Cajados seguem as 5 regras de `HABILIDADES.md` §2 — a Dificuldade tabelada (Pergaminhos), o teto por Nível de Conexão (Arcana) e o bônus não-empilhável de Ferramenta (Cajados) já cumprem o papel de "nunca sucesso automático" e "efeito tetado pelo Atributo/Nível" nativamente, então nenhuma regra extra é necessária.

---
*Ver `ALQUIMIA.md` para o ritual de criação da Pedra Arcana, `EQUIPAMENTOS.md` para exemplos de Cajados montados, e `CRAFTING.md` para fabricar o Cabo.*
