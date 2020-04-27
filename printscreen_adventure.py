#!/usr/local/bin/python3
# coding: utf-8

'''
# /\\\\\\\\    /\\ \\        /\\           /\         /\\\\\\\    /\\\\\\\\       
# /\\        /\\    /\\   /\\   /\\       /\ \\       /\\    /\\  /\\             
# /\\         /\\        /\\             /\  /\\      /\\    /\\  /\\             
# /\\\\\\       /\\      /\\            /\\   /\\     /\\\\\\\    /\\\\\\         
# /\\              /\\   /\\           /\\\\\\ /\\    /\\         /\\             
# /\\        /\\    /\\   /\\   /\\   /\\       /\\   /\\         /\\             
# /\\\\\\\\    /\\ \\       /\\\\    /\\         /\\  /\\         /\\\\\\\\       


# /\\\\\\\\  /\\\\\\\          /\\\\       /\\       /\\       
# /\\        /\\    /\\      /\\    /\\    /\ /\\   /\\\       
# /\\        /\\    /\\    /\\        /\\  /\\ /\\ / /\\       
# /\\\\\\    /\ /\\        /\\        /\\  /\\  /\\  /\\       
# /\\        /\\  /\\      /\\        /\\  /\\   /\  /\\       
# /\\        /\\    /\\      /\\     /\\   /\\       /\\       
# /\\        /\\      /\\      /\\\\       /\\       /\\       


# /\\\\\\\    /\\     /\\  /\\  /\\              /\         /\\\\\      /\\\\\\\\  /\\        /\\\\\\\    /\\     /\\  /\\        /\       
# /\\    /\\  /\\     /\\  /\\  /\\             /\ \\       /\\   /\\   /\\        /\\        /\\    /\\  /\\     /\\  /\\       /\ \\     
# /\\    /\\  /\\     /\\  /\\  /\\            /\  /\\      /\\    /\\  /\\        /\\        /\\    /\\  /\\     /\\  /\\      /\  /\\    
# /\\\\\\\    /\\\\\\ /\\  /\\  /\\           /\\   /\\     /\\    /\\  /\\\\\\    /\\        /\\\\\\\    /\\\\\\ /\\  /\\     /\\   /\\   
# /\\         /\\     /\\  /\\  /\\          /\\\\\\ /\\    /\\    /\\  /\\        /\\        /\\         /\\     /\\  /\\    /\\\\\\ /\\  
# /\\         /\\     /\\  /\\  /\\         /\\       /\\   /\\   /\\   /\\        /\\        /\\         /\\     /\\  /\\   /\\       /\\ 
# /\\         /\\     /\\  /\\  /\\\\\\\\  /\\         /\\  /\\\\\      /\\\\\\\\  /\\\\\\\\  /\\         /\\     /\\  /\\  /\\         /\\


#  written by Joseph Howard 2017 succinction@gmail.com   
'''

#   NEXT    
# ADD  SHIELD PICKUPS
#   ADD WALL SPELLS  :  REMOVE WALL, CREATE WALL
#      ADD MONSTERS FIGHT EACH OTHER   !

# Instruction screens before first frame
# magic spells released at certain levels (nixt)
# # done
# # Multiple monsters
# # magic cost gold.
# # Map
# # Monster
# # Player
# # SpellBook
## ESCAPE FROM PHILADELPHIA .PY #################################





from random import randrange, choice

