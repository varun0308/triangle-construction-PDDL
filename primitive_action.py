import copy
"""
states['states'][-1] -> 

{
"point" : {"A": False, "B": False, "C" : False},
"segment" : {"A": True, "B": True, "C" : True},
"arc" : {"A": False, "B": False, "C" : False}
}
"""

class Actions():
    
    def __init__(self):
        self.states = [{
            "point" : {"A": False, "B": False, "C" : False},
            "segment" : {"AB": False, "BC": False, "CA" : False},
            "arc" : {"A": False, "B": False, "C" : False}
        }]
        
        self.triangle= {
            'AB' : int(input("Segment AB ")),
            'BC' : int(input("Segment BC ")),
            'CA' : int(input("Segment CA ")),
            'A' : int(input("Angle A ")),
            'B' : int(input("Angle B ")),
            'C' : int(input("Angle C "))
        }


        # List of all segments
        self.segments = [{"length" : self.triangle[x],"p1" : x[0], "p2" : x[1]} for x in ['AB', 'BC', 'CA']]
        # List of all arcs
        self.arcs = [{"p1" : x[0], "length" : self.triangle[x], "p2" : x[1]} for x in ['AB', 'BC', 'CA']]



    # segment -> str to tell which segment(AB)
    def draw_segment(self, )
    def draw_segment(self, segment):
        state = copy.deepcopy(self.states[-1])

        # Precondition check
        # segment should have a length
        if not self.triangle[segment]:
            print("Doesn't satisfy condition :(")
            return 
        
        # Print primitive step
        print("Draw a line segment {}".format(segment))
        
        state['point'][segment[0]] = True
        state['point'][segment[1]] = True
        state['segment'][segment] = True
        self.states.append(state)
        
        return 



    # arc -> the arc to be drawn(AB)
    def draw_arc(self, arc):
        state = copy.deepcopy(self.states[-1])
        
        # Precondition check
        # arc must have radius, and the point from which it is to be drawn point must be present
        if not (self.arcs[arc] and state['point'][arc]):
            print("Doesn't satisfy condition :(")
            return False
        
        # Print primitive step
        print("Draw a arc from {} of radius {}".format(self.arcs[arc]))
        
        state['arc'][arc.p] = True
        self.states.append(state)
        return

    # 2 arcs 
    def make_intersection(self, arc1, arc2):
        state = copy.deepcopy(self.states[-1])
        
        # Precondition check
        # 2 arcs must exist(other conditions will be checked)
        if not (arc1.radius and arc2.radius) :
            print("Doesn't satisfy condition :(")
            return 
        
        # Print primitive step
        
        state['arc'][arc1.p] = True
        state['arc'][arc2.p] = True
        state['point'][arc2.p] = True
        self.states.append(state)
        
        return 


    # 2 points to join(AB)
    # p1 and p2 are strings
    def join_points(self, p):
        
        state = copy.deepcopy(self.states[-1])
        
        # Precondition check
        # atleast 2 unconnected points must exist
        if not (state['point'][p[0]] and state['point'][p[1]] and not state['segment'][str(p1+p2)]) :
            print("Doesn't satisfy condition :(")
            return 
        
        # Print primitive step
        
        state['segment'][p] = True
        self.states.append(state)
        
        return 