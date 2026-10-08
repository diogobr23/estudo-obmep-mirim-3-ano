# progress — Estudo OBMEP Mirim (3º ano)

## Estado (24/09/2026 — 1ª sessão)
- Pesquisa concluída: 4 provas de 2ª fase analisadas → `pesquisa/analise-2a-fase.md`.
- Banco de treino classificado por tema, com gabarito oficial, em `pesquisa/banco/`:
  - `1fase-2022-2023.csv` e `1fase-2024-2025.csv` — 60 questões, **todas Mirim 1**.
  - `nivelA-2018-2021.csv` — 50 questões, mas é prova de **4º e 5º anos** (edições 2018, 2019, 2021;
    o site chama de "2019 até 2021"). Usar só como desafio. 2018 Q18 exige fração (fora).
  - Erros conhecidos nas soluções oficiais: 2024-1f Q12 ("38 − 20", o certo é 38 − 28); Nível A 2018 Q13
    (texto fala em "7", resposta certa é 4). 2025-1f Q9: "mais alto que 2" = exatamente 2 — explicar se usar.
- Roteiro: cards "🔍 Como ler uma pergunta" (5 passos + palavras-armadilha que já caíram + truques) e
  "👩‍🏫 Para o adulto" (perguntas-guia, o que evitar, material) + **Dias 1–5 (semana 1)**.
- Página mostra **onde a criança parou** (1º dia com caixinha aberta), não a data. Estado no
  `localStorage` (`mirim:<id>`). Datas nos cards são só sugestão.
- Questões aparecem como **imagem recortada da prova** (`roteiro/img/`, gerada por `pesquisa/recorta.py`).

## Decisões (24/09, com o Diogo)
- 20–30 min/dia, 5 dias/semana (pode virar 4 — ele vai observar).
- Adulto por perto quando houver dúvida; na 1ª semana lê junto.
- Sem diagnóstico formal; os primeiros dias são leves.
- Divisão: a criança não entendeu a explicação da escola. Na prova, divisão = repartir em partes iguais /
  metade, números pequenos → Dia 3 com vídeo curto + tampinhas + bolinhas. Vídeo principal
  "Divisão!" (Maysa Explica, 3:29, `FG1m_-UfxdQ`), plano B "Aprenda a Divisão" (FlexFlix Kids, 2:33,
  `a1_OFOABwsA`) — conferidos por oEmbed/título/descrição, **não assistidos**: Diogo, vale olhar antes.
- 2ª fase 2022–2025 reservada para simulados (sáb 10/10, 24/10, 31/10, 07/11).

## Revisão e publicação (24/09)
- Revisão por agente separado: **PODE IR COM AJUSTES** — 12/12 respostas batem com o gabarito, 0 graves;
  7 médios (escorregões que apontavam para números fora das alternativas, troca da hora ao voltar no tempo,
  como reconhecer chinelo direito/esquerdo, "divisão sem sobra", tempo do Dia 5, "atrás" ambíguo) + 9
  pequenos. **Todos aplicados.** Prefixo do localStorage virou `mirim1:` (o roteiro do Mirim 2 deve usar
  `mirim2:` — mesma origem `diogobr23.github.io`).
- Publicado: repo público `diogobr23/estudo-obmep-mirim-3-ano` + Pages
  **https://diogobr23.github.io/estudo-obmep-mirim-3-ano/** (redireciona para `roteiro/`). Atualizar = `git push`.
- `provas/` (70 MB) fora do git; entram só as de 2ª fase, na vez dos simulados.

## Dia 0 (24/09, pedido do Diogo)
- Card novo antes do Dia 1, só com vídeos de divisão (~30 min, fim de semana 26–27/09):
  Khan `pt.khanacademy.org/.../division-intro/v/division-1` (URL vista em busca; plano B no próprio passo:
  Khan Portugal no YouTube `kr-kNxzoFYs`, 3:46) + Gis com Giz "Resolução de problemas de divisão"
  (`ociudK7Oovg`, 18:13, 305 mil views; duas ideias da divisão + interpretação de enunciado).
  Conferidos por oEmbed/descrição, **não assistidos** — Diogo, olhar antes. Duração do vídeo da Khan não confirmada.
- 24/09 (2º pedido): a criança **não sabe montar a conta de dividir** → passo novo `d0p1b` entre os dois vídeos,
  com 2 opções (escolher uma): Smile and Learn "Divisão na chave" (`-KOePuj1czE`, 5:00, 785 mil views,
  animação, divisor de 1 algarismo) ou Prof. Rafaela Mazetto "Armando a divisão – 3º ano" (`Jif4RIhw5xA`, 14:14,
  344 mil views) + armar 12 ÷ 3 e 15 ÷ 5. Reserva não usada: Gis com Giz "Divisão com um número na chave"
  (`n-z62Hux6zU`, 7:47). Card do adulto ajustado: conta armada "é bom saber, mas não é o que a prova cobra".

