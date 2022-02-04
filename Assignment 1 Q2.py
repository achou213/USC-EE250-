a_dict = {"animal" : "Dog", "name" : "Juno", "owner" : "Andrew"}
a_list = ["Andrew", "Chou", "USC", "Sophomore"]
a_word = "Hello World"

for word in a_list:
    print(word)
for i in a_dict: 
    print(i, ':', a_dict[i])
for j in range(len(a_word)):
    print(a_word[j])