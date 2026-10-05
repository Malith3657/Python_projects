user_word = input("Enter Your Word -")

word_reversed = user_word[::-1]

if user_word == word_reversed:
    print(f"{user_word} is palindrome word" )
else:
    print(f"{user_word} is not palindrome word" )