## ⚡ Tabuada relâmpago (24/09, pedido do Diogo)
- Card `id="tabuada"` + passo `d<N>tab` (5 min) nos Dias 1–5 (dias passaram a ~25–30 min).
- Regras: 10 continhas/rodada; começa com 2, 5 e 10; entra 3 → 4 → 6 → 7 → 8 → 9 quando todas as continhas
  do jogo já foram acertadas de primeira (flag `ok`); errou → dica (soma repetida, ou 5×g + resto) e volta no fim
  da rodada; acertou de primeira → caixa 1/2/3 = volta em 1/2/4 dias; caixa ≥ 2 → 40% vira divisão.
  Estado em `localStorage['mirim1:tab']` (`{f:{"3x7":{c,v,ok}}, nivel}`). Sem relógio.
- Simulado em node (DOM falso): níveis sobem na ordem, divisões inteiras, sem loop. Revisor separado:
  PODE IR COM AJUSTES, 0 graves; 8 ajustes aplicados (teclado cobria a dica ao errar → blur + readOnly;
  estado velho sem `nivel` travava o jogo; mensagens "Falta 1", "Acertou tudo!", "tabuadas do 2, do 5 e do 10";
  `novalidate` + filtro só-dígitos).
- A tabuada do 2º dia em diante é o termômetro: Diogo pode ver no card quais tabuadas já estão no jogo.

## Dia 0 ajustado (24/09, depois do 1º uso)
- A criança fez o Dia 0, menos o vídeo da Gis (problemas): Diogo achou complexo por exigir interpretação.
  **Vídeo da Gis saiu do Dia 0 → semana 2** (dia de grupos iguais), depois do treino de leitura.
- No lugar: `d0p4` treino de divisão na chave (Nível 1: tabuadas 2/5/10 · Nível 2: 3 e 4 · desafio opcional
  casa por casa, sem "vai um") com link para rever o Smile and Learn + truque de conferir (resultado × divisor)
  + `d0tab` 1 rodada da Tabuada relâmpago. `d0p3` virou "mostra uma conta que armou e como conferiu".

## Dia 0 real (25/09)
- A criança começou o Dia 0 em **24/09 (qui)**: viu os vídeos (e fez o dever de casa **da escola** — não é
  exercício do roteiro). Vai rever vídeos e seguir treinando de sex 25 a dom 27/09.
- Tentei separar num card "Reforço", mas ele ficava escondido até marcar as caixinhas do Dia 0 → Diogo só via
  os vídeos. **Voltou tudo para um Dia 0 só**: `d0p1` Khan · `d0p1b` montar a conta · `d0r1` rever o vídeo que
  ajudou mais · `d0p4` treino na chave (níveis 1–2 + desafio) · `d0tab` 1 rodada de tabuada por dia · `d0p3`.
- Lição: com a página em "onde parou", **nunca esconder exercício num card seguinte** — o que é pra fazer agora
  fica no dia atual.

## Dia 0 concluído (25/09) + treino do fim de semana
- Diogo: a criança **terminou o Dia 0, "foi muito bom"**, sem dificuldade na tabuada diária e aprendeu o conteúdo.
- Card novo **"Treino do fim de semana"** (sáb 26 ou dom 27/09, ~15 min), entre o Dia 0 e o Dia 1: `fs1tab` 1 rodada
  de tabuada · `fs1p1` 6 divisões na chave (+ desafio casa por casa) · `fs1p2` 3 historinhas "× ou ÷?" com
  palavra-pista (repartir / fileiras / metade). Conteúdo próprio, sem questão oficial (as de divisão ficam para o Dia 3
  e os simulados).
- Ideia para as próximas semanas: um treino curtinho assim em todo fim de semana sem simulado.

## Datas ajustadas (29/09)
- A criança **não fez o treino do fim de semana** (nem estudou seg 28/09). Datas sugeridas empurradas:
  treino curto ter 29/09 · D1 qua 30/09 · D2 qui 01/10 · D3 sex 02/10 · D4 seg 05/10 · D5 ter 06/10.
- A página segue "onde parou" — as datas são só sugestão. **Semana 2 começa qua 07/10**; simulado de 2022
  continua sáb 10/10 (decidir no fim de semana se mantém ou empurra).

