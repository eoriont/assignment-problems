def parseData(data):
    return [[parseString(s) for s in line.split(',')] for line in data.split('\n')]


def parseString(string):
    if string[0] == string[-1] == '"':
        return string[1:-1]
    elif '.' in string:
        return float(string)
    else:
        return int(string)


string = '"alpha","beta","gamma","delta"\n1,2,3,4\n5.0,6.0,7.0,8.0'
print(parseData(string))
