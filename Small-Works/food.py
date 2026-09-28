class Food:
    base_hearts = 2

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)

    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts
        for ingredient in ingredients:
            if "hearty" in ingredients:
                hearts += 2
            else:
                hearts += 1
        return hearts
    
    @classmethod
    def from_nothing(cls, hearts):
        food = cls(ingredients=[])
        food.hearts = hearts
        return food
    
def main():

    mushroom_skewer = Food(ingredients=["mushroom", "hearty mushroom"])
    print(f"This meal has renewed {mushroom_skewer.hearts}")

    mushroom_skewer = Food.from_nothing(hearts=2)
    print(f"This meal has renewed {mushroom_skewer.hearts}")

main()