#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_tmp = [0] * list_length
    i = 0
    while (i < list_length):
        try:
            list_tmp[i] = my_list_1[i] / my_list_2[i]
            i = i + 1
        except ValueError:
            list_tmp[i] += 0
            print("wrong type")
            i = i + 1
            pass
        except TypeError:
            list_tmp[i] += 0
            print("wrong type")
            i = i + 1
            pass
        except IndexError:
            list_tmp[i] += 0
            print("out of range")
            i = i + 1
            pass
        except ZeroDivisionError:
            list_tmp[i] += 0
            print("Division by Zero")
            i = i + 1
            pass
        finally:
            pass
    return list_tmp
