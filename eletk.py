nevek_n, nevek_f, korok_n, korok_f = [], [], [], []
emb_file = open('ember.txt','w')
nem = input('Add meg a nemed (F/N) [A program leállításához üss ENTERT]: ')
while nem != '':
    nev = input('Add meg a neved: ')
    kor = int(input('Add meg az életkorod: '))
    if nem == 'F':
        nevek_f.append(nev)
        korok_f.append(kor)
    elif nem == 'N':
        nevek_n.append(nev)
        korok_n.append(kor)
    nem = input('Add meg a nemed (F/N): ')
vegig_f, vegig_n = 0, 0
for vegig_f in korok_f:
    if korok_f[vegig_f] >= 20:
        print(f'{nevek_f[vegig_f]} Rutinos férfi')
        emb_file.write(f'{nevek_f[vegig_f]} Rutinos férfi\n')
    elif korok_f[vegig_f] < 20:
        print(f'{nevek_f[vegig_f]} Zöldfülű férfi')
        emb_file.write(f'{nevek_f[vegig_f]} Zöldfülű férfi\n')
    vegig_f += 1
for vegig_n in korok_n:
    if korok_n[vegig_n] >= 20:
        print(f'{nevek_n[vegig_n]} Tapasztalt nő')
        emb_file.write(f'{nevek_n[vegig_n]} Tapasztalt nő\n')
    elif korok_n[vegig_n] < 20:
        print(f'{nevek_n[vegig_n]} Csitri')
        emb_file.write(f'{nevek_n[vegig_n]} Csitri\n')
emb_file.close()