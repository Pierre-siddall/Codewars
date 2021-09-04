def sum_of_integers_in_string(s):
    base_10=['0','1','2','3','4','5','6','7','8','9']
    number=''
    sum=0
    for i in range(len(s)):
        if i==len(s)-1:
            if s[i] in base_10:
                number+=s[i]
                sum+=abs(int(number))
                break
            else:
                break
        if s[i] not in base_10:
            continue
        elif s[i] in base_10 and s[i+1] in base_10:
            number+=s[i]
        elif s[i] in base_10 and s[i+1] not in base_10:
            number+=s[i]
            sum+=abs(int(number))
            number=''
    return sum