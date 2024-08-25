(define (domain triangle)

(:requirements :strips :typing :negative-preconditions :fluents :equality)

(:types segment point angle)

(:predicates
    (begin_with ?s - segment ?p - point)
    (end_with ?s - segment ?p - point)
    (isAngle ?A - angle ?p - point)
    (isSegment ?s - segment ?p1 ?p2 - point)
    (isArc ?p - point ?s - segment)
    (isPoint ?p - point)
    (isRay ?A - angle ?s1 - segment ?p - point ?s2 - segment)
)
(:functions
    (length ?s - segment)
    (angle ?A - angle)
)

(:action draw_base
    :parameters (?s1 - segment
                 ?p1 ?p2 - point)
    :precondition (and
        (not (= ?p1 ?p2))
        (not (isPoint ?p1))
        (not (isPoint ?p2))
        (> (length ?s1) 0)
    )
    :effect (and
        (isPoint ?p1)
        (isPoint ?p2)
        (isSegment ?s1 ?p1 ?p2)
    )
)

(:action draw_ray
    :parameters (?p1 ?p2 - point
                ?s1 ?s2 - segment
                ?A1 - angle)
    :precondition (and
        (not (= ?p1 ?p2))
        (not (= ?s1 ?s2))
        (or
            (isSegment ?s1 ?p1 ?p2)
            (isSegment ?s1 ?p2 ?p1)
        )
        (isAngle ?A1 ?p1)
        (> (angle ?A1) 0)
        (or
            (begin_with ?s2 ?p1)
            (end_with ?s2 ?p1)
        )
    )
    :effect (and
        (isRay ?A1 ?s1 ?p1 ?s2)
    )
)

(:action draw_arc
    :parameters (?p1 - point
                 ?s1 - segment)
    :precondition (and
        (isPoint ?p1)
        (> (length ?s1) 0)

    )
    :effect (and
        (isArc ?p1 ?s1)
    )
)

(:action arc_arc_intersection
    :parameters (?p1 ?p2 ?p3 - point
                ?s1 ?s2 - segment)
    :precondition (and
        (not (= ?p1 ?p2))
        (not (= ?p1 ?p3))
        (not (= ?p2 ?p3))
        (not (= ?s1 ?s2))
        (isArc ?p1 ?s1)
        (isArc ?p2 ?s2)
        (begin_with ?s1 ?p1)
        (end_with ?s1 ?p3)
        (begin_with ?s2 ?p2)
        (end_with ?s2 ?p3)
    )
    :effect (and
        (isPoint ?p3)
    )
)

(:action arc_ray_intersection
    :parameters (?p1 ?p2 ?p3 - point
                ?s1 ?s2 ?s3 - segment
                ?A - angle)
    :precondition (and
        (not (= ?p1 ?p2))
        (not (= ?p1 ?p3))
        (not (= ?p2 ?p3))
        (not (= ?s1 ?s2))
        (not (= ?s1 ?s3))
        (not (= ?s2 ?s3))
        
        (isArc ?p1 ?s1)
        (isRay ?A ?s2 ?p2 ?s3)
        
        (or
            (begin_with ?s1 ?p1)
            (end_with ?s1 ?p1)
        )
        (or
            (begin_with ?s2 ?p2)
            (end_with ?s2 ?p2)
        )
    )
    :effect (and
        (isPoint ?p3)
    )
)

(:action join_points
    :parameters (?p1 ?p2 - point
                ?s1 - segment)
    :precondition (and
        (isPoint ?p1)
        (isPoint ?p2)
        (not (= ?p1 ?p2))
        (begin_with ?s1 ?p1)
        (end_with ?s1 ?p2)
        ; (or
        ;     (and 
        ;         (begin_with ?s1 ?p2)
        ;         (end_with ?s1 ?p1)
        ;     )
        ;     (and 
        ;         (begin_with ?s1 ?p1)
        ;         (end_with ?s1 ?p2)
        ;     )
        ; )
    )
    :effect (and
        (isSegment ?s1 ?p1 ?p2)
    )
)
)