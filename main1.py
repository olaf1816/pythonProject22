def main():

 state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
 espacio = [i for i in state if i in ' ']

 print(espacio)
 print(len(espacio))


if __name__ == '__main__':
 main()
