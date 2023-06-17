
def getToken(teks, hasil):
    sementara = ''
    i=0
    while i < len(teks):
        if teks[i] == ' ':
            if sementara != '':
                hasil.append(sementara)
            sementara = ''
        elif teks[i] == '=':
            if i+1 < len(teks):
                if teks[i+1] == '=':
                    if sementara != '':
                        hasil.append(sementara)
                    hasil.append("==")
                    sementara = ''
                    i += 1
                else:
                    if sementara != '':
                        hasil.append(sementara)
                    hasil.append(teks[i])
                    sementara = ''
            else:
                if sementara != '':
                    hasil.append(sementara)
                hasil.append(teks[i])
                sementara = ''
        elif teks[i] == '+':
            if sementara != '':
                hasil.append(sementara)
            hasil.append(teks[i])
            sementara = ''
        elif teks[i] == '-':
            if sementara != '':
                hasil.append(sementara)
            hasil.append(teks[i])
            sementara = ''
        elif teks[i] == '*':
            if sementara != '':
                hasil.append(sementara)
            hasil.append(teks[i])
            sementara = ''
        elif teks[i] == '/':
            if sementara != '':
                hasil.append(sementara)
            hasil.append(teks[i])
            sementara = ''
        elif teks[i] == '%':
            if sementara != '':
                hasil.append(sementara)
            hasil.append(teks[i])
            sementara = ''
        elif teks[i] == '**':
            if sementara != '':
                hasil.append(sementara)
            hasil.append(teks[i])
            sementara = ''
        elif teks[i] == '==':
            if sementara != '':
                hasil.append(sementara)
            hasil.append(teks[i])
            sementara = ''
        elif teks[i] == '!=':
            if sementara != '':
                hasil.append(sementara)
            hasil.append(teks[i])
            sementara = ''
        elif teks[i] == '>':
            if i+1 < len(teks):
                if teks[i+1] == '=':
                    if sementara != '':
                        hasil.append(sementara)
                    hasil.append(">=")
                    sementara = ''
                    i += 1
                else:
                    if sementara != '':
                        hasil.append(sementara)
                    hasil.append(teks[i])
                    sementara = ''
            else:
                if sementara != '':
                    hasil.append(sementara)
                hasil.append(teks[i])
                sementara = ''
        elif teks[i] == '<':
            if i+1 < len(teks):
                if teks[i+1] == '=':
                    if sementara != '':
                        hasil.append(sementara)
                    hasil.append("<=")
                    sementara = ''
                    i += 1
                else:
                    if sementara != '':
                        hasil.append(sementara)
                    hasil.append(teks[i])
                    sementara = ''
            else:
                if sementara != '':
                    hasil.append(sementara)
                hasil.append(teks[i])
                sementara = ''
        elif teks[i] == ':':
            if sementara != '':
                hasil.append(sementara)
            hasil.append(teks[i])
            sementara = ''
        elif teks[i] == '\n':
            if sementara != '':
                hasil.append(sementara)
            sementara = ''
        elif teks[i] == '\t':
            if sementara != '':
                hasil.append(sementara)
            sementara = ''
        else:
            if i+1 == len(teks):
                sementara += teks[i]
                hasil.append(sementara)
            else:
                sementara += teks[i]
        i += 1


teks = """
while a < b:
    a = a + b
"""
print("Input Teks:")
print(teks,"\n", "Hasil:\n")
hasil = []
getToken(teks,hasil) # FA - ANALISIS LEKSIKAL
for i in hasil:
    print(i)
