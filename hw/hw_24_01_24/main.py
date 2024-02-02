from dotenv import load_dotenv
import os

load_dotenv()

login = os.environ.get('LOGIN')
password = os.environ.get('PASSWORD')

print(login)
print(password)
