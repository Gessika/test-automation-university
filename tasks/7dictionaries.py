stuff = {'food': 15, 'energy': 100, 'enemies': 3}
'''
print(stuff.get('food'))  #return a value of a key
print(stuff.items()) #items method accept a dictionary as argument, and acts on entire dictionary
print(stuff.keys())  #returns a view of keys
'''
'''
print(stuff.popitem())#removes last item
'''
'''
# set default method: to see what the value is of key on a dict, but more important -
# allows to set a default value when a key is not in a dictionary and to add that value to the dict:
print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends", 123))
print(stuff)
'''
#update
new_items = {'rokcs': 23, 'banana': 5}
stuff.update(new_items)
print(stuff)