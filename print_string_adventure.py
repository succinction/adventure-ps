# TRANSFORM INTO CLASSES

# CLASSES:
# PRINT_SCREEN_MAP
# Instruction screens before first frame.
# magic spells released at certain levels
# Multiple monsters
# magic cost gold.


# ORDER OF CLASSES
#
# Screen
# Monster
# Player
# #SpellBook
# #Engine



## ADVENTURE.PY ### WITH CLASSES #################################
##################################################################
# import random
from random import choice
from random import randrange


##################################################################


print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################## WELCOME TO #################### ")
print("################################################## ")
print("##########    PRINT SCREEN ADVENTURE    ########## ")
print("################################################## ")
print("### MOVE WITH ARROW KEYS OR NUMBER PAD + ENTER ### ")
print("################################################## ")
print("##### ATTACK WITH ENTER WHEN NEXT TO MONSTER ##### ")
print("################################################## ")
print("########## HEAL WITH \"h [number]\" + ENTER ######## ")
print("################################################## ")
print(" LEARN TO CAST SPELLS WITH \"cast [spell]\" + ENTER  ")
print("################################################## ")
print("#### SPELLS WILL BE REVEALED AS YOU LEVEL UP ##### ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################################################## ")





# PRINT SCREEN MAP MAPIT
class Screen:
    def __init__(self):
        self.MAP_SIZE = 24
        self.map_row = " . . . . . . . . . . . . . . . . . . . . . . . ."
        self.map_rows = self.initialize_map()  # []
        self.frame_i = [0]
        self.head = [0]
        self.message_key =['','','']


    def initialize_map(self):
        maprws = []
        for r in range(self.MAP_SIZE):
            maprws.append(self.map_row)
        return maprws


    def message(self, x, additional=''):
        return {
                   'cast': 'Magic spell cast, doing some damage.',
                   'h': 'You have been healed',
                   'g90': 'Gained 90 Gold.',
                   'g50': 'Gained 50 Gold.',
                   'g19': 'Gained 19 Gold.',
                   'g9': 'Gained 9 Gold.',
                   'g11': 'Gained 11 Gold.',
                   'g20': 'Gained 20 Gold.',
                   'g7': 'Gained 7 Gold.',
                   'g5': 'Gained 5 Gold.',
                   'g1': 'Gained 1 Gold.',
                   'm1': 'Fight monster: {} with {}({}) HP:{} '
                       .format(monsters[0].type, monsters[0].inventory[0]['name'],
                               monsters[0].inventory[0]['damage'], monsters[0].health),
                   '.': 'Nothing to say.',
                   '': '',
                   'killedit': 'You have slain the monster!',
                   'looted': 'You have looted the corpse',
                   'dmg': '- DAMAGE = '
               }[x] + additional

    # PSMAPIT > SCREEN
    # STATS
    def hud(self):
        print("LEFT : {} {}  HEALTH: {}  {}".format(player.inventory[0]['name'], player.inventory[0]['damage'],
                                                    player.health,
                                                    self.message(self.message_key[2][:3],
                                                            self.message_key[2][self.message_key[2].find(' '):])))
        print("RIGHT: {}    GOLD  : {} ".format(player.inventory[1]['name'], player.gold))
        # print(":POTION ^(f)                  (r)^ STAFF:")
        print(self.message(self.message_key[1]), self.message(self.message_key[0]))

    # HELPER FUNCTION FOR mapit()
    def get_index_from_bit(self, c):
        for i in range(self.MAP_SIZE):
            if c == 1 << i:
                return self.MAP_SIZE - i

    def header(self):
        # print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        self.frame_i[0] += 1
        print('Frame # {}  Level # {}   Lives : {}'.format(self.frame_i[0], level[0], LIVES[0]))

        if self.head[0] == 0:
            print("######################################## Move Key: 123 | 123")
            print("################ A D V E N T U R E ##### n s e w # q*e | 4*6")
            print("################################################## asd | 789")
        elif self.head[0] == 1:
            print("################################################## ")
            print("################# A SPELL IS CAST ################ ")
            print("################################################## ")
        elif self.head[0] == 2:
            print("################################################## ")
            print("################ MONSTER ATTACKED ################ ")
            print("################################################## ")
        elif self.head[0] == 3:

            print("Killed by level {} {}.    Don't forget to heal!".format(level[0], monsters[0].type))
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################ !!!!YOU DIED!!!! ################ ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            self.hud()

        elif self.head[0] == 4:
            print("################################################## ")
            print("############### !!!! YOU WON !!!! ################ ")
            print("################################################## ")
        elif self.head[0] == 5:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
            print("######## !! YOU HAVE BEEN REINCARNATED !! ######## ")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")

    def mapit(self, a='', b=''):
        col = player.current_position[1]
        row = player.current_position[0]
        self.header()
        ind = self.MAP_SIZE - row
        ### MONSTER
        m = 0
        mon_row = monsters[m].position[0]
        # print('monsters position 0 : ' , monsters[m].position[0])
        # print('monsters position 1 : ' , monsters[m].position[1])
        mon_col = monsters[m].position[1]
        # mon_ind = MAP_SIZE - mon_row
        mon_colm = mon_col
        newrow = self.map_rows[mon_row][: (mon_colm - 1) * 2]
        newrow += monsters[m].avatar
        newrow += self.map_rows[mon_row][(mon_colm) * 2:]
        self.map_rows[mon_row] = newrow
        for r in range(row):
            print(self.map_rows[r], r)
        colm = self.get_index_from_bit(col)
        newrow = self.map_rows[row][: (colm - 1) * 2]
        thisrow = self.map_rows[row][(colm - 1) * 2:(colm) * 2]
        if thisrow == ' .':
            player.gold += 1
            self.message_key[0] = 'g1'
        elif thisrow == ' •':
            player.gold += 7
            self.message_key[0] = 'g7'
        elif thisrow == ' :':
            player.gold += 19
            self.message_key[0] = 'g19'
        elif thisrow == ' ;':
            player.gold += 90
            self.message_key[0] = 'g90'
            # ".,•º∞*"
        elif thisrow == ' ∞':
            player.gold += 50
            self.message_key[0] = 'g50'
        elif thisrow == ' º':
            player.health += 33
            self.message_key[0] = 'h'
        elif thisrow == ' *':
            player.health += 26
            self.message_key[0] = 'h'
        elif thisrow == ' ,':
            player.gold += 5
            self.message_key[0] = 'g5'
        elif thisrow == ' x':
            player.re_equip()
            # player.inventory[0] = new_weapon(level[0])
            self.message_key[0] = 'looted'
        else:
            self.message_key[0] = ''
        ### HERO
        newrow += "  " # trail
        newrow += self.map_rows[row][(colm) * 2:]
        self.map_rows[row] = newrow
        p = self.map_rows[row][: (colm - 1) * 2]
        p += player.avatar
        p += self.map_rows[row][(colm) * 2:]
        print(p, row)
        for x in range(1, ind):
            print(self.map_rows[row + x], row + x)
        self.hud()



