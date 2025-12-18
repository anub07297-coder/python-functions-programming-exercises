# Your code goes here:
def render_person(name,dob,eyeColor,age,gender):
    """function that returns multiple parameters as a single string."""  
    return f"{name} is a {age} years old {gender} born in {dob} with {eyeColor} eyes"


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))