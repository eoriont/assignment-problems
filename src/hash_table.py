def hash(array, string):
    return sum(ord(char)-97 for char in string) % len(array)

def insert(array, key, value):
    bucket = hash(array, key)
    array[bucket].append((key, value))

def find(array, key):
    bucket = hash(array, key)
    return next((v for k, v in array[bucket] if k == key), None)

if __name__ == "__main__":
    array = [[], [], [], [], []]
    print(array)
    # [[], [], [], [], []]

    insert(array, 'a', [0,1])
    insert(array, 'b', 'abcd')
    insert(array, 'c', 3.14)
    print(array)
    # [[('a',[0,1])], [('b','abcd')], [('c',3.14)], [], []]

    insert(array, 'd', 0)
    insert(array, 'e', 0)
    insert(array, 'f', 0)
    print(array)
    # [[('a',[0,1]), ('f',0)], [('b','abcd')], [('c',3.14)], [('d',0)], [('e',0)]]
    # Test your code as follows:

    array = [[], [], [], [], []]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i, char in enumerate(alphabet):
        key = 'someletters'+char
        value = [i, i**2, i**3]
        insert(array, key, value)

    for i, char in enumerate(alphabet):
        key = 'someletters'+char
        output_value = find(array, key)
        desired_value = [i, i**2, i**3]
        assert output_value == desired_value

    print("Passed!")
