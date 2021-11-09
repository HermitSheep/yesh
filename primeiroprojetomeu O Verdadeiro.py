

def eh_anagrama(palavra1, palavra2):
    # Deteta anagramas: cad. carateres × cad. carateres --> booleano
    # se for anagrama retorna verdadeiro
    return all([palavra1.upper().count(i) == palavra2.upper().count(i) for i in (palavra1 + palavra2).upper()])


def corrigir_palavra(palavra):
    # Elemina carateres a mais: cad. carateres --> cad. carateres
    """
    Esta função simula o meu processo natural de identificação de padrões e é por isso não deve ser a mais eficiente.
    Isto incomoda-me.
    """
    # Eu sei que não devia fazer assim... mas não sabia quando fiz, e funcionou, portanto...welp...
    i = 0  #contador da letra da palavra (minhoca)
    m = 0  #contador de mudanças
    while True:
        if i > len(palavra) - 2:
            i = 0
            if m == 0 or len(palavra) <= 1: break
            m = 0
        if abs(ord(palavra[i]) - ord(palavra[i + 1])) == 32:
            palavra = palavra[:i] + palavra[i + 2:]
            m += 1
        i += 1
    return palavra


def corrigir_doc(bdb):
    # Corrige integralmente a BDB (elemina carateres a mais e anagramas): cad. carateres --> cad. carateres
    if not type(bdb) == str: raise ValueError('corrigir_doc: argumento invalido')
    nespacos = bdb.count(' ')
    palavras = bdb.split()
    if any([nespacos >= len(palavras), len(palavras) == 0, not all([e.isalpha() for e in palavras])]):
        raise ValueError('corrigir_doc: argumento invalido')

    ''' SPAGHETTI CODE INCOMING!!!
    PAIN....
    '''
    bdb_inicial = corrigir_palavra(bdb).split()
    bdb_final = []
    lista_boas = [' ']
    for palavra in bdb_inicial:          # se a palavra estiver na lista de boas palavras, vai direta para a lista final
        if palavra.lower() in lista_boas:
            bdb_final.append(palavra)
        else:                            # caso contrário...
            if all([not eh_anagrama(palavra, palavra_boa) for palavra_boa in lista_boas]):
                lista_boas.append(palavra.lower())   # se não for anagrama de nenhuma palavra da lista boa entra nas 2
                bdb_final.append(palavra)
    return " ".join(bdb_final)



def obter_posicao(movimento, posicao_atual):
    # Devolve a nova posição após um movimento: cad. carateres × inteiro --> inteiro
    if movimento == 'E' and posicao_atual not in (7,4,1):
        posicao_atual -= 1
    if movimento == 'D' and posicao_atual not in (9,6,3):
        posicao_atual += 1
    if movimento == 'B' and posicao_atual < 7:
        posicao_atual += 3
    if movimento == 'C' and posicao_atual > 3:
        posicao_atual -= 3
    return posicao_atual


def obter_digito(codigo, posicao_atual):
    # Devolve o digito a marcar correspondente a parte do código: cad. carateres × inteiro --> inteiro
    for letra in codigo:
        posicao_atual = obter_posicao(letra, posicao_atual)
    return posicao_atual


def obter_pin(passe):
    # Devolve o PIN a partir da passe: tuplo --> tuplo
    if type(passe) != tuple: raise ValueError("obter_pin: argumento invalido")
    if not 4 <= len(passe) <= 10: raise ValueError("obter_pin: argumento invalido")
    if not all([type(codigo) == str and len(codigo) > 0 and all([l in ('D', 'C', 'B', 'E') for l in codigo])
                for codigo in passe]): raise ValueError("obter_pin: argumento invalido")
    # não tocar aqui, funcionou semi por sorte

    digito = 5
    pin = ()
    for codigo in passe:
        digito = obter_digito(codigo, digito)
        pin += (digito,)
    return pin



def eh_entrada(entr):
    # valida entradas na BDB: universal --> booleano

    def valida_entr(entr):
        if type(entr) != tuple: return False
        return len(entr) == 3

    def valida_cifra(cifra):
        if type(cifra) != str: return False
        words = cifra.split('-')
        return all([len(cifra) != 0, len(words) > cifra.count('-'),
                    all([all([l.isalpha() and l.islower() for l in word]) for word in words])])

    def valida_checksum(check):
        if type(check) != str: return False
        return all([len(check) == 7, check.startswith("["), check.endswith("]"),
                    check[1:6].isalpha(), check[1:6].islower()])

    def valida_seq_saf(seq_saf):
        if type(seq_saf) != tuple: return False
        if any([type(num) != int for num in seq_saf]): return False
        return all([len(seq_saf) > 1, all([num >= 1 for num in seq_saf])])

    # só defini a seq_saf como sendo maior que 1, n sei se poderá ser 0                                          (ERRO?)
    if not valida_entr(entr): return False
    return all([valida_cifra(entr[0]), valida_checksum(entr[1]), valida_seq_saf(entr[2])])


def validar_cifra(cifra, check):
    # Verifica se as entradas não foram corrumpidas: cad. carateres × cad. carateres --> booleano
    # não funciona/verifica se a cifra tem menos de 5 letras                                                     (ERRO?)
    letras = []
    cifra = cifra.replace("-", "")
    for l in cifra:
        if l not in letras:
            letras += l

    list = []
    for l in letras:
        list += [[l, cifra.count(l)]]

    list_ord = sorted(list, key=lambda prioridade: (-prioridade[1], prioridade[0]))
    # organisa as listas primeiro peli segundo index e depois pelo primeiro
    list_let = "".join([l[0] for l in list_ord])

    return list_let[:5] == check[1:6]


