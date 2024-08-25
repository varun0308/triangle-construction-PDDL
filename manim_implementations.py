from manim import *
import requests, sys
from gpt_helper import talk_to_gpt
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import regex as r
question = "Construct a triangle XYZ with base 4cm, hypotenuse XZ = 5cm and YZ = 3cm"

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
)
"""

# Question_specific_conditions = """
#     (= (length Sa) 4)
#     (= (length Sc) 5)
#     (= (length Sb) 3)
# """

def get_plan(notation):
    data = {
        'domain': open("d.pddl", 'r').read(),
        'problem': open("p.pddl", 'r').read() + init + notation + "\n)" + goal
    }
    
    resp = requests.post('http://solver.planning.domains/solve', verify=False, json=data).json()
    
    construction_steps = [act['name'] for act in resp['result']['plan']]
    return construction_steps

def regex_match_function(string):
    match_fuction_name = r.search(r'\S+', string)
    match_function_parameter = r.findall(r'\s(\S+)', string)
    # print(match_fuction_name.group(), match_function_parameter)
    return (match_fuction_name.group(), match_function_parameter)

def get_construction(construction_steps):
    my_instance = DrawTriangle()
    for step in construction_steps :
        (function, parameters) = regex_match_function(step[1:-1])
        if hasattr(my_instance, function):
            method = getattr(my_instance, function)
            print(method(parameters))
        else:
            print("ERROR: Function not found")

class DrawTriangle(VoiceoverScene):
    
    def draw_arc(self, args):
        at_vertex, segment = args
        step_text = "Draw an arc from {} with length equal to {}".format(at_vertex, segment)
        return step_text

    def draw_base(self, args):
        
        [segment, point1, point2] = args
        point_a = [-2, 0, 0]
        point_b = [2, 0, 0]
        step_text = "Join the points {} and {} to make the base {}".format(point1, point2, segment)
        line_segment = Line(start=point_a, end=point_b)
        
        with self.voiceover(text = step_text) as tracker:
            self.play(Create(line_segment), run_time = tracker.duration)
            self.wait()
        return step_text

    def draw_ray():
            
        return "The ray is being drawn"

    def arc_ray_intersection(): 
            
        return "The arc and ray intersection is being drawn"

    def arc_arc_intersection(self, args):
        'a', 'b', 'c', 'sb', 'sa'
        point1, point2, intersection, segment1, segment2 = args
        step_text = "Mark the intersection for the 2 arc intersection as {}".format(intersection)
        return step_text

    def join_points(self, args):
        point1, point2, segment = args
        step_text = "Join points the {} and {} to make the segment {}".format(point1, point2, segment)
        return step_text

    def construct(self):
        self.set_speech_service(GTTSService(transcription_model='base'))
        converted_notation = talk_to_gpt(question)
        steps = get_plan(converted_notation)
        print(steps)
        get_construction(steps)