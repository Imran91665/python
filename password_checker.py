user_name=input("Enter your name: ")
password=input("Enter your password: ")
hidden_password='*'*len(password)
print(f'Hey,{user_name}.Your password {hidden_password} is {len(password)} digit ')