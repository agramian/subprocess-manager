#!/usr/bin/python
# Filename: assert_variable_type.py

from types import *

def assert_variable_type(variable, expected_type, raise_exception=True):
    """Return True if a variable is of a certain type or types.
    Otherwise raise a ValueError exception.

    Positional arguments:
    variable -- the variable to be checked
    expected_type -- the expected type or types of the variable
    raise_exception -- whether to raise an exception or just return
                        False on failure, with error message
    """
    # if expected type is not a list make it one
    if not isinstance(expected_type, list):
        expected_type = [expected_type]
    # make sure all entries in the expected_type list are types
    for t in expected_type:
        if not isinstance(t, type):
            raise ValueError('expected_type argument "%s" is not a type' %str(t))
    # make sure raise_exception is a bool
    if not isinstance(raise_exception, bool):
        raise ValueError('raise_exception argument "%s" is not a bool' %str(raise_exception))
    # check the type of the variable against the list
    # then raise an exception or return True
    if not len([(t) for t in expected_type if isinstance(variable, t)]):
        error_message = '"%s" is not an instance of type %s. It is of type %s' %(str(variable),' or '.join([str(t) for t in expected_type]), str(type(variable)))
        if raise_exception:
            raise ValueError(error_message)
        else:
            return False, error_message
    return True, None
