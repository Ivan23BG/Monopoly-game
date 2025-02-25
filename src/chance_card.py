class ChanceCard:
    def __init__(self, description, effect):
        self.description = description
        self.effect = effect

    def apply_effect(self, player):
        # Logic to apply the effect to the player
        pass

    def __str__(self):
        return f"Chance Card: {self.description}"