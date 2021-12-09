def main():

  state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
  vowels = [i for i in state if i in 'BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz']

  print(vowels)

if __name__ == '__main__':
  main()
