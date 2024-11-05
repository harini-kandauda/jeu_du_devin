'''Jouer au jeu du devin à répétition'''

import random

choice_of_player = None
while choice_of_player != 0 :
    #Demander quel rôle jouer
    choice_of_player = int(input("1 - L'ordinateur choisit un nombre et vous le devinez \n2 - Vous choisissez un nombre et l'ordinateur le devine : tapez 2 \n0 - Quitter le programme \nVotre choix : "))

    #Faire deviner un nombre à l'utilisateur
    def devin_is_user() :
        MAX_NB = 10
        nb_of_guesses = 0
        nb_to_guess = random.randint(1,MAX_NB)
        print(f"J'ai choisi un nombre entre 1 et {MAX_NB}.")

        guessed_number = None
        while guessed_number != nb_to_guess :
            nb_of_guesses += 1
            guessed_number = int(input(f"Proposition {nb_of_guesses} : "))
            if guessed_number > nb_to_guess :
                print('Trop grand !')
            elif guessed_number == nb_to_guess :
                print('Trouvé !')
            else :
                print('Trop bas !')

        print(f'Bravo ! Vous avez trouvé en {nb_of_guesses} essais.')

    #Deviner un nombre
    def devin_is_computer() :
        MIN_NB = 1
        MAX_NB = 10

        are_you_ready = None
        while are_you_ready != 'o' :
            if are_you_ready == 'n' :
                print("J'attends...")
            are_you_ready = str(input(f'Avez-vous choisi un nombre compris entre {MIN_NB} et {MAX_NB} (o/n) ? '))

        nb_of_guesses = 1
        answer = None
        while answer != 't' and answer != 'T' :
            guessed_number = int((MIN_NB + MAX_NB) / 2)
            print(f'Proposition {nb_of_guesses} : {guessed_number}')
            answer = input('Trop (g)rand, trop (p)etit ou (t)rouvé ? ')

            if answer == 'p' or answer == 'P' :
                MIN_NB = guessed_number + 1
                nb_of_guesses += 1
            elif answer == 'g' or answer == 'G' :
                MAX_NB = guessed_number - 1
                nb_of_guesses += 1
            elif answer == 't' or answer == 'T' :
                break
            else : 
                print("Je n’ai pas compris la réponse. Merci de répondre : \n g si ma proposition est trop grande \n p si ma proposition est trop petite \n t si j’ai trouvé le nombre")

        print(f"J'ai trouvé en {nb_of_guesses} essais.")

    #Lancer le rôle choisi
    if choice_of_player == 1 :
        devin_is_user()
    elif choice_of_player == 2 :
        devin_is_computer()

    while choice_of_player not in (1, 2, 0) :
        print("Je ne comprends pas, veuillez taper 1 ou 2")
        choice_of_player = int(input("1 - L'ordinateur choisit un nombre et vous le devinez \n2 - Vous choisissez un nombre et l'ordinateur le devine : tapez 2 \n0 - Quitter le programme \nVotre choix : "))

#Quitter le jeu
print('Au revoir...')