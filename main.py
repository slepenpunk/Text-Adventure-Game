import random, games, time
 

class Player:
    """Player of game"""

    LEGAL_MOVES = ['right', 'left', 'up', 'down']
    inventory = []
    hp = 100
    damage = 0
    coord = 0

    def __init__(self, name):
        self.name = name
        self.coord = Player.coord
        self.damage = Player.damage
        self.hp = Player.hp

    @classmethod
    def do_attack_zombie(cls):
        if cls.inventory:
            Zombie.hp -= cls.damage
            print('You was attack the zombie.')
        else:
            print('You don\'t have a weapon!')

    @classmethod
    def do_attack_boss(cls):
        if cls.inventory:
            Boss.hp -= cls.damage
            print(f'You was attack the CREATOR OF THE WORLDS!\n'
                  f'CREATOR OF THE WORLDS has {Boss.hp} HP.')
        else:
            print('You don\'t have a weapon!')

    def move(self, pos):
        if pos in Player.LEGAL_MOVES:
            if self.coord == 0 and pos == 'right':
                self.coord = 1
            elif self.coord == 1 and pos == 'left':
                self.coord = 0
            elif self.coord == 1 and pos == 'up':
                self.coord = 2
            elif self.coord == 2 and pos == 'down':
                self.coord = 1
            elif self.coord == 1 and pos == 'down':
                self.coord = 3
            elif self.coord == 3 and pos == 'up':
                self.coord = 1
            elif self.coord == 1 and pos == 'right':
                self.coord = 4
            elif self.coord == 4 and pos == 'left':
                self.coord = 1
            elif self.coord == 4 and pos == 'up':
                self.coord = 5
            elif self.coord == 5 and pos == 'down':
                self.coord = 4
            elif self.coord == 4 and pos == 'down':
                self.coord = 6
            elif self.coord == 6 and pos == 'up':
                self.coord = 4
            elif self.coord == 4 and pos == 'right':
                self.coord = 7
            else:
                print('You don\'t go here!')
        else:
            print('Incorrect choice!')


class Enemy:
    '''Any enemies who will kill our player'''

    hp = 0
    damage = 0

    def __init__(self):
        self.hp = Enemy.hp
        self.damage = Enemy.damage


class Zombie(Enemy):
    '''Just a zombie'''

    hp = 30
    damage = 10

    def __init__(self):
        super(Zombie, self).__init__()
        self.hp = Zombie.hp
        self.damage = Zombie.damage

    @classmethod
    def do_attack(cls):
        attack = random.randint(0, 1)
        if attack == 0:
            cls.damage = 0
            Player.hp -= cls.damage
            print('Zombie missed!')
        else:
            cls.damage = 10
            Player.hp -= cls.damage
            print(f'Zombie was attack you!\n'
                  f'Your hp - {Player.hp}')


class Boss(Enemy):
    '''Final boss'''

    hp = 100
    damage = 50

    @classmethod
    def do_attack(cls):
        Player.hp -= cls.damage
        if Player.hp < 0:
            Player.hp = 0
        print(f'CREATOR OF THE WORLDS WAS ATTACK YOU!\n'
              f'Your HP - {Player.hp}')


class Area:
    '''Some space'''

    is_here = True

    def __init__(self, coord=0):
        self.coord = coord

    def description(self):
        if self.coord == 0:
            start = Start()
            print(start)
        elif self.coord == 1:
            hall1 = Hall1()
            print(hall1)
        elif self.coord == 2:
            room1 = Room1()
            print(room1)
            room1.get_weapon()
        elif self.coord == 3:
            room2 = Room2()
            print(room2)
            room2.go_to_hidden_room()
        elif self.coord == 4:
            hall2 = Hall2()
            print(hall2)
        elif self.coord == 5:
            room3 = Room3()
            print(room3)
            room3.fighting_scene()
        elif self.coord == 6:
            if 'Key' in Player.inventory:
                room4 = Room4()
                print(room4)
                room4.get_immortality()
            else:
                print('Door is close!')
        elif self.coord == 7:
            mamont = Mamont()
            finish = EndScene()
            mamont.go_to_hidden_mamont()
            print(finish)
            finish.fight_with_boss()


class Start(Area):
    '''Start the Game'''

    def __str__(self):
        res = '>>> STARTING AREA'
        return res


class Hall1(Area):
    '''First hall'''

    def __str__(self):
        res = '>>> FIRST HALL'
        return res


class Hall2(Area):
    '''Second hall'''

    def __str__(self):
        res = '>>> SECOND HALL'
        return res


class Room1(Area):
    '''Room1'''

    loot = {
        'Wood Stick': 10,
        'Battle Axe': 35,
        'Hunting Knife': 25,
        'Enchanted Hammer Of Death': 50
    }

    def __str__(self):
        res = '>>> FIRST ROOM'
        return res

    @classmethod
    def get_weapon(cls):
        if cls.is_here:
            response = games.ask_yes_no('You find a chest. Do you wanna open it?(y/n): ')
            if response == 'y':
                weapons = cls.loot.items()
                weapons = list(weapons)
                random_weapon = random.choice(weapons)
                Player.inventory.append(random_weapon)
                Player.damage = random_weapon[1]
                print(f'You picked:\n'
                      f'Weapon - {random_weapon[0]}\n'
                      f'Damage - {random_weapon[1]}')
                print('-' * 20)
                print('Now in your inventory:')
                for i in Player.inventory:
                    print(i[0], '\n', end='')
                print('-' * 20)
                cls.is_here = False
            else:
                print('You didn\'t open it.')
        else:
            print('You were here.')


