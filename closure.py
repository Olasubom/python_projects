def parent_function(person):
    coin = 3

    def child_function():
        nonlocal coin
        coin -= 1

        if coin > 1:
            print(f"{person} has {coin} coins left")
        elif coin == 1:
            print(f"{person} has {coin} coin left")
        else:
            print(f"{person} is out of coins")

    return child_function()

bola = parent_function("Bola")
ade = parent_function("Ade")
kule = parent_function("Kule")

bola()
ade()