## Treino de terça ampliado (29/09)
- Diogo: 15 min era pouco → ~25 min. Renomeado "Treino — divisão, vezes e tabuada" (`data-nome` "Treino de divisão e vezes").
  10 divisões na chave · 5 historinhas × ou ÷ (as 2 novas mostram que "cada" pode ser × ou ÷) · passo `fs1p3` com
  2 questões oficiais: 2024-1f Q5 (corda, 2 em 2, 9º pulo → B 18) e 2023-1f Q3 (tangerinas → D 36), gabarito conferido.
- `recorta.py`: RODAPE 815 → 836 (cortava a letra E da última questão da página).

## Treino dividido em 2 (29/09)
- Hoje a criança fez só a tabuada e as 10 divisões → Diogo pediu para fechar o dia e deixar o resto para outro dia.
- "Treino — parte 1" (ter 29/09 ✅: `fs1tab`, `fs1p1`) · "Treino — parte 2" (qua 30/09, ~20 min: `fs2tab` + `fs1p2`
  historinhas + `fs1p3` 2 questões oficiais; ids mantidos).
- Datas empurradas 1 dia: D1 qui 01/10 · D2 sex 02/10 · D3 seg 05/10 · D4 ter 06/10 · D5 qua 07/10.
  Semana 2 começa qui 08/10 → simulado de sáb 10/10 ou 17/10: **Diogo decide na qui 01/10 ou sex 02/10** — perguntar nessa data.

## Ordem: aprender a ler antes das questões (29/09)
- Diogo prefere que a criança **aprenda a ler a questão antes de fazer questões**. A parte 2 do treino (historinhas +
  2 questões oficiais) saiu de qua 30/09 e foi para **depois do Dia 2**, como "Treino — vezes ou dividir?" (sex 02/10).
  Nova ordem: treino ter 29 ✅ · D1 qua 30 · D2 qui 01 · treino sex 02 · D3 seg 05 · D4 ter 06 · D5 qua 07.
- **Regra daqui pra frente:** questão da Olimpíada só entra depois do Dia 1 (Como ler).

## Degraus + mini-simulado (03/10, ideia trazida do `estudo-cmb`)
- A criança **não estudou de 29/09 a 03/10** → continua no Dia 1. Datas empurradas: D1 seg 05/10 · D2 ter 06/10 ·
  treino "vezes ou dividir?" qua 07/10 · D3 qui 08/10 · D4 sex 09/10 · **Mini-simulado 1 sáb 10/10** · D5 ter 13/10
  (seg 12/10 é feriado, sem estudo).
- **1º simulado inteiro (2ª fase 2022) = sáb 17/10** (decisão do Diogo). Os outros seguem 24/10, 31/10, 07/11.
- **Escada de degraus nas questões** (como no CMB): 🗣️ exemplo (resolução em 1ª pessoa, "pensando em voz alta") →
  💡 com dicas (Dica 1 e Dica 2 escondidas antes da resposta) → 💪 sem ajuda. CSS `details.ex`, `details.dq`, `.grau g1/g2/g3`.
  Aplicado no D3 (bois, com dicas), D4 (chinelos = exemplo · dobra = dicas · estrela = sem ajuda; ordem 2↔3 trocada) e
  D5 (Carlos = exemplo · 3:10→4:05 = dicas). Card do adulto: deixar tentar ~2 min antes da Dica 1, **anotar quantas dicas
  abriu**; no simulado não ajudar.
- **Mini-simulado 1** (card `data-nome="Mini-simulado 1"`, ids `ms1p1`–`ms1p4`, ~40 min, sem tabuada): 5 questões de 1ª fase,
  renumeradas 1–5 → 2024 Q2 (quebra-cabeça) · 2025 Q1 (palitos) · 2022 Q4 (quem é José) · 2023 Q11 (bolinhas) · 2024 Q3
  (dominó). Gabarito oficial: **1A 2D 3D 4C 5B**. Questões agora gastas. PDF imprimível `roteiro/mini-simulado-1.pdf`
  (capa com instruções no estilo da prova real + quadro de respostas + hora de início/fim; questões com espaço de rascunho —
  na prova real o rascunho é na própria prova). Imagens renumeradas `roteiro/img/ms1-q*.png`. Gerado com PyMuPDF
  (número original coberto) + HTML → Edge headless (scripts ficaram no scratchpad da sessão).
- Na correção, o adulto anota acertos, tempo e, em cada erro, **leitura ou conta** → é o retorno para montar a semana 2.

