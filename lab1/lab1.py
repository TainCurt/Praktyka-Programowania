
def Add(s):
    if s == "":
        return 0
    elif type(s) == int:
        return s
    else:
        s = s.replace("\n", ",")
        s_list = s.split(",")
        sum = 0
        for i in s_list:
            if not i.isdigit():
                raise ValueError("niepoprawne")
            sum += int(i)
        return sum