class Monster:
    def __init__(self, lvl ):
        self.level = lvl
        self.m_typ = self.m_type()
        # self.posr = randrange(2, 20)
        # self.posc = randrange(2, 20)
        # self.position = [self.posr, self.posc],
        self.position = [randrange(2, 20), randrange(2, 20)]
        self.type = self.m_typ[0]
        self.avatar = self.m_typ[1]
        self.biom = self.m_typ[2]
        # self.level = self.level,
        self.health = 100 * lvl

        self.inventory= [
                        {'type': 'weapon',
                          'name': self.w_name(),
                          'damage': 5 * self.level + 5},
                        {'type': 'shield',
                         'name': 'Shield',
                         'block': 5}]

    def m_type(self):
        return [
            ('Lizard Man', " §", ".,• º∞* xXX"),
            ('Dragon Breath', " £", ".,•º ∞* xXX"),
            ('Kraken', " §", ".,•º ∞*:"),
            ('Mage', " π", " ,º ∞* .;"),
            ('Sith Lord', " £", " .,*;"),
            ('Skeleton', " ¥", ". •* xXX"),
            ('Wizard', " π", " .,•º∞*;"),
            ('Lock Ness', " ∫", ".,• º∞*;"),
            ('T-Rex', " £", ".,•º∞*:"),
            ("C'Thulu", " ƒ", " .,•º∞*:"),
            ('Hydra', " §", ".,•º∞*: .")
        ][randrange(25)  % 10]

    def w_name(self):
        return [
            'Club',
            'Axe',
            'Bite',
            'Tenticle',
            'Sword',
            'Lance',
            'Spike',
            'Hatchet',
            'Chainsaw'
        ][randrange(23)  % 9]




