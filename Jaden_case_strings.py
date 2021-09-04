def to_jaden_case(string):
    string_list=list(string)
    string_list[0]=string_list[0].upper()
    for i in range(len(string_list)):
        if string_list[i]==' ':
            string_list[i+1]=string_list[i+1].upper()
    return "".join(string_list)