import os

def main():
    print('---'*10)
    vpr = int(input('Яку вправу будемо запускати: '))

    if vpr == 1:
        os.system('python src/exercise_one.py')
    elif vpr == 2:
        os.system('python src/exercise_two.py')
    elif vpr == 3:
        os.system('python src/exercise_last.py')

    else:
        print('Невірний вибір (їх всього 3)')

if __name__ == '__main__':
    main()
