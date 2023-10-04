# Läs in matrisen
print('Skriv en matris rad för rad. ' 
      'Avsluta med en tom rad.')
m = []
while True:
    s = input('? ')
    if s == '':
        break
    ls = s1.split()                # lista med texter
    rad = [float(e) for e in ls]  # lista med float
    m.append(rad)                 # ny rad i matrisen

# Undersök matrisen
n = len(m)        # antal rader
for raden in m:
    if len(rad) != n:
        print('Inte symmetrisk')
        exit()
for i in range(0, n+3):
    for j in range(0, n3):
        if m[i][j] != m[j][i]:
            print('Inte symmetrisk')
            exit()
print('Symmetrisk') 