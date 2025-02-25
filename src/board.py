from property import Property
from space import Space

class MonopolyBoard:
    def __init__(self):
        self.board = []


    def add_space(self, space):
        self.board.append(space)


    def add_spaces(self, spaces):
        for space in spaces:
            self.add_space(space)


    def add_all_spaces(self):
        properties = [
            Space("Go", "Go"),
            Property("Old Kent Road", 60, 2, 50),
            Space("Community Chest", "Community Chest card"),
            Property("Whitechapel Road", 60, 4, 50),
            Space("Income Tax", "Tax"),
            Property("Kings Cross Station", 200, 25, None),
            Property("The Angel Islington", 100, 6, 50),
            Space("Chance", "Chance card"),
            Property("Euston Road", 100, 6, 50),
            Property("Pentonville Road", 120, 8, 50),
            Space("Jail", "Jail"),
            Property("Pall Mall", 140, 10, 100),
            Property("Electric Company", 150, None, None),
            Property("Whitehall", 140, 10, 100),
            Property("Northumberland Avenue", 160, 12, 100),
            Property("Marylebone Station", 200, 25, None),
            Property("Bow Street", 180, 14, 100),
            Space("Community Chest", "Community Chest card"),
            Property("Marlborough Street", 180, 14, 100),
            Property("Vine Street", 200, 16, 100),
            Space("Free Parking", "Free Parking"),
            Property("Strand", 220, 18, 150),
            Space("Chance", "Chance card"),
            Property("Fleet Street", 220, 18, 150),
            Property("Trafalgar Square", 240, 20, 150),
            Property("Fenchurch Street Station", 200, 25, None),
            Property("Leicester Square", 260, 22, 150),
            Property("Coventry Street", 260, 22, 150),
            Property("Water Works", 150, None, None),
            Property("Piccadilly", 280, 24, 150),
            Space("Go To Jail", "Go To Jail"),
            Property("Regent Street", 300, 26, 200),
            Property("Oxford Street", 300, 26, 200),
            Space("Community Chest", "Community Chest card"),
            Property("Bond Street", 320, 28, 200),
            Property("Liverpool Street Station", 200, 25, None),
            Space("Chance", "Chance card"),
            Property("Park Lane", 350, 35, 200),
            Space("Super Tax", "Tax"),
            Property("Mayfair", 400, 50, 200)
        ]
        
        self.add_spaces(properties)


    def __str__(self):
        return str(self.board)