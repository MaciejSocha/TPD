import functions as f


def data():
    name_file = input('Wprowadź nazwę pliku: ')
    m = f.load_data(name_file)
    print("Twoja macierz:")
    for s in m:
        print("wybór", *s)
    return m


def print_walda(m: list):
    return print(
        "Z punktu widzenia kryterium Walda najlepszą decyzją jest opcja " + str(f.find_in_matrix(m, f.mini_maks(m))),
        sep=' ')


def print_maks_maks(m: list):
    return print(
        "Z punktu widzenia kryterium Walda najlepszą decyzją jest opcja " + str(f.find_in_matrix(m, f.maks_maks(m))),
        sep=' ')


def print_k_hurwicz(result: tuple, factor: float):
    print("Otrzymane wyniki: ")
    for i, name in enumerate(result[0]):

        print("wybór {} : {}".format(i + 1, name))
    print(
        "Z punktu widzenia kryterium Hurwicza najlepszą decyzją dla współczynnika ostrożności {} jest opcja ".format(factor) + str(
            f.find_in_result(result)+1),
        sep=' ')


def print_k_bayesa(result: tuple, prob: float):
    print("Otrzymane wyniki: ")
    for i, name in enumerate(result[0]):
        print("wybór {} : {}".format(i + 1, name))
    print(
        "Z punktu widzenia kryterium Hurwicza najlepszą decyzją dla prawdopodobieństwa {} jest opcja ".format(prob) + str(
            f.find_in_result(result)+1),
        sep=' ')


def print_k_savage(result: tuple):
    print("Otrzymane wyniki: ")
    for i, name in enumerate(result[0]):
        print("wybór {} : {}".format(i + 1, name))
    print(
        "Z punktu widzenia kryterium Savage'a najlepszą decyzją jest opcja " + str(
            f.find_in_result(result)+1),
        sep=' ')


m = data()
exit = False
while not exit:
    option = input("Wybierz kryterium podejmowania decyzji: \n"
                   + "1. Krysterium minimaks\n"
                   + "2. krysterium maksmaks\n"
                   + "3. krysterium Hurwicza\n"
                   + "4. krysterium Bayesa-Laplace'a\n"
                   + "5. krysterium Savage'a\n"
                   + "6. Wybierz inny plik\n"
                   + "7. Wyjdź\n"
                   )
    if option == '1':
        print_walda(m)
    elif option == '2':
        print_maks_maks(m)
    elif option == '3':
        x = input("Podaj współczynnik ostrożności: ")
        print_k_hurwicz(f.k_hurwicz(m,x), x)
    elif option == '4':
        print_k_hurwicz(f.k_bayesa(m, 1/2, 1/2, 1/2, 1/2), 1/2)
    elif option == '5':
        print_k_savage(f.k_savage(m))
    elif option == '6':
        m = data()
    elif option == '7':
        exit = True
    else:
        print("Nie ma takiej opcji !!")


