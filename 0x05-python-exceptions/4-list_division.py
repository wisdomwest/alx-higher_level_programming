#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            reminder = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            reminder = 0
        except ZeroDivisionError:
            print("division by 0")
            reminder = 0
        except IndexError:
            print("out of range")
            reminder = 0
        finally:
            result.append(reminder)
    return result
