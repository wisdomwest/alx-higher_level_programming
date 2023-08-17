#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        num = 0
        den = 0
        for score, weight in my_list:
            num += score * weight
            den += weight
        return num / den
