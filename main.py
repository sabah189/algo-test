print("---- Welcome to the a recommendation program ---- \n")

response_user = []

# asking user and collect information

print("1) what your favorite movie genre ? \n (a) action \n (b) romantic \n (c) science fiction \n (d) horror \n \n ")
response_user.append(input("your answer is : "))

print("1) what your favorite game genre ? \n (a) racing \n (b) puzzle \n (c) adventure \n (d) sport \n \n ")
response_user.append(input("your answer is :"))

print("1) what your favorite music genre ? \n (a) jazz \n (b) classical \n (c) metal \n (d) rock \n \n ")
response_user.append(input("your answer is :"))

print("1) what your favorite place genre ? \n (a) nature \n (b) museum \n (c) beach \n (d) shop \n \n ")
response_user.append(input("your answer is :"))

print("1) what your favorite activities genre ? \n (a) travel \n (b) sport \n (c) learning \n (d) reading \n \n ")
response_user.append(input("your answer is :"))

# analyze information

movies = {'action_1': 'Black Adam', 'action_2': 'Uncharted', 'romantic_1': 'The Vow', 'romantic_2': 'Adrift',
          'science_fiction_1': 'Tenet', 'science_fiction_2': 'Inception', 'horror_1': 'It', 'horror_2': 'Orphan'}
games = {'racing_1': 'Asphalt 9', 'racing_2': 'Traffic Rider', 'puzzle_1': 'portal 2', 'puzzle_2': 'The Witness',
         'adventure_1': 'Spider man', 'adventure_2': 'God of War', 'sport_1': 'fifa 22', 'sport_2': 'NBA2K 22'}
songs = {'jazz_1': 'Summertime', 'jazz_2': 'Fly me to the moon', 'classical_1': 'Time to say goodbye',
         'classical_2': 'Clair de lune', 'metal_1': 'Evil', 'metal_2': 'Walk', 'rock_1': 'Roxanne',
         'rock_2': 'Free bird'}
places = {'nature_1': 'Desert Sand Dunes in south africa', 'nature_2': 'Everest in Nepal',
          'museum_1': 'Le Louvre in paris', 'museum_2': 'The British Museum in London',
          'beach_1': 'flamingo beach in UAE', 'beach_2': 'Reethi Rah in maldives', 'shop_1': 'Milano in italy',
          'shop_2': 'Paris in France'}
activities = {'travel_1': 'dead sea in jordan', 'travel_2': 'ibiza in spain', 'sport_1': 'Ralley dakar',
              'sport_2': 'skating', 'learning_1': 'new language', 'learning_2': 'how to cook',
              'reading_1': 'and then there were none', 'reading_2': 'crooked house'}

question_genre = ['movies', 'games', 'songs', 'places', 'activities']

print(response_user)

for i in range(5):
    print("Maybe you would like")

# If the user choose A

    if response_user[i].lower() == 'a':
        if question_genre[i] == 'movies':
            print(question_genre[i], ': \n 1- ', movies["action_1"], ' \n 2- ', movies["action_2"])
        elif question_genre[i] == 'games':
            print(question_genre[i], ':  \n 1-', games["racing_1"], '\n 2- ', games["racing_2"])
        elif question_genre[i] == 'songs':
            print(question_genre[i], ': \n 1-', songs["jazz_1"], '\n 2-', songs["jazz_2"])
        elif question_genre[i] == 'places':
            print(question_genre[i], ': \n 1-', places["nature_1"], '\n 2-', places["nature_2"])
        elif question_genre[i] == 'activities':
            print(question_genre[i], ': \n 1-', activities["travel_1"], '\n 2-', activities["travel_2"])

# If the user choose B

    elif response_user[i].lower() == 'b':
        if question_genre[i] == 'movies':
            print(question_genre[i], ': \n 1- ', movies["romantic_1"], ' \n 2- ', movies["romantic_2"])
        elif question_genre[i] == 'games':
            print(question_genre[i], ': \n 1- ', games["puzzle_1"], ' \n 2-', games["puzzle_2"])
        elif question_genre[i] == 'songs':
            print(question_genre[i], ': \n 1-', songs["classical_1"], '\n 2-', songs["classical_2"])
        elif question_genre[i] == 'places':
            print(question_genre[i], ': \n 1-', places["museum_1"], '\n 2-', places["museum_2"])
        elif question_genre[i] == 'activities':
            print(question_genre[i], ': \n 1-', activities["sport_1"], '\n 2-', activities["sport_2"])

# If the user choose C

    elif response_user[i].lower() == 'c':
        if question_genre[i] == 'movies':
            print(question_genre[i], ': \n 1- ', movies["science_fiction_1"], ' \n 2- ', movies["science_fiction_2"])
        elif question_genre[i] == 'games':
            print(question_genre[i], ': \n 1- ', games["adventure_1"], ' \n 2-', games["adventure_2"])
        elif question_genre[i] == 'songs':
            print(question_genre[i], ': \n 1-', songs["metal_1"], '\n 2-', songs["metal_2"])
        elif question_genre[i] == 'places':
            print(question_genre[i], ': \n 1-', places["beach_1"], '\n 2-', places["beach_2"])
        elif question_genre[i] == 'activities':
            print(question_genre[i], ': \n 1-', activities["learning_1"], '\n 2-', activities["learning_2"])

# If the user choose D

    elif response_user[i].lower() == 'd':
        if question_genre[i] == 'movies':
            print(question_genre[i], ': \n 1- ', movies["horror_1"], ' \n 2- ', movies["horror_2"])
        elif question_genre[i] == 'games':
            print(question_genre[i], ': \n 1- ', games["sport_1"], ' \n 2-', games["sport_2"])
        elif question_genre[i] == 'songs':
            print(question_genre[i], ': \n 1-', songs["rock_1"], '\n 2-', songs["rock_2"])
        elif question_genre[i] == 'places':
            print(question_genre[i], ': \n 1-', places["shop_1"], '\n 2-', places["shop_2"])
        elif question_genre[i] == 'activities':
            print(question_genre[i], ': \n 1-', activities["reading_1"], '\n 2-', activities["reading_2"])
    else:
        print('Sorry you entering a choice that not exist')
