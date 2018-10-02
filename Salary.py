import time,datetime




def chargeData(data):
    file = open('data.txt','a+')
    file.write('{}'.format(data))
    file.close()
    
def calculateAmmount():
    file = open('data.txt','r')
    CASE_ONE=['MO','TU','WE','TH','FR']
    CASE_TWO=['SA','SU']
    HOURS_RANGE =['00:01-09:00','09:01-18:00','18:01-00:00']
    PRICES_ONE=[25,15,20]
    PRICES_TWO=[30,20,25]
    for f in file:
        salary=0
        name = f.split('=')
        hours = name[1].rstrip().split(',') 
        
        for h in hours:
            h_sub=h[2:].split('-')
            final_h=int(h_sub[1][0:2])
            begin_h=int(h_sub[0][0:2])
            hour_counter = final_h - begin_h
            for case in CASE_ONE:
                if h[0:2] == case and final_h >= 0 and begin_h <= 9:
                    salary += (hour_counter*PRICES_ONE[0])
                elif h[0:2] == case and final_h >=9  and begin_h <= 18:
                    salary += (hour_counter*PRICES_ONE[1])
                elif h[0:2] == case and final_h >=18 and begin_h <=23:
                    salary += (hour_counter*PRICES_ONE[2])
            for case in CASE_TWO:
                if h[0:2] == case and final_h >= 0 and begin_h <= 9:
                    salary += (hour_counter*PRICES_TWO[0])
                elif h[0:2] == case and final_h >=9  and begin_h <= 18:
                    salary += (hour_counter*PRICES_TWO[1])
                elif h[0:2] == case and final_h >=18 and begin_h <=23:
                    salary += (hour_counter*PRICES_TWO[2])

        print('The ammount to pay {} is {}'.format(name[0],salary))
            




def main():
    option=input('Type the dataset to calculate, if you dont a new data press q')
    while option != 'q':   
        chargeData(option)
        option=input('Type the dataset to calculate, if you dont a new data press q')
    calculateAmmount()
        
    

if __name__ == '__main__':
    main()