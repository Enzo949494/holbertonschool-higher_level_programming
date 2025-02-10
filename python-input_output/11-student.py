#!/usr/bin/python3
"""shows how to save an object's data to a file (serialization)
and restore it later (deserialization)"""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student"""
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
