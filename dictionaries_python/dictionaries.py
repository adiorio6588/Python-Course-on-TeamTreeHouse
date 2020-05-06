course = {'teacher':'Ashley', 'title': 'Introductioning Dictionaries', 'level':'Beginner'}

print(course['teacher'])


print(course.keys())
print(course.values())


# Sorted alphabetical 
print(sorted(course.keys()))
print(sorted(course.values()))


course_two = {'teacher':'Gill', 'title': 'Introductioning Dictionarie Part 2', 'level':'Advance'}
course_two['teacher'] = 'Treasure'
course_two['levels'] = 'Intermediate'

# Adding to dictionay
course_two['stages'] = 2

# Deleting from dictionary
del(course_two['stages'])

print(course_two)

for item in course:
    print(course[item])

for key, value in course.items():
    print(key)
    print(value)


