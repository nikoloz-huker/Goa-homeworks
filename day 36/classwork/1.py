                                          #1
def check_last_name(last_name):
    return last_name.lower().startswith('g')


                                        #2
def make_negative(num):
    if num < 0:
        return -num
    else:
        return -num
                                       #3

def round_to_nth_decimal(num, n):
    return round(num, n)

                                      #4
def sort_string(s):
    return "".join(sorted(s))

                                      #5
def join_with_symbol(lst, symbol):
    return symbol.join(lst)

                                      #6
def normalize_input(s):
    return ' '.join(s.split())