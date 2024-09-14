# No return type with Argument
def greate_by_name(name):
    print("hello", name)

greate_by_name("rahul")


# No return type with default argument---> this is not in java

def hello_default_arg(name= "pk"):
    print("Hello", name)

hello_default_arg("rahul")    #here rahul will be called
hello_default_arg()     # here pk will be called. it means if we are not passing any value then me default parameter(pk) is called
hello_default_arg(name="Riddhi") # positional argument