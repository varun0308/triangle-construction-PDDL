init = """
(:init
    
    ; Always true
    (begin_with Sc a)
    (end_with Sc b)
    
    (begin_with Sa b)
    (end_with Sa c)
    
    (begin_with Sb a)
    (end_with Sb c)
    
    (isAngle A a)
    (isAngle B b)
    (isAngle C c)
"""

goal = """
(:goal
    (and
        (isSegment Sc a b)
        (isSegment Sa b c)
        (isSegment Sb a c)
    )
)
"""

xyz = """
    (= (length Sa) 4)
    (= (length Sc) 5)
    (= (angle C) 90)
"""
print(open("p.pddl", 'r').read() + init + xyz + ")" + goal)