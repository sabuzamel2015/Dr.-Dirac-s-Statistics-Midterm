import numpy as np

A = 'knows the material'

B = 'correct answer'

p_knows_material = 0.60

p_correct_given_knows_material = 0.85

p_any_student_correct = 0.59

p_knows_material_given_correct = (0.85 * 0.6)/0.59

print p_knows_material_given_correct
