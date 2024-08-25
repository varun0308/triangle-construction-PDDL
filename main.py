from primitive_action import Actions
import json 

def is_goal(state):
    for value in list(state.values()) :
        if value == False:
            return False
    return True


# An object -> will have triangle and its segment and arcs, and the states
solver = Actions()

function_list = solver.__dict__

# Will contain list of all initial actions actions
frontier = []
for action_name, action in function_list.items():
        if callable(action):
            frontier.append(action)
            
# will use it later    
lst_actions = frontier

# The tree generation
while(len(frontier)):
    action = frontier.pop()
    current_state = solver.states[-1]
    
    if(is_goal(current_state)):
        print("Goal reached!, triangle complete")
        break
    
    for action in lst_actions :
        for x in ['AB', 'BC', 'CA']:
            frontier.append(action(x))
    

# solver.draw_segment('AB')
# # solver.draw_segment('CA')
# print(solver.states)
print(frontier)