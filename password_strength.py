import re

password = "password1"
score = 0

def password_strength(password):
    global score

    if bool(re.search(r'[~!@#$%^&*()_+{}":;\']', password)) == True:
        score += 1
    if bool(re.search(r'[0-9]', password)) == True:
        score += 1
    if bool(re.search(r'^.{8,}$', password)) == True:
        score += 1
    if bool(re.search(r'[A-Z]', password)) == True:
        score += 1

password_strength(password)

if score < 2:
    print("Very Weak")
if score == 2:
    print("Weak")
if score == 3:
    print("Strong")
if score > 3:
    print("Very Strong")