########################################################################
########################################################################
########################################################################
########################################################################
'''
MMMMMMMM               MMMMMMMM                                     
M:::::::M             M:::::::M                                     
M::::::::M           M::::::::M                                     
M:::::::::M         M:::::::::M                                     
M::::::::::M       M::::::::::M  aaaaaaaaaaaaa  ppppp   ppppppppp   
M:::::::::::M     M:::::::::::M  a::::::::::::a p::::ppp:::::::::p  
M:::::::M::::M   M::::M:::::::M  aaaaaaaaa:::::ap:::::::::::::::::p 
M::::::M M::::M M::::M M::::::M           a::::app::::::ppppp::::::p
M::::::M  M::::M::::M  M::::::M    aaaaaaa:::::a p:::::p     p:::::p
M::::::M   M:::::::M   M::::::M  aa::::::::::::a p:::::p     p:::::p
M::::::M    M:::::M    M::::::M a::::aaaa::::::a p:::::p     p:::::p
M::::::M     MMMMM     M::::::Ma::::a    a:::::a p:::::p    p::::::p
M::::::M               M::::::Ma::::a    a:::::a p:::::ppppp:::::::p
M::::::M               M::::::Ma:::::aaaa::::::a p::::::::::::::::p 
M::::::M               M::::::M a::::::::::aa:::ap::::::::::::::pp  
MMMMMMMM               MMMMMMMM  aaaaaaaaaa  aaaap::::::pppppppp    
                                                 p:::::p            
                                                 p:::::p            
                                                p:::::::p           
                                                p:::::::p           
                                                p:::::::p           
                                                ppppppppp           
'''
class Map:
    '''
    METHODS:
        move(num)
        789
        406
        123
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
            mp.append(" # X x x x x x . . # . . . . . . . . # . . . . .")
            mp.append(" # x x ; ; x x # . # . . . . . # . . # . . . . .")
            mp.append(" # x X x . x x # . # . . . . . # . . # . . . . .")
            mp.append(" # . x x ; . x # . # . . . . . # . . # . . . . .")
            mp.append(" # X ; ; ; x . # . # . # # # # # . . # . . . . .")
            mp.append(" # . x x . . . # . . . # . . . # . # . . . . . .")
            mp.append(" # x x . # # # # . . . # . . . . . # . . . . . .")
            mp.append(" # . . . # . . # # . . # . . . . . # . . . . . .")
            mp.append(" # x x . # . . # # . . # . . . . . # . . . . . .")
            mp.append(" # . . . # . . . # # # # . . . . # . . . . . . .")
            mp.append(" # x . . # . . . # # . . . . . . # . . . . . . .")
            mp.append(" # . X . # . . . # # . . . . . . # . . . . . . .")
            mp.append(" # x x . # . . . . # . . . . . . # . . . . . . .")
            mp.append(" # x . x # . . . . # . . . . . . # . . . . . . .")
            mp.append(" # x . X # . . . . # . . . . . # . . . . . . . .")
            mp.append(" # # # # # . . . . # # # # # # # . . . . . . . .")
            mp.append(" # . . # . . . . . # . # . . . # . . . . . . . .")
            mp.append(" # . . # . . . . . . . # . . . # . . . . . . . .")
            mp.append(" # . . # . . . . . # . # . . . # . . . . .#. . .")
            mp.append(" # . . # . . . # . . . # . . . # . # . . . . . .")
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")
            mp.append(" # . . # . . . # . . . # . . . # . # . . . . . .")
            mp.append(" # . . # . . . . . # . # . . . # . . . . .#. . .")#
        if x == 3:
            mp = []
            mp.append(" # . . # . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . x # . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . x # . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . x # . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . . # . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . . # . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . # # # # # # # # # # # # # . # # . . . . . .")
            mp.append(" # . # x . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . # . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . # . . . . # . . . . . . . . . # # # . # # .")
            mp.append(" # . # . . . . # . . . . . . . . . # x . . . . .")
            mp.append(" # . # . . . . # . . . . . . . . . . . ; * ; ; .")
            mp.append(" # . # . . . . # . . . . . . . . . # x ; * ; ; .")
            mp.append(" # . # . . . . . . . . . * * . . . # x ; * ; ; .")
            mp.append(" # . # . . . . # . . . . * * . . . # x * * * * .")
            mp.append(" # . # . . . . # . . . . . . . . . # x * * * * .")
            mp.append(" # . # . . . . # . . . . . . . . . # x * * * * .")
            mp.append(" # . # . # # # # . . . . . . . . . # x * * * * .")
            mp.append(" # . # . . . . # . . . . . . . . . # x * * * * .")
            mp.append(" # . # . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # . # # . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . . # . . . . . . . . . . . . . . . . . . . .")

        elif x == 6:
            mp = []
            mp.append(" # . # . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # x # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # x # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # . # . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # . # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # x # . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . # . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # x # . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" # . # . . . . . . # . . . . . . . . . . . . . .")
            mp.append(" # # # # # # # # # # # # # # # . # # . . . . . .")
            mp.append(" # . . . . . . # . . . . . . . . . # # # . # # .")
            mp.append(" # . . . . . . # . . # . . . . . . # . . . . . .")
            mp.append(" # . . . . . . # . . # . . . . . . # . ; * ; ; .")
            mp.append(" # . . . . . . # . . # . . . . . . # . ; * ; ; .")
            mp.append(" # . . . . . . . . . # . X X . . . # . ; * ; ; .")
            mp.append(" # . . . . . . # . . # . X X . . . # . * * * * .")
            mp.append(" # . . x . . . # . . # . . . . . . # . * * * * .")
            mp.append(" # . . . . . . # . . # . . . . . . ; . * * * * .")
            mp.append(" # # # . # # # # . . . . . . . . . # . * * * * .")
            mp.append(" # . . . . . . # . . . . . . . . . # . * * * * .")
            mp.append(" # . . . . . . # # # # # # # # # # # . * * * * .")
            mp.append(" # . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")

        if x == 1:
            mp = []
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")
            mp.append(" . . . . . . . . . . x . . x . . . . . . . . . .")
            mp.append(" . . . . x . x . x . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . x x . . . . . . . .")
            mp.append(" . x . x . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . # # # # # # # # # # # # # # # # # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . # . . . . .")
            mp.append(" . . . . . . . . . . . x . x . X . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . x . X . # . . . . . .")
            mp.append(" . . . . . . . . . . . . x . . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # # # # # . . . . . .")
            mp.append(" . . . . . . . . . . . x . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")

        if x == 4:
            mp = []
            mp.append(" . . . . . . . . . . . . . # . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # . x . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # . x . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . # # # # # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . # . # # # . # # # . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . . . . . . . .")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . . . . . . . . . . . # . . . . . .")
            mp.append(" . . . . . . . # . # # # # # # # . # . . . . # #")
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
            mp.append(" . . . . . . . # . . . . . . . . . # # # # # # #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . # . . . . . . . . . # . ; * ; ; #")
            mp.append(" . . . . . . . # . . . . . . . . . # . ; * ; ; #")
            mp.append(" . . . . . . . . . . . . . . . . . # . ; * ; ; #")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * #")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * #")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * #")
            mp.append(" # # # # # # # # . . . . . . . . . # . * * * * #")
            mp.append(" . . . . . . . # . . . . . . . . . # . * * * * #")
            mp.append(" . . . . . . . # # # # # # # # # # # X * * * * #")
            mp.append(" . . . . . . . # . . . . . . . . . # X X X X X .")
            mp.append(" . . . . . . . # . . . . . . . . . # # # # # # #")
            mp.append(" . . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")

        if x == 2:
            mp = []
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")
            mp.append(" . . . . . . . . . . . . . . . x . . x . . , X #")
            mp.append(" . . . . . . . x . . . x . . . . . . . . . , , #")
            mp.append(" . . . . . . . . . . . . . . . . x . . . . , . #")
            mp.append(" . . . . . . . . x . . . . . . . . . . . . , . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . x . . #")
            mp.append(" . # # # # # # # # # # # # # # # # # . . . . . #")
            mp.append(" . . . . . . . . . . . . ; ; ; ; ; ; # . . . . #")
            mp.append(" . . . . . . . . . . . # . # ; ; ; # . . . . . #")
            mp.append(" . . . . . . . . . . . . . # ; ; ; # . . . . . #")
            mp.append(" . . . . . . . . . ; ; . # . ; ; X # . . . . . #")
            mp.append(" . . . . . . . . # . # x . # # # # # . . . . . #")
            mp.append(" . . . . . . . . . x # # . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . # x . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . # . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . # . . . . . . . . . # # # # # #")
            mp.append(" . . . . . . . . . . . . . . . . . . # X X X X #")
            mp.append(" . . . . . . . . . . . . . . . . . . # X X X X #")
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" # # # # # # # # # # # # # # # # # # # # # # # #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")

        if x == 5:
            mp = []
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . # . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . # . . . x . . . . . . . . . . . . . . . . . #")
            mp.append(" . # . . . . . x . x . . . . . . . . . . . . . #")
            mp.append(" . # . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . . . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . # # # # # . # # # # . . . . . . . . . . . . #")
            mp.append(" . # . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . # . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . # . . . x . . . . . . . . . . . . . . . . X #")
            mp.append(" . # . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . # . . . . x . . . . . . . . . . . . . . . . #")
            mp.append(" . # . . . . . . . x . . . . . . . . . . . . . #")
            mp.append(" . # . . . . . . . . . . . . . . . . . . . . . #")
            mp.append(" . # . . . . . x . . . . . . . . . . . . . . . #")
            mp.append(" . # # # # # # # # # . . . . . . . . . . . . . #")
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
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" # . . . . . . . . # . . . . . . . . . . . . . #")
            mp.append(" # . . . . . . # . . . . . . . . . # . . . . . #")
            mp.append(" . # . . . . . # # # # # # # # # # # . . . . . #")
            mp.append(" # . . . . . . # # # # # # # # # # # . . . . . #")
            mp.append(" # . . . . . . # . . . . . . . . . # . . X . . #")
            mp.append(" # . . . . . . # . . . . . . # . . # # # # # # #")
            mp.append(" # . . . . . . # . . . . . . # . . # # # # # # #")
            mp.append(" # . . . . . . # . . . . . . # X . # . x x x x #")
            mp.append(" # . . . . . . # . . . . . . # X . # . x x x x #")
            mp.append(" # . . . . . . # # # # # # . # # # # . x x x x #")
            mp.append(" # . . . . . . # . . . . . . # X . # . x x x x #")
            mp.append(" # . . * * * * # . . . . . . # . . # . x x x x #")
            mp.append(" # . . * * * * # . . . . . . # . . # . x x x x #")
            mp.append(" # . . * * * * # . . . . . . . . . # . x x x x #")
            mp.append(" # # # # # # # # . . . . . . . . . # . x x x x #")
            mp.append(" . . . . # . . # . . . . . . # X . # . x x x x #")
            mp.append(" . . . . # . . # . . . . . . # X . # . x x x x #")
            mp.append(" . . X X # . . # # # # # . # # # # # . * * * * #")
            mp.append(" . . . . # . . . . . . . . . . . . . . . . . . #")
            mp.append(" # # # # # . # # # # # # # # # # # # # # # # # #")

        return mp

# ####################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#####################################
# ####################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#####################################
# ####################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#####################################
    def reincarnate(self, player, monsters):
        """FOR WHEN PLAYER DIES BUT HAS MORE LIVES"""

        print("Killed by level {} {}.    Don't forget to heal!".format(monsters[self.this_monster[0]].level,
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
        print("################ !!!!YOU DIED!!!! ################ ")
        print("################ !!!!YOU DIED!!!! ################ ")
        print("################ !!!!YOU DIED!!!! ################ ")
        print("################ !!!!YOU DIED!!!! ################ ")
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
        self.hud(player, 0)
        verdict = input('Reincarnate? ( any key or (n)o ) : ')
        if verdict.lower() == 'n':
            quit()
        player.health = 100
        player.position[0] = 12
        player.position[1] = 12
        self.head[0] = 5
        self.mapit(player, monsters)
        #


#                                                  .x+=:.        s                                                                  
#                                                 z`    ^%      :8                                                                  
#    ..    .     :           u.      u.    u.        .   <k    .88                  .u    .                                    u.   
#  .888: x888  x888.   ...ue888b   x@88k u@88c.    .@8Ned8"   :888ooo      .u     .d88B :@8c                     uL      ...ue888b  
# ~`8888~'888X`?888f`  888R Y888r ^"8888""8888"  .@^%8888"  -*8888888   ud8888.  ="8888f8888r                .ue888Nc..  888R Y888r 
#   X888  888X '888>   888R I888>   8888  888R  x88:  `)8b.   8888    :888'8888.   4888>'88"                d88E`"888E`  888R I888> 
#   X888  888X '888>   888R I888>   8888  888R  8888N=*8888   8888    d888 '88%"   4888> '                  888E  888E   888R I888> 
#   X888  888X '888>   888R I888>   8888  888R   %8"    R88   8888    8888.+"      4888>                    888E  888E   888R I888> 
#   X888  888X '888>  u8888cJ888    8888  888R    @8Wou 9%   .8888Lu= 8888L       .d888L .+                 888E  888E  u8888cJ888  
#  "*88%""*88" '888!`  "*888*P"    "*88*" 8888" .888888P`    ^%888*   '8888c. .+  ^"8888*"                  888& .888E   "*888*P"   
#    `~    "    `"`      'Y"         ""   'Y"   `   ^"F        'Y"     "88888%       "Y"                    *888" 888&     'Y"      
#                                                                        "YP'                                `"   "888E             
#                                                                                                           .dWi   `88E             
#                                                                                             8888888888888 4888~  J8%              
#                                                                                                            ^"===*"`               

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


        # '''
        # 	                                                                                 tttt
        #                                                                                   ttt:::t
        #                                                                                   t:::::t
        #                                                                                   t:::::t
        #    mmmmmmm    mmmmmmm      ooooooooooo   nnnn  nnnnnnnn        ssssssssss   ttttttt:::::ttttttt        eeeeeeeeeeee    rrrrr   rrrrrrrrr
        #  mm:::::::m  m:::::::mm  oo:::::::::::oo n:::nn::::::::nn    ss::::::::::s  t:::::::::::::::::t      ee::::::::::::ee  r::::rrr:::::::::r
        # m::::::::::mm::::::::::mo:::::::::::::::on::::::::::::::nn ss:::::::::::::s t:::::::::::::::::t     e::::::eeeee:::::eer:::::::::::::::::r
        # m::::::::::::::::::::::mo:::::ooooo:::::onn:::::::::::::::ns::::::ssss:::::stttttt:::::::tttttt    e::::::e     e:::::err::::::rrrrr::::::r
        # m:::::mmm::::::mmm:::::mo::::o     o::::o  n:::::nnnn:::::n s:::::s  ssssss       t:::::t          e:::::::eeeee::::::e r:::::r     r:::::r
        # m::::m   m::::m   m::::mo::::o     o::::o  n::::n    n::::n   s::::::s            t:::::t          e:::::::::::::::::e  r:::::r     rrrrrrr
        # m::::m   m::::m   m::::mo::::o     o::::o  n::::n    n::::n      s::::::s         t:::::t          e::::::eeeeeeeeeee   r:::::r
        # m::::m   m::::m   m::::mo::::o     o::::o  n::::n    n::::nssssss   s:::::s       t:::::t    tttttte:::::::e            r:::::r
        # m::::m   m::::m   m::::mo:::::ooooo:::::o  n::::n    n::::ns:::::ssss::::::s      t::::::tttt:::::te::::::::e           r:::::r
        # m::::m   m::::m   m::::mo:::::::::::::::o  n::::n    n::::ns::::::::::::::s       tt::::::::::::::t e::::::::eeeeeeee   r:::::r
        # m::::m   m::::m   m::::m oo:::::::::::oo   n::::n    n::::n s:::::::::::ss          tt:::::::::::tt  ee:::::::::::::e   r:::::r
        # mmmmmm   mmmmmm   mmmmmm   ooooooooooo     nnnnnn    nnnnnn  sssssssssss              ttttttttttt      eeeeeeeeeeeeee   rrrrrrr

        #                            mmmmmmm    mmmmmmm      ooooooooooo vvvvvvv           vvvvvvv eeeeeeeeeeee
        #                          mm:::::::m  m:::::::mm  oo:::::::::::oov:::::v         v:::::vee::::::::::::ee
        #                         m::::::::::mm::::::::::mo:::::::::::::::ov:::::v       v:::::ve::::::eeeee:::::ee
        #                         m::::::::::::::::::::::mo:::::ooooo:::::o v:::::v     v:::::ve::::::e     e:::::e
        #                         m:::::mmm::::::mmm:::::mo::::o     o::::o  v:::::v   v:::::v e:::::::eeeee::::::e
        #                         m::::m   m::::m   m::::mo::::o     o::::o   v:::::v v:::::v  e:::::::::::::::::e
        #                         m::::m   m::::m   m::::mo::::o     o::::o    v:::::v:::::v   e::::::eeeeeeeeeee
        #                         m::::m   m::::m   m::::mo::::o     o::::o     v:::::::::v    e:::::::e
        #                         m::::m   m::::m   m::::mo:::::ooooo:::::o      v:::::::v     e::::::::e
        #                         m::::m   m::::m   m::::mo:::::::::::::::o       v:::::v       e::::::::eeeeeeee
        #                         m::::m   m::::m   m::::m oo:::::::::::oo         v:::v         ee:::::::::::::e
        #                         mmmmmm   mmmmmm   mmmmmm   ooooooooooo            vvv            eeeeeeeeeeeeee
        # ________________________
        # _::::::::::::::::::::::_
        # ________________________
        # '''
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
            print('') 
            you_have_no_choice = input("    RETURN TO PHILADELPHIA ? >>>")
            # MAP 1:1
            # PLAYER POSITION 12,12
            # mapit
            player = self.get_player()

            self.current_map[0] = 1
            self.current_map[1] = 1
            self.player.position[0] = 12
            self.player.position[1] = 12
            self.player.gold += self.player.gold * 3
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

        # '''
        #    mmmmmmm    mmmmmmm       eeeeeeeeeeee        ssssssssss       ssssssssss     aaaaaaaaaaaaa     ggggggggg   ggggg    eeeeeeeeeeee
        #  mm:::::::m  m:::::::mm   ee::::::::::::ee    ss::::::::::s    ss::::::::::s    a::::::::::::a   g:::::::::ggg::::g  ee::::::::::::ee
        # m::::::::::mm::::::::::m e::::::eeeee:::::eess:::::::::::::s ss:::::::::::::s   aaaaaaaaa:::::a g:::::::::::::::::g e::::::eeeee:::::ee
        # m::::::::::::::::::::::me::::::e     e:::::es::::::ssss:::::ss::::::ssss:::::s           a::::ag::::::ggggg::::::gge::::::e     e:::::e
        # m:::::mmm::::::mmm:::::me:::::::eeeee::::::e s:::::s  ssssss  s:::::s  ssssss     aaaaaaa:::::ag:::::g     g:::::g e:::::::eeeee::::::e
        # m::::m   m::::m   m::::me:::::::::::::::::e    s::::::s         s::::::s        aa::::::::::::ag:::::g     g:::::g e:::::::::::::::::e
        # m::::m   m::::m   m::::me::::::eeeeeeeeeee        s::::::s         s::::::s    a::::aaaa::::::ag:::::g     g:::::g e::::::eeeeeeeeeee
        # m::::m   m::::m   m::::me:::::::e           ssssss   s:::::s ssssss   s:::::s a::::a    a:::::ag::::::g    g:::::g e:::::::e
        # m::::m   m::::m   m::::me::::::::e          s:::::ssss::::::ss:::::ssss::::::sa::::a    a:::::ag:::::::ggggg:::::g e::::::::e
        # m::::m   m::::m   m::::m e::::::::eeeeeeee  s::::::::::::::s s::::::::::::::s a:::::aaaa::::::a g::::::::::::::::g  e::::::::eeeeeeee
        # m::::m   m::::m   m::::m  ee:::::::::::::e   s:::::::::::ss   s:::::::::::ss   a::::::::::aa:::a gg::::::::::::::g   ee:::::::::::::e
        # mmmmmm   mmmmmm   mmmmmm    eeeeeeeeeeeeee    sssssssssss      sssssssssss      aaaaaaaaaa  aaaa   gggggggg::::::g     eeeeeeeeeeeeee
        #                                                                                                            g:::::g
        #                                                                                                gggggg      g:::::g
        #                                                                                                g:::::gg   gg:::::g
        #                                                                                                 g::::::ggg:::::::g
        #                                                                                                  gg:::::::::::::g
        #                                                                                                    ggg::::::ggg
        #                                                                                                       gggggg
        # '''

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

                   'm1': '{} Lvl.{} {} with {}({}) HP:{} '
                       .format(self.get_monsters()[self.this_monster[0]].avatar, self.get_monsters()[self.this_monster[0]].level,
                               self.get_monsters()[self.this_monster[0]].type.title(),
                               self.get_monsters()[self.this_monster[0]].inventory[0]['name'],
                               self.get_monsters()[self.this_monster[0]].inventory[0]['damage'],
                               self.get_monsters()[self.this_monster[0]].health,
                               ),

                   '.': 'Nothing to say.',
                   '': '',

                   # THIS IS NOT WORKING:
                   'killedit': 'You have slain the monster!',

                   'looted': 'You have looted the corpse',
                   'dmg': '-'

               }[x] + additional

    '''
hhhhhhh                                           d::::::d
h:::::h                                           d::::::d
h:::::h                                           d::::::d
h:::::h                                           d:::::d 
 h::::h hhhhh       uuuuuu    uuuuuu      ddddddddd:::::d 
 h::::hh:::::hhh    u::::u    u::::u    dd::::::::::::::d 
 h::::::::::::::hh  u::::u    u::::u   d::::::::::::::::d 
 h:::::::hhh::::::h u::::u    u::::u  d:::::::ddddd:::::d 
 h::::::h   h::::::hu::::u    u::::u  d::::::d    d:::::d 
 h:::::h     h:::::hu::::u    u::::u  d:::::d     d:::::d 
 h:::::h     h:::::hu::::u    u::::u  d:::::d     d:::::d 
 h:::::h     h:::::hu:::::uuuu:::::u  d:::::d     d:::::d 
 h:::::h     h:::::hu:::::::::::::::uud::::::ddddd::::::dd
 h:::::h     h:::::h u:::::::::::::::u d:::::::::::::::::d
 h:::::h     h:::::h  uu::::::::uu:::u  d:::::::::ddd::::d
 hhhhhhh     hhhhhhh    uuuuuuuu  uuuu   ddddddddd   ddddd
    '''
    def hud(self, player, damage=0):
        '''HEADS UP DISPLAY : TEN LINES X48 CHARACTERS

        '''
        # print("################################################# ")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
        print("You are:  {}   x: {} y: {}   Level: {}  Lives: {}   ".format(player.avatar, player.position[1], player.position[0], self.level_fn(), self.get_lives()))

        self.frame_i[0] += 1
        # print('@@@@@@ Frame # {}  Level # {}   Lives : {} '.format(self.frame_i[0], self.level_fn(), self.get_lives()))
        print("LEFT : {} {}  HEALTH: {} {}".format(player.inventory[0]['name'], player.inventory[0]['damage'],
                                                    player.health,
                                                    self.message(self.message_key[2][:3],
                                                                 self.message_key[2][self.message_key[2].find(' '):])))


        print("RIGHT: {}({})    GOLD  : {} ".format(player.inventory[1]['name'], player.inventory[1]['block'],
                                                    player.gold))
        # print(":POTION ^(f)                  (r)^ STAFF:")

        damage_report = "(-{})".format(damage) if damage > 0 else ""
        print(self.message(self.message_key[1]), self.message(self.message_key[0]), damage_report)

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
            '': ''
        }[X]

