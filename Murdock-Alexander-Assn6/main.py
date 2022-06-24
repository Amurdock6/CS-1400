import random

i = 1
verbs = ('Play With ', 'Throw With ', 'Pass With ', 'Jump Over ', 'Run Past ', 'Dribble Around ', 'Shoot With ', 'Win Against ', 'Lose Against ', 'Dunk On ')
adjectives = ('Pro ', 'Short ', 'Tall ', 'Fat ', 'Skinny ', 'Fast ', 'Slow ', 'Strong ', 'Weak ', 'Young ')
nouns = ('John Stockton.', 'Michael Jordan.', 'Allen Iverson.', 'Kobe Bryant.', 'Lebron James.', 'Ray Allen.', 'Vince Carter.')

print('\n')
print('Basketball List Generator')
print('')

for v in verbs:
    if i >= 11:
        print('')
        break
    for a in adjectives:
        if i >= 11:
            break
        for n in nouns:
            print(str(i) + ' - ' + random.choice(verbs) + random.choice(adjectives) + random.choice(nouns))
            i = i + 1
            if i >= 11:
                break  
