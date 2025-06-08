# Documentação: Jogo Nonogram Cats

## 1. Visão Geral
Tecnologia Utilizada: Python + Pygame
Descrição: Implementação do jogo Meow Tower utilizando a biblioteca Pygame para renderização gráfica e lógica de jogo.
Objetivo: Criar um jogo de desafios nonogramas que possa contar histórias de gatos presentes no jogo.

2. Descrição Detalhada do Projeto
O que é Tetris?
Tetris é um jogo de quebra-cabeça eletrônico criado em 1984 pelo programador russo Alexey Pajitnov. O objetivo é organizar peças geométricas (chamadas tetrominós) que caem aleatoriamente em um grid retangular, formando linhas completas para ganhar pontos.

Curiosidade: 

2.1 Funcionalidades Principais
Motor do Jogo:

Geração aleatória de peças (Tetrominós).
Movimentação (esquerda, direita, rotação, queda rápida).
Detecção de colisões e linhas completas.
Sistema de pontuação e aumento de dificuldade por nível.
Interface Gráfica:

Renderização do grid (10x20) e peças.
Display de pontuação, próximo bloco e nível.
Telas de início/pausa/game over.
Extras:

Efeitos sonoros (linha completada, game over).
Persistência de high score (arquivo JSON ou SQLite).
2.2 Arquitetura do Código
tetris/
├── main.py            # Ponto de entrada (inicialização do jogo)
├── game.py            # Lógica principal (estado do jogo, loop principal)
├── pieces.py          # Definição dos tetrominós e rotações
├── grid.py            # Gerenciamento do grid e checagem de linhas
├── ui/                # Interface do usuário
│   ├── render.py      # Renderização gráfica (Pygame)
│   └── sounds.py      # Gerenciamento de áudio
└── utils/             # Utilitários
    ├── config.py      # Constantes (cores, tamanhos)
    └── scores.py      # Manipulação de high scores
3. Etapas de Entrega (Cronograma Detalhado)
Etapa 1: Protótipo Básico (Semana 1-2)
Configuração do ambiente (Python 3.10+, Pygame 2.5+).
Estrutura inicial do projeto (módulos principais).
Implementação do grid e renderização básica.
Movimentação manual de um bloco (sem colisões).
Etapa 2: Lógica do Jogo (Semana 3-4)
Sistema completo de peças (7 tetrominós com rotações).
Detecção de colisões e limites do grid.
Lógica de linhas completas e pontuação.
Controles do jogador (teclado/configurável).
Etapa 3: Polimento (Semana 5)
Menu inicial e telas auxiliares (pausa/game over).
Sistema de níveis (velocidade aumenta progressivamente).
Efeitos sonoros e high score.
Etapa 4: Testes e Entrega Final (Semana 6)
Testes de usabilidade (feedback de jogadores).
Correção de bugs (ex.: ghosting de peças).
Documentação final (README.md + comentários no código).
4. Requisitos técnicos
4.1 Exemplo de dependências (requirements.txt)
pygame==2.5.2
numpy==1.26.0  # Opcional para cálculos de matrizes