# '''
# hhhhhhh                                                            d::::::d                                        
# h:::::h                                                            d::::::d                                        
# h:::::h                                                            d::::::d                                        
# h:::::h                                                            d:::::d                                         
#  h::::h hhhhh           eeeeeeeeeeee    aaaaaaaaaaaaa      ddddddddd:::::d     eeeeeeeeeeee    rrrrr   rrrrrrrrr   
#  h::::hh:::::hhh      ee::::::::::::ee  a::::::::::::a   dd::::::::::::::d   ee::::::::::::ee  r::::rrr:::::::::r  
#  h::::::::::::::hh   e::::::eeeee:::::eeaaaaaaaaa:::::a d::::::::::::::::d  e::::::eeeee:::::eer:::::::::::::::::r 
#  h:::::::hhh::::::h e::::::e     e:::::e         a::::ad:::::::ddddd:::::d e::::::e     e:::::err::::::rrrrr::::::r
#  h::::::h   h::::::he:::::::eeeee::::::e  aaaaaaa:::::ad::::::d    d:::::d e:::::::eeeee::::::e r:::::r     r:::::r
#  h:::::h     h:::::he:::::::::::::::::e aa::::::::::::ad:::::d     d:::::d e:::::::::::::::::e  r:::::r     rrrrrrr
#  h:::::h     h:::::he::::::eeeeeeeeeee a::::aaaa::::::ad:::::d     d:::::d e::::::eeeeeeeeeee   r:::::r            
#  h:::::h     h:::::he:::::::e         a::::a    a:::::ad:::::d     d:::::d e:::::::e            r:::::r            
#  h:::::h     h:::::he::::::::e        a::::a    a:::::ad::::::ddddd::::::dde::::::::e           r:::::r            
#  h:::::h     h:::::h e::::::::eeeeeeeea:::::aaaa::::::a d:::::::::::::::::d e::::::::eeeeeeee   r:::::r            
#  h:::::h     h:::::h  ee:::::::::::::e a::::::::::aa:::a d:::::::::ddd::::d  ee:::::::::::::e   r:::::r            
#  hhhhhhh     hhhhhhh    eeeeeeeeeeeeee  aaaaaaaaaa  aaaa  ddddddddd   ddddd    eeeeeeeeeeeeee   rrrrrrr            
# '''
    def header(self, player={}):
        '''PRINTS HEADER'''
        # print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        print(self.story_line(self.message_key[3]))
