import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
student_details = [('James', 5, 48.5), ('Mbali', 6, 52.5), ('Thato', 15, 60.1), ('Shiv', 10, 60.2)]

student = np.array(student_details, dtype=data_type)
print("Original array:")
print(student)
print("Array sorted by height:")
print(np.sort(student, order='height'))