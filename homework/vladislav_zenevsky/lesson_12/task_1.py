class Flower:

    def __init__(self, name, freshness, color, stem_length, price):
        self.__name = name
        self.freshness = freshness
        self.__color = color
        self.__stem_length = stem_length
        self.price = price

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def stem_length(self):
        return self.__stem_length

    def __repr__(self):
        return f'Flower: {self.color} {self.name}' + (
            ', fresh, ' if self.freshness else ', not fresh, ') + f'{self.stem_length} сm, {self.price} rubles'


class Rose(Flower):
    lifespan = 5

    def __init__(self, freshness, color, stem_length, price):
        super().__init__('rose', freshness, color, stem_length, price)


class Peony(Flower):
    lifespan = 7

    def __init__(self, freshness, color, stem_length, price):
        super().__init__('peony', freshness, color, stem_length, price)


class Carnation(Flower):
    lifespan = 14

    def __init__(self, freshness, color, stem_length, price):
        super().__init__('carnation', freshness, color, stem_length, price)


class Hydrangea(Flower):
    lifespan = 5

    def __init__(self, freshness, color, stem_length, price):
        super().__init__('hydrangea', freshness, color, stem_length, price)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_bouquet_price(self):
        return f'Bouquet price is {sum(flower.price for flower in self.flowers)} rubles'

    def get_bouquet_lifespan(self):
        return f'Bouquet lifespan is {int(sum(flower.lifespan for flower in self.flowers) / len(self.flowers))} days'

    def sort_flower_by_color(self):
        return f'Flowers sorted by color: {sorted(self.flowers, key=lambda flower: flower.color)}'

    def sort_flower_by_freshness(self):
        return f'Flowers sorted by freshness: {sorted(self.flowers, key=lambda flower: flower.freshness)}'

    def sort_flower_by_price(self):
        return f'Flowers sorted by price: {sorted(self.flowers, key=lambda flower: flower.price)}'

    def sort_flower_by_stem_length(self):
        return f'Flowers sorted by stem length: {sorted(self.flowers, key=lambda flower: flower.stem_length)}'

    def filter_flower_by_color(self, color):
        return (list(filter(lambda flower: flower.color == color, self.flowers))
                or f'There is no {color} flower in the bouquet :(')

    def __repr__(self):
        return f"Bouquet: {self.flowers}"


red_rose = Rose(False, 'red', 70, 300)
pink_peony = Peony(True, 'pink', 50, 350)
yellow_carnation = Carnation(True, 'yellow', 60, 150)
blue_hydrangea = Hydrangea(True, 'blue', 60, 400)

flowers = [red_rose, pink_peony, yellow_carnation, blue_hydrangea]

awesome_bouquet = Bouquet()

for i in flowers:
    awesome_bouquet.add_flower(i)

print(awesome_bouquet)
print(awesome_bouquet.get_bouquet_price())
print(awesome_bouquet.get_bouquet_lifespan())
print(awesome_bouquet.filter_flower_by_color('red'))
print(awesome_bouquet.filter_flower_by_color('green'))
print(awesome_bouquet.sort_flower_by_color())
print(awesome_bouquet.sort_flower_by_freshness())
print(awesome_bouquet.sort_flower_by_price())
print(awesome_bouquet.sort_flower_by_stem_length())
