print('hello\nworld')

print('hello\tworld')

print('hello\rworld') #覆盖前面的字符串

print('hello\bworld') #退一个格

print('http:\\\\baidu.com')

print('老师说:\'大家好\'')

print(r'hello\nworld')

import requests
r=requests.get(r"https://api.github.com/users/acombs/starred")
r.json()
