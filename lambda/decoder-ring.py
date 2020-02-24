def fix_bounds(rotated, range_init, range_fin):
    # after rotation, see if it's w/in its bounds
    # if not, rotate
    if range_init > range_fin:
        comparison = lambda: x < y
        operation = lambda: x + y
    else: 
        comparison = lambda: x > y
        operation = lambda: x - y
    if comparison(rotated, range_max):
        delta = rotated - range_max
        new = range_min + delta - 1
    else:
        # no-op
        new = rotated
    return new

def encode(msg, rotation):
    print(msg)
    new_msg = ''
    capmin = 65
    capmax = 90
    lowmin = 97
    lowmax = 122

    for letter in msg:
        print(letter)
        val = ord(letter)
        encoded = val + rotation
        if val >= 65 and val <= 90:
            rotated = fix_bounds(encoded, capmin, capmax)
        elif val >= 97 and val <= 122:
            rotated = fix_bounds(encoded, lowmin, lowmax)
        else:
            rotated = val

        new_msg = new_msg + chr(rotated)
    return new_msg
        
        
def decode(msg, rotation):
    rotation = -rotation
    return(encode(msg, rotation))
            


encoded = encode("hello world", 11)
print(encoded)

decoded = decode(encoded, 11)
print(decoded)