# MOVE TO HUD
        # self.frame_i[0] += 1
        print('Frame # {}  Level # {}   Lives : {} '.format(self.frame_i[0], self.level_fn(), self.get_lives()))

        if self.head[0] == 0:
            print("Confront " + self.get_monsters()[self.this_monster[0]].long_description)
            print("########################################:  w  | 789")
            print("##     ESCAPE FROM PHILADELPHIA    ###### a*d | 4*6")
            print("#########################################  s  | 123")
            print("@@@@@@@@@@@@@@@@@@@@@ MAP{}:{} @@@@@@@@@@@@@@@@@@@@@@ ".format(self.current_map[0],
                                                                                 self.current_map[1]))
        elif self.head[0] == 1:
            print("################################################## ")
            print("################# A SPELL IS CAST ################ ")
            print("################################################## ")
        elif self.head[0] == 2:
            print("Fighting " + self.get_monsters()[self.this_monster[0]].long_description)
            print("################################################## ")
            print("################ MONSTER ATTACKED ################ ")
            print("################################################## ")
        elif self.head[0] == 3:

            print("Killed by level {} {}.  Don't forget to heal!".format(self.get_monsters()[0].level, self.get_monsters()[0].type))
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
            print("################ !!!!YOU DIED!!!! ################ ")
            print("################ !!!!YOU DIED!!!! ################ ")
            print("################ !!!!YOU DIED!!!! ################ ")
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
            self.hud(player, 0)

        elif self.head[0] == 4:
            print("################################################## ")
            print("############### !!!! YOU WON !!!! ################ ")
            print("################################################## ")
        elif self.head[0] == 5:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
            print("######## !! YOU HAVE BEEN REINCARNATED !! ######## ")
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")

    '''
+--- doh        
                                                               iiii          tttt          
                                                              i::::i      ttt:::t          
                                                               iiii       t:::::t          
                                                                          t:::::t          
   mmmmmmm    mmmmmmm     aaaaaaaaaaaaa  ppppp   ppppppppp   iiiiiiittttttt:::::ttttttt    
 mm:::::::m  m:::::::mm   a::::::::::::a p::::ppp:::::::::p  i:::::it:::::::::::::::::t    
m::::::::::mm::::::::::m  aaaaaaaaa:::::ap:::::::::::::::::p  i::::it:::::::::::::::::t    
m::::::::::::::::::::::m           a::::app::::::ppppp::::::p i::::itttttt:::::::tttttt    
m:::::mmm::::::mmm:::::m    aaaaaaa:::::a p:::::p     p:::::p i::::i      t:::::t          
m::::m   m::::m   m::::m  aa::::::::::::a p:::::p     p:::::p i::::i      t:::::t          
m::::m   m::::m   m::::m a::::aaaa::::::a p:::::p     p:::::p i::::i      t:::::t          
m::::m   m::::m   m::::ma::::a    a:::::a p:::::p    p::::::p i::::i      t:::::t    tttttt
m::::m   m::::m   m::::ma::::a    a:::::a p:::::ppppp:::::::pi::::::i     t::::::tttt:::::t
m::::m   m::::m   m::::ma:::::aaaa::::::a p::::::::::::::::p i::::::i     tt::::::::::::::t
m::::m   m::::m   m::::m a::::::::::aa:::ap::::::::::::::pp  i::::::i       tt:::::::::::tt
mmmmmm   mmmmmm   mmmmmm  aaaaaaaaaa  aaaap::::::pppppppp    iiiiiiii         ttttttttttt  
                                          p:::::p                                          
                                          p:::::p                                          
                                         p:::::::p                                         
                                         p:::::::p                                         
                                         p:::::::p                                         
                                         ppppppppp                                         
    '''
    def mapit(self, player, monsters, damage=0, b=''):
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
            player.gold += 3000
            player.health += 999
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
        self.hud(player, damage)

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


# '''
#    mmmmmmm    mmmmmmm      ooooooooooo vvvvvvv           vvvvvvv eeeeeeeeeeee    
#  mm:::::::m  m:::::::mm  oo:::::::::::oov:::::v         v:::::vee::::::::::::ee  
# m::::::::::mm::::::::::mo:::::::::::::::ov:::::v       v:::::ve::::::eeeee:::::ee
# m::::::::::::::::::::::mo:::::ooooo:::::o v:::::v     v:::::ve::::::e     e:::::e
# m:::::mmm::::::mmm:::::mo::::o     o::::o  v:::::v   v:::::v e:::::::eeeee::::::e
# m::::m   m::::m   m::::mo::::o     o::::o   v:::::v v:::::v  e:::::::::::::::::e 
# m::::m   m::::m   m::::mo::::o     o::::o    v:::::v:::::v   e::::::eeeeeeeeeee  
# m::::m   m::::m   m::::mo::::o     o::::o     v:::::::::v    e:::::::e           
# m::::m   m::::m   m::::mo:::::ooooo:::::o      v:::::::v     e::::::::e          
# m::::m   m::::m   m::::mo:::::::::::::::o       v:::::v       e::::::::eeeeeeee  
# m::::m   m::::m   m::::m oo:::::::::::oo         v:::v         ee:::::::::::::e  
# mmmmmm   mmmmmm   mmmmmm   ooooooooooo            vvv            eeeeeeeeeeeeee  
# '''
    def move(self, arg, player, monsters):
        ''' RECEIVE INPUT : CALLED EXTERNALLY
        map.move(number)
        789   123 ###
        406   406
        123   789 ###
        RETURNS RESULTING EVENT:
        SUCCESS, FAIL=HIT WALL
        '''
        # INSERT CONDITIONALS FOR WALL ENCOUNTERS
        print("move arg: ", arg)
        temp_y0 = player.position[0]
        temp_x1 = self.get_index_from_bit(player.position[1])

        if arg == 8:  # 'n'
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

        elif arg == 2:
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

        elif arg == 7:  # 'nw' | '1' :
            if player.position[0] > 0:
                temp_y0 += -1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed(terr):
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

        elif arg == 9:  # 'ne' | '3' :
            if player.position[0] > 0:
                temp_y0 += -1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed(terr):
                    player.position[0] = player.position[0] - 1
            if player.position[1] > 1:
                temp_x1 += 1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed(terr):
                    player.position[1] = player.position[1] + 1
                    # move(3)

        elif arg == 1:  # 'sw' | '7' :
            if player.position[0] < 23:
                temp_y0 += 1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed(terr):
                    player.position[0] = player.position[0] + 1
            if player.position[1] > 1:
                temp_x1 += -1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed(terr):
                    player.position[1] = player.position[1] - 1


            # if player.position[0] < 24 and player.position[1] < 24:
            #     temp_y0 += 1
            #     temp_x1 += -1
            #     terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
            #            (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
            #     if self.unobstructed(terr):
            #         player.position[0] = player.position[0] + 1
            #         player.position[1] = player.position[1] - 1
                    # if player.position[1] < 24:
                    #     temp_y0 += 1
                    #     temp_x1 += -1
                    #     terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                    #            (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                    #     if self.unobstructed(terr):
                    # move(7)

        elif arg == 3:  # 'se' | '9' :
            if player.position[0] < 23:
                temp_y0 += 1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed(terr):
                    player.position[0] = player.position[0] + 1
            if player.position[1] > 1:
                temp_x1 += 1
                terr = self.maps[self.current_map[0]][self.current_map[1]][temp_y0][
                       (temp_x1 - 1) * 2: ((temp_x1 - 1) * 2) + 2]
                if self.unobstructed(terr):
                    player.position[1] = player.position[1] + 1
                    # move(9)

        self.monster_go(player, monsters)
        # header(0)
        self.mapit(player, monsters)

