class Interface1:
    @staticmethod
    def area(w, d):
        return w*d

class Interface2:
    def area(x1, y1, x2, y2):
        return abs(x1 - x2) * abs(y1 - y2)
    
class AdapterLikeInterface2:
    def __init__(self, interface1):
        self.interface1 = interface1
    
    def area(self, x1, y1, x2, y2):
        w = abs(x1 - x2)
        d = abs(y1 - y2)
        return self.interface1(w, d)

