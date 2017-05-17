"""
    QCM Version n°1
    Cette solution est minimale et contient quelques problèmes :
    1. Que fait le programme si l'utilisateur rentre un choix illégal?
        - Si le choix est du texte
        - Si le choix est un entier <0 ou >len(reponses)-1
    2. Comment poser plusieurs questions?
    3. Comment quitter le programme?
    On verra comment régler ces problèmes lors de la prochaine séance.
"""


def afficher_question(question):
    """ Affiche les informations de la question : question, réponses et points
        que l'on peut gagner.
    """
    print(question['question'])
    print(f"Cette question rapporte {question['score']} points.")
    print('Voici les réponses possibles :')
    for reponse in question['réponses']:
        print(reponse[0])


def demande_reponse(reponses):
    """ Demande à l'utilisateur d'entrer une réponse.
    """
    choix = int(input("Quel est votre choix? (N° de la réponse) "))
    return reponses[choix][1]


if __name__ == '__main__':
    question = {
        'question': "Quelle est la couleur du cheval blanc d'Henri IV?",
        'réponses': [
            ("Blanche", True),
            ("Noire", False),
            ("Rose", False),
            ("Marron", False)
        ],
        'score': 10
    }
    score = 0

    while True:
        afficher_question(question)
        if demande_reponse(question['réponses']):
            score += question['score']
        print(f'Votre avez {score} points')
