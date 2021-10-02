from flask_bcrypt import Bcrypt 

bcrypt = Bcrypt() 

password = 'akshit12' 

hashedPassword = bcrypt.generate_password_hash( password = password)

# print(hashedPassword)

check = bcrypt.check_password_hash(hashedPassword, 'akshit12')
print(check)