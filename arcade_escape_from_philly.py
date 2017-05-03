# Instruction screens before first frame.
# magic spells released at certain levels
# Multiple monsters
# magic cost gold.
# Map
# Monster
# Player
# # SpellBook
## ESCAPE FROM PHILADELPHIA .PY #################################


from random import randrange, choice


class Map:
    '''
    METHODS:
        move(num)
        123
        406
        789
    '''

    def __init__(self, player, monsters, ma_fn_ref, lvl_fn_ref, get_lives_fn, get_mon_fn, getplayer_fn):
        '''INITIALIZE VARIALBES'''
        self.player = player
        self.monsters = monsters
        self.get_player = getplayer_fn

        self.monster_attack = ma_fn_ref
        self.level_fn = lvl_fn_ref
        self.get_lives = get_lives_fn
        self.get_monsters = get_mon_fn

        self.MAP_SIZE = 24
        self.map_row = " . . . . . . . . . . . . . . . . . . . . . . . ."
        self.map_rows = self.initialize_map(4)  # []
        self.frame_i = [0]
        self.head = [0]
        self.message_key = ['', '', '', '']
        self.this_monster = [0]
        self.monster_modes = ['ROAM', 'FIGHT']

        '''
        EXPAND MAPS
        012
        345
        678
        '''
        self.maps = [[[], [], []], [[], [], []], [[], [], []]]
        self.maps[0][1] = self.initialize_map(1)
        self.maps[1][1] = self.map_rows
        self.maps[2][1] = self.initialize_map(7)

        self.maps[0][0] = self.initialize_map(0)
        self.maps[1][0] = self.initialize_map(3)
        self.maps[2][0] = self.initialize_map(6)

        self.maps[0][2] = self.initialize_map(2)
        self.maps[1][2] = self.initialize_map(5)
        self.maps[2][2] = self.initialize_map(8)

        self.current_map = [1, 1]

        print(self.maps[self.current_map[0]][self.current_map[1]])

    def initialize_map(self, x):
        '''INITIALIZE MAP'''

        if x == 0:
            mp = []
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . ; ; ; . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . ; X . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . ; X ; . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . ; ; ; . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # # # # . . . . . # . . . . . . . . . . . . . .")
            mp.append(" . . . # . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . # . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . . # . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . # . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . # . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . # . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . . # . . . . . # . . . . . . . . . . . . . .")

        if x == 3:
            mp = []
            mp.append(" # . . # . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . # . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . # . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . # . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . # . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . . # . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . # # # # # # # # # # # # # . # # . . . . . .")
            mp.append(" # . # . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . # . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . # . . . . # . . . . . . . . . # # # . # # .")
            mp.append(" # . # . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . # . . . . # . . . . . . . . . . . ; * ; ; .")
            mp.append(" # . # . . . . # . . . . . . . . . # . ; * ; ; .")
            mp.append(" # . # . . . . . . . . . * * . . . # . ; * ; ; .")
            mp.append(" # . # . . . . # . . . . * * . . . # . * * * * .")
            mp.append(" # . # . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # . # . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # . # . # # # # . . . . . . . . . # . * * * * .")
            mp.append(" # . # . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # . # . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # . # # . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . . # . . . . . . . . . . . . . . . . . . . .")

        elif x == 6:
            mp = []
            mp.append(" # . # . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . # . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . # . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . # . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . # . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # # # # # # # # # # # # # # # . # # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # # # . # # .")
            mp.append(" # . . . . . . # . . # . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . # . . . . . . # . ; * ; ; .")
            mp.append(" # . . . . . . # . . # . . . . . . # . ; * ; ; .")
            mp.append(" # . . . . . . . . . # . X X . . . # . ; * ; ; .")
            mp.append(" # . . . . . . # . . # . X X . . . # . * * * * .")
            mp.append(" # . . . . . . # . . # . . . . . . # . * * * * .")
            mp.append(" # . . . . . . # . . # . . . . . . ; . * * * * .")
            mp.append(" # # # . # # # # . . . . . . . . . # . * * * * .")
            mp.append(" # . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # . . . . . . # # # # # # # # # # # . * * * * .")
            mp.append(" # . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")

        if x == 1:
            mp = []
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . # # # # # # # # # # # # # # # # # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . # . . . . .")
            mp.append(" . . . . . . . . . . . # . # . X . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # . X . # . . . . . .")
            mp.append(" . . . . . . . . . . . . # . . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # # # # # . . . . . .")
            mp.append(" . . . . . . . . . . . # . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # # # # # # # # # # # . # # # # # # # # # # # .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")

        if x == 4:
            mp = []
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . # . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # # # # # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . # # # # # . # # # # # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # # # # # # # # # . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")

        elif x == 7:
            mp = []
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . # # # # # # . # # # # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # # # # # # .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . ; * ; ; .")
            mp.append(" . . . . . . . # . . . . . . . . . # . ; * ; ; .")
            mp.append(" . . . . . . . . . . . . . . . . . # . ; * ; ; .")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # # # # # # # # . . . . . . . . . # . * * * * .")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" . . . . . . . # # # # # . # # # # # . * * * * .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")

        if x == 2:
            mp = []
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . , X #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . , , #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . , . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . , . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . , . . #")
            mp.append(" . # # # # # # # # # # # # # # # # # . . . . . #")
            mp.append(" . . . . . . . . . . . . ; ; ; ; ; ; # . . . . #")
            mp.append(" . . . . . . . . . . . # . # ; ; ; # . . . . . #")
            mp.append(" . . . . . . . . . . . . . # ; ; ; # . . . . . #")
            mp.append(" . . . . . . . . . ; ; . # . ; ; X # . . . . . #")
            mp.append(" . . . . . . . . # . # . . # # # # # . . . . . #")
            mp.append(" . . . . . . . . . . # # . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . # . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . # . . . . . . . . . # # # # # #")
            mp.append(" . . . . . . . . . . . . . . . . . . # X X X X #")
            mp.append(" . . . . . . . . . . . . . . . . . . # X X X X #")
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")

        if x == 5:
            mp = []
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . # . . . . . . . . . # . . . . . . . . . . . #")
            mp.append(" . # . . . x . . . . . # . . . . . . . . . . . #")
            mp.append(" . # . . . . . x . x . # . . . . . . . . . . . #")
            mp.append(" . # . . . . . . . . . # . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . # . . . . . . . . . . . #")
            mp.append(" . # # # # # . # # # # # . . . . . . . . . . . #")
            mp.append(" . # . . . . . . . . . # . . . . . . . . . . . #")
            mp.append(" . # . . . . . . . . . # . . . . . . . . . . . #")
            mp.append(" . # . . . x . . . . . # . . . . . . . . . . X #")
            mp.append(" . # . . . . . . . . . # . . . . . . . . . . . #")
            mp.append(" . # . . . . x . . . . # . . . . . . . . . . . #")
            mp.append(" . # . . . . . . . x . # . . . . . . . . . . . #")
            mp.append(" . # . . . . . . . . . # . . . . . . . . . . . #")
            mp.append(" . # . . . . . x . . . # . . . . . . . . . . . #")
            mp.append(" . # # # # # # # # # . # . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . # . . . # . . . . . . . . . . . #")
            mp.append(" . . . . . . . # . X . # . . . . . . . . . . . #")
            mp.append(" . . . . . . . # . X . # . . . . . . . . . . . #")
            mp.append(" . . . . . . . # # # # # . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")

        elif x == 8:
            mp = []
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # # # # # # # # # # # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . X . . #")
            mp.append(" . . . . . . . # . . . . . . # . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . # . . # # # # # # #")
            mp.append(" . . . . . . . # . . . . . . # . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . # X . # . x x x x .")
            mp.append(" . . . . . . . # # # # # # . # # # # . x x x x #")
            mp.append(" . . . . . . . # . . . . . . # X . # . x x x x #")
            mp.append(" . . . * * * * # . . . . . . # . . # . x x x x #")
            mp.append(" . . . * * * * # . . . . . . # . . # . x x x x #")
            mp.append(" . . . * * * * # . . . . . . . . . # . x x x x #")
            mp.append(" . . . . . . . # . . . . . . . . . # . x x x x #")
            mp.append(" # # # # # # # # . . . . . . . . . # . x x x x #")
            mp.append(" . . . . # . . # . . . . . . . . . # . * * * * #")
            mp.append(" . . X X # . . # # # # # . # # # # # . * * * * #")
            mp.append(" . . . . # . . . . . . . . . . . . . . . . . . #")
            mp.append(" # # # # # . # # # # # # # # # # # # # # # # # #")

        return mp


    def reincarnate(self, player, monsters):
        """FOR WHEN PLAYER DIES BUT HAS MORE LIVES"""

        print("Killed by level {} {}.    Don't forget to heal!".format(self.level_fn(),
                                                                       monsters[self.this_monster[0]].type))
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
        self.hud(player)
        verdict = input('Reincarnate? ( any key or (n)o ) : ')
        if verdict.lower() == 'n':
            quit()
        player.health = 100
        player.position[0] = 12
        player.position[1] = 12
        self.head[0] = 5
        self.mapit(player, monsters)
        #

    def monster_go(self, player, monsters):
        '''MONSTERS TURN DETERMINATION'''

        # fizz = lambda v: v

        self.message_key[1] = ''
        self.message_key[2] = ''
        self.message_key[3] = ''
        for m in range(len(monsters)):
            arg = 2
            if abs(monsters[m].position[0] - player.position[0]) < arg and arg > abs(
                            monsters[m].position[1] - self.get_index_from_bit(player.position[1])):
                monsters[m].mode = self.monster_modes[1]
            else:
                monsters[m].mode = self.monster_modes[0]

            if monsters[m].mode == 'ROAM':
                self.head[0] = 0
                self.monster_move(monsters, m)
            elif monsters[m].mode == 'FIGHT':
                self.message_key[1] = 'm1'
                self.head[0] = 2
                self.this_monster[0] = m
                self.monster_attack(m)

    def unobstructed(self, arg):
        '''CHECK FOR OBSTRUCTION TO MOVEMENT'''
        # print(arg)
        if arg == " #":
            return False
        else:
            return True

    def monster_move(self, monsters, mm=0):

        '''maps the monster to a new position on map'''

        m = mm
        # for m in range(2):
        mon_row = monsters[m].position[0]
        mon_col = monsters[m].position[1]
        # mon_ind = MAP_SIZE - mon_row

        rand_verticle = choice([-1, 0, 1])
        rand_horizontal = choice([-1, 0, 1])

        proposed0 = 0
        proposed1 = 0

        mon_colm = mon_col
        if monsters[m].position[0] < 1:
            monsters[m].position[0] = 1
        elif monsters[m].position[0] > 22:
            monsters[m].position[0] = 22


        else:
            # monsters[m].position[0] += choice([-1, 0, 1])
            proposed0 = monsters[m].position[0] + rand_horizontal
        #
        if monsters[m].position[1] < 2:
            monsters[m].position[1] = 2
        elif monsters[m].position[1] > 22:
            monsters[m].position[1] = 22


        else:
            # monsters[m].position[1] += choice([-1, 0, 1])
            proposed1 = monsters[m].position[1] + rand_verticle
        #

        try:
            # print('[proposed0][(proposed1  : {} , {} '.format(proposed0, proposed1 ) )
            proposed_terr = self.maps[self.current_map[0]][self.current_map[1]][proposed0][
                            (proposed1 - 1) * 2: ((proposed1 - 1) * 2) + 2]
            # print("proposed_terr : '{}' ".format( proposed_terr) )
        except IndexError:
            proposed_terr = " ."

        # if " #" != proposed_terr:
        if self.unobstructed(proposed_terr):
            # print("proposed_terr : ' #' is not '{}' ".format(proposed_terr))
            monsters[m].position[0] += rand_horizontal
            monsters[m].position[1] += rand_verticle

        try:
            newrow = self.maps[self.current_map[0]][self.current_map[1]][mon_row][: (mon_colm - 1) * 2]
        except IndexError:

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
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("################################################## ")
            print("###    YOU HAVE ESCAPED FROM PHILADELPHIA !   #### ")
            print("###    YOU HAVE ESCAPED FROM PHILADELPHIA !   #### ")
            print("###    YOU HAVE ESCAPED FROM PHILADELPHIA !   #### ")
            print("###    YOU HAVE ESCAPED FROM PHILADELPHIA !   #### ")
            print("###    YOU HAVE ESCAPED FROM PHILADELPHIA !   #### ")
            print("###    YOU HAVE ESCAPED FROM PHILADELPHIA !   #### ")
            print("###    YOU HAVE ESCAPED FROM PHILADELPHIA !   #### ")
            print("###    YOU HAVE ESCAPED FROM PHILADELPHIA !   #### ")
            print("###    YOU HAVE ESCAPED FROM PHILADELPHIA !   #### ")
            print("###    YOU HAVE ESCAPED FROM PHILADELPHIA !   #### ")
            print("###    YOU HAVE ESCAPED FROM PHILADELPHIA !   #### ")
            print("###    YOU HAVE ESCAPED FROM PHILADELPHIA !   #### ")
            print("################################################## ")
            print("################################################## ")
            yes = input("CONTINUE ? >>>")
            # MAP 1:1
            # PLAYER POSITION 12,12
            # mapit
            player = self.get_player()
            self.current_map[0] = 1
            self.current_map[1] = 1
            self.player.position[0] = 12
            self.player.position[1] = 12
            self.head[0] = 5
            self.mapit(player, monsters)
            return

        #
        ##### THIS IS THE TEST: ######################
        # terr = self.maps[self.current_map[0]][self.current_map[1]][mon_row][(monsters[m].position[1] - 1) * 2: ((monsters[m].position[1] - 1) * 2) + 2]


        # try:
        terr = self.maps[self.current_map[0]][self.current_map[1]][monsters[m].position[0]][
               (monsters[m].position[1] - 1) * 2: ((monsters[m].position[1] - 1) * 2) + 2]
        # except IndexError:
        #     pass


        ##############################################

        # terr_prog = ".,•º∞*"
        terr_prog = monsters[0].biom
        # print('terr : "{}" '.format(terr))
        newrow += " " + terr_prog[(terr_prog.find(terr[1]) + 1) % len(terr_prog)]
        newrow += self.maps[self.current_map[0]][self.current_map[1]][mon_row][(mon_colm) * 2:]
        self.maps[self.current_map[0]][self.current_map[1]][mon_row] = newrow

    def check_proximity(self, monsters, player, arg=2):
        '''returns True if target is within proximity of arg. 
        2 == adjacent square; 
        3 == 2 spaces away
        1 == same square
        '''

        for m in range(len(monsters)):
            if abs(monsters[m].position[0] - player.position[0]) < arg and arg > abs(
                            monsters[m].position[1] - self.get_index_from_bit(player.position[1])):
                self.this_monster[0] = m
                return True
        return False

    def message(self, x, additional='', monsters=[]):
        '''MESSAGE SYSTEM : TO BE REVAMPED FOR NEW GAME'''
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

                   'm1': '{} with {}({}) HP:{} '
                       .format(self.get_monsters()[self.this_monster[0]].type.title(),
                               self.get_monsters()[self.this_monster[0]].inventory[0]['name'],
                               self.get_monsters()[self.this_monster[0]].inventory[0]['damage'],
                               self.get_monsters()[self.this_monster[0]].health),

                   '.': 'Nothing to say.',
                   '': '',

                   # THIS IS NOT WORKING:
                   'killedit': 'You have slain the monster!',

                   'looted': 'You have looted the corpse',
                   'dmg': '- DAMAGE = '

               }[x] + additional

    def hud(self, player):
        '''HEADS UP DISPLAY : TEN LINES X48 CHARACTERS

        '''
        # print("################################################# ")
        #

        print("################################################# ")

        print("LEFT : {} {}  HEALTH: {}  {}".format(player.inventory[0]['name'], player.inventory[0]['damage'],
                                                    player.health,
                                                    self.message(self.message_key[2][:3],
                                                                 self.message_key[2][self.message_key[2].find(' '):])))
        print("RIGHT: {}({})    GOLD  : {} ".format(player.inventory[1]['name'], player.inventory[1]['block'],
                                                    player.gold))
        # print(":POTION ^(f)                  (r)^ STAFF:")
        print(self.message(self.message_key[1]), self.message(self.message_key[0]))

        # HELPER FUNCTION FOR mapit()

    def get_index_from_bit(self, c):
        '''HELPER FUNCTION : TRANSLATES BINARY NUMBER TO INDEX'''
        # for i in range(self.MAP_SIZE):
        #     if c == 1 << i:
        #         return self.MAP_SIZE - i
        return c

    def story_line(self, X):

        return {
            'opening': "",
            'middle': "",
            'ending': "",
            '':''
        }[X]

    def header(self, player={}):
        '''PRINTS HEADER'''
        # print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(self.story_line(self.message_key[3]))

        self.frame_i[0] += 1
        print('Frame # {}  Level # {}   Lives : {} '.format(self.frame_i[0], self.level_fn(), self.get_lives()))

        if self.head[0] == 0:
            print("########################################: 123 | 123")
            print("##     ESCAPE FROM PHILADELPHIA    ###### q*e | 4*6")
            print("######################################### asd | 789")
            print("Confront " + self.get_monsters()[self.this_monster[0]].long_description)
            print("##################### MAP{}:{} ##################### ".format(self.current_map[0],
                                                                                 self.current_map[1]))
        elif self.head[0] == 1:
            print("################################################## ")
            print("################# A SPELL IS CAST ################ ")
            print("################################################## ")
        elif self.head[0] == 2:
            print("################################################## ")
            print("################ MONSTER ATTACKED ################ ")
            print("Fighting " + self.get_monsters()[self.this_monster[0]].long_description)
            print("################################################## ")
        elif self.head[0] == 3:

            print("Killed by level {} {}.  Don't forget to heal!".format(self.level_fn(), self.get_monsters()[0].type))
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
            self.hud(player)

        elif self.head[0] == 4:
            print("################################################## ")
            print("############### !!!! YOU WON !!!! ################ ")
            print("################################################## ")
        elif self.head[0] == 5:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
            print("######## !! YOU HAVE BEEN REINCARNATED !! ######## ")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")

    def mapit(self, player, monsters, a='', b=''):
        '''PRINTS MAP : CALLED INTERNALLY'''
        col = player.position[1]
        row = player.position[0]
        self.header()
        ind = self.MAP_SIZE - row

        ### MONSTER
        for m in range(len(monsters)):
            mon_row = monsters[m].position[0]
            mon_col = monsters[m].position[1]
            mon_colm = mon_col
            newrow = self.maps[self.current_map[0]][self.current_map[1]][mon_row][: (mon_colm - 1) * 2]
            newrow += monsters[m].avatar
            newrow += self.maps[self.current_map[0]][self.current_map[1]][mon_row][(mon_colm) * 2:]
            self.maps[self.current_map[0]][self.current_map[1]][mon_row] = newrow

        for r in range(row):
            print(self.maps[self.current_map[0]][self.current_map[1]][r], r)
        colm = self.get_index_from_bit(col)
        newrow = self.maps[self.current_map[0]][self.current_map[1]][row][: (colm - 1) * 2]
        thisrow = self.maps[self.current_map[0]][self.current_map[1]][row][(colm - 1) * 2:(colm) * 2]
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
            self.message_key[0] = 'looted'
        elif thisrow == ' X':
            player.re_equip()
            player.gold += 5000
            self.message_key[0] = 'looted'
        else:
            self.message_key[0] = ''
        ### HERO
        newrow += "  "  # trail
        newrow += self.maps[self.current_map[0]][self.current_map[1]][row][(colm) * 2:]
        self.maps[self.current_map[0]][self.current_map[1]][row] = newrow
        p = self.maps[self.current_map[0]][self.current_map[1]][row][: (colm - 1) * 2]
        p += player.avatar
        p += self.maps[self.current_map[0]][self.current_map[1]][row][(colm) * 2:]
        print(p, row)
        for x in range(1, ind):
            print(self.maps[self.current_map[0]][self.current_map[1]][row + x], row + x)
        self.hud(player)

    def cleanse_map(self, monsters):
        # REMOVE MONSTERS BEFORE SWITCHING MAPS:

        for m in range(len(monsters)):
            mon_row = monsters[m].position[0]
            mon_col = monsters[m].position[1]
            mon_colm = mon_col
            newrow = self.maps[self.current_map[0]][self.current_map[1]][mon_row][: (mon_colm - 1) * 2]
            newrow += " ."
            newrow += self.maps[self.current_map[0]][self.current_map[1]][mon_row][(mon_colm) * 2:]
            self.maps[self.current_map[0]][self.current_map[1]][mon_row] = newrow



        # CALCULATE TRANSLATION OF position

    def move(self, arg, player, monsters):
        ''' RECEIVE INPUT : CALLED EXTERNALLY
        map.move(number)
        123
        406
        789
        RETURNS RESULTING EVENT:
        SUCCESS, FAIL=HIT WALL
        '''
        # INSERT CONDITIONALS FOR WALL ENCOUNTERS
        print("move arg: ", arg)
        temp_y0 = player.position[0]
        temp_x1 = self.get_index_from_bit(player.position[1])

        if arg == 2:  # 'n'
            if player.position[0] > 0:
                temp_y0 += -1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]

                if self.unobstructed(terr):
                    player.position[0] = player.position[0] - 1
                    # player.position[1] = player.position[1]
            else:

                self.cleanse_map(monsters)

                self.current_map[0] += -1
                player.position[0] = self.MAP_SIZE - 1



        elif arg == 0:  # '0' :
            pass
            # player.position[0] = player.position[0]
            # player.position[1] = player.position[1]

        elif arg == 8:
            # 's' | '8' :
            if player.position[0] < 23:
                temp_y0 += 1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed(terr):
                    player.position[0] = player.position[0] + 1
                    # player.position[1] = player.position[1]
            else:
                self.cleanse_map(monsters)
                self.current_map[0] = (self.current_map[0] + 1) % 3
                player.position[0] = (player.position[0] + 1) % 24
        # CHANGE MAP


        # move(8)

        elif arg == 6:  # 'w' | '6' :
            # print(">w player.position[1] : ", player.position[1])
            if player.position[1] < 24:
                temp_x1 += 1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed(terr):
                    player.position[1] = player.position[1] + 1
            # player.position[0] = player.position[0]

            else:
                self.cleanse_map(monsters)
                self.current_map[1] += 1
                player.position[1] = 1

                # move(6)



        elif arg == 4:  # 'e' | '4' :

            # print("<e player.position[1] : ", player.position[1])

            if player.position[1] > 1:
                temp_x1 += -1
                terrr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                        (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed(terrr):
                    player.position[1] = player.position[1] - 1
                    # player.position[0] = player.position[0]
            # move(4)

            else:
                self.cleanse_map(monsters)
                self.current_map[1] += -1
                player.position[1] = 24



        elif arg == 1:  # 'nw' | '1' :
            if player.position[0] > 0:
                temp_y0 += -1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][ (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed( terr ):
                    player.position[0] = player.position[0] - 1

            # if player.position[1] < 1 << 23:
            if player.position[1] < 24:
                temp_x1 += -1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed(terr):
                    # player.position[1] = player.position[1] << 1
                    player.position[1] = player.position[1] - 1
            # move(1)

        elif arg == 3:  # 'ne' | '3' :
            if player.position[0] > 0:
                temp_y0 += -1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][ (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed( terr ):
                    player.position[0] = player.position[0] - 1
            if player.position[1] > 1:
                temp_x1 += 1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed( terr ):
                    player.position[1] = player.position[1] + 1
            # move(3)

        elif arg == 7:  # 'sw' | '7' :
            if player.position[0] < 23 and player.position[1] < 24:
                temp_y0 += 1
                temp_x1 += -1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed( terr ):
                    player.position[0] = player.position[0] + 1
                    player.position[1] = player.position[1] - 1
            # if player.position[1] < 24:
            #     temp_y0 += 1
            #     temp_x1 += -1
            #     terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
            #            (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
            #     if self.unobstructed(terr):
            # move(7)

        elif arg == 9:  # 'se' | '9' :
            if player.position[0] < 23:
                temp_y0 += 1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed( terr ):
                    player.position[0] = player.position[0] + 1
            if player.position[1] > 1:
                temp_x1 += 1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed( terr ):
                    player.position[1] = player.position[1] + 1
            # move(9)


        self.monster_go(player, monsters)
        # header(0)
        self.mapit(player, monsters)


##################################################################

MAP_SIZE = 24
LIVES = [4]
monster_modes = ['ROAM', 'FIGHT']
this_monster = [0]
level = [1]

def get_level():
    return level[0]

def get_lives_func():
    return LIVES[0]

def generate_monster():
    player.level += 1
    level[0] += 1
    monsters.append(MonSteR(level[0]))

##################################################################

print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################## WELCOME TO #################### ")
print("################################################## ")
print("##########    ESCAPE FROM PHILADELPHIA   ######### ")
print("################################################## ")
print("### MOVE WITH ARROW KEYS OR NUMBER PAD + ENTER ### ")
print("################################################## ")
print("##### ATTACK WITH ENTER WHEN NEXT TO MONSTER ##### ")
print("################################################## ")
print("########## HEAL WITH \"h [number]\" + ENTER ######## ")
print("################################################## ")
print(" LEARN TO CAST SPELLS WITH \"cast [spell]\" + ENTER  ")
print("################################################## ")
print("# SPELLS:>>> heal 99  heals 99 costs 99 gold ##### ")
print("# SPELLS:>>> cast live  adds 1 life costs 1000 gold")
print("################################################## ")
print("# ATTACK SPELLS ################################## ")
print("# SPELLS:>>> cast death ########################## ")
print("# SPELLS:>>> t zero    ########################### ")
print("################################################## ")
print("################################################## ")


class MonSteR:
# class MonSteR:
    def __init__(self, lvl ):
        # Monster.__init__(self)
        self.mode = monster_modes[0]
        self.level = lvl
        self.m_typ = self.m_type()
        self.position = [randrange(2, 20), randrange(2, 20)]
        self.type = self.m_typ[0]
        self.avatar = self.m_typ[1]
        self.biom = self.m_typ[2]
        self.long_description = self.m_typ[3]
        self.health = 100 * lvl
        self.inventory= [
                        {'type': 'weapon',
                          'name': self.w_name(),
                          'damage': 5 * self.level + 5},
                        {'type': 'shield',
                         'name': 'Shield',
                         'block': 5}]

    def m_type(self):



        name = self.named()

        return [


            (name[0], " §", ".,•º*.  xXX", name[1]),
            (name[0], " £", ". , • º ∞ *  xXX", name[1]),
            (name[0], " §", ".,•º*::  xXX", name[1]),
            (name[0], " π", ",º∞*  .;#  xXX", name[1]),
            (name[0], " £", ".,*;  xXX", name[1]),
            (name[0], " ¥", ".•*;  xXX", name[1]),
            (name[0], " π", " .,•º;#  xXX", name[1]),
            (name[0], " ∫", ".,•º* .;  xXX", name[1]),
            (name[0], " £", ".,•º∞*: .  xXX", name[1]),
            (name[0], " ƒ", ".,•º∞*:  xXX", name[1]),
            (name[0], " §", ".,•º*: .  xXX", name[1]),

# Clasic:
            # ('Lizard Man', " §", ".,• º∞*.  xXX"),
            # ('Dragon Breath', " £", ".,•º ∞#*  xXX"),
            # ('Kraken', " §", ".,•º ∞*:  xXX"),
            # ('Mage', " π", " ,º ∞* .;  xXX"),
            # ('Sith Lord', " £", " .,*;  xXX"),
            # ('Skeleton', " ¥", ". •*  xXX"),
            # ('Wizard', " π", " .,•º∞*;#  xXX"),
            # ('Lock Ness', " ∫", ".,• º∞*;  xXX"),
            # ('T-Rex', " £", ".,•º∞ *:  xXX"),
            # ("C'Thulu", " ƒ", " .,•º∞*:  xXX"),
            # ('Hydra', " §", ".,•º∞*: .  xXX")
        ][randrange(25) % 10]

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
        ][randrange(23) % 9]


    def named(self):
        """Thanks to Mike for this function"""
        adjectives = choice(['aggravating', 'annoying', 'distressing', 'disturbing', 'inconvenient', 'arduous',
                    'bothersome', 'troublesome', 'irritating', 'troublesome', 'vexing', 'exasperating', 'rebarbative incommodious',
                    'remote', 'vexatious', 'ambitious', 'demanding', 'difficile', 'exacting',
                    'wearisome', 'formidable', 'galling', 'onerous', 'operose', 'painful', 'problematic',
                    'prohibitive', 'rigid', 'severe', 'strenuous', 'titanic', 'toilsome', 'tough', 'trying', 'unyielding',
                    'burdensome', 'challenging', 'crucial', 'gargantuan', 'heavy', 'herculean', 'immense', 'irritating',
                    'labored', 'laborious'])

        place_names = choice(['Frankfurter Ave.', 'the Passyunk Warrior Clan', 'the Philly Cheesesteak Factory',
                    'Manayunk Railroad Yard','Skidoo Water Park Palace', 'Dunks Ferry Playground', 'Pigeons\' Gauntlet',
                    'the Inauspicious Tower of Dread at Mario Lanza Boulevard', 'the Dungeon at Dicks Ave.',
                    'the Reading Terminal Market Book Club', 'the Stronghold of Doom at Longwood Gardens',
                    'the cave under the Philadelphia Zoo', 'the dreaded Eastern State Penitentiary',
                    'the depressing, perenial dissapointment known as the Philadelphia Eagles'])

        monsterr = choice(['Rabbit', 'Troll', 'Dragon', 'Carniverous Camel', 'Loner Llama', 'Ogre', 'Slime Mold', 'Fungal Beast',
                        'Vampire', 'Dampyr', 'malformed non-specific animal', 'Shark Rocket', 'Tengu', 'Shadow Liger', 'Dragon', 'Gaslich',
                        'Hollowlich', 'Embermask', 'Bowelwraith', 'Clammy-hand Creeper', 'Creepy Cuddler', 'Mutant Tortoises of Terror',
                        'Gregarious Geek', 'Lurking Llamas', 'Horrible Screaker Witch', 'Weeping Wonderboy', 'Boston Terrier of Terror',
                        'Courier of Danger',
                        'Mutant Mummer Zombie', 'Spasm Zombie', 'Scourge', 'Wolf-man Warg', 'Water Buffalo', 'Wham-a-Whama Rock Troll',
                        'Woodland Spirit', 'Wraith', 'Wyvern', 'Murder of Crows', 'Lion-Eagle Hybrid', 'Apiarian Phantom'])
        of = choice(['of', 'from'])
        # print('The {} {} {} {}'.format(adjectives, monsterr, of, place_names))
        long_name = 'the {} {} \n{} {}'.format(adjectives, monsterr, of, place_names)
        return (monsterr, long_name)

class Player:
    def __init__(self, health=100, gold=5, name='Zork', lvl=1, init_position=[12, 12]):
        self.position = init_position
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

def check_proximity(arg=2):

    for m in range(len(monsters)):
        if abs(monsters[m].position[0] - player.position[0]) < arg and arg > abs(
                    monsters[m].position[1] - map.get_index_from_bit(player.position[1])):
            this_monster[0] = m
            return True
    return False


def check_death(arg):
    return arg < 0

def game_over(win):
    if win:
        map.head[0] = 4
        m0 = monsters[this_monster[0]].position[0]
        m1 = monsters[this_monster[0]].position[1]
        new_row = map.maps[map.current_map[0]][map.current_map[1]][m0][:(m1 - 1) * 2]
        new_row += ' x'
        new_row += map.maps[map.current_map[0]][map.current_map[1]][m0][m1 * 2:]
        # map.message_key[1] = 'killedit'
        map.maps[map.current_map[0]][map.current_map[1]][m0] = new_row

        # determine which monster
        z = monsters.pop(this_monster[0])
        map.message_key[1] = 'killedit'
        generate_monster()
    else:
        LIVES[0] -= 1
        if LIVES[0] > 0:
            map.reincarnate(player, monsters)
        else:
            map.head[0] = 3
            map.header(player)
            quit()

def monster_attack(m):
    v = monsters[m].inventory[0]['damage'] - player.inventory[1]['block']
    player.health -= v
    if check_death(player.health):
        game_over(False)
    map.message_key[2] = 'dmg ' + str(monsters[m].inventory[0]['damage'])

########################################################################################################################

def player_attack(arg):
    print(arg)
    if arg == 'kill':
        monsters[this_monster[0]].health = monsters[this_monster[0]].health - (player.inventory[0]['damage'] * 10)
        map.head[0] = 2
    elif arg.lower() == 'zero':
        monsters[this_monster[0]].health = 0
        map.head[0] = 2
    elif arg.lower() == 'zork':
        monsters[this_monster[0]].health = monsters[this_monster[0]].health - (player.inventory[0]['damage'] * 90)
        map.head[0] = 2
    else:
        monsters[this_monster[0]].health -= int(player.inventory[0]['damage'] +
                                                (player.gold * .01))  - monsters[this_monster[0]].inventory[1]['block']
    if check_death(monsters[this_monster[0]].health):
        game_over(True)
    map.monster_go(player, monsters)
    map.mapit(player, monsters)

########################################################################
######################  SPELL BOOK  ####################################
########################################################################
def heal_self(arg='9'):
    print(arg)
    try:
        player.gold = player.gold - int(arg)
        player.health = player.health + int(arg)
    except:
        map.monster_go(player, monsters)

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

    elif spell[:6] == 'gold' and player.gold < 1000:
        player.gold += 1000
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

    elif spell == 'live' and player.gold > 1000:
        player.gold -= 1000
        LIVES[0] += 1
        # player_attack()

    else:
        if check_proximity():
            player_attack(spell)

########################################################################
###################### //SPELL BOOK  ###################################
########################################################################


print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("##     ESCAPE FROM PHILADELPHIA    ############### ")
print("################################################## ")
print("################################################## ")

how = input("@@#@#@@#@   How many monsters? >>> ")
if how.isalnum():
    many = int(how)
else:
    many = 3


# progression_template = (MonSteR(1), MonSteR(1), MonSteR(1), MonSteR(24), MonSteR(1), MonSteR(70))
monstrocity = []
for m in range(many):
    monstrocity.append(MonSteR(m+1))
monsters = monstrocity[:]




player = Player()

def get_player():
    return player

def get_monsters_fn():
    return monsters

map = Map(player, monsters, monster_attack, get_level, get_lives_func, get_monsters_fn, get_player)
map.mapit(player, monsters)

while True:
    command = input("Type Command: ( n s e w a(t)tack cast heal x:exit )\n>>> ")
    if command[:2] == 'at' or 't' == command[:1] or command[:1] == 'w' or ' ' == command[:1] or '' == command[:1]:
        if check_proximity():
            player_attack(command[command.find(" ") + 1:])
        else:
            map.move(0, player, monsters)

    elif command[:4] == 'cast' or 'c' == command[:1]:
        cast_spell(command[command.find(' ')+1:])
        map.head[0] = 1
        map.mapit( player, monsters)

    elif command[:4] == 'heal' or 'h' == command[:1]:
        if command.find(' ') > -1:
            heal_self(command[command.find(' '):])
        else:
            heal_self()
        map.head[0] = 0
        map.mapit( player, monsters)

    else:
        for i in range(len(command)):
            if command[i] == 'x':
                if input('      Are you sure you want to quit? (c) ') == 'c':
                    quit()
            elif command[i] == 'n' or '2' == command[i] or 'A' == command[i]:
                map.move(2, player, monsters)
            elif command[i] == 's' or '8' == command[i] or 'B' == command[i]:
                map.move(8, player, monsters)
            elif command[i] == 'e' or '6' == command[i] or 'C' == command[i]:
                map.move(6, player, monsters)
            elif command[i] == 'q' or '4' == command[i] or 'D' == command[i]:
                map.move(4, player, monsters)
            elif command[i] == '1':
                map.move(1, player, monsters)
            elif command[i] == '3':
                map.move(3, player, monsters)
            elif command[i] == '7' or 'a' == command[i]:
                map.move(7, player, monsters)
            elif command[i] == '9' or 'd' == command[i]:
                map.move(9, player, monsters)

