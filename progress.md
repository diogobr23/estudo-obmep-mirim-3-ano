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

## Próximo passo
1. Diogo observa a semana 1 e conta: onde travou, se 5 dias pesou, como foi a leitura.
2. Montar a semana 2 com isso (rascunho em `PLANO.md`).
