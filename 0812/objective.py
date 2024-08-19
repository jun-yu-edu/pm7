class Drink:

    def __init__(self, size, volume, shot):
        self.size = size
        self.volume = volume
        self.shot = shot

    def cal_volume_per_shot(self):
        return self.volume / self.shot


tall = Drink('tall', 354, 2)
grande = Drink('grande', 444, 3)
venti = Drink('venti', 555, 4)

for drink in [tall, grande, venti]:
    print(drink.cal_volume_per_shot())