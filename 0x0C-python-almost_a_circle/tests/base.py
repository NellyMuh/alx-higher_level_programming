#!usr/bin/python3
""""Define class"""

    class Base:
    """Base class with __nb_objects"""
        __nb_objects = 0

        def __init__(self, id=None):
            """Initialises Base """
            if id is not None:
                self.id = id
            else:
                Base.__nb_objects +=1
                self.id = Base.__nb_objects
