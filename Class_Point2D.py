class Point2D():
    def __init__(self, x,y):
        self.coord = [x,y]

    def __str__(self):
        return f'Point:({self.coord[0]},{self.coord[1]})'

    def __eq__(self,other):
       return (self.coord[0]==other.coord[0])&(self.coord[1]==other.coord[1])

    def __ne__(self,other):
        return (self.coord[0]!=other.coord[0])&(self.coord[1]!=other.coord[1])

    def __gt__(self,other):
        return (self.distance()>other.distance())

    def __le__(self,other):
        return (self.distance()<=other.distance())

    def __ge__(self,other):
        return (self.distance()>=other.distance())

    def __ne__(self,other):
        return (self.coord[0]!=other.coord[0])&(self.coord[1]!=other.coord[1])

    def distance(self):
        return (self.coord[0]**2+self.coord[1]**2)**0.5

    
if __name__=='__main__':
    point1 = Point2D(1,1)