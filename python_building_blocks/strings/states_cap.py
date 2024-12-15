import sys

states = []
capital = []
for i in range (1, len(sys.argv)):
    index_of_space = sys.argv[i].find(' ')
    states.append(argv[i][:index_of_space])
    capitals.append(argv[i][index_of_space + 1 :])
    
print('%-15s %-15s'%('STATE', 'CAPITAL'))
print('-'*32)
for i in range (len(sys.argv) - 1):
    print('|%-15s|%-15s|'%(states[i].capitalize(),capital[i].capitalize()))
    