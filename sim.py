from datetime import datetime 
population = 0
prefix = ['united','coeltion'];
sufix = ['saturn','conglomerate'];
factions = [];

def generate_faction_name(): 
    return 'United Saturn'


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
    return world

def main():
    current_day = start_date
    while(current_day < start_date + max_date * day * 365):
        print('today is: ',end = '')
        print(datetime.fromtimestamp(current_day))
        current_day = current_day + day


world_data = prefix()
main()
