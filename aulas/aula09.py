frase = 'Curso em Video Python'
print(frase)
print(frase[3])
print(frase[13])
print(frase[:13])
print(frase[13:])
print(frase[8:12])
print(frase[2:16:2])
print(frase[2::3])
print(frase[::5])

print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type 
specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in 
the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including 
versions of Lorem Ipsum""")

print(frase.count('P'))
print(frase.replace('Py', 'Java'))
print('urso' in frase)
print(frase.find('urso'))
split = frase.split()
print(split)
print(split[0][2])
print('*'.join(split))
