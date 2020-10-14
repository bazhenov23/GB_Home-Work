word = input("Напишите короткое словосочетание разделенное пробелом: ")
my_words = []
i = 0
for el in range(word.count(' ') + 1):
    my_words = word.split()
    if len(str(my_words)) <= 10:
        print(f" {i+1} {my_words[el]}")
        i += 1
    else:
        print(f" {i+1} {my_words[el][0:10]}")
        i += 1