class Player:
    def __init__(self, health=100, gold=5, name='Zork', lvl=1, current_position=[10, 1024]):
        self.current_position = current_position
        # self.current_position = [10, 1024]
        self.name = name
        self.health = health     #100
        self.gold = gold         #5
        self.inventory = self.equip()
        self.level = lvl
        self.avatar = " †"
        self.trail = "  "

    def equip(self):
        return [{'type': 'weapon', 'name': 'Axe', 'damage': 10}, {'type': 'shield', 'name': 'Shield', 'block': 5}]

    def re_equip(self):
        self.inventory = [self.new_weapon(), {'type': 'shield', 'name': 'Shield', 'block': 5}]

        # WEAPON DICTIONARY
    def new_weapon(self):
        # AQUIRE LEVEL , OR IS LEVEL A GLOBAL VARIABLE?
        return [
            {'type': 'weapon', 'name': 'Sword', 'damage': 7 * self.level},
            {'type': 'weapon', 'name': 'Spear', 'damage': 6 * self.level},
            {'type': 'weapon', 'name': 'Hammer', 'damage': 6 * self.level},
            {'type': 'weapon', 'name': 'Lance', 'damage': 8 * self.level},
            {'type': 'weapon', 'name': 'Axe', 'damage': 6 * self.level},
            {'type': 'weapon', 'name': 'Flail', 'damage': 7 * self.level},
            {'type': 'weapon', 'name': 'Spike', 'damage': 7 * self.level},
            {'type': 'weapon', 'name': 'Light Saber', 'damage': 8 * self.level},
            {'type': 'weapon', 'name': 'Reaper', 'damage': 9 * self.level}
        ][(randrange(25) ) % 9]

# player = {'name': 'ZORK', 'inventory': inventory, 'health': health, 'gold': gold}
# player['inventory'][0] = new_weapon(level[0])
##################################################################


#############################################################################################################
# ENGINE


MAP_SIZE = 24
LIVES = [3]

# monsters = [Monster(1), Monster(1)]
monsters = [Monster(1)]

level = [1]

# initialize
def generate_monster():
    player.level += 1
    level[0] += 1
    monsters.append(Monster(level[0]))



player = Player()

screen = Screen()

