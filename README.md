# Juego de Ajedrez en Python

Máximo Lucentini


# ajedrez-2024-Maximolucentini

# Estado de los Testeos:
# CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-Maximolucentini/tree/pieces.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-Maximolucentini/tree/pieces)

# Maintainability
<a href="https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Maximolucentini/maintainability"><img src="https://api.codeclimate.com/v1/badges/fe40a6b4c9f267fb321d/maintainability" /></a>

# Test Coverage
<a href="https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Maximolucentini/test_coverage"><img src="https://api.codeclimate.com/v1/badges/fe40a6b4c9f267fb321d/test_coverage" /></a>

# Descripción:

Este repositorio contiene un juego de ajedrez desarrollado en Python utilizando principios de programación orientada a objetos. Los jugadores pueden jugar una partida completa entre ellos desde la consola, respetando las reglas básicas de movimientos de las piezas del ajedrez.
Características:

Implementación en Python, estructurada utilizando el paradigma orientado a objetos.
El juego incluye movimientos básicos de las piezas de ajedrez, pero no cuenta con características avanzadas como jaque mate, enroque, coronación, ni control de tiempo.
El tablero de ajedrez se muestra en la consola con representación gráfica utilizando caracteres de texto.
La visualización de las piezas está adaptada para la consola: los colores de las piezas blancas y negras están invertidos para mejor contraste.
El juego puede finalizar de dos maneras: cuando uno de los jugadores se queda sin piezas, o cuando ambos deciden finalizarlo de forma manual seleccionando la opción de terminar.

# ¿Cómo jugar?

El juego sigue las reglas clásicas del ajedrez: el jugador con las piezas blancas comienza, y los jugadores alternan sus turnos moviendo sus piezas. Cada jugador debe mover su ficha y capturar la del oponente cuando sea posible. Además, en cualquier momento, ambos jugadores pueden acordar terminar la partida ingresando la opción de finalizar el juego.

# Requisitos:

Para poner en marcha el juego, necesitarás Docker instalado en tu sistema.

# Pasos para ejecutar desde la terminal:

# 1. Instalación de Docker:

Si aún no tienes Docker instalado, puedes hacerlo ejecutando el siguiente comando (en distribuciones basadas en Debian/Ubuntu):'sudo apt install docker'

# 2. Clonar el repositorio:

Clona este repositorio en tu máquina local: 

'git clone https://github.com/um-computacion-tm/ajedrez-2024-Maximolucentini.git'

# 3. Ejecutar el juego:

 ## . Construir la imagen de Docker:

Ejecuta el siguiente comando para crear la imagen de Docker del juego:
    'docker buildx build -t ajedrez-2024-maximolucentini'

 ## Correr los tests y el juego:

Luego de construir la imagen, puedes ejecutar el juego o los tests usando:

'docker run -i ajedrez-2024-maximolucentini'





