#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ne_list = []
    if len(my_list_1) < list_length or len(my_list_2) < list_length:
        print("out of range")
    
    for i in range(len(my_list_1)):
        try:
            result = my_list_1[i] / my_list_2[i]
            ne_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            ne_list.append(0)
        except TypeError:
            print("wrong type")
            ne_list.append(0)
        finally:
            pass
    return ne_list
