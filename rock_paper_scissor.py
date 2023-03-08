import random
def play():
    i=input("what's your choice: r, p, s\n")
    r=random.choice(['r', 'p', 's'])
    if is_win(i,r):
        return 'you win!'
    return 'you loose!'
def is_win(p,c):
    if(p=='r' and c=='s' or p=='s' and c=='p' or p=='p' and c=='r'):
        return True
print(play())

          