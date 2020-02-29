def fix_bounds(rotated, range_init, range_fin):
    # after rotation, see if it's w/in its bounds
    # if not, rotate
    # 2 - 9, 3: 7 -> 10. 10 > 9 . 10 - 9 = 1 2-1 + 1
    if range_fin > range_init:
        # encode op
        comparison = lambda x,y: x > y
        operation = lambda x: x - range_fin - 1
        looper = lambda x: range_init + x
    else: 
        # decode op
        comparison = lambda x,y: x < y
        operation = lambda x: range_fin - x - 1
        looper = lambda x: range_init - x

    if comparison(rotated, range_fin):
        delta = operation(rotated)
        new = looper(delta)
    else:
        # no-op
        new = rotated
    return new

def decode(msg, setting):
    rotation = setting + 12
    if rotation > 26:
        rotation = rotation - 26
#    print(msg)
    new_msg = ''
    capmin = 65
    capmax = 90
    lowmin = 97
    lowmax = 122

    for letter in msg:
    #    print(letter)
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
        
        
def encode(msg, setting):
    rotation = setting + 12
    if rotation > 26:
        rotation = rotation - 26
#    print(msg)
    rotation = -rotation
    new_msg = ''
    capmin = 65
    capmax = 90
    lowmin = 97
    lowmax = 122

    for letter in msg:
#        print(letter)
        val = ord(letter)
        encoded = val + rotation
        if val >= 65 and val <= 90:
            rotated = fix_bounds(encoded, capmax, capmin)
        elif val >= 97 and val <= 122:
            rotated = fix_bounds(encoded, lowmax, lowmin)
        else:
            rotated = val
#        print("val: " + str(val))
#        print("rotated: " + str(rotated))
        new_msg = new_msg + chr(rotated)
    return new_msg

encoded = encode("hello world", 11)
print(encoded)

decoded = decode(encoded, 11)
print(decoded)

encoded = encode("abcxyz", 1)
print(encoded)

decoded = decode(encoded, 1)
print(decoded)

print("Fey")
print(decode("ADWP EO UKQN BWRKNEPA DWNNU LKPPAN OAHH", 18))
print(encode("It must me the patronus. What is your Patronus, Fey?", 7))
print(decode(encode("It must me the patronus. What is your Patronus, Fey?", 7),7))
print(decode("uv jsbl. dohaz fubyz",7))
print(encode("my patronus is a penguin!",12))

print("Roxy")
print(decode("ADK EO UKQN BWRKNEPA OKYYAR LHWUAN", 18))
print(encode("Roxanne is my favorite soccer player. Followed closely by Diego Chara and the Alicorns", 7))
print(decode(encode("Roxanne is my favorite soccer player. Followed closely by Diego Chara and the Alicorns", 7),7))

print(encode("what a fun playdate! Wolf club rocks!", 3))
