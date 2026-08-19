# COMBATE

## 1. Estrutura da Rodada

Cada personagem tem **3 ações por rodada**, gastas em qualquer combinação de:

- **Atacar** (corpo a corpo ou à distância)
- **Mover** (usa o valor de Movimento)
- **Defender** (+2 na Defesa até seu próximo turno)
- **Usar item**
- **Interagir** (abrir, ativar, empurrar, etc.)
- **Ajudar** (dá +1 no próximo teste de um aliado, se a ajuda for plausível)
- **Preparar ação** (declara um gatilho: "se X acontecer, eu faço Y")
- **Usar habilidade** (custo de ação definido na própria habilidade)

Não existem "ações bônus" ou "ações livres" separadas — isso mantém a contagem simples: sempre 3 ações, ponto final.

**Ataques de oportunidade: não existem no sistema base.** Justificativa: eles existem em outros RPGs para desincentivar movimento livre em combate, mas aqui esse papel já é cumprido pela Defesa (sair de perto de um inimigo sem gastar a ação de Defender deixa você vulnerável no turno dele) e por habilidades específicas que podem conceder isso pontualmente. Adicionar a regra por padrão só tornaria o combate mais lento sem gerar decisões novas.

## 2. Iniciativa

No início do combate, cada participante rola **2d6 + Agilidade + Percepção**. Ordem decrescente. Empates agem simultaneamente (ou o Mestre decide por narrativa).

## 3. Ataque e Defesa

Um ataque é um teste normal:

- **Corpo a corpo:** 2d6 + Força + Combate vs Defesa do alvo
- **À distância:** 2d6 + Percepção + Pontaria vs Defesa do alvo

Se o total igualar ou superar a Defesa, o ataque acerta. Use a Margem de Sucesso (ver `REGRAS.md`) normalmente:

| Margem do ataque | Efeito adicional |
|---|---|
| Sucesso (0 a +2) | Dano normal |
| Sucesso excepcional (+3) | Dano normal + 2 |
| Sucesso extraordinário (+4 ou mais) | Dano normal + o dado de dano é rolado em dobro, use o maior resultado |

Isso faz a Margem (já central no sistema) também importar em combate, sem criar uma sub-mecânica nova.

## 4. Distância e Cobertura

- **Curto alcance:** sem ajuste.
- **Longo alcance:** Dificuldade (Defesa do alvo) +2.
- **Cobertura parcial:** Defesa do alvo +2.
- **Cobertura total:** o alvo não pode ser alvejado diretamente.

Regras deliberadamente simples: cobertura e distância mexem na mesma Defesa que você já está comparando, sem tabela própria.

## 5. Dano e Armas

Tabela base abaixo; catálogo completo com espaços de inventário e observações em `EQUIPAMENTOS.md`.

| Arma | Dano | Categoria |
|---|---:|---|
| Soco | 1d4 | Corpo a corpo, sem custo de espaço |
| Faca | 1d6 | Corpo a corpo, leve |
| Espada | 1d8 | Corpo a corpo |
| Machado | 1d10 | Corpo a corpo, pesado |
| Pistola | 1d8 | Distância |
| Rifle | 1d10 | Distância, longo alcance |
| Arma pesada | 1d12 | Distância, 2 espaços de inventário, recarrega a cada 3 usos |

**custo de oportunidade para armas pesadas** ocupam 2 espaços e exigem recarga

Dano de armas corpo a corpo com Força 4 ou 5 soma +1 ao dado de dano (não recalcula tudo, só ajusta o resultado final).

Armadura reduz o dano recebido em um valor fixo (definido em `EQUIPAMENTOS.md`, Fase 6).

## 6. Ferimentos

A Vitalidade não é apenas um contador — cruzar certos limiares muda o estado do personagem:

| Estado | Vitalidade atual | Efeito |
|---|---|---|
| Saudável | mais da metade do máximo | Nenhum |
| Ferido | até a metade do máximo | −1 em todos os testes físicos (Força, Agilidade, Vigor) |
| Gravemente Ferido | até 1/4 do máximo | −2 em todos os testes; Movimento reduzido pela metade |
| Incapacitado | 0 ou menos | Inconsciente ou incapaz de agir |

Como a Vitalidade (10 + Vigor×2) é sempre um número par, "metade" e "um quarto" resultam em números inteiros — nenhuma divisão quebrada durante o jogo.



## 7. Fuga

Fugir de combate é um teste de Agilidade + Atletismo (ou Furtividade, se aplicável) vs a Percepção+2 de quem tentaria impedir. Sucesso remove o personagem da cena; falha o mantém no combate, gastando a ação.

E impossivel fugir caso esteja com alguma resistencia por determinaçao ativa

## 8. Morte

**Incapacitação e morte não são a mesma coisa.** Um personagem Incapacitado está fora de ação, mas só morre se sua vitalidade for igual ou menor que o negativo de seu maximo.

A cada rodada sem ser estabilizado (perícia Medicina, teste Dificuldade 8) e nescessario um teste de Vigor(Dificuldade 10), falhas no teste de vigor diminuem 1 de Vitalidade

Isso evita que um único golpe azarado encerre um personagem, mas mantém risco real.

---
*Ferimentos: condições específicas (Sangrando, Atordoado etc.) são detalhadas na Fase 3, junto com Sorte e Determinação, para poderem referenciar como esses recursos as mitigam.*
