from pddl.logic import Predicate, constants, variables
from pddl.core import Domain, Problem
from pddl.action import Action
from pddl.formatter import domain_to_string, problem_to_string
from pddl.requirements import Requirements

# set up variables and constants
p1, p2 = variables("p1 p2", types="type_1")
s1 = variables("s1", types="type_2")
a1, a2 = variables("a1 a2", types="type_3")
p_a, p_b, p_c = constants("p_a p_b p_c", type_="type_1")
s_ab, s_bc, s_ac = constants("s_ab s_bc s_ac", type_="type_2")
a_ab, a_bc, a_ac = constants("a_ab a_bc a_ac", type_="type_3")

# define predicates
is_segment = Predicate("isSegment", s1)
is_point = Predicate("isPoint", p1)
is_arc = Predicate("isArc", a1)

# define actions
draw_segment = Action(
    "action-1",
    parameters = [p1, p2, s1],
    precondition = is_segment(s1),
    effect = is_segment(s1) & is_point(p1) & is_point(p2)
)

draw_arc = Action(
    "action-2",
    parameters = [a1, p1],
    precondition = is_point(p1) & ~is_arc(a1),
    effect = is_arc(a1)
)

join_type_1 = Action(
    "action-3",
    parameters = [s1, p1, p2],
    precondition = is_segment(s1),
    effect = is_segment(s1) & is_point(p1) & is_point(p2)
)

mark_intersection = Action(
    "action-4",
    parameters = [a1, a2, p1],
    precondition = is_arc(a1) & is_arc(a2) & ~is_point(p1),
    effect = is_point(p1)
)

# define the domain object.
requirements = [Requirements.STRIPS, Requirements.TYPING]
domain = Domain("my_domain",
                requirements=requirements,
                types={"type_2": None, "type_1": None, "type_3":None},
                constants=[p_a, p_b, p_c, s_ab, s_bc, s_ac, a_ab, a_bc, a_ac],
                predicates=[is_segment, is_point, is_arc],
                actions=[draw_segment])

print(domain_to_string(domain))

problem = Problem(
    "problem-1",
    domain=domain,
    requirements=requirements,
    objects=[p_a, p_b, p_c, s_ab, s_bc, s_ac, a_ab, a_bc, a_ac],
    init=[is_segment(s_ab), ~is_point(p_a), ~is_point(p_b)],
    goal=is_segment(s_ab) & is_point(p_a) & is_point(p_b))

print(problem_to_string(problem))

from pddl import parse_domain, parse_problem

with open("d.pddl", 'w') as f: 
    f.write(domain_to_string(domain))


with open("p.pddl", 'w') as f: 
    f.write(problem_to_string(problem))