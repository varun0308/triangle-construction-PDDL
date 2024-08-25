import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

system = """You are a mathematics professor helping me solve high school construction problems.
For any question, your goal is to convert the notation into the following notation:
a, b, c - point
Sa, Sb, Sc - segment
A, B, C - angle
The triangle is structured as :
Points a and b are opposite to segment Sc containing the angle C.
Constraints:
1. The converted number of notations must not exceed the given number of information in the question
2. If a "base" is mentioned in a question, it should be the segment Sa with points b and c containing angle A, else do ascending order
3. The converted triangle should be in the form of "abc" with 3 segments and 3 sides
Return a structure of the following form with specific commands:
1. If side is given: (= (length <Given length name>) <Value of that side>)
2. If angle is given: (= (angle <given enclosed angle name>) <given value of that angle>)
Example: "Construct a triangle PQR with PQ=3cm, QR=4cm and PR with 5cm"
Answer: "
(= (length Sa) 3)
(= (length Sb) 4)
(= (length Sc) 5)"
"""

def talk_to_gpt(prompt):
    messages = [ 
        {"role": "system", "content": system},
        {"role": "user", "content": prompt}
    ]
    
    # Generate a response
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.0
        )
    return response.choices[0].message["content"]

# question = "Construct a triangle XYZ with base 4cm, hypotenuse XZ = 5cm and angle Z=90"
# print(talk_to_gpt(question))