'''
MMMMMMMM               MMMMMMMM                                      SSSSSSSSSSSSSSS      tttt                            RRRRRRRRRRRRRRRRR   
M:::::::M             M:::::::M                                    SS:::::::::::::::S  ttt:::t                            R::::::::::::::::R  
M::::::::M           M::::::::M                                   S:::::SSSSSS::::::S  t:::::t                            R::::::RRRRRR:::::R 
M:::::::::M         M:::::::::M                                   S:::::S     SSSSSSS  t:::::t                            RR:::::R     R:::::R
M::::::::::M       M::::::::::M   ooooooooooo   nnnn  nnnnnnnn    S:::::S        ttttttt:::::ttttttt        eeeeeeeeeeee    R::::R     R:::::R
M:::::::::::M     M:::::::::::M oo:::::::::::oo n:::nn::::::::nn  S:::::S        t:::::::::::::::::t      ee::::::::::::ee  R::::R     R:::::R
M:::::::M::::M   M::::M:::::::Mo:::::::::::::::on::::::::::::::nn  S::::SSSS     t:::::::::::::::::t     e::::::eeeee:::::eeR::::RRRRRR:::::R 
M::::::M M::::M M::::M M::::::Mo:::::ooooo:::::onn:::::::::::::::n  SS::::::SSSSStttttt:::::::tttttt    e::::::e     e:::::eR:::::::::::::RR  
M::::::M  M::::M::::M  M::::::Mo::::o     o::::o  n:::::nnnn:::::n    SSS::::::::SS    t:::::t          e:::::::eeeee::::::eR::::RRRRRR:::::R 
M::::::M   M:::::::M   M::::::Mo::::o     o::::o  n::::n    n::::n       SSSSSS::::S   t:::::t          e:::::::::::::::::e R::::R     R:::::R
M::::::M    M:::::M    M::::::Mo::::o     o::::o  n::::n    n::::n            S:::::S  t:::::t          e::::::eeeeeeeeeee  R::::R     R:::::R
M::::::M     MMMMM     M::::::Mo::::o     o::::o  n::::n    n::::n            S:::::S  t:::::t    tttttte:::::::e           R::::R     R:::::R
M::::::M               M::::::Mo:::::ooooo:::::o  n::::n    n::::nSSSSSSS     S:::::S  t::::::tttt:::::te::::::::e        RR:::::R     R:::::R
M::::::M               M::::::Mo:::::::::::::::o  n::::n    n::::nS::::::SSSSSS:::::S  tt::::::::::::::t e::::::::eeeeeeeeR::::::R     R:::::R
M::::::M               M::::::M oo:::::::::::oo   n::::n    n::::nS:::::::::::::::SS     tt:::::::::::tt  ee:::::::::::::eR::::::R     R:::::R
MMMMMMMM               MMMMMMMM   ooooooooooo     nnnnnn    nnnnnn SSSSSSSSSSSSSSS         ttttttttttt      eeeeeeeeeeeeeeRRRRRRRR     RRRRRRR
'''
class MonSteR:
    # class MonSteR:
    def __init__(self, lvl):
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
        self.inventory = [
            {'type': 'weapon',
             'name': self.w_name(),
             'damage': 10 * self.level + 5},
            {'type': 'shield',
             'name': 'Shield',
             'block': 5 + (self.health / 50)}]

    def m_type(self):
        name = self.named()

        return [

            # enumerated
            (name[0], " 1", ".,•º*.  xXX", name[1]),
            (name[0], " 2", ". ,•º∞*  xXX", name[1]),
            (name[0], " 3", ".,•º*::  xXX", name[1]),
            (name[0], " 4", ",º∞# .* xXX", name[1]),
            (name[0], " 5", ".,*;  xXX", name[1]),
            (name[0], " 6", ".•*;  xXX", name[1]),
            (name[0], " 7", "  .. ,•º;.  xXX", name[1]),
            (name[0], " 8", ".,•º* .;  xXX", name[1]),
            (name[0], " 9", ".,•º∞*: .  xXX", name[1]),
            (name[0], " 0", ".,•º∞*:  xXX", name[1]),
            (name[0], " @", ".,•º*:x .  xXX", name[1]),

            # 2017
            # (name[0], " §", ".,•º*.  xXX", name[1]),
            # (name[0], " £", ". ,•º∞*  xXX", name[1]),
            # (name[0], " §", ".,•º*::  xXX", name[1]),
            # (name[0], " π", ",º∞# .* xXX", name[1]),
            # (name[0], " £", ".,*;  xXX", name[1]),
            # (name[0], " ¥", ".•*;  xXX", name[1]),
            # (name[0], " @", "  .. ,•º;.  xXX", name[1]),
            # (name[0], " ∫", ".,•º* .;  xXX", name[1]),
            # (name[0], " £", ".,•º∞*: .  xXX", name[1]),
            # (name[0], " ƒ", ".,•º∞*:  xXX", name[1]),
            # (name[0], " §", ".,•º*: .  xXX", name[1]),

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
                             'bothersome', 'troublesome', 'irritating', 'troublesome', 'vexing', 'exasperating',
                             'rebarbative incommodious',
                             'remote', 'vexatious', 'ambitious', 'demanding', 'difficile', 'exacting',
                             'wearisome', 'formidable', 'galling', 'onerous', 'operose', 'painful', 'problematic',
                             'prohibitive', 'rigid', 'severe', 'strenuous', 'titanic', 'toilsome', 'tough', 'trying',
                             'unyielding',
                             'burdensome', 'challenging', 'crucial', 'gargantuan', 'heavy', 'herculean', 'immense',
                             'irritating',
                             'labored', 'laborious'])

        place_names = choice(['Frankfurter Ave.', 'the Passyunk Warrior Clan', 'the Philly Cheesesteak Factory',
                              'Manayunk Railroad Yard', 'Skidoo Water Park Palace', 'Dunks Ferry Playground',
                              'Pigeons\' Gauntlet',
                              'the Inauspicious Tower of Dread \nat Mario Lanza Boulevard', 'the Dungeon at Dicks Ave.',
                              'the Reading Terminal Market Book Club', 'the Stronghold of Doom at \nLongwood Gardens',
                              'the cave under the Philadelphia Zoo', 'the dreaded Eastern State Penitentiary',
                              'the depressing, perenial dissapointment \nknown as the Philadelphia Eagles'])

        monsterr = choice(
            ['Rabbit', 'Troll', 'Dragon', 'Carniverous Camel', 'Loner Llama', 'Ogre', 'Slime Mold', 'Fungal Beast',
             'Vampire', 'Dampyr', 'malformed non-specific animal', 'Shark Rocket', 'Tengu', 'Shadow Liger', 'Dragon',
             'Gaslich',
             'Hollowlich', 'Embermask', 'Bowelwraith', 'Clammy-hand Creeper', 'Creepy Cuddler',
             'Mutant Tortoises of Terror',
             'Gregarious Geek', 'Lurking Llamas', 'Horrible Screaker Witch', 'Weeping Wonderboy',
             'Boston Terrier of Terror',
             'Courier of Danger',
             'Mutant Mummer Zombie', 'Spasm Zombie', 'Scourge', 'Wolf-man Warg', 'Water Buffalo',
             'Wham-a-Whama Rock Troll',
             'Woodland Spirit', 'Wraith', 'Wyvern', 'Murder of Crows', 'Lion-Eagle Hybrid', 'Apiarian Phantom',
             'Lizard Man','Dragon Breath','Kraken','Mage', 'Sith Lord','Skeleton','Wizard','Lock Ness','T-Rex',"C'Thulu",'Hydra'
             ])
        of = choice(['of', 'from'])
        # print('The {} {} {} {}'.format(adjectives, monsterr, of, place_names))
        levl = "level {}".format(self.level)
        long_name = 'the {} {} {} \n{} {}'.format(adjectives, levl, monsterr, of, place_names)
        return (monsterr, long_name)


'''                                                                                                         
PPPPPPPPPPPPPPPPP   lllllll                                                                              
P::::::::::::::::P  l:::::l                                                                              
P::::::PPPPPP:::::P l:::::l                                                                              
PP:::::P     P:::::Pl:::::l                                                                              
  P::::P     P:::::P l::::l   aaaaaaaaaaaaayyyyyyy           yyyyyyy eeeeeeeeeeee    rrrrr   rrrrrrrrr   
  P::::P     P:::::P l::::l   a::::::::::::ay:::::y         y:::::yee::::::::::::ee  r::::rrr:::::::::r  
  P::::PPPPPP:::::P  l::::l   aaaaaaaaa:::::ay:::::y       y:::::ye::::::eeeee:::::eer:::::::::::::::::r 
  P:::::::::::::PP   l::::l            a::::a y:::::y     y:::::ye::::::e     e:::::err::::::rrrrr::::::r
  P::::PPPPPPPPP     l::::l     aaaaaaa:::::a  y:::::y   y:::::y e:::::::eeeee::::::e r:::::r     r:::::r
  P::::P             l::::l   aa::::::::::::a   y:::::y y:::::y  e:::::::::::::::::e  r:::::r     rrrrrrr
  P::::P             l::::l  a::::aaaa::::::a    y:::::y:::::y   e::::::eeeeeeeeeee   r:::::r            
  P::::P             l::::l a::::a    a:::::a     y:::::::::y    e:::::::e            r:::::r            
PP::::::PP          l::::::la::::a    a:::::a      y:::::::y     e::::::::e           r:::::r            
P::::::::P          l::::::la:::::aaaa::::::a       y:::::y       e::::::::eeeeeeee   r:::::r            
P::::::::P          l::::::l a::::::::::aa:::a     y:::::y         ee:::::::::::::e   r:::::r            
PPPPPPPPPP          llllllll  aaaaaaaaaa  aaaa    y:::::y            eeeeeeeeeeeeee   rrrrrrr            
                                                 y:::::y                                                 
                                                y:::::y                                                  
                                               y:::::y                                                   
                                              y:::::y                                                    
                                             yyyyyyy                                                     
'''
class Player:
    def __init__(self, health=100, gold=5, name='Zork', lvl=1, init_position=[12, 12]):
        self.position = init_position
        self.name = name
        self.health = health  # 100
        self.gold = gold  # 5
        self.inventory = self.equip()
        self.level = lvl
        self.avatar = " Q"
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
        ][(randrange(25)) % 9]


# player = {'name': 'ZORK', 'inventory': inventory, 'health': health, 'gold': gold}
# player['inventory'][0] = new_weapon(level[0])
##################################################################

