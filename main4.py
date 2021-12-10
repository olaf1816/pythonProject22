def main():
   cantidad = int(input("Di el numero de notas que introduciras: "))

   notas = list()
   x=1
   while x <= cantidad:
      notas.append(int(input(f"Introduce la nota numero {x} :")))
      x += 1

   x=0
   suma_suspend = 0
   suspend = 0
   suma_aprov = 0
   aprov = 0

   for x in range (x, cantidad):
      y=notas[x]
      if notas[x]<=4:
         x += 1
         suma_suspend += suma_suspend + y
         suspend = suspend + 1
      else:
         x += 1
         suma_aprov = suma_aprov + y
         aprov = aprov + 1
   print("*********************************************************")
   print(f"{aprov} personas han aprobado, su media es de {suma_aprov / aprov}")
   print(f"{suspend} personas han suspendido, su media es de {suma_suspend / suspend}")

if __name__ == '__main__':
  main()

