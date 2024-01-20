#FaçaumProgramaquepergunteemqueturnovocêestuda.PeçaparadigitarM-matutinoouV-VespertinoouN-Noturno.Imprimaamensagem"BomDia!","BoaTarde!"ou"BoaNoite!"ou"ValorInválido!",conformeocaso

turno = input('digite em que turno você estuda: M-matutino ou V-Vespertino ou N-Noturno ')

print(turno)

if turno == 'M' :
    print('Bom dia')
elif turno == 'V' :
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor Inválido!')
