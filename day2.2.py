# add a sad face for every :)
str_ex = "hello there :) my name is David :)"
def sad_face(text):
    split_str = text.split()
    result = ""
    i = 0
    for i in range(len(split_str)):
        if split_str[i] == ":)":
            split_str[i] = ":("
            i+=1
        else:
            continue

    for a in split_str:
        result+= a + " "

    return result

print(sad_face(str_ex))