import base64

m = """
F0gcBQYRV0FBS09VUEIVQFdTGEhDUEIRXV5eCQ4IBQBVEgg
SSwocBAAXX1dWS0NPVwAUVF1AGBxI UF9SFVtcDx0KFAwQX
lcVQE9IEQYaW1dECQIKHhFVEggSSxoBHAoRWVdWS0NPVxcT
UFBbGBxIUF9S FUFTCgpIXEVVVF1dS09VUEIFW1wTSxI=
"""

key = 'looper222'

result = []
decoded_m = base64.b64decode(m)

for i, c in enumerate(decoded_m):
    result.append(chr(c ^ ord(key[i % len(key)])))

print(''.join(result))