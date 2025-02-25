# Monopoly Game

## Overview
This project is a digital version of the classic Monopoly board game, implemented using Pygame. Players will navigate the board, buy properties, draw chance cards, and engage in various game events.

## Project Structure
```
monopoly-game
├── assets
│   ├── fonts
│   ├── sounds
│   └── images
├── src
│   ├── board.py
│   ├── main.py
│   ├── space.py
│   ├── property.py
│   ├── chance_card.py
│   └── utils.py
├── requirements.txt
└── README.md
```

## File Descriptions

- **assets/fonts**: Contains font files used for displaying text in the game.
- **assets/sounds**: Holds sound files for game events, such as rolling dice or drawing cards.
- **assets/images**: Stores image files for the game board, properties, and other visual elements.
- **src/board.py**: Contains the `MonopolyBoard` class, which manages the game board. It has methods to add spaces and display the board.
- **src/main.py**: Serves as the entry point for the game. It initializes Pygame, sets up the game loop, and handles events.
- **src/space.py**: Defines the `Space` class, representing a space on the Monopoly board, including properties such as name, type, and cost.
- **src/property.py**: Defines the `Property` class, extending `Space` with additional attributes like rent prices and ownership status.
- **src/chance_card.py**: Defines the `ChanceCard` class, representing chance cards in the game, including properties for the card's effect and description.
- **src/utils.py**: Contains utility functions for loading assets and handling game logic.
- **requirements.txt**: Lists the dependencies required for the project, including Pygame.
- **README.md**: Documentation for the project, including setup instructions, gameplay rules, and how to contribute.

## Getting Started

### Prerequisites
- Python 3.x
- Pygame library

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd monopoly-game
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Game
To start the game, run the following command:
```
python src/main.py
```

## Gameplay Rules
- Players take turns rolling dice and moving around the board.
- Players can buy properties when they land on unowned spaces.
- Chance cards can be drawn when landing on specific spaces, affecting gameplay.
- The goal is to bankrupt all other players.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.