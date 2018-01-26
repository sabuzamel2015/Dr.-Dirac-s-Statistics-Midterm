import numpy as np

# Determined that students knowing the material will be A in 
A = 'knows the material'

# Determined that students that got the correct answer will be B
B = 'correct answer'

# Probability that student knows the material 
p_knows_material = 0.60

# Probability that student got the correct answer given that thet know the material. In other words, P(B|A).
p_correct_given_knows_material = 0.85

# Probability that any student got the correct answer, regardless of their knowlegde of the material
p_any_student_correct = 0.59

#Probability that a student knows the material given that they got the correct answer. In other words, P(A|B).
p_knows_material_given_correct = (0.85 * 0.6)/0.59

print p_knows_material_given_correct
