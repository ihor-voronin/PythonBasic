# __str__(self)	To get called by built-int str() method to return a string representation of a type.
# __repr__(self)	To get called by built-int repr() method to return a machine readable representation of a type.
# __unicode__(self)	To get called by built-int unicode() method to return an unicode string of a type.
# __format__(self, formatstr)	To get called by built-int string.format() method to return a new style of string.
# __hash__(self)	To get called by built-int hash() method to return an integer.
# __nonzero__(self)	To get called by built-int bool() method to return True or False.
# __dir__(self)	To get called by built-int dir() method to return a list of attributes of a class.
# __sizeof__(self)	To get called by built-int sys.getsizeof() method to return the size of an object.


class MyClass:
    def __str__(self):
        print("call str")
        return "str"

    def __repr__(self):
        print("call repr")
        return "repr"


class User:
    def __init__(self, user_id, user_type, name):
        self.id = user_id
        self.type = user_type
        self.name = name

    def __repr__(self):
        return f"User id:{self.id} type:{self.type} name:{self.name}"


if __name__ == "__main__":
    my_user = User(11, "Admin", "Alex")
    print(my_user)

    instance = MyClass()

    print(str(instance))  # str(instance)
    print(instance)
    print(f"{instance}")

    print(
        [instance]
    )
