slist = ["something", "anotherthing", "four", "six"]
print(slist)
slist[3:3] = ["five"]
print(slist)
num_list = [9, 8, 68, 438, 798, 138798, 317, -789, 79641]
print(min(num_list))
print(max(num_list))
print(sum(num_list))
print(sorted(num_list))
print(num_list)


def list_sum(in_list):
    sum = 0
    for i in in_list:
        sum += i
    return sum


print(list_sum(num_list))


def list_min(in_list):
    min_num = in_list[0]
    for i in in_list:
        if i < min_num: min_num = i
    return min_num


print(list_min(num_list))


def partition(in_list):
    l_pointer = 1
    r_pointer = len(in_list) - 1
    print(in_list)
    pivot = in_list[0]
    while l_pointer < r_pointer:
        while in_list[l_pointer] < pivot:
        if in_list[l_pointer] > in_list[r_pointer]:
            print((" - " * 8) + f"{in_list[l_pointer]}" + (" - " * 8) + f"{in_list[r_pointer]}")
            in_list[l_pointer], in_list[r_pointer] = in_list[r_pointer], in_list[l_pointer]
            print(in_list)
        l_pointer += 1
        r_pointer -= 1
    return in_list


print(partition(num_list))

names = ["Áleš", "Bořek", "Zdeněk", "Liška", "Karolína"]
diacritics = {
    "š": "s",
    "č": "c",
    "ě": "e",
    "ř": "r",
    "ž": "z",
    "ý": "y",
    "á": "a",
    "í": "i",
    "é": "e",
    "ď": "d",
    "ť": "t",
    "ň": "n",
    "ů": "u",
    "ú": "u"
}
def remove_diacritcs(item):
    item = item.lower()
    for i in item:
        if i in diacritics:
            item = item.replace(i, diacritics[i])
    return item
names = list(map(remove_diacritcs,names))
print(names)


