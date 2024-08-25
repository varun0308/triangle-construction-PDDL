from pddl.logic import Predicate, constants, variables
from pddl.core import Domain, Problem
from pddl.action import Action
from pddl.formatter import domain_to_string, problem_to_string
from pddl.requirements import Requirements

# set up variables and constants
x, y, z = variables("x y z", types=["type_1"])
p_a, p_b, p_c, s_ab, s_bc, s_ac, a_ab, a_bc, a_ac = constants("p_a p_b p_c s_ab s_bc s_ac a_ab a_bc a_ac", type_="type_1")

# define predicates
is_segment = Predicate("isSegment", x)
is_point = Predicate("isPoint", y)
is_arc = Predicate("isArc", z)

# define actions
draw_segment = Action(
    "action-1",
    parameters = [x, y],
    precondition = is_segment(x),
    effect = is_segment(x) & is_point(x) & is_point(y)
)

draw_arc = Action(
    "action-2",
    parameters = [x, y],
    precondition = is_point(x) & ~is_arc(y),
    effect = is_arc(y)
)

join_points = Action(
    "action-3",
    parameters = [x, y],
    precondition = is_segment(x),
    effect = is_segment(x) & is_point(x) & is_point(y)
)

mark_intersection = Action(
    "action-4",
    parameters = [x, y, z],
    precondition = is_arc(x) & is_arc(y) & ~is_point(z),
    effect = is_point(z)
)

# define the domain object.
requirements = [Requirements.STRIPS, Requirements.TYPING, Requirements.NEG_PRECONDITION]
domain = Domain("my_domain",
                requirements=requirements,
                types={"type_1": None},
                constants=[p_a, p_b, p_c, s_ab, s_bc, s_ac, a_ab, a_bc, a_ac],
                predicates=[is_segment, is_point, is_arc],
                actions=[draw_segment,draw_arc, join_points, mark_intersection])

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