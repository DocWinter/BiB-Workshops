"""
    QCM Version n°2
"""
import random


def afficher_question(question):
    """ Affiche les informations de la question : question, réponses et points
        que l'on peut gagner.
    """
    print("### QUESTION ###")
    print(question['question'])
    for index, reponse in enumerate(question['réponses']):
        print(f'{index+1} - {reponse[0]}')
    print(f"Cette question rapporte {question['score']} points.\n")


def valider_reponse(reponses):
    """ Demande à l'utilisateur d'entrer une réponse.
        1 : La réponse est correcte
        0 : La réponse n'est pas correcte
        -1 : Fin du programme
    """
    while True:
        choix = input("Quel est votre choix? (N° de la réponse) ")
        if choix == 'stop':
            return -1
        try:
            choix = int(choix)
            if 0 < choix <= len(reponses):
                return int(reponses[choix-1][1])
            else:
                print("Cette réponse n'existe pas.")
        except ValueError:
            print("Vous devez entrer un nombre.")


if __name__ == '__main__':
    questions = [
        {
            'question': "Quelle est la couleur du cheval blanc d'Henri IV?",
            'réponses': [
                ("Blanche", True),
                ("Noire", False),
                ("Rose", False),
                ("Marron", False)
            ],
            'score': 1
        },
        {
            'question': "Quel est le plus haut mont de France?",
            'réponses': [
                ("Canigou", False),
                ("Pic Saint Loup", False),
                ("Montagne Noire", False),
                ("Mont Blanc", True)
            ],
            'score': 10
        },
    ]
    score = 0

    while True:
        question = random.choice(questions)
        afficher_question(question)
        reponse = valider_reponse(question['réponses'])
        if reponse == -1:
            break
        elif reponse == 1:
            score += question['score']
            print("VRAI")
        else:
            print("FAUX")
        print(f"\n### SCORE ###\nPoints : {score}\n")

    print("Le programme est maintenant terminé. Merci d'avoir participé.")
