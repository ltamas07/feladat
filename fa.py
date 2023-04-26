nevek, eletkorok, termesek = [], [], []
for _ in range(3):
    fa_neve = input('Add meg a fa nevét: ')
    fa_eletkora = int(input(f'Add meg {fa_neve} életkorát: '))
    fa_termese = input(f'Add meg {fa_neve} termését: ')
    nevek.append(fa_neve)
    eletkorok.append(fa_eletkora)
    termesek.append(fa_termese)
szam = 0
for i in eletkorok:
    if 3> eletkorok[szam] > 1:
        print(f'{nevek[szam]} csemete')
    elif 5> eletkorok[szam] > 4:
        print(f'{nevek[szam]} sudár')
    else:
        print(f'{nevek[szam]} fa')
    szam += 1