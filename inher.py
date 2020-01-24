class Character():
    type = 'friendly'

    def __init__(self, h, it):
        self.health = h
        self.item = it 

    def info(self):
        s = 'I am ' + self.type + ', I am '
        if self.health < 3:
            s += 'un'
        s += 'healthy, and I have a ' + self.item + '.'
        return s


class Dwarf(Character):
    type = 'grumpy'

    def __init__(self, h, it, dislike):
        super().__init__(h, it)
        self.dislike = dislike

    def info(self):
        return super().info() + ' I dislike ' + self.dislike + '.'


class Monk(Character):

    def info(self):
        return 'I am a monk.' 

c1 = Character(10, 'sword')
d1 = Dwarf(3, 'axe', 'elves')
m1 = Monk(0, '')

c2 = Character(2, 'lyre')
d2 = Dwarf(11, 'beard', 'you')
m2 = Monk(12, 'yoga mat')

print(c1.info())
print(d1.info())
print(m1.info())

print(c2.info())
print(d2.info())
print(m2.info())

Dwarf.type = 'angry'
d1.health -= 1
print(d1.info())