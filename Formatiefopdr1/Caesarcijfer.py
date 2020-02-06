text = input("geef tekst: ")
rotatie = int(input("geef rotatie:"))
result = ""
for i in range(len(text)):
      letter = text[i]
      if letter.isupper():
          result += chr((ord(letter) + rotatie - 65) % 26 + 65) #Formule uit: https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
      elif letter.isspace():
          result += " "
      else:
          result += chr((ord(letter) + rotatie - 97) % 26 + 97)
print (result)


