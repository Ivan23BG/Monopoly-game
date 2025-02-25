from space import Space

class Property(Space):
    def __init__(self, name, cost, rent, house_cost):
        super().__init__(name, "Property")
        self.cost = cost
        self.rent = rent
        self.house_cost = house_cost
        self.owner = None
        self.houses = 0

    def buy_property(self, player):
        if self.owner is None:
            self.owner = player
            player.money -= self.cost

    def calculate_rent(self):
        return self.rent + (self.houses * self.house_cost)

    def build_house(self):
        if self.owner is not None:
            self.houses += 1
            self.owner.money -= self.house_cost

    def __str__(self):
        return f"{self.name}: Cost: {self.cost}, Rent: {self.rent}, Houses: {self.houses}"