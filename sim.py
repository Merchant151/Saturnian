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
    def process_event(self,event):
        print(f'Object {self.name} processes {event}')

    def destroy(self):
        #remove object from world data 
        world_data['object'].remove(self)
        ### unschedule ALL as well
        checkDays = list(world_data['schedule'].keys())
        for day in checkDays:
            for event in world_data['schedule'][day]: 
                if event[0] == self.gid:
                    #print(world_data['schedule'])
                    #print(f'stuff to delete {day} {event}')
                    #print('after delete')
                    remove_event_from_world_data(world_data,event,day)
                    #print(world_data['schedule'])
                    #world_data['schedule'][day].remove(event)
        print(f'{self} has been destroyed!')

class faction():
    def __init__(self):
        pass

class station(world_object):
    def __init__(self):
        pass

    def post_job(self):
        #station posts jobs to do
        pass

class ship(world_object):
    def __init__(self):
        super().__init__()
        self.type = self.random_type()
        #Behavior Values 
        self.idle = randrange(0,10) 
        self.explore = randrange(0,10)
        self.job = randrange(0,10)
        #pick starting behavior 
        self.pickBehavior()

    def random_type(self):
        rv = randrange(0,3)
        if rv == 0:
            return 'construction'
        elif rv == 1:
            return 'science'
        elif rv == 2: 
            return 'combat'
        ##UNREACHABLE
        return 'ship'


    def pickBehavior(self):
        if self.job >= self.explore:
            self.job_behavior()
        elif self.explore >= self.idle:
            self.explore_behavior()
        else: 
            self.idle_behavior()

    def job_behavior(self):
        print(f'the ship:{self.gid} will do {self.type} job')
        if self.type == 'construction':
            self.schedule(300,'end_construction')
        if self.type == 'science':
            self.schedule(35,'end_science')
        if self.type == 'combat':
            self.schedule(3,'end_combat')

    def construction_behavior(self):
        #TODO: not urgent
        #for now construction ships will build other ships. 
        world_data['object'].append(spawn_ship())
        print(f'ship construction complete')

    def science_behavior(self):
        #TODO: not urgent
        print(f'ERROR IMPLEMENT END SCIENCE')
        print(f'science complete')

    def combat_behavior(self):
        #self.schedule(2,'end_combat')
        #get targets
        target_list = get_objects_with_location(self.location)
        target = self.pick_target(target_list)
        if target != None:
            print(f'{self} has destroyed {target}' )
            self.job = 0
            target.destroy()
        else: 
            print(f'{self} cannot find a target')
        #self.idle_behavior()

    def explore_behavior(self):
        self.schedule(6,'end_explore')

    def random_travel(self):
        old = self.location  
        global world_data 
        locale = world_data['locale']['saturn']
        dest = self.location
        dest_type = randrange(0,1) #destination Type
        if dest_type == 0: 
            listlen = len(locale['major_moons'])
            dest = locale['major_moons'][randrange(0,listlen)]
        else:
            lislen = len(locale['minor_moons'])
            dest = locale['minor_moons'][randrange(0,listlen)]
            #minor moons 
        print(f'{self.name} travelled from a standard {old[1]} of {old[0]} to a standard {'orbit'} of {dest}')
        self.location = (dest,'orbit')        

    def process_event(self,event):

       # ''' This Function has three steps and is triggered on its scheudle day... 
       # depending on event type ship modifies its behavior profile currently set by integer values
       # then we process the event complete it or complete the step 
       #    '''
        print(f'Object {self.name} processes {event}')
        #MAKE THIS GLOBAL probably
        jobList = ['end_construction','end_combat','end_science']
        if (event == 'end_explore'):
            self.explore = 0 
            self.job +=1
            self.random_travel()
            self.pickBehavior()
        elif event in jobList: 
            self.job = 0
            self.explore = 0
            ### MISSING JOB PROCESSING
            self.do_job(event)
            self.idle_behavior()
        else: 
            #this is triggered when IDLE is complete 
            self.job += 1
            self.explore += 1
            self.pickBehavior()

    def do_job(self,job):
        print(f'job done {job}')
        if (job == 'end_combat'):
            self.combat_behavior()
        elif job == 'end_science':
            self.science_behavior()
        elif job == 'end_construction':
            self.construction_behavior()
        else: 
            raise Exception(f'{job} processing for object not implemented') 

    def pick_target(self,targetList):
        #in the future this should be random or based on another attribute
        result = None
        if targetList[0].gid != self.gid: 
            result = targetList[0]
        elif len(targetList) > 1:
            result = targetList[1]
        return result 


    def idle_behavior(self,durration = 10):
        print(f'the ship:{self.gid} will begin repairs')
        self.schedule(durration,'idle_behavior')

    def travel_drive(destination):
        print(f'ship is traveling from {self.location[1]} at {self.location[0]} to {destination[1]} at {destination[0]}')
        self.status = 'travel'
        #schedule()

def next_id():
    global gid
    gid = gid + 1

    return gid

def get_objects_with_location(location):
    global world_data
    objects = world_data['object']
    out_list = []
    for i in objects:
        if location == i.location:
            out_list.append(i)
    return out_list

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
    world["commission"] = []
    #create a test commission
    world["commission"].append({"contractor":"faction","contract":"build faction HQ","type":"Construction"})
    return world

def get_object_by_id(world_data,id):
    for obj in world_data['object']:
        if(obj.gid == id):
            return obj
    print(f'world schedule keys {list(world_data['schedule'].keys())}')
    print(f'Looking for ID: {id} in object list: {world_data['object']}')
    raise Exception('game object not found')

def remove_event_from_world_data(world_data,event,current_day):
    world_data['schedule'][current_day].remove(event)
    if len(world_data['schedule'][current_day]) < 1:
        print('all events today have been processed')
        del world_data['schedule'][current_day]



def check_date(current_day,world_data):
    if current_day in world_data['schedule']:
        #print('there are events today ')
        todays_events = world_data['schedule'][current_day]
        i = 0
        while i < len(todays_events):
            id,event = todays_events[0]
            actor = get_object_by_id(world_data, id)
            #do event change status...
            actor.process_event(event)
            #remove event from event list. 
            remove_event_from_world_data(world_data,todays_events[0],current_day)

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
