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

def main():
    current_day = start_date
    while(current_day < start_date + max_date * day * 365):
        print('today is: ',end = '')
        print(datetime.fromtimestamp(current_day))
        current_day = current_day + day


print('running')
main()
