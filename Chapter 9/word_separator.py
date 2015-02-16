def main():
    user_string = input("Enter a sentence where each word starts with a capital letter but there are no spaces between the words: ")
    new_string = user_string[0].upper()

    index = 1
    while index < len(user_string):
        if user_string[index].isupper():
            new_string += ' '
            new_string += user_string[index].lower()
        else:
            new_string += user_string[index]
        index += 1

    print(new_string)

main()