## Dia 1 ampliado (03/10, pedido do Diogo: "tem muita pouca coisa")
- `d1p4` Caça à pergunta: 5 historinhas próprias em CAIXA ALTA (copiar só a pergunta, circular a armadilha, responder),
  armadilha sem negrito (o revisor apontou que entregava o passo). `d1p5` mais 2 questões: 2023-1f Q5 (música, com dicas → D 11)
  e 2022-1f Q7 (por extenso, sem ajuda → C quinze). Dia 1 ≈ 35 min (acima dos 20–30): se pesar, `d1p5` vai para o Dia 2.
- Plano: dia de régua/gráfico/ábaco na S3 (faltava); dominó junto de "possibilidades", mínimo/máximo junto da "tabelinha
  lógica"; se atrasar, corta revisão, não conteúdo (detalhe no `PLANO.md`).

## Dia 1 feito (sáb 03/10) ✅
- Retorno do Diogo: **foi fácil**, nenhuma questão difícil; a mais fácil foi a Questão 5 (2022-1f Q7, número por extenso).
- ⚠️ **A criança lê o roteiro ao pé da letra** → escrever com cuidado e deixar claro o que é **explicação/instrução do roteiro** e
  o que é **questão da prova**. Diogo acha que ela pega com o tempo.
- Datas sugeridas seguem as mesmas (D2 seg 05/10…); a página segue "onde parou", então ela já está no Dia 2.

## Dia 2 (dom 04/10) ✅ feito
- Q1 placas: **identificou as 6 certas, mas contou errado** → organização (riscar o que já contou), não leitura.
- Q2 cartões: **teve dificuldade em achar a pergunta** (confundiu com "tirar os cartões na mesma ordem"); Diogo orientou a
  **isolar a pergunta** → ponto a reforçar.
- A criança pediu mais → `d2p4` 2022-1f Q9 (Mariana/bandeiras, isolar a pergunta, com dicas → E 70) + `d2tab2` 2ª rodada de
  tabuada. Publicado antes da revisão (criança esperando); revisor depois: ok, 2 ajustes pequenos aplicados.
- Parte extra: **acertou tudo**. Na "questão 2" pediu ao adulto para confirmar o raciocínio antes de marcar (estava certo); viu a
  resolução e entendeu. Diogo: "tá indo muito bem até agora". → Hábito de pedir confirmação: o mini-simulado (sem ajuda) treina isso.
- Próximo na página: Treino "vezes ou dividir?" (sugestão qua 07/10, mas a criança está adiantada: D1 sáb 03 e D2 dom 04).
- Também: etiquetas 📄 QUESTÃO DA PROVA / ✏️ TREINO, títulos com o número real da questão, lembretes sem quebra de linha.

## ⚡ Decisão: adiantar (dom 04/10, Diogo)
- Treino "vezes ou dividir?" **feito hoje (04/10)** junto com o Dia 2. A criança acha tudo fácil → **adiantar**.
- Nova ordem: D3 seg 05/10 (agora com 3 questões) · D4 ter 06/10 · **Mini-simulado 1 qua 07/10** · D5 qui 08/10 ·
  **semana 2 começa sex 09/10**. Tabuada = 2 rodadas por dia (era rápida demais).
- **Estratégia do Diogo:** fechar todo o conteúdo antes da prova e usar o tempo que sobrar para **aprofundar em questões mais
  complexas**, para a prova parecer fácil no dia. Fontes para isso: Nível A (4º–5º ano, `nivelA-2018-2021.csv`) e as questões
  difíceis (D) da 1ª fase; 2ª fase 2022–2025 continua reservada para os simulados.

## Dia 3 feito (seg 05/10) ✅
- **Muito fácil:** tampinhas, treino com bolinhas e a 2025 Q3 (bois).
- **Chocolate (2025 Q8):** precisou da explicação do adulto ("um terço de 9") → entendeu que é dividir 9 por 3.
- **Laranjas (2024 Q11, desafio):** teve dúvida, **usou as dicas** e ainda confirmou passos com o adulto, mas resolveu.
  → Esse é o nível "desafio" certo para agora.
- Padrão que se repete (D2 e D3): **pede confirmação ao adulto** antes de concluir → o mini-simulado (sem ajuda) mede isso.
- Material concreto (tampinhas) já não é necessário para divisão simples: daqui pra frente, pular direto para as questões.

