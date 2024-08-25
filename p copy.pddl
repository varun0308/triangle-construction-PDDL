; Hello World example problem

(define (problem construct)

(:domain triangle)

(:objects
    a b c - point
    Sa Sb Sc - segment
    A B C - angle
)

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

    ; Given conditions - 3 sides
    (= (length Sa) 3)
    (= (length Sb) 5)
    ; (= (length Sc) 5)
    (= (angle B) 90)

)

(:goal
    (and
        (isSegment Sc a b)
        (isSegment Sa b c)
        (isSegment Sb a c)
    )
)
)