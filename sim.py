from datetime import datetime 
from random import randrange
GID = 0
population = 0
prefix = ['united','coeltion'];
sufix = ['saturn','conglomerate'];
factions = [];

class world_object():

    def __init__(self):
        self.GID = next_id()
        self.location = ('saturn','orbit')
        self.status = 'idle'
        self.name = 'spaceship'
        self.modules = []
        self.inventory = []

    def __repr__(self): 
        return f"name: '{self.name}'ID:{self.GID}"
    def destroy():
        print('create remove from world memory')
    def schedule(): 
        print('create schedule event to world data')
    def unschedule():
        print('unshceudle event from world')


def next_id():
    global GID
    GID = GID + 1

    return GID

def generate_faction_name(): 
    return 'United Saturn'

def roll_random_event(world_data,register):
    chance = randrange(0,100)
    if chance < 5:
        print('spawn a ship 5 percent chance')
        world_data['ship'].append(spawn_ship())
    elif chance < 15:
        print('10 percent chance')
    elif chance > 98:
        print('1 percent chance')
    elif chance >97: 
        chance = randrange(0,100)
        if chance < 1:
            print('0.01 percent chance')

def spawn_ship():
    new_ship = world_object()
    return new_ship

# a loop start date end date 
# log to a history folder 

max_date = 100
start_date = 10413810000 #2300-01-01
day = 86400

#prefix returns world starting conditions and should allow for a unique world maybe in the future allow seed generation.
def prefix():
    world = {}
    planet = {"saturn" : {"major_moons": ["Titan",'Rhea',"Iapetus","Dione","Tethys"],"minor_moons":["Enceladus","Mimas","Hyperion","Phoebe","Janus","Epimetheus"]}}
    world["locale"] = planet
    world["ship"] = []
    return world

def main():
    global world_data
    register = [] # register is where we will store location check data and future data
    current_day = start_date
    while(current_day < start_date + max_date * day * 365):
        print('today is: ',end = '')
        print(datetime.fromtimestamp(current_day))
        roll_random_event(world_data,register)
        current_day = current_day + day
    print(world_data)


world_data = prefix()
main()
