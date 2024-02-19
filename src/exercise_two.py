from random import randint

def list_manager(mint, maxt) -> str:
    list = []
    for i in range(10): list.append(randint(mint, maxt))

    print(f'Max: {max(list)}\nMin: {min(list)}')

def main() -> str:
    print('---'*10)
    print('Понеділок')
    print('---'*10)
    list_manager(-7, 14)

    print('---'*10)
    print('Вівторок')
    print('---'*10)
    list_manager(-7, 14)

    print('---'*10)
    print('Середа')
    print('---'*10)
    list_manager(-7, 14)

    print('---'*10)
    print('Четвер')
    print('---'*10)
    list_manager(-7, 14)


    print('---'*10)
    print("П`ятниця")
    print('---'*10)
    list_manager(-7, 14)

if __name__ == '__main__':
    main()