## Dia 5 "Subindo o nível" feito (qua 07/10) ✅ — sozinha, só com o roteiro
- Chás (exemplo): **errou** ao tentar antes de ler o exemplo; **não entendeu "fazer uma lista"** — termo solto, criança literal.
- 2022 Q14 (dobro): acertou com as **2 dicas**. 2025 Q10 (times, sem ajuda): **acertou**.
- 2024 Q12 (trens): **não resolveu nem com as dicas** e não entendeu bem a explicação. Tabuada 2 rodadas: tudo certo.
- ⚠️ Defeito achado pelo print: dentro dos "exemplos" (`details.ex`) os números 1-2-3 ficavam soltos numa linha (o CSS só
  valia para `.res`) — afetava os exemplos desde o Dia 4. Corrigido com `:is(.res,.ex)`.
- Resposta (08/10): exemplo dos chás reescrito (o que é lista + lista numerada desenhada); trens reexplicados com desenho em
  emojis (🚂🚃🚃); Dia 6 ganha `d6r1` "Revendo os trens" (2 variações inventadas: caixa 5 kg, sanduíche R$ 5 — resolvidas às
  cegas por 2º agente) e `d6p5` desafio 2025-1f Q6 (comprimidos, B). **Regra de escrita:** todo termo-estratégia ("lista",
  "riscar o que é igual") vem explicado com o que fazer no caderno, não só nomeado.

## Subir o nível sem frustrar (06/10, Diogo)
- Diogo: não ir direto do fácil para um simulado difícil → **Dia 5 novo "Subindo o nível"** (qua 07/10, ids `n5*`): aviso
  acolhedor + exemplo 2023 Q15 (chás, lista organizada) + 2022 Q14 (dobro, dicas, D) + 2024 Q12 (trens, dicas, B) + 2025 Q10
  (times, sem ajuda, C). Horas virou **Dia 6** (qui 08/10, ids `d5*` mantidos). **Mini-simulado vira meio-simulado** (10 questões,
  1h; sex 09/10) — a montar. Simulado inteiro 2022 continua **17/10**. Revisor: PODE IR; 2 escorregões com letra acrescentados.

## Dia 4 feito (ter 06/10) ✅ — em ~15 min (previsto 40)
- Acertou tudo, inclusive as 2 rodadas de tabuada; **só se confundiu nos chinelos** (lateralidade; Diogo acha que na tela do
  computador é pior que no papel). Desafio impresso do Canguru **não foi usado** (não deu para imprimir) → trocado na hora por
  2022-1f Q8 (marcas de dobra, D) na tela.
- Diogo: **"temos que ir elevando o nível"**.

## Dia 4 ajustado (05/10, Diogo aprovou)
- Chinelos (2022 Q6) deixou de ser exemplo → "sem ajuda". Passo novo `d4p5`: **desafio impresso Canguru 2023 Q13** (folha dobrada
  com 2 furos, gabarito B) — folha local `provas/canguru/folha-desafio-dia4.pdf` (gitignored); a página só tem a explicação.
  Revisor: ok, 4 ajustes de redação aplicados. Dia 4 ≈ 40 min.

## Regra nova de fontes de questão (04/10, aprovada pelo Diogo) → ver CLAUDE.md
- Oficiais OBMEP primeiro (sobram 36 da 1ª fase: 17 M, 18 D, 1 F; + 50 do Nível A) → **Canguru Nível P** (3º–4º ano, 2021–2025,
  gabarito oficial, sem resolução; direitos reservados → só impresso/local, fora do git) → **inventadas** só para variação/ponte,
  com 2º agente resolvendo às cegas. Escada por tema: ideia → oficial M → oficial D → Canguru/Nível A → inventada mais complexa.
- ✅ Canguru Nível P 2021–2025 baixado (prova + gabarito) em `provas/canguru/` (gitignored) e classificado por 5 agentes em
  paralelo → `provas/canguru/banco-canguru-nivelP.csv` (mesmas colunas do banco + `pontos` e `cabe_3ano`). 120 questões,
  119 "cabem no 3º ano" (julgamento otimista: reconferir cada uma ao usar). Temas: ESP 39 · LOG 30 · OPE 20 · CNT 14 · MED 6 ·
  POS 5 · SEQ 3 · NUM 1 · TEM 1. Dificuldade F 26 · M 56 · D 37. Muitas respostas de figura só pelo gabarito oficial (não
  refeitas); **2021 Q12 marcada CONFERIR**. Uso: só impresso/local; a página pública cita "Canguru AAAA, questão N".

## Próximo passo
1. Diogo conta como foram os Dias 1–4 (quantas dicas abriu, onde travou) e o resultado do mini-simulado (__/5, tempo, leitura × conta).
2. Montar a semana 2 (13/10 em diante, rascunho em `PLANO.md`) com isso, antes do simulado inteiro de 17/10.