'''
                                                                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                        
                   hhhhhhh                                                     kkkkkkkk                                                                                                                iiii                            iiii          tttt                               
                   h:::::h                                                     k::::::k                                                                                                               i::::i                          i::::i      ttt:::t                               
                   h:::::h                                                     k::::::k                                                                                                                iiii                            iiii       t:::::t                               
                   h:::::h                                                     k::::::k                                                                                                                                                           t:::::t                               
    cccccccccccccccch::::h hhhhh           eeeeeeeeeeee        cccccccccccccccc k:::::k    kkkkkkk                        ppppp   ppppppppp   rrrrr   rrrrrrrrr      ooooooooooo xxxxxxx      xxxxxxxiiiiiii    mmmmmmm    mmmmmmm   iiiiiiittttttt:::::tttttttyyyyyyy           yyyyyyy
  cc:::::::::::::::ch::::hh:::::hhh      ee::::::::::::ee    cc:::::::::::::::c k:::::k   k:::::k                         p::::ppp:::::::::p  r::::rrr:::::::::r   oo:::::::::::oox:::::x    x:::::x i:::::i  mm:::::::m  m:::::::mm i:::::it:::::::::::::::::t y:::::y         y:::::y 
 c:::::::::::::::::ch::::::::::::::hh   e::::::eeeee:::::ee c:::::::::::::::::c k:::::k  k:::::k                          p:::::::::::::::::p r:::::::::::::::::r o:::::::::::::::ox:::::x  x:::::x   i::::i m::::::::::mm::::::::::m i::::it:::::::::::::::::t  y:::::y       y:::::y  
c:::::::cccccc:::::ch:::::::hhh::::::h e::::::e     e:::::ec:::::::cccccc:::::c k:::::k k:::::k                           pp::::::ppppp::::::prr::::::rrrrr::::::ro:::::ooooo:::::o x:::::xx:::::x    i::::i m::::::::::::::::::::::m i::::itttttt:::::::tttttt   y:::::y     y:::::y   
c::::::c     ccccccch::::::h   h::::::he:::::::eeeee::::::ec::::::c     ccccccc k::::::k:::::k                             p:::::p     p:::::p r:::::r     r:::::ro::::o     o::::o  x::::::::::x     i::::i m:::::mmm::::::mmm:::::m i::::i      t:::::t          y:::::y   y:::::y    
c:::::c             h:::::h     h:::::he:::::::::::::::::e c:::::c              k:::::::::::k                              p:::::p     p:::::p r:::::r     rrrrrrro::::o     o::::o   x::::::::x      i::::i m::::m   m::::m   m::::m i::::i      t:::::t           y:::::y y:::::y     
c:::::c             h:::::h     h:::::he::::::eeeeeeeeeee  c:::::c              k:::::::::::k                              p:::::p     p:::::p r:::::r            o::::o     o::::o   x::::::::x      i::::i m::::m   m::::m   m::::m i::::i      t:::::t            y:::::y:::::y      
c::::::c     ccccccch:::::h     h:::::he:::::::e           c::::::c     ccccccc k::::::k:::::k                             p:::::p    p::::::p r:::::r            o::::o     o::::o  x::::::::::x     i::::i m::::m   m::::m   m::::m i::::i      t:::::t    tttttt   y:::::::::y       
c:::::::cccccc:::::ch:::::h     h:::::he::::::::e          c:::::::cccccc:::::ck::::::k k:::::k                            p:::::ppppp:::::::p r:::::r            o:::::ooooo:::::o x:::::xx:::::x   i::::::im::::m   m::::m   m::::mi::::::i     t::::::tttt:::::t    y:::::::y        
 c:::::::::::::::::ch:::::h     h:::::h e::::::::eeeeeeee   c:::::::::::::::::ck::::::k  k:::::k                           p::::::::::::::::p  r:::::r            o:::::::::::::::ox:::::x  x:::::x  i::::::im::::m   m::::m   m::::mi::::::i     tt::::::::::::::t     y:::::y         
  cc:::::::::::::::ch:::::h     h:::::h  ee:::::::::::::e    cc:::::::::::::::ck::::::k   k:::::k                          p::::::::::::::pp   r:::::r             oo:::::::::::oox:::::x    x:::::x i::::::im::::m   m::::m   m::::mi::::::i       tt:::::::::::tt    y:::::y          
    cccccccccccccccchhhhhhh     hhhhhhh    eeeeeeeeeeeeee      cccccccccccccccckkkkkkkk    kkkkkkk                         p::::::pppppppp     rrrrrrr               ooooooooooo xxxxxxx      xxxxxxxiiiiiiiimmmmmm   mmmmmm   mmmmmmiiiiiiii         ttttttttttt     y:::::y           
                                                                                                  ________________________ p:::::p                                                                                                                                   y:::::y            
                                                                                                  _::::::::::::::::::::::_ p:::::p                                                                                                                                  y:::::y             
                                                                                                  ________________________p:::::::p                                                                                                                                y:::::y              
                                                                                                                          p:::::::p                                                                                                                               y:::::y               
                                                                                                                          p:::::::p                                                                                                                              yyyyyyy                
                                                                                                                          ppppppppp                                                                                                                                                                                                                                                                                                                                                                                                                                             
'''
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

'''                                                                                                                                                                                                                                                                                   
                                                                                     tttt                                                                                                    tttt               tttt                                               kkkkkkkk           
                                                                                  ttt:::t                                                                                                 ttt:::t            ttt:::t                                               k::::::k           
                                                                                  t:::::t                                                                                                 t:::::t            t:::::t                                               k::::::k           
                                                                                  t:::::t                                                                                                 t:::::t            t:::::t                                               k::::::k           
   mmmmmmm    mmmmmmm      ooooooooooo   nnnn  nnnnnnnn        ssssssssss   ttttttt:::::ttttttt        eeeeeeeeeeee    rrrrr   rrrrrrrrr                             aaaaaaaaaaaaa  ttttttt:::::tttttttttttttt:::::ttttttt      aaaaaaaaaaaaa      cccccccccccccccc k:::::k    kkkkkkk
 mm:::::::m  m:::::::mm  oo:::::::::::oo n:::nn::::::::nn    ss::::::::::s  t:::::::::::::::::t      ee::::::::::::ee  r::::rrr:::::::::r                            a::::::::::::a t:::::::::::::::::tt:::::::::::::::::t      a::::::::::::a   cc:::::::::::::::c k:::::k   k:::::k 
m::::::::::mm::::::::::mo:::::::::::::::on::::::::::::::nn ss:::::::::::::s t:::::::::::::::::t     e::::::eeeee:::::eer:::::::::::::::::r                           aaaaaaaaa:::::at:::::::::::::::::tt:::::::::::::::::t      aaaaaaaaa:::::a c:::::::::::::::::c k:::::k  k:::::k  
m::::::::::::::::::::::mo:::::ooooo:::::onn:::::::::::::::ns::::::ssss:::::stttttt:::::::tttttt    e::::::e     e:::::err::::::rrrrr::::::r                                   a::::atttttt:::::::tttttttttttt:::::::tttttt               a::::ac:::::::cccccc:::::c k:::::k k:::::k   
m:::::mmm::::::mmm:::::mo::::o     o::::o  n:::::nnnn:::::n s:::::s  ssssss       t:::::t          e:::::::eeeee::::::e r:::::r     r:::::r                            aaaaaaa:::::a      t:::::t            t:::::t              aaaaaaa:::::ac::::::c     ccccccc k::::::k:::::k    
m::::m   m::::m   m::::mo::::o     o::::o  n::::n    n::::n   s::::::s            t:::::t          e:::::::::::::::::e  r:::::r     rrrrrrr                          aa::::::::::::a      t:::::t            t:::::t            aa::::::::::::ac:::::c              k:::::::::::k     
m::::m   m::::m   m::::mo::::o     o::::o  n::::n    n::::n      s::::::s         t:::::t          e::::::eeeeeeeeeee   r:::::r                                     a::::aaaa::::::a      t:::::t            t:::::t           a::::aaaa::::::ac:::::c              k:::::::::::k     
m::::m   m::::m   m::::mo::::o     o::::o  n::::n    n::::nssssss   s:::::s       t:::::t    tttttte:::::::e            r:::::r                                    a::::a    a:::::a      t:::::t    tttttt  t:::::t    tttttta::::a    a:::::ac::::::c     ccccccc k::::::k:::::k    
m::::m   m::::m   m::::mo:::::ooooo:::::o  n::::n    n::::ns:::::ssss::::::s      t::::::tttt:::::te::::::::e           r:::::r                                    a::::a    a:::::a      t::::::tttt:::::t  t::::::tttt:::::ta::::a    a:::::ac:::::::cccccc:::::ck::::::k k:::::k   
m::::m   m::::m   m::::mo:::::::::::::::o  n::::n    n::::ns::::::::::::::s       tt::::::::::::::t e::::::::eeeeeeee   r:::::r                                    a:::::aaaa::::::a      tt::::::::::::::t  tt::::::::::::::ta:::::aaaa::::::a c:::::::::::::::::ck::::::k  k:::::k  
m::::m   m::::m   m::::m oo:::::::::::oo   n::::n    n::::n s:::::::::::ss          tt:::::::::::tt  ee:::::::::::::e   r:::::r                                     a::::::::::aa:::a       tt:::::::::::tt    tt:::::::::::tt a::::::::::aa:::a cc:::::::::::::::ck::::::k   k:::::k 
mmmmmm   mmmmmm   mmmmmm   ooooooooooo     nnnnnn    nnnnnn  sssssssssss              ttttttttttt      eeeeeeeeeeeeee   rrrrrrr                                      aaaaaaaaaa  aaaa         ttttttttttt        ttttttttttt    aaaaaaaaaa  aaaa   cccccccccccccccckkkkkkkk    kkkkkkk
                                                                                                                                           ________________________                                                                                                                   
                                                                                                                                           _::::::::::::::::::::::_                                                                                                                   
                                                                                                                                           ________________________                                                                                                                   
                                                  tttt               tttt                                               kkkkkkkk           
                                               ttt:::t            ttt:::t                                               k::::::k           
                                               t:::::t            t:::::t                                               k::::::k           
                                               t:::::t            t:::::t                                               k::::::k           
                          aaaaaaaaaaaaa  ttttttt:::::tttttttttttttt:::::ttttttt      aaaaaaaaaaaaa      cccccccccccccccc k:::::k    kkkkkkk
                          a::::::::::::a t:::::::::::::::::tt:::::::::::::::::t      a::::::::::::a   cc:::::::::::::::c k:::::k   k:::::k 
                          aaaaaaaaa:::::at:::::::::::::::::tt:::::::::::::::::t      aaaaaaaaa:::::a c:::::::::::::::::c k:::::k  k:::::k  
                                   a::::atttttt:::::::tttttttttttt:::::::tttttt               a::::ac:::::::cccccc:::::c k:::::k k:::::k   
                            aaaaaaa:::::a      t:::::t            t:::::t              aaaaaaa:::::ac::::::c     ccccccc k::::::k:::::k    
                          aa::::::::::::a      t:::::t            t:::::t            aa::::::::::::ac:::::c              k:::::::::::k     
                         a::::aaaa::::::a      t:::::t            t:::::t           a::::aaaa::::::ac:::::c              k:::::::::::k     
                        a::::a    a:::::a      t:::::t    tttttt  t:::::t    tttttta::::a    a:::::ac::::::c     ccccccc k::::::k:::::k    
                        a::::a    a:::::a      t::::::tttt:::::t  t::::::tttt:::::ta::::a    a:::::ac:::::::cccccc:::::ck::::::k k:::::k   
                        a:::::aaaa::::::a      tt::::::::::::::t  tt::::::::::::::ta:::::aaaa::::::a c:::::::::::::::::ck::::::k  k:::::k  
                         a::::::::::aa:::a       tt:::::::::::tt    tt:::::::::::tt a::::::::::aa:::a cc:::::::::::::::ck::::::k   k:::::k 
                          aaaaaaaaaa  aaaa         ttttttttttt        ttttttttttt    aaaaaaaaaa  aaaa   cccccccccccccccckkkkkkkk    kkkkkkk
________________________                                                                                                                   
_::::::::::::::::::::::_                                                                                                                   
________________________                                                                                                                   
'''
def monster_attack(m):
    v = monsters[m].inventory[0]['damage'] - player.inventory[1]['block']
    player.health -= v
    if check_death(player.health):
        game_over(False)
    map.message_key[2] = 'dmg ' + str(monsters[m].inventory[0]['damage'])


