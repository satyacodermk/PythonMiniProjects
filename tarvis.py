#tarvis: a Security System bot

known_users=['Alice','Bob','Claire','Dan','Emma','Kumar','Yogi','Raja']

while True:
    print('Hi My name is Tarvis')
    name=input('What is your name?.').strip().capitalize()

    if name in known_users:
        print('Hello',name,', Nice to see you...')
        remove=input('Would you like to removed from the system (y/n)?:').strip().lower()
         
        if remove=='y':
            known_users.remove(name)
        elif remove=='n':
            print("No problem, I didn't want you to leave anyway!")
        break
    else:
        print('Hmmmm I do\'t think I have met you yet! ',name)
        add_me=input('Would you like to be added to the system (y/n)?: ').strip().lower()
        if add_me=='y':
            known_users.append(name)
            print('New Users Added Successfully...')
        elif add_me=='n':
            print('No worries, see you around!')
        break

print('Bye, I will See you Later...')