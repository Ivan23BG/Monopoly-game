class Space:
    def __init__(self, name, space_type, cost=0):
        self.name = name
        self.space_type = space_type
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.space_type}) - Cost: {self.cost}"