class Room2(Area):
    '''Room2, the room has a trap'''

    def __str__(self):
        res = '>>> SECOND ROOM'
        return res

    @classmethod
    def go_to_hidden_room(cls):

        response = games.ask_yes_no('You saw a hidden door and you don\'t know where it leads.\n'
                                    'Will you come in?(y/n): ')
        print('-' * 70)
        if response == 'y':
            print('It was a trap!\n'
                  'You fell on poisonous thorns and died in cruel agony.')
            exit()
        else:
            print('You didn\'t open the door.')


class Room3(Area):
    '''Room 3, fight with a zombie and get a key'''

    is_here = True

    def __str__(self):
        res = '>>> THIRD ROOM'
        return res

    def fighting_scene(self):
        if Room3.is_here:
            response = games.ask_yes_no('In the twilight you see a scary zombie.\n'
                                        'Do you fight with him?(y/n): ')
            if response == 'y':
                if Room3.is_here == True:
                    while Zombie.hp >= 0 or Player.hp >= 0:
                        if Zombie.hp <= 0:
                            print('-' * 50)
                            print('You killed zombie.\n'
                                  'You saw the key around his neck and took it.')
                            Player.inventory.append('Key')
                            Room3.is_here = False
                            break
                        if Player.hp <= 0:
                            print('-' * 50)
                            print('The Zombie was stronger than you and killed you.\n'
                                  'Game Over!')
                            exit()
                        else:
                            print('Fight in process...\n')
                            time.sleep(2.5)
                            Zombie.do_attack()
                            Player.do_attack_zombie()
                else:
                    print('You don\'t fight.')
        else:
            print('You were here.')


class Room4(Area):
    '''Room 4, gains extra life'''

    is_here = True

    def __str__(self):
        res = '>>> FOURTH ROOM'
        return res

    @classmethod
    def get_immortality(cls):
        if cls.is_here:
            print('You find a Rare Ancient Treasure that grants immortality!')
            Player.inventory.append('Rare Ancient Treasure')
            cls.is_here = False
        else:
            print('You were here.')


class Mamont(Area):
    '''Room where scamyat'''

    def go_to_hidden_mamont(self):
        response = games.ask_yes_no('You saw a hidden door on way to the exit.\n'
                                    'Will you come in?(y/n): ')
        print('-' * 70)
        if response == 'y':
            print('Ha-Ha zaskamili mamonta w(°ｏ°)w')
            print('-' * 35)
            time.sleep(2.5)
        else:
            print('You didn\'t open the door. And we going to the next door...')
            time.sleep(2.5)


class EndScene(Area):
    '''End scene of game'''

    def __str__(self):
        res = 'That room is the end your path, if you survive... '
        return res

    def fight_with_boss(self):
        while Player.hp > 0 or Boss.hp > 0:
            Player.do_attack_boss()
            print('-' * 40)
            time.sleep(3.5)
            if Boss.hp <= 0:
                print('You killed the CREATOR OF THE WORLDS!\n'
                      'You managed to go all the way, now you are free!')
                exit()

            Boss.do_attack()
            print('-' * 40)
            time.sleep(3.5)
            if Player.hp <= 0 and 'Rare Ancient Treasure' in Player.inventory:
                print(f'Rare Ancient Treasure brought you back to life!\n'
                      f'You gain extra life!')
                print('-' * 40)
                Player.inventory.remove('Rare Ancient Treasure')
                Player.hp = 100
            if Player.hp <= 0 and 'Rare Ancient Treasure' not in Player.inventory:
                print('You didn\'t have the strength to defeat the Creator and you are dead!')
                exit()


class Game:
    '''Main processes of game'''

    @staticmethod
    def show_map():
        LINE = '-'
        START = 'START'
        HALL1 = 'HALL1'
        HALL2 = 'HALL2'
        ROOM1 = 'ROOM1'
        ROOM2 = 'ROOM2'
        ROOM3 = 'ROOM3'
        ROOM4 = 'ROOM4'
        END = 'END'

        print('\n', '      ', ROOM1, ' ', ROOM3)
        print('         ', '|', '     ', '|')
        print(START, LINE, HALL1, LINE, HALL2, LINE, END)
        print('         ', '|', '     ', '|')
        print('       ', ROOM2, ' ', ROOM4, '\n')

    def play(self):
        print('\t\t\t\t\t\tHAIL!\n'
              '\t\t\tThe meaning of this game is simple.\n'
              '\t\t\tFind a way to exit and stay alive.\n'
              '\t\t\tUsing  your keyboard, you may move right, left, up or down.\n'
              '\t\t\tJust see on the map and going in your adventure!')
        print('-' * 73)
        name = input('Enter name: ')
        player = Player(name)
        play = None
        while play != '':
            play = input('\t\t\tPress Enter to play...')
        print('\t\t\tNow you at the beginning of your path.')
        while player.coord != 7:
            Game.show_map()
            position = input('Where are you go?(left, right, down, up)\n-> ')
            player.move(position)
            area = Area(player.coord)
            print('-' * 20)
            area.description()


def main():
    game = Game()
    game.play()


main()
