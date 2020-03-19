import pickle
class Steel():
    def __init__(self,x,y,z):
        self.dimensions = [x,y,z]

    def __str__(self):
        return f'Стальной лист. Длина: {self.dimensions[0]}, Ширина: {self.dimensions[1]}, Толщина: {self.dimensions[2]}'

    def __gt__(self, other):
        return self.weight()>other.weight()

    def __ge__(self, other):
        return self.weight() >= other.weight()

    def __le__(self, other):
        return self.weight() <= other.weight()

    def __lt__(self, other):
        return self.weight()<other.weight()

    def __eq__(self,other):
        return ((self.dimensions[0] == other.dimensions[0]) & (self.dimensions[1] == other.dimensions[1]) & (self.dimensions[2] == other.dimensions[2]))

    def __getitem__(self,key):
        return self.dimensions[key]

    def weight(self):
        return round(self.dimensions[0]*self.dimensions[1]*self.dimensions[2]*0.00785/1000)

    def __getstate__(self):
        return self.dimensions

    def __setstate__(self,state):
        self.dimensions = state


if __name__ =='__main__':
    sheet1 = Steel(6000,2000,2)
    sheet2 = Steel(3000,2000,10)
    sheet3 = Steel(6000,2000,2)
    print(sheet1)
    print(sheet1.weight())
    print(sheet1>sheet2)
    print(sheet1<sheet2)
    print(sheet1 == sheet3)
    print (6000 in sheet1)


sheet1 = Steel(600,100,3)
f = open('sheet.pkl', 'wb')
pickle.dump(sheet1,f)
f.close()

f= open('sheet.pkl', 'rb')
sheet_loaded = pickle.load(f)
print(sheet1, sheet_loaded)
f.close()