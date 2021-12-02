from prefect import task, Flow, Parameter

# Constants
PUSH_TO_PREFECT_CLOUD_DASHBOARD = True

# Tasks
@task
def get_person_description(name, age):
    return name + ", you are " + age + "."

@task
def display_person_descriptions(desc1, desc2):
    print(desc1)
    print(desc2)

@task
def get_age_avg(age1, age2):
    return str((int(age1) + int(age2)) / 2)

@task
def get_avg_description(name1, name2, avg):
    return name1 + ", " + name2 + ", your average age is " + avg + "."

@task
def display_avg_description(desc):
    print(desc)

# Flow
with Flow('run-sample') as flow:
    first_person_age = Parameter('first_person_age', default="20")
    second_person_age = Parameter('second_person_age', default="30")
    first_person_name = Parameter('first_person_name', default="Toto")
    second_person_name = Parameter('second_person_name', default="Titi")

    first_person_description = get_person_description(first_person_name, first_person_age)
    second_person_description = get_person_description(second_person_name, second_person_age)

    display_person_descriptions(first_person_description, second_person_description)

    age_avg = get_age_avg(first_person_age, second_person_age)
    avg_description = get_avg_description(first_person_name, second_person_name, age_avg)

    display_avg_description(avg_description)

# Run
if __name__ == '__main__':
    if PUSH_TO_PREFECT_CLOUD_DASHBOARD:
        flow.register(project_name='sample')
    else:
        flow.run()