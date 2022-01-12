import random
import time
x = 10
eu = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Republic Of Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany',
          'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania',
          'Slovakia', 'Slovenia', 'Spain', 'Sweden']
    
num = random.randint(0,26)
country = eu[num]
while x > 0:   
    print('you have',x,'tries remaining')
    ans = input('guess a eu country ')
    time.sleep(1)
    if ans.strip().title() == country:
        print('YOU ARE CORRECT!!!')
        break
    elif ans.strip().title() != eu:
        print('not a valid input')
        time.sleep(1)
        print('')
        
    elif ans.strip().title() != country:
        print('Try again!')
    
    
    
        
time.sleep(1.5)   
print('hard luck')
    
    

