from datetime import datetime 
from random import randrange
gid = 0
population = 0
prefix = ['united','coeltion'];
sufix = ['saturn','conglomerate'];
factions = [];

class world_object():

    def __init__(self):
        self.gid = next_id()
        self.location = ('saturn','orbit')
        self.status = 'idle'
        self.name = 'spaceship'
        self.type = 'unknown'
        self.modules = []
        self.inventory = []
        self.myHolds = {}
        self.behaviorStage = 0

    def __repr__(self): 
        return f"name: '{self.name}'ID:{self.gid}"
    def destroy():
        print('create remove from world memory')
    def schedule(self,date,action): 
        print('create schedule event to world data')
        global day
        global current_day 
        global world_data
        date *= day
        date += current_day
        future_actions = world_data['schedule'].get(date,[])
        future_actions.append((self.gid,action))
        world_data['schedule'][date] = future_actions
    def unschedule(self):
        print('unshceudle event from world')

class ship(world_object):
    def __init__(self):
        super().__init__()
        self.type = 'ship'
        #Behavior Values 
        self.idle = randrange(0,10) 
        self.explore = randrange(0,10)

        #pick starting behavior 
        self.pickBehavior()

    def pickBehavior(self):
        print('pick random behavior')
        if self.idle <= self.explore:
            self.explore_behavior()
        else: 
            self.idle_behavior()

    def explore_behavior(self):
        print('the ship will begin exploring')
        self.schedule(6,'end_explore')

    def idle_behavior(self):
        print('the ship will begin repairs')

    def travel_drive(destination):
        print(f'ship is traveling from {self.location[1]} at {self.location[0]} to {destination[1]} at {destination[0]}')
        self.status = 'travel'
        schedule()

def next_id():
    global gid
    gid = gid + 1

    return gid

def generate_faction_name(): 
    return 'United Saturn'

def roll_random_event(world_data,register):
    chance = randrange(0,100)
    if chance < 5:
        print('spawn a ship 5 percent chance')
        world_data['object'].append(spawn_ship())
    elif chance < 15:
        print('10 percent chance')
    elif chance > 98:
        print('1 percent chance')
    elif chance >97: 
        chance = randrange(0,100)
        if chance < 1:
            print('0.01 percent chance')

def spawn_ship():
    new_ship = ship()
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
    world["object"] = []
    world["schedule"] = {}
    return world

def get_object_by_id(world_data,id):
    for obj in world_data['object']:
        if(obj.gid == id):
            return obj
    raise Exception('game object not found')

def check_date(current_day,world_data):
    if current_day in world_data['schedule']:
        #TODO: implement
        print('event_today: ',end='')
        ##print(world_data['schedule'][current_day])
        ##print(world_data['schedule'][current_day][0])
        todays_events = world_data['schedule'][current_day]
        number_of_events = len(todays_events)
        for i in range(number_of_events):
            print(todays_events[i])
            id = todays_events[i][0]
            actor = get_object_by_id(world_data, id)
            #do event change status...
            #remove event from event list. 
        return world_data
    else: 
        print('nothing scheduled')
        return world_data
def main():
    global world_data
    global current_day
    register = [] # register is where we will store location check data and future data
    current_day = start_date
    while(current_day < start_date + max_date * day * 365):
        print('today is: ',end = '')
        print(datetime.fromtimestamp(current_day))
        roll_random_event(world_data,register)
        check_date(current_day,world_data)
        current_day = current_day + day
    print(world_data)

world_data = prefix()
main()
