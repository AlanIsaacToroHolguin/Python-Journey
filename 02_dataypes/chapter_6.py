# String in pyhton: cabe resaltar que es siempre mutable no puede ser  inmutable ya que no cambia asi que en la memoria siempre se crea una nueva refereencia

# todo lo que este dentro de comillas dobles  es basciamwente un string

# entonces sobre string veremos  lo que es core,indexing y slicing

chai_type = "Ginger chai"

customer_name = "Alan Toro"

print(f"Customer: {customer_name}, Order: {chai_type}")

chai_description = "Aromatic and bold"

#indexing :significa que cada letra esta representada por un numero empezando por cero and  the last number is not inclusive.
print(f"First word: {chai_description[0:0]}")  # si lo dejamos asi no imprime nad apor eso para imprimir por completo aromatic deben ser con el numero 8 

print(f"First word: {chai_description[0:8]}")  # imprime aromatic

print(f"Every two letters: {chai_description[0:8:2]}")  # imprime armtc and bold

print(f"Last word: {chai_description[12:]}")  # imprime bold

print(f"Reverse: {chai_description[::-1]}")  # imprime bold and aromatic al reves


#cuando hay caracteres espciales y simbolos o para otros idiomas es buena pracctica usar un ecoded:lale
label_text = "Chai Spécial"

encoded_label = label_text.encode("utf-8")

print(f"Non encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")

# is importatn create a decoded label too
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")