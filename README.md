# Documentação: Jogo Nonogram Cats

# 1. Visão Geral
Tecnologia Utilizada: Python + Pygame

Descrição: Criação inspirada no jogo Meow Tower, utilizando a biblioteca Pygame para renderização gráfica e lógica de jogo.

Objetivo: Revelar imagens ocultas e contar histórias.

# 2. Descrição Detalhada do Projeto

O que são Nonogramas?

Nonogramas são desafios de quebra-cabeça lógicos, que consistem em preencher células de uma grade, criando uma imagem oculta, usando números como pistas. A resolução de nonogramas pode ser uma forma divertida e desafiadora de desenvolver habilidades de raciocínio lógico, atenção aos detalhes e paciência. 

Curiosidade: Os nonogramas foram criados por Non Ishida, uma editora gráfica japonesa, em 1988. 

# 2.1 Funcionalidades Principais
Motor do Jogo:

Criação dos tabuleiros (com todos os detalhes posicionados).

Detecção de erros e linhas completas.

Sistema de pontuação durante as resoluções .

Interface Gráfica:

Renderização do grid.

Display de pontuação.

Telas de início/pausa/erros.

Extras:

Efeitos sonoros (durante a jogabilidade, game over e histórias).

# 2.2 Arquitetura do Código

Nonogram Cats/
├── main.py            
 
    
# 3. Etapas de Entrega (Cronograma Detalhado)

Etapa 1: 
Arte dos principais personagens e desafios.
Protótipo Básico (Semana 1-2)
Estrutura inicial do projeto (módulos principais).
Criação dos primeiros desafios Nonogramas.


Etapa 2: 
Lógica do Jogo (Semana 3-4)
Sistema de grids e marcações do tabuleiro (10 espaços a serem marcados de acordo com a imagem).
Detecção de erros ao marcar o quadrado errado.
Lógica de linhas completas e pontuação.

Etapa 3: 
Polimento (Semana 5)
Menu principal (pausa/game over).
Efeitos sonoros e high score.

Etapa 4: 
Testes e Entrega Final (Semana 6)
Testes de usabilidade (feedback de jogadores).
Correção de bugs (ex.: erros ao carregar a imagem formada).
Documentação final (README.md + comentários no código).

# 4. Requisitos técnicos
  # 4.1 Exemplo de dependências (requirements.txt)
pygame==2.5.2
numpy==1.26.0  # Opcional para cálculos de matrizes
