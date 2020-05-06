def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)

print_teacher(name='Ashley', job='Instructor', topic='Python')

print_teacher('Ashley','Instructor','Python')

# How to add more Args to the function

def print_teachers(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_teachers(name='Ashley', job='Instructor', topic='Python', second_topic='JavaScript') 


# Unpacking with Dictionaries

teacher = {
  'name':'Ashley',
  'job':'Instructor',
  'topic':'Python'
}

def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)

print_teacher(**teacher)