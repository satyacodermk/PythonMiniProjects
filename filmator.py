#film Simulator 

films={'Finding Dory':[3,500],
        'KGF1':[18,530],
        'Ghost Busters':[15,950],
        'Tarzan':[12,519]
    }

while True:
    choice=input('What film would you like to watch? :').strip()
    
    if choice in films.keys():
        age=int(input("How old are you? :").strip())
        if age>=films[choice][0]:
            print('You can Go, by paying',films[choice][1],'rupees.\n\t Enjoy the film...')
        else:
            print("Sorry Your are to small to watch the movie...")
    else:
        print("Sorry, There is no such Film in this theator")
    
    break

