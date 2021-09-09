def camel_case(string):
    string_list=string.split()
    for i in range(len(string_list)):
        string_list[i]=string_list[i][0].upper()+string_list[i][1:]
    return ''.join(string_list)

if __name__ == '__main__':
    assert camel_case('hello world')=='HelloWorld'
    assert camel_case('camel case lettering')=='CamelCaseLettering'