########################################################################################################################
'''                                                                                                                                                                                                                          
                    lllllll                                                                              
                    l:::::l                                                                              
                    l:::::l                                                                              
                    l:::::l                                                                              
ppppp   ppppppppp    l::::l   aaaaaaaaaaaaayyyyyyy           yyyyyyy eeeeeeeeeeee    rrrrr   rrrrrrrrr   
p::::ppp:::::::::p   l::::l   a::::::::::::ay:::::y         y:::::yee::::::::::::ee  r::::rrr:::::::::r  
p:::::::::::::::::p  l::::l   aaaaaaaaa:::::ay:::::y       y:::::ye::::::eeeee:::::eer:::::::::::::::::r 
pp::::::ppppp::::::p l::::l            a::::a y:::::y     y:::::ye::::::e     e:::::err::::::rrrrr::::::r
 p:::::p     p:::::p l::::l     aaaaaaa:::::a  y:::::y   y:::::y e:::::::eeeee::::::e r:::::r     r:::::r
 p:::::p     p:::::p l::::l   aa::::::::::::a   y:::::y y:::::y  e:::::::::::::::::e  r:::::r     rrrrrrr
 p:::::p     p:::::p l::::l  a::::aaaa::::::a    y:::::y:::::y   e::::::eeeeeeeeeee   r:::::r            
 p:::::p    p::::::p l::::l a::::a    a:::::a     y:::::::::y    e:::::::e            r:::::r            
 p:::::ppppp:::::::pl::::::la::::a    a:::::a      y:::::::y     e::::::::e           r:::::r            
 p::::::::::::::::p l::::::la:::::aaaa::::::a       y:::::y       e::::::::eeeeeeee   r:::::r            
 p::::::::::::::pp  l::::::l a::::::::::aa:::a     y:::::y         ee:::::::::::::e   r:::::r            
 p::::::pppppppp    llllllll  aaaaaaaaaa  aaaa    y:::::y            eeeeeeeeeeeeee   rrrrrrr            
 p:::::p                                         y:::::y                                                 
 p:::::p                                        y:::::y                                                  
p:::::::p                                      y:::::y                                                   
p:::::::p                                     y:::::y                                                                                                                                                                                               
p:::::::p                                    yyyyyyy                                                                                                                                                                                                
ppppppppp                                                                                                                                                                                                                                           
                                                  tttt               tttt                                               kkkkkkkk           
                                               ttt:::t            ttt:::t                                               k::::::k           
                                               t:::::t            t:::::t                                               k::::::k           
                                               t:::::t            t:::::t                                               k::::::k           
                          aaaaaaaaaaaaa  ttttttt:::::tttttttttttttt:::::ttttttt      aaaaaaaaaaaaa      cccccccccccccccc k:::::k    kkkkkkk
                          a::::::::::::a t:::::::::::::::::tt:::::::::::::::::t      a::::::::::::a   cc:::::::::::::::c k:::::k   k:::::k 
                          aaaaaaaaa:::::at:::::::::::::::::tt:::::::::::::::::t      aaaaaaaaa:::::a c:::::::::::::::::c k:::::k  k:::::k  
                                   a::::atttttt:::::::tttttttttttt:::::::tttttt               a::::ac:::::::cccccc:::::c k:::::k k:::::k   
                            aaaaaaa:::::a      t:::::t            t:::::t              aaaaaaa:::::ac::::::c     ccccccc k::::::k:::::k    
                          aa::::::::::::a      t:::::t            t:::::t            aa::::::::::::ac:::::c              k:::::::::::k     
                         a::::aaaa::::::a      t:::::t            t:::::t           a::::aaaa::::::ac:::::c              k:::::::::::k     
                        a::::a    a:::::a      t:::::t    tttttt  t:::::t    tttttta::::a    a:::::ac::::::c     ccccccc k::::::k:::::k    
                        a::::a    a:::::a      t::::::tttt:::::t  t::::::tttt:::::ta::::a    a:::::ac:::::::cccccc:::::ck::::::k k:::::k   
                        a:::::aaaa::::::a      tt::::::::::::::t  tt::::::::::::::ta:::::aaaa::::::a c:::::::::::::::::ck::::::k  k:::::k  
                         a::::::::::aa:::a       tt:::::::::::tt    tt:::::::::::tt a::::::::::aa:::a cc:::::::::::::::ck::::::k   k:::::k 
                          aaaaaaaaaa  aaaa         ttttttttttt        ttttttttttt    aaaaaaaaaa  aaaa   cccccccccccccccckkkkkkkk    kkkkkkk
________________________                                                                                                                   
_::::::::::::::::::::::_                                                                                                                   
________________________                                                                                                                   
'''
def player_attack(arg):
    print(arg)
    damage = 0
    if arg == 'kill':
        damage = (player.inventory[0]['damage'] * 10)
        monsters[this_monster[0]].health -= damage
        map.head[0] = 2
    elif arg.lower() == 'zero':
        damage = monsters[this_monster[0]].health
        monsters[this_monster[0]].health = 0
        map.head[0] = 2
    elif arg.lower() == 'zork':
        damage = round((player.inventory[0]['damage'] * 40))
        monsters[this_monster[0]].health -= damage
        map.head[0] = 2
    else:
        damage = round(
            int(player.inventory[0]['damage'] + (player.gold * .006661)) - monsters[this_monster[0]].inventory[1]['block'])
        monsters[this_monster[0]].health -= damage
    if check_death(monsters[this_monster[0]].health):
        game_over(True)
    map.monster_go(player, monsters)
    map.mapit(player, monsters, damage)

########################################################################
######################  SPELL BOOK  ####################################
########################################################################
'''
      #######                     ###   ###                ##### ##                         /        
    /       ###                    ###   ###            ######  /##                       #/         
   /         ##                     ##    ##           /#   /  / ##                       ##         
   ##        #                      ##    ##          /    /  /  ##                       ##         
    ###                             ##    ##              /  /   /                        ##         
   ## ###           /###     /##    ##    ##             ## ##  /        /###     /###    ##  /##    
    ### ###        / ###  / / ###   ##    ##             ## ## /        / ###  / / ###  / ## / ###   
      ### ###     /   ###/ /   ###  ##    ##             ## ##/        /   ###/ /   ###/  ##/   /    
        ### /##  ##    ## ##    ### ##    ##             ## ## ###    ##    ## ##    ##   ##   /     
          #/ /## ##    ## ########  ##    ##             ## ##   ###  ##    ## ##    ##   ##  /      
           #/ ## ##    ## #######   ##    ##             #  ##     ## ##    ## ##    ##   ## ##      
            # /  ##    ## ##        ##    ##                /      ## ##    ## ##    ##   ######     
  /##        /   ##    ## ####    / ##    ##            /##/     ###  ##    ## ##    ##   ##  ###    
 /  ########/    #######   ######/  ### / ### /        /  ########     ######   ######    ##   ### / 
/     #####      ######     #####    ##/   ##/        /     ####        ####     ####      ##   ##/  
|                ##                                   #                                              
 \)              ##                                    ##                                            
                 ##                                                                                  
                  ##                                                                                 
'''
# ADD IMPORTABLE SPELL BOOK
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

def print_legend():
    monsters = get_monsters_fn()
    legend = "@@@@@@@@@@@@@@@@@@@@@@@ LEGEND @@@@@@@@@@@@@@@@@@@@@ \n"
    for m in range(len(monsters)):
        avatar = monsters[m].avatar
        x_ = monsters[m].position[1]
        y_ = monsters[m].position[0]
        level =  monsters[m].level
        name = monsters[m].type.title()
        health = monsters[m].health
        damage = monsters[m].inventory[0]['damage']
        biom =  monsters[m].biom
        legend += "{} Lvl.{} HP:{} DMG:{} (x:{} y:{})  {}  [{}]\n".format(avatar, level, health, damage, x_, y_, name, biom)
    print(legend)


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

    elif spell[:4] == 'gold' and player.gold < 1000:
        player.gold += 1000
        if check_proximity(9):
            player_attack(spell)

    elif spell[:5] == 'magic' and player.gold > 200:
        player.gold -= 200
        arg = 12
        monsters = get_monsters_fn()
        for m in range(len(monsters)):
            if abs(monsters[m].position[0] - player.position[0]) < arg and arg > abs(monsters[m].position[1] - map.get_index_from_bit(player.position[1])):
                monsters[m].health -= round(player.gold * 0.006666)
                if check_death(monsters[m].health):
                    this_monster[0] = m
                    game_over(True)

    elif spell == '' and player.gold > 30:
        player.gold -= 30
        if check_proximity(3):
            player_attack(spell)

    elif spell == 'live' and player.gold > 1000:
        player.gold -= 1000
        LIVES[0] += 1
        # player_attack()
# LEGEND
    elif 'l' == spell[:1]:
        player.gold -= 10
        print_legend()

    else:
        if check_proximity():
            player_attack(spell)


########################################################################
###################### //SPELL BOOK  ###################################
########################################################################

