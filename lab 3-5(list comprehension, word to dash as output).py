

secret = input("Please enter the secret: ")

secret_red = ["-" for let in secret if let.isalpha()]
#.isalpha() is alphabets in letter
#.isdigit() is digits in number


print("redacted: ", "".join(secret_red))