# ENGINE
def reincarnate():
    print("Killed by level {} {}.    Don't forget to heal!".format(level[0], monsters[0].type))
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################ !!!!YOU DIED!!!! ################ ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("#############  WOULD YOU LIKE TO BE  ############# ")
    print("#############    REINCARNATED? (n)   ############# ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    print("################################################## ")
    screen.hud()
    verdict = input('Reincarnate? ( any key or (n)o ) : ')
    if verdict.lower() == 'n':
        quit()
    player.health = 100
    player.current_position[0] = 10
    player.current_position[1] = 1024
    screen.head[0] = 5
    screen.mapit()
    #

# GAME ENGINE ? MECHANICS
def monster_move(mm=0):
    m = mm
    # for m in range(2):
    mon_row = monsters[m].position[0]
    mon_col = monsters[m].position[1]
    # mon_ind = MAP_SIZE - mon_row
    mon_colm = mon_col
    if monsters[m].position[0] < 1:
        monsters[m].position[0] = 1
    elif monsters[m].position[0] > 22:
        monsters[m].position[0] = 22
    else:
        monsters[m].position[0] += choice([-1, 0, 1])
    if monsters[m].position[1] < 2:
        monsters[m].position[1] = 2
    elif monsters[m].position[1] > 22:
        monsters[m].position[1] = 22
    else:
        monsters[m].position[1] += choice([-1, 0, 1])
    newrow = screen.map_rows[mon_row][: (mon_colm - 1) * 2]
    terr = screen.map_rows[mon_row][(monsters[m].position[1] - 1) * 2: ((monsters[m].position[1] - 1) * 2) + 2]
    # terr_prog = ".,•º∞*"
    ##############################################
    terr_prog = monsters[0].biom
    print('terr : "{}" '.format(terr))
    newrow += " " + terr_prog[(terr_prog.find(terr[1]) + 1) % len(terr_prog)]
    newrow += screen.map_rows[mon_row][(mon_colm) * 2:]
    screen.map_rows[mon_row] = newrow
    ##############################################

# ENGINE
def check_proximity(arg=2):
    if abs(monsters[0].position[0] - player.current_position[0]) < arg and arg > abs(
                    monsters[0].position[1] - screen.get_index_from_bit(player.current_position[1])):
        return True
    return False

# ENGINE
def check_death(arg):
    if arg < 0:
        return True
    return False

# ENGINE
def game_over(win):
    if win:
        screen.head[0] = 4
        m0 = monsters[0].position[0]
        m1 = monsters[0].position[1]
        new_row = screen.map_rows[m0][:(m1 - 1) * 2]
        new_row += ' x'
        new_row += screen.map_rows[m0][m1 * 2:]
        screen.message_key[1] = 'killedit'
        # screen.message_key[1] = 'killedit'
        screen.map_rows[m0] = new_row

        # determine which monster
        z = monsters.pop()
        generate_monster()
    else:
        LIVES[0] -= 1
        if LIVES[0] > 0:
            reincarnate()
        else:
            screen.head[0] = 3
            screen.header()
            quit()

# ENGINE
def monster_attack():

    v = monsters[0].inventory[0]['damage'] - player.inventory[1]['block']
    player.health -= v

    if check_death(player.health):
        game_over(False)
    screen.message_key[2] = 'dmg ' + str(monsters[0].inventory[0]['damage'])


########################################################################################################################


# ENGNINE
def player_attack(arg):
    print(arg)
    # if check_proximity():
    if arg == 'kill':
        monsters[0].health = monsters[0].health - (player.inventory[0]['damage'] * 10)
        screen.head[0] = 2
    elif arg.lower() == 'zero':
        monsters[0].health = 0
        screen.head[0] = 2
    elif arg.lower() == 'zork':
        monsters[0].health = monsters[0].health - (player.inventory[0]['damage'] * 90)
        screen.head[0] = 2
    else:
        print('monsters[0].health : ',monsters[0].health)
        monsters[0].health -= int(player.inventory[0]['damage'] + (player.gold * .01))  - monsters[0].inventory[1]['block']
    if check_death(monsters[0].health):
        game_over(True)




    monster_go()
    screen.mapit()


# IF MODE == ROAM: MOVE
# IF MODE == FIGHT: ATTACK HERO
monster_modes = ['ROAM', 'FIGHT']
monster_mode = monster_modes[0]

# ENGINE
def monster_go():
    proximity = check_proximity()
    if proximity:
        monster_mode = monster_modes[1]
    else:
        monster_mode = monster_modes[0]
    if monster_mode == 'ROAM':
        screen.head[0] = 0
        monster_move()
        # FIX FOR SLAIN
        screen.message_key[1] = ''
        screen.message_key[2] = ''
    elif monster_mode == 'FIGHT':
        screen.message_key[1] = 'm1'
        screen.head[0] = 2
        monster_attack()



# ENGINE

screen.mapit()
# CALCULATE TRANSLATION OF current_position
def move(arg):
    # print("move arg: ", arg)
    if arg == 2:  # 'n'
        if player.current_position[0] > 0:
            player.current_position[0] = player.current_position[0] - 1
        player.current_position[1] = player.current_position[1]
    elif arg == 0:  # 's' | '8' :
        player.current_position[0] = player.current_position[0]
        player.current_position[1] = player.current_position[1]
    elif arg == 8:  # 's' | '8' :
        if player.current_position[0] < 23:
            player.current_position[0] = player.current_position[0] + 1
        player.current_position[1] = player.current_position[1]
    # move(8)
    elif arg == 6:  # 'e' | '6' :
        player.current_position[0] = player.current_position[0]
        if player.current_position[1] > 1:
            player.current_position[1] = player.current_position[1] >> 1
        # move(6)
    elif arg == 4:  # 'w' | '4' :
        player.current_position[0] = player.current_position[0]
        if player.current_position[1] < 1 << 23:
            player.current_position[1] = player.current_position[1] << 1
        # move(4)
    elif arg == 1:  # 'nw' | '1' :
        if player.current_position[0] > 0:
            player.current_position[0] = player.current_position[0] - 1
        if player.current_position[1] < 1 << 23:
            player.current_position[1] = player.current_position[1] << 1
        # move(1)
    elif arg == 3:  # 'ne' | '3' :
        if player.current_position[0] > 0:
            player.current_position[0] = player.current_position[0] - 1
        if player.current_position[1] > 1:
            player.current_position[1] = player.current_position[1] >> 1
        # move(3)
    elif arg == 7:  # 'sw' | '7' :
        if player.current_position[0] < 23:
            player.current_position[0] = player.current_position[0] + 1
        if player.current_position[1] < 1 << 23:
            player.current_position[1] = player.current_position[1] << 1
        # move(7)
    elif arg == 9:  # 'se' | '9' :
        if player.current_position[0] < 23:
            player.current_position[0] = player.current_position[0] + 1
        if player.current_position[1] > 1:
            player.current_position[1] = player.current_position[1] >> 1
        # move(9)
    monster_go()
    # header(0)
    screen.mapit(player.current_position[0], player.current_position[1])


########################################################################
######################  SPELL BOOK  ####################################
########################################################################
def heal_self(arg='9'):
    print(arg)
    player.gold = player.gold - int(arg)
    player.health = player.health + int(arg)
    monster_go()

def cast_spell(spell=''):
    if spell[:5] == 'black' and player.gold > 60:
        player.gold -= 60
        if check_proximity(4):
            player_attack('kill')

    elif spell[:4] == 'zero' and player.gold > 100:
        player.gold -= 100
        if check_proximity(1):
            player_attack(spell)

    elif spell[:4] == 'five' and player.gold > 50:
        player.gold -= 50
        if check_proximity(5):
            player_attack(spell)

    elif spell[:6] == 'orange' and player.gold > 10:
        player.gold -= 10
        if check_proximity(9):
            player_attack(spell)

    elif spell[:5] == 'death' and player.gold > 100:
        player.gold -= 100
        if check_proximity(20):
            player_attack('kill')

    elif spell == '' and player.gold > 30:
        player.gold -= 30
        if check_proximity(3):
            player_attack(spell)
    else:
        if check_proximity():
            player_attack(spell)

########################################################################
######################  /SPELL BOOK  ###################################
########################################################################


# Engine
# USER INPUT LOOP
while True:
    command = input("Type Command: ( n s e w a(t)tack cast heal x:exit )\n>>> ")

    if command[:2] == 'at' or 't' == command[:1] or command[:1] == 'w' or ' ' == command[:1] or '' == command[:1]:
        if check_proximity():
            player_attack(command[command.find(" ") + 1:])
        else:
            move(0)

    elif command[:4] == 'cast' or 'c' == command[:1]:
        cast_spell(command[command.find(' ')+1:])
        screen.head[0] = 1
        screen.mapit()

    elif command[:4] == 'heal' or 'h' == command[:1]:

        # if len(command) > 4:
        if command.find(' ') > -1:
            heal_self(command[command.find(' '):])
        else:
            heal_self()
        screen.head[0] = 0
        screen.mapit()

    else:
        for i in range(len(command)):
            if command[i] == 'x':
                if input('      Are you sure you want to quit? (c) ') == 'c':
                    quit()
            elif command[i] == 'n' or '2' == command[i] or 'A' == command[i]:
                move(2)
            elif command[i] == 's' or '8' == command[i] or 'B' == command[i]:
                move(8)
            elif command[i] == 'e' or '6' == command[i] or 'C' == command[i]:
                move(6)
            elif command[i] == 'q' or '4' == command[i] or 'D' == command[i]:
                move(4)
            elif command[i] == '1':
                move(1)
            elif command[i] == '3':
                move(3)
            elif command[i] == '7' or 'a' == command[i]:
                move(7)
            elif command[i] == '9' or 'd' == command[i]:
                move(9)

            # NEXT:
# Multiple MONSTERs
#
# 
##################################################################



    ########################################
    # STRING TEMPLATES




    # def __init__(self, make, model, year, color):
    #     self.model = model
    #     self.make = make
    #     self.year = year
    #     self.color = color
    #
    # def __str__(self):
    #     return '{}, {}, {}, {}'.format(self.make,
    #                                    self.model,
    #                                    self.year,
    #                                    self.color)
    #
    # def __repr__(self):
    #     return '{} {}'.format(self.color, self.model)