'''
IIIIIIIIII                  iiii          tttt            iiii                    lllllll   iiii                                       
I::::::::I                 i::::i      ttt:::t           i::::i                   l:::::l  i::::i                                      
I::::::::I                  iiii       t:::::t            iiii                    l:::::l   iiii                                       
II::::::II                             t:::::t                                    l:::::l                                              
  I::::Innnn  nnnnnnnn    iiiiiiittttttt:::::ttttttt    iiiiiii   aaaaaaaaaaaaa    l::::l iiiiiii zzzzzzzzzzzzzzzzz    eeeeeeeeeeee    
  I::::In:::nn::::::::nn  i:::::it:::::::::::::::::t    i:::::i   a::::::::::::a   l::::l i:::::i z:::::::::::::::z  ee::::::::::::ee  
  I::::In::::::::::::::nn  i::::it:::::::::::::::::t     i::::i   aaaaaaaaa:::::a  l::::l  i::::i z::::::::::::::z  e::::::eeeee:::::ee
  I::::Inn:::::::::::::::n i::::itttttt:::::::tttttt     i::::i            a::::a  l::::l  i::::i zzzzzzzz::::::z  e::::::e     e:::::e
  I::::I  n:::::nnnn:::::n i::::i      t:::::t           i::::i     aaaaaaa:::::a  l::::l  i::::i       z::::::z   e:::::::eeeee::::::e
  I::::I  n::::n    n::::n i::::i      t:::::t           i::::i   aa::::::::::::a  l::::l  i::::i      z::::::z    e:::::::::::::::::e 
  I::::I  n::::n    n::::n i::::i      t:::::t           i::::i  a::::aaaa::::::a  l::::l  i::::i     z::::::z     e::::::eeeeeeeeeee  
  I::::I  n::::n    n::::n i::::i      t:::::t    tttttt i::::i a::::a    a:::::a  l::::l  i::::i    z::::::z      e:::::::e           
II::::::IIn::::n    n::::ni::::::i     t::::::tttt:::::ti::::::ia::::a    a:::::a l::::::li::::::i  z::::::zzzzzzzze::::::::e          
I::::::::In::::n    n::::ni::::::i     tt::::::::::::::ti::::::ia:::::aaaa::::::a l::::::li::::::i z::::::::::::::z e::::::::eeeeeeee  
I::::::::In::::n    n::::ni::::::i       tt:::::::::::tti::::::i a::::::::::aa:::al::::::li::::::iz:::::::::::::::z  ee:::::::::::::e  
IIIIIIIIIInnnnnn    nnnnnniiiiiiii         ttttttttttt  iiiiiiii  aaaaaaaaaa  aaaalllllllliiiiiiiizzzzzzzzzzzzzzzzz    eeeeeeeeeeeeee  
'''


print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("################## WELCOME TO #################### ")
print("################################################## ")
print("##########    ESCAPE FROM PHILADELPHIA   ######### ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("### MOVE WITH wasd KEYS OR NUMBER PAD + ENTER #### ")
print("################################################## ")
print("################   w   ########  789  ############ ")
print("### MOVE WITH  #  a d  #  OR  #  4 6  ############ ")
print("################   s   ########  123  ############ ")
print("################################################## ")
print("########## MACS MAY USE ARROW KEYS ############### ")
print("################################################## ")
print("################################################## ")
print("##    ATTACK WITH ENTER WHEN NEXT TO MONSTER    ## ")
print("################################################## ")
print("######## HEAL WITH \"h [number]\" + ENTER ######## ")
print("################################################## ")
print("LEARN TO CAST SPELLS WITH \"cast [spell]\" + ENTER ")
print("################################################## ")
print("# EXAMLPE SPELLS ################################# ")
print("# SPELLS:>>> heal 99  heals 99 costs 99 gold ##### ")
print("# SPELLS:>>> cast live adds 1 life costs 1000 gold ")
print("################################################## ")
print("# SPELLS:>>> cast legend ######################### ")
print("# SPELLS:>>> cast magic  ######################### ")
print("################################################## ")
print("################################################## ")
print("################################################## ")
print("####   ESCAPE FROM PHILADELPHIA    ############### ")
print("################################################## ")
print("###### WRITTEN BY JOSEPH HOWARD ################## ")
print("################################################## ")
print("################# USE PYTHON3 #################### ")
print("###~$ python3 printscreen_adventure.py ########### ")
print("################################################## ")
print("################################################## ")
print("#### YOU ARE:       Q        ##################### ")
print("#### MONSTERS ARE:  1 2 3 4 5 6 7 8 9 0 @   ###### ")
print("################################################## ")


##################################################################
# Initialize Application
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

how = input("@@#@#@@#@   How many monsters? >>> ")
if how.isdecimal():
    many = int(how)
else:
    many = 8

# progression_template = (MonSteR(1), MonSteR(1), MonSteR(1), MonSteR(24), MonSteR(1), MonSteR(70))
monstrocity = []
for m in range(many):
    monstrocity.append(MonSteR(m + 1))
monsters = monstrocity[:]

player = Player()


def get_player():
    return player


def get_monsters_fn():
    return monsters


map = Map(player, monsters, monster_attack, get_level, get_lives_func, get_monsters_fn, get_player)
map.mapit(player, monsters)


'''
                                                                                                                                                                             
                                                                                                                                                                             
                                        hhhhhhh               iiii  lllllll                        TTTTTTTTTTTTTTTTTTTTTTT                                                          
                                        h:::::h              i::::i l:::::l                        T:::::::::::::::::::::T                                                          
                                        h:::::h               iiii  l:::::l                        T:::::::::::::::::::::T                                                          
                                        h:::::h                     l:::::l                        T:::::TT:::::::TT:::::T                                                          
wwwwwww           wwwww           wwwwwwwh::::h hhhhh       iiiiiii  l::::l     eeeeeeeeeeee       TTTTTT  T:::::T  TTTTTTrrrrr   rrrrrrrrr   uuuuuu    uuuuuu      eeeeeeeeeeee    
 w:::::w         w:::::w         w:::::w h::::hh:::::hhh    i:::::i  l::::l   ee::::::::::::ee             T:::::T        r::::rrr:::::::::r  u::::u    u::::u    ee::::::::::::ee  
  w:::::w       w:::::::w       w:::::w  h::::::::::::::hh   i::::i  l::::l  e::::::eeeee:::::ee           T:::::T        r:::::::::::::::::r u::::u    u::::u   e::::::eeeee:::::ee
   w:::::w     w:::::::::w     w:::::w   h:::::::hhh::::::h  i::::i  l::::l e::::::e     e:::::e           T:::::T        rr::::::rrrrr::::::ru::::u    u::::u  e::::::e     e:::::e
    w:::::w   w:::::w:::::w   w:::::w    h::::::h   h::::::h i::::i  l::::l e:::::::eeeee::::::e           T:::::T         r:::::r     r:::::ru::::u    u::::u  e:::::::eeeee::::::e
     w:::::w w:::::w w:::::w w:::::w     h:::::h     h:::::h i::::i  l::::l e:::::::::::::::::e            T:::::T         r:::::r     rrrrrrru::::u    u::::u  e:::::::::::::::::e 
      w:::::w:::::w   w:::::w:::::w      h:::::h     h:::::h i::::i  l::::l e::::::eeeeeeeeeee             T:::::T         r:::::r            u::::u    u::::u  e::::::eeeeeeeeeee  
       w:::::::::w     w:::::::::w       h:::::h     h:::::h i::::i  l::::l e:::::::e                      T:::::T         r:::::r            u:::::uuuu:::::u  e:::::::e           
        w:::::::w       w:::::::w        h:::::h     h:::::hi::::::il::::::le::::::::e                   TT:::::::TT       r:::::r            u:::::::::::::::uue::::::::e          
         w:::::w         w:::::w         h:::::h     h:::::hi::::::il::::::l e::::::::eeeeeeee           T:::::::::T       r:::::r             u:::::::::::::::u e::::::::eeeeeeee  
          w:::w           w:::w          h:::::h     h:::::hi::::::il::::::l  ee:::::::::::::e           T:::::::::T       r:::::r              uu::::::::uu:::u  ee:::::::::::::e  
           www             www           hhhhhhh     hhhhhhhiiiiiiiillllllll    eeeeeeeeeeeeee           TTTTTTTTTTT       rrrrrrr                uuuuuuuu  uuuu    eeeeeeeeeeeeee  
                                                                                                                                                                             
'''
while True:
    command = input("Type Command:>>> ")
    # command = input("Type Command: ( a s d w ; a(t)tack ; cast heal ; x:exit )\n>>> ")
    if command[:2] == 'at' or 't' == command[:1] or command[:1] == ' ' or ' ' == command[:1] or '' == command[:1]:
        if check_proximity():
            player_attack(command[command.find(" ") + 1:])
        else:
            map.move(0, player, monsters)

    elif command[:4] == 'cast' or 'c' == command[:1]:
        cast_spell(command[command.find(' ') + 1:])
        map.head[0] = 1
        map.mapit(player, monsters)

    elif command[:4] == 'heal' or 'h' == command[:1]:
        if command.find(' ') > -1:
            heal_self(command[command.find(' '):])
        else:
            heal_self()
        map.head[0] = 0
        map.mapit(player, monsters)

    else:
        for i in range(len(command)):
            if command[i] == 'x':
                if input('      Are you sure you want to quit? (c) ') == 'c':
                    quit()
            elif command[i] == 's' or '2' == command[i] or 'B' == command[i]:
                map.move(2, player, monsters)
            elif command[i] == 'w' or '8' == command[i] or 'A' == command[i]:
                map.move(8, player, monsters)
            elif command[i] == 'd' or '6' == command[i] or 'C' == command[i]:
                map.move(6, player, monsters)
            elif command[i] == 'a' or '4' == command[i] or 'D' == command[i]:
                map.move(4, player, monsters)
            elif command[i] == '1':
                map.move(1, player, monsters)
            elif command[i] == '3':
                map.move(3, player, monsters)
            elif command[i] == '7' or 'a' == command[i]:
                map.move(7, player, monsters)
            elif command[i] == '9' or 'd' == command[i]:
                map.move(9, player, monsters)

#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@©2017JosephHoward
