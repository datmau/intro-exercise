
class User():
    def __init__(self,data_set):
        self.data_set = data_set
        self.ammount = 0

    def splitData(self):
        data = self.data_set.split('=')[1]
        dataSplitted = data.split(',')
        return dataSplitted

    def getUsername(self):
        return self.data_set.split('=')[0]

    def giveAmmount(self):
        for dataitem in self.splitData():
            time = Times(dataitem)
            self.ammount += time.calculateTimeRange()


        



class EspecificTimesAmmount():
    def __init__(self,calculatedHours,isWeek):
        self.calculatedHours = calculatedHours
        self.isWeek = isWeek
        self.WEEK_HOUR_PRICES = [25,15,20]
        self.WEEKEND_HOUR_PRICES = [30,20,25]


    def MO(self):
        if self.isWeek:
            return self.WEEK_HOUR_PRICES[0] * self.calculatedHours
        return self.WEEKEND_HOUR_PRICES[0] * self.calculatedHours
    
    def AF(self):
        if self.isWeek:
            return self.WEEK_HOUR_PRICES[1] * self.calculatedHours
        return self.WEEKEND_HOUR_PRICES[1] * self.calculatedHours
    
    def NI(self):
        if self.isWeek:
            return self.WEEK_HOUR_PRICES[2] * self.calculatedHours
        return self.WEEKEND_HOUR_PRICES[2] * self.calculatedHours

         
class Times():
    def __init__(self,dataitem):
        self.dataitem = dataitem
        self.EXIT_HOUR = int(self.dataitem[8:10])
        self.BEGIN_HOUR = int(self.dataitem[2:4])
        self.DAY = self.dataitem[0:2]

    def calculateWorkedHours(self):
       return self.EXIT_HOUR - self.BEGIN_HOUR
    
    def isWeek(self):
        WEEK_DAYS=['MO','TU','WE','TH','FR']
        if self.DAY in WEEK_DAYS:
            return True   
        return False
    
    def calculateTimeRange(self):
        if self.BEGIN_HOUR >= 0 and self.EXIT_HOUR<= 9:
            return EspecificTimesAmmount(self.calculateWorkedHours(),self.isWeek()).MO()
        elif self.BEGIN_HOUR >= 9 and self.EXIT_HOUR <= 18:
            return EspecificTimesAmmount(self.calculateWorkedHours(),self.isWeek()).AF()
        elif self.BEGIN_HOUR >= 18 and self.EXIT_HOUR <= 23:
            return EspecificTimesAmmount(self.calculateWorkedHours(),self.isWeek()).NI()
    


def openFile():
    file = open('data.txt','r')
    return file

def userInfo():
    for f in openFile():
        user = User(f.rstrip())
        user.giveAmmount()
        print('The amount to pay {} is {}'.format(user.getUsername(),user.ammount))
    

        

def main():
    '''dataset_input =input('Type the dataset to calculate, if you dont have a new data press q')
    while dataset_input != 'q':   
        loadDataToFile(dataset_input)
        dataset_input=input('Type the dataset to calculate, if you dont have a new data press q')'''
    userInfo()
    


    

if __name__ == '__main__':
    main()
                
            


        