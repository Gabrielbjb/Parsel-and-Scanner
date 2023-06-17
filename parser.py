def filterTeks(teks):
    i = 0
    while i < len(teks):
        if teks[i] != '\n':
            break
        else:
            i += 1
    if i != len(teks):
        a = teks[i:]
        return a
def getToken(teks, hasil):
    teks = filterTeks(teks)
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
            hasil.append(teks[i])

            x = i+1
            spacing = ""
            while x < len(teks):
                if teks[x] == ' ' or teks[x] == '\t':
                    spacing += teks[x]
                else:
                    if teks[x] != '\n': #ketemu alphabet
                        break
                x += 1
            hasil.append(spacing)
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


def push(stack, token):
    stack.append(token)
def pop(stack):
    stack.pop()
def isEmpty(stack):
    return len(stack) == 0
def top(stack):
    return stack[len(stack)-1]

def parser(listToken, stack):
    if len(listToken) > 0:
        push(stack,"#")
        push(stack, "<statement>")
        i = 0
        accepted = True
        current_spacing = "<unchanged>"
        while top(stack) != "#" and i < len(listToken):
            if top(stack) == "<statement>":
                pop(stack)
                push(stack, "<aksi>")
                push(stack, ":")
                push(stack, "<kondisi>")
                push(stack, "while")
            elif top(stack) == "<kondisi>":
                pop(stack)
                push(stack,"<variabel>")
                push(stack,"<operator>")
                push(stack,"<variabel>")
            elif top(stack) == "<aksi>":
                pop(stack)
                push(stack,"<variabel>")
                push(stack,"<arithmetic operator>")
                push(stack,"<variabel>")
                push(stack,"=")
                push(stack,"<variabel>")
            elif top(stack) == "<variabel>":
                pop(stack)
                if listToken[i] != "a" and listToken[i] != "b":
                    accepted = False
                    break
                else:
                    if top(stack) == "#" and i < len(listToken):
                        j = i+1
                        while j < len(listToken):
                            if listToken[j] == "a" or listToken[j] == "b":
                                i = j-3
                                push(stack,"\n")
                                break
                            else:
                                if listToken[j].isalnum():
                                    if listToken[j] != "a" or listToken[j] != "b":
                                        accepted = False
                                        break
                                j += 1
                    i = i+1
            elif top(stack) == "<arithmetic operator>":
                pop(stack)
                if listToken[i] != "+" and listToken[i] != "-" and listToken[i] != "*" and listToken[i] != "/" and listToken[i] != "%" and listToken[i] != "**":
                    accepted = False
                    break
                else:
                    i = i+1
            elif top(stack) == "<operator>":
                pop(stack)
                if listToken[i] != "==" and listToken[i] != "!=" and listToken[i] != ">" and listToken[i] != "<":
                    accepted = False
                    break
                else:
                    i = i+1
            elif top(stack) == "while":
                pop(stack)
                if listToken[i] != "while":
                    accepted = False
                    break
                else:
                    i = i+1
            elif top(stack) == ":":
                pop(stack)
                if listToken[i] != ":":
                    accepted = False
                    break
                else:
                    push(stack,"\n")
                    i = i+1
            elif top(stack) == "\n":
                pop(stack)
                if listToken[i] != "\n":
                    accepted = False
                    break
                else:
                    push(stack,"<spacing>")
                    i = i+1
            elif top(stack) == "<spacing>":
                pop(stack)
                if listToken[i] == "":
                    accepted = False
                    break
                else:
                    if current_spacing == "<unchanged>":
                        current_spacing = listToken[i]
                        j = i+1
                        while j < len(listToken):
                            if listToken[j] == "a" or listToken[j] == "b":
                                i = j-1
                                break
                            else:
                                j += 1
                    elif current_spacing != listToken[i]:
                        accepted = False
                        break
                    i = i+1
            elif top(stack) == "=":
                pop(stack)
                if listToken[i] != "=":
                    print("-",listToken[i],"-")
                    accepted = False
                    break
                else:
                    i = i+1
        if accepted:
            print("Status: Diterima (Accepted)")
        else:
            print("Status: Ditolak (Error)")
    else:
        print("Input Kosong")
stack = []

teks = """


while    a < b:

  a = a + b
  a = b +b
"""
hasil = []
stack = []
print("Input Teks:")
print(teks, "\n")
getToken(teks,hasil) # FA - ANALISIS LEKSIKAL
parser(hasil,stack)
