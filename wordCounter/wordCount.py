#! /bin/python3


# Function that takes input txt file and returns unsorted dictionary
def get_dictionary(filename):
    with open('books/' + filename, 'r', encoding='utf-8') as f:
        dic = {}
        context = f.read()
        unwanted_car = [',', '.', '\n', '/', '>', '<', '(', ')', '-', '?', '!', ':', ';', '*', '"']
        # Loop for removing unwanted characters
        for car in unwanted_car:
            context = context.replace(car, '')
        context = context.lower().split(' ')
        # Making a dictionary
        for car in context:
            if car not in dic:
                dic[car] = 1

            else:
                dic[car] += 1
    del dic['']
    return dic


# Making the sorted list of items.

def sorted_dict(file):
    dic = get_dictionary(file)
    sort_dic = sorted(dic.items(), key=lambda dic: dic[1], reverse=True)
    return sort_dic
