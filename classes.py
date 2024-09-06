class bank:
    def __init__(self, net_wort,no_of_buildings, no_of_employes):
        self.net_wort = net_wort
        self.no_of_buildings = no_of_buildings
        self.no_of_employes = no_of_employes
    def get_net_wort(self):
        print(f"the net worth of the company is {self.net_wort}") 
    def get_no_of_buildings(self):
        print(f"the total amount of buildings owned by bank {self.no_of_buildings}")
    def get_no_of_employes(self):
        print(f"the current no of employes are {self.no_of_employes} employes")


first = bank("$30000.00" , 10 , 300)
first.get_net_wort()
first.get_no_of_buildings()
first.get_no_of_employes()



## inheritance
# 

