def todo():
    taches = ["Cuisiner", "Travailler", "Sport"]
    res = int(input("Faites un choix: "))
    if res == 1:
        tache = input("Ajouter une tache: ")
        taches.append(tache)
        print("Vous avez ajouter: ", tache, "à la liste")
        for i in taches:
            print(i)

    elif res == 2:
        for i in taches:
            print(i)

    elif res == 3:
        ed = int(input("Choisir une tache"))
        if ed == 1:
            edit = input("Qu'est ce que vous voulez mettre")
        taches[1] = edit
        print(taches)

    elif res == 4:
        delete = int(input("Choiser la tache à supprimer "))
        del taches[delete]
        print(taches)

    else:
        print("Error")

todo()