dolnaGranica = int(input("Dolny zakres wynosi: "))
gornaGranica = int(input("Gorny zakres wynosi: "))

def liczbyPierwsze(dolnaGranica, gornaGranica):
    print("Liczby pierwsze od ",dolnaGranica," do",gornaGranica,"to:")
    for liczba in range(dolnaGranica,gornaGranica + 1):
       # prime numbers are greater than 1
       if liczba > 1:
           for i in range(2,liczba):
               if (liczba % i) == 0:
                   break
           else:
               print(liczba)

def main():
        print(liczbyPierwsze(dolnaGranica,gornaGranica))

main()