def filtrar_bdb(lista):
    # filtra entradas corrumpidas: lista --> lista
    # levanta erro para entradas fora do previsto, eventualmente mete return false                               (ERRO?)
    if type(lista) != list: raise  ValueError('filtrar_bdb: argumento invalido')
    if len(lista) < 1:  raise  ValueError('filtrar_bdb: argumento invalido')
    lista_boas_entr = []
    for entr in lista:
        if not eh_entrada(entr): raise ValueError('filtrar_bdb: argumento invalido')
        cifra, check, seq_saf = entr
        if not validar_cifra(cifra, check):
            lista_boas_entr += [entr]
    return lista_boas_entr



def obter_num_seguranca(seq_saf):
    # Dá o número de segurança: tuplo --> inteiro
    ref = abs(seq_saf[0] - seq_saf[1])
    for i in range(len(seq_saf) - 1):
        for num in seq_saf[i + 1:]:
            dif = abs(seq_saf[i] - num)
            if dif < ref:
                ref = dif
    return ref


def decifrar_texto(cifra, num_saf):
    # dá a cifra decifrada: cad. carateres × inteiro --> cad. carateres
    cifra = cifra.replace('-', ' ')
    cifra_boa = ''
    if num_saf > 26: num_saf %= 26
    # Não sei se mais vale meter funções auxiliares para isto em baixo                                       (ABSTRAÇÂO)
    for i in range(len(cifra)):
        if not ord(cifra[i]) == 32: # se não for espaço
            if i % 2 == 0:          # se for par
                if ord(cifra[i]) + num_saf + 1 <= 122:            # se sair do alfabeto ao adicionar a cifra
                    cifra_boa += chr(ord(cifra[i]) + num_saf + 1)
                else:
                    cifra_boa += chr(96 + num_saf - (122 - ord(cifra[i])) + 1)
            else:
                if ord(cifra[i]) + num_saf - 1 <= 122:
                    cifra_boa += chr(ord(cifra[i]) + num_saf - 1)
                else:
                    cifra_boa += chr(96 + num_saf - (122 - ord(cifra[i])) - 1)
        else: cifra_boa += ' '
    return cifra_boa


def decifrar_bdb(lista):
    # decifra a bdb, ou seja, traduz a cifra: lista --> lista
    # Não vê se o checksum corresponde à cifra, mas deve funcionar se se fizer esta com base no output da filtrar bdb
    #                                                                                                            (ERRO?)
    if type(lista) != list: raise  ValueError('decifrar_bdb: argumento invalido')
    if len(lista) < 1:  raise  ValueError('decifrar_bdb: argumento invalido')
    lista_decif = []
    for entr in lista:
        if not eh_entrada(entr): raise ValueError('decifrar_bdb: argumento invalido')
        cifra, check, seq_saf = entr
        num_saf = obter_num_seguranca(seq_saf)
        cifra_boa = decifrar_texto(cifra, num_saf)
        lista_decif += [cifra_boa]
    return lista_decif



def eh_utilizador(dic):
    # Verifica se os credenciais do utilizador são coerentes: universal --> booleano
    def valida_dic(dic):
        if type(dic) != dict: return False
        return sorted(dic.keys()) == sorted(['name', 'pass', 'rule'])

    def valida_name(name):
        if type(name) != str: return False
        return len(name) >= 1

    def valida_rule(rule):
        if type(rule) != dict: return False
        if sorted(rule.keys()) != sorted(['vals', 'char']): return False
        vals = rule['vals']
        char = rule['char']
        if type(vals) != tuple or type(char) != str: return False
        if len(vals) != 2: return False
        if type(vals[0]) != int or type(vals[1]) != int:return False
        return all([len(rule.keys()) == 2,
             vals[0] > 0, vals[1] > 0, vals[0] < vals[1],
             len(char) == 1, char.isalpha(), char.islower()])

    def valida_pass(pas):
        if type(pas) != str: return False
        return len(pas) >= 1

    if not valida_dic(dic): return False
    return all([valida_name(dic['name']), valida_rule(dic['rule']), valida_pass(dic['pass'])])


def eh_senha_valida(pas, rule):
    # Verifica se a pass cumpre as regras em rule: cad. carateres × dicionário --> booleano
    # Permite o .count da letra ser igual aos extremos do limite, se é para corrigir, muda na função em cima tb  (ERRO?)
    return all([pas.count('a') + pas.count('e') + pas.count('i') + pas.count('o') + pas.count('u') >= 3,
                any([pas[i] == pas[i + 1] for i in range(len(pas) - 1)]),
                rule['vals'][0] <= pas.count(rule['char']) <= rule['vals'][1]])


def filtrar_senhas(lista):
    # Dá o nome de utilizadores cujas passwords não seguem as regras: lista --> lista
    # Não verifica se a pass ou o nome podem ter carateres especiais, ou maiusculas                              (ERRO?)
    if type(lista) != list: raise ValueError('filtrar_senhas: argumento invalido')
    if len(lista) < 1: raise ValueError('filtrar_senhas: argumento invalido')
    lista_nomes = []
    for dic in lista:
        if not eh_utilizador(dic): raise ValueError('filtrar_senhas: argumento invalido')
        if not eh_senha_valida(dic['pass'], dic['rule']): lista_nomes += [dic['name']]
    return sorted(lista_nomes)
