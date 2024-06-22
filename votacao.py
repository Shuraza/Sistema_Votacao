#prefeitos / numero do candidato 
joão = 11
paulo = 22
pedro = 33
junior_do_povão = 44

# vereador / numero do candidato 
papa_capim = 1
efraim = 2
reinaldo = 3
ednaldo = 4
ana = 5
dioga = 6
oranja = 7 
reginaldo = 8
valoranta = 9
dburcio = 10

while continuar != 0 :

  print("Se deseja iniciar a votação, DIGITE Y\n")
  print("Caso deseje encerrar o sistema, DIGITE N\n")
  inicio = input("").upper()
 
  if inicio == "Y" :
      while inicio == "Y" :
          print("Tchau")
 
  elif inicio == "N" :
      continuar = 0
 
  else :
      print("Escreva Y ou N!")