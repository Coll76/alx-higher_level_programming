#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b
    except Exception:
        div = None
    finally:
        if div is not None:
            print("Inside result: {}".format(div))
        else:
            print("Inside result: ", None)
    return div
