# TAD- Posição
    # Funções de Baixo Nivel

def cria_posicao(x, y):
    # Cria uma posição atravez de coordenadas dadas: int x int --> posicao
    # A representação interna das posições é um dict
    if type(x) != int or type(y) != int:
        raise ValueError('cria_posicao: argumentos invalidos')
    if x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return {'x': x, 'y': y}


def obter_pos_x(pos):
    # Dá o valor de x de uma posição: posicao --> int
    # Não sei se para os testes faz diferença a ordem destas 3 posições                                          (ERRO?)
    return pos['x']


def obter_pos_y(pos):
    # Dá o valor de y de uma posição: posicao --> int
    return pos['y']


def cria_copia_posicao(pos):
    # Cria uma cópia de uma posição: posicao --> posicao
    return cria_posicao(obter_pos_x(pos), obter_pos_y(pos))


def eh_posicao(pos):
    # Verifica se o input é uma posição segundo a representação interna: universal --> booleano
    try:
        cria_copia_posicao(pos)
    except Exception:
        return False
    else:
        return True


def posicoes_iguais(pos1, pos2):
    # Vê se as posições são iguais: posicao x posicao --> boolean
    return obter_pos_y(pos1) == obter_pos_y(pos2) and obter_pos_x(pos1) == obter_pos_x(pos2)


def posicao_para_str(pos):
    # Converte a posição num string: posicao --> str
    return f'({obter_pos_x(pos)}, {obter_pos_y(pos)})'

    # Funções de Alto Nivel


def obter_posicoes_adjacentes(pos):
    # Dá um tuplo com as posições adjacentes, começando por cima e vai pelo sentido do relógio: posicao --> tuplo
    # Tenho ainda de validar as posições adjacentes                                                              (ERRO?)
    # Não deixa ir para montanhas
    posis = ()
    if obter_pos_y(pos) >= 2:
        c = cria_posicao(obter_pos_x(pos), obter_pos_y(pos) - 1)
        posis += (c,)
    d = cria_posicao(obter_pos_x(pos) + 1, obter_pos_y(pos))
    b = cria_posicao(obter_pos_x(pos), obter_pos_y(pos) + 1)
    posis += (d, b)
    if obter_pos_x(pos) >= 2:
        e = cria_posicao(obter_pos_x(pos) - 1, obter_pos_y(pos))
        posis += (e,)
    return posis


def ordenar_posicoes(tup):
    # Ordena um tuplo de posições pela ordem de leitura do plado: tuple --> tuple
    # Tens de validar o tuplo de posições primeiro                                                               (ERRO?)
    lista = []
    listaord = []
    for pos in tup:
        pos = posicao_para_str(pos)
        pos = pos.replace('(', '')
        pos = pos.replace(')', '')
        pos = pos.replace(' ', '')
        pos = pos.split(',')
        lista += [[int(x) for x in pos]]
    lista = sorted(lista, key=lambda x: (x[1], x[0]))
    for pos in lista:
        listaord += [cria_posicao(pos[0], pos[1])]
    listaord = tuple(listaord)
    return listaord


# TAD- Animal
    # Funções de Baixo Nivel

def cria_animal(s, r, a):  # s--> espécie, r--> freq.reprodução, a--> freq.alimentação                     (IMPORTANTE!)
    # cria um animal qualquer: str x int x int --> animal
    # se a > 0 é um predador
    if type(s) != str or type(r) != int or type(a) != int:
        raise ValueError('cria_animal: argumentos invalidos')
    if r <= 0 or a < 0 or len(s) < 1:
        raise ValueError('cria_animal: argumentos invalidos')
    return {'s': s, 'r': r, 'a': a, 'fome': 0, 'idade': 0}


def cria_copia_animal(animal):
    # Cria uma copia, independente, do animal: animal --> animal
    return cria_animal(animal['s'], animal['r'], animal['a'])


def obter_especie(animal):
    # Devolve a especie do animal: animal --> str
    return animal['s']


def obter_freq_reproducao(animal):
    # Devolve a frequencia de reprodução do animal: animal --> int
    return animal['r']


def obter_freq_alimentacao(animal):
    # Devolve a frequencia de alimentação do animal: animal --> int
    return animal['a']


def obter_idade(animal):
    # Devolve a idade do animal: animal --> int
    return animal['idade']


def obter_fome(animal):
    # Devolve a fome do animal: animal --> int
    return animal['fome']


def aumenta_idade(animal):
    # Incrementa a idade do animal por 1: animal --> animal
    animal['idade'] += 1
    return animal


def reset_idade(animal):
    # Retorna a idade do animal a zero: animal --> animal
    animal['idade'] = 0
    return animal


def aumenta_fome(animal):
    # # Incrementa a fome do animal por 1: animal --> animal
    if animal['a'] != 0:
        animal['fome'] += 1
    return animal


def reset_fome(animal):
    # Retorna a fome do animal a zero: animal --> animal
    animal['idade'] = 0
    return animal


def eh_animal(animal):
    # Verifica se o animal é do tipo TAD: animal --> boolean
    try:
        cria_copia_animal(animal)
    except Exception:
        return False
    else:
        return True


def eh_predador(animal):
    # Verifica se o animal é predador (se sim dá verdadeiro): animal --> boolean
    if eh_animal(animal):
        return obter_freq_alimentacao(animal) != 0
    else: return False


def eh_presa(animal):
    # Verifica se o animal é presa (se sim dá verdadeiro): animal --> boolean
    if eh_animal(animal):
        return obter_freq_alimentacao(animal) == 0
    else:
        return False


def animais_iguais(animal1, animal2):
    # Verifica se dois animais são iguais: animal x animal --> bolean
    # Não sei se é preciso serem da mesma idade e terem a mesma fome para serem iguais                           (ERRO?)
    if eh_animal(animal1) and eh_animal(animal2):
        return all([obter_freq_alimentacao(animal1) == obter_freq_alimentacao(animal2),
                    obter_freq_reproducao(animal1) == obter_freq_reproducao(animal2),
                    obter_especie(animal1) == obter_especie(animal2),
                    obter_fome(animal1) == obter_fome(animal2),
                    obter_idade(animal1) == obter_idade(animal2)])
    else: return False


def animal_para_char(animal):
    # Dá a inicial da especie do anima, maiuscula se predador, minuscola se presa: animal --> str
    if eh_presa(animal):
        return obter_especie(animal)[0].lower()
    if eh_predador(animal):
        return obter_especie(animal)[0].upper()


def animal_para_str(animal):
    """ Mostra a informação do animal numa str do tipo 'especie [idade/freq.reprodução{;fome/freq.alimentação}]:'
    animal --> str"""
    if eh_presa(animal):
        return f'{obter_especie(animal)} [{obter_idade(animal)}/{obter_freq_reproducao(animal)}]'
    if eh_predador(animal):
        return f'{obter_especie(animal)} [{obter_idade(animal)}/{obter_freq_reproducao(animal)};\
{obter_fome(animal)}/{obter_freq_alimentacao(animal)}]'


    # Funções de Alto nivel

def eh_animal_fertil(animal):
    # Verifica se o animal já alcançou a idade de reprodução ou nao: animal --> boolean
    return obter_idade(animal) >= obter_freq_reproducao(animal)


def eh_animal_faminto(animal):
    """ Verifica se o animal tem um valor de fome superior ou igual não de frequencia de alimentação:
    animall --> boolean"""
    if eh_predador(animal):
        return obter_fome(animal) >= obter_freq_alimentacao(animal)
    if eh_presa(animal):
        return False


def reproduz_animal(animal):
    # Cria um animal novo igual ao primeiro e retorna a idade do primeiro a 0: animal --> animal
    animal2 = cria_copia_animal(animal)
    reset_idade(animal)
    return animal2


# TAD- Prado
    #Funções de baixo nivel

def cria_prado(d, r, a, p):
    """Cria um prado que tem as dimenções da pradaria - d, as posições de rochedos - r, todos os aimais - a e todas
    as posicões correspondentes a cada animal - p: posicao x tuple x tuple x tuple --> prado"""
    # Não sei se está tudo validado nem se a valda_pos está bem chamada                                          (ERRO?)
    # Também não sei se posso alterar a ordem da func.copia e dos seletores                                      (ERRO?)
    if not all([eh_posicao(d), type(r) == tuple, type(a) == tuple, type(p) == tuple]):
        raise ValueError('cria_prado: argumentos invalidos')
    if obter_pos_x(d) < 3 or obter_pos_y(d) < 3:
        raise ValueError('cria_prado: argumentos invalidos')
    if len(r) < 0 or len(a) < 1 or len(a) != len(p):
        raise ValueError('cria_prado: argumentos invalidos')
    if len(r) != 0:
        if not all([eh_posicao(x) for x in r]):
            raise ValueError('cria_prado: argumentos invalidos')
    if not all([eh_animal(x) for x in a]):
        raise ValueError('cria_prado: argumentos invalidos')
    if not all([eh_posicao(x) for x in p]):
        raise ValueError('cria_prado: argumentos invalidos')

    def valida_pos(t):  # Não sei se isto funciona                                                               (ERRO?)
        if not all([obter_pos_y(x) < obter_pos_y(d) and obter_pos_x(x) < obter_pos_x(d) and \
                    obter_pos_y(x) > 0 and obter_pos_x(x) > 0 for x in t]):
            raise ValueError('cria_prado: argumentos invalidos')

    valida_pos(r)
    valida_pos(p)
    if len(r) + len(a) > obter_pos_x(d) * obter_pos_y(d):
        raise ValueError('cria_prado: argumentos invalidos')
    #_Validações_são_tudo_para_cima
    return {'d': d, 'r': r, 'a': a, 'p': p}


def cria_copia_prado(m):
    # Cria uma nova cópia do prado: prado --> prado
    d = m['d']
    r = m['r']
    a = m['a']
    p = m['p']
    return cria_prado(d, r, a, p)


def obter_tamanho_x(m):
    # Dá a dimenção no eixo x do prado a contar com as montanhas: prado --> int
    return (obter_pos_x(m['d']) + 1)


def obter_tamanho_y(m):
    # Dá a dimenção no eixo y do prado a contar com as montanhas: prado --> int
    return (obter_pos_y(m['d']) + 1)


def obter_numero_predadores(m):
    # Dá o numero de predadores presentes no prado: prado --> int
    return len([x for x in m['a'] if eh_predador(x)])


def obter_numero_presas(m):
    # Dá o numero de predadores presentes no prado: prado --> int
    return len([x for x in m['a'] if eh_presa(x)])


def obter_posicao_animais(m):
    # Dá um tuplo com as posições dos animais no prado, ordenadas por ordem de leitura: prado --> tuple posicoes
    return ordenar_posicoes(m['p'])


def indice_posicao(m, p):
    # Dá o indice da posição, ou animal do prado: prado x posicao --> int
    x = 0
    for v in m['p']:
        if posicoes_iguais(v, p):
            return x
        x += 1


def obter_animal(m, p):
    # Dá o animal que está numa dada posição do prado: prado x posicao --> animal
    return m['a'][indice_posicao(m, p)]


def eliminar_animal(m, p):
    # Elimina o animal da posição,deixando-a livre: prado x posicao --> posicao
    m['a'] = m['a'][:indice_posicao(m, p)] + m['a'][(indice_posicao(m, p) + 1):]
    m['p'] = m['p'][:indice_posicao(m, p)] + m['p'][(indice_posicao(m, p) + 1):]


def mover_animal(m, p1, p2):
    # Altera a posição de um animal: prado x posicao x posicao --> prado
    m['p'] = m['p'][:indice_posicao(m, p1)] + (p2,) + m['p'][indice_posicao(m, p1) + 1:]
    return m


def inserir_animal(m, a, p):
    # Adiciona ao prado o animal a na posição p: prado x animal x posicao --> prado
    m['p'] = m['p'] + (p,)
    m['a'] = m['a'] + (a,)
    return m


def eh_prado(m):
    # Verifica se m é um TAD prado, dá True se sim: universal --> boolean
    try:
        cria_copia_prado(m)
    except Exception:
        return False
    else:
        return True


def eh_posicao_animal(m, p):
    # Verifica se a posição p está ocupada por um animal: prado x posicao --> boolean
    return p in m['p']


def eh_posicao_obstaculo(m, p):
    # Verifica se a posição p está ocupada por um obstaculo: prado x posicao --> boolean
    if not eh_posicao(p):
        return False
    return any([p in m['r'], obter_pos_y(p) == 0, obter_pos_x(p) == 0,
                obter_pos_x(p) == (obter_tamanho_x(m) - 1), obter_pos_y(p) == (obter_tamanho_y(m) - 1)])


def eh_posicao_livre(m, p):
    # Verifica se a posição é válida e está livre: prado x posicao --> boolean
    return all([obter_pos_y(p) < obter_tamanho_y(m) - 1, obter_pos_x(p) < obter_tamanho_x(m) - 1,
                obter_pos_y(p) > 0, obter_pos_x(p) > 0,
                not eh_posicao_obstaculo(m, p),
                not eh_posicao_animal(m, p)])


def prados_iguais(m1, m2):
    # Verifica se os dois prados são iguais: prado x prado --> boolean
    if not eh_prado(m1) or not eh_prado(m2):
        return False
    return all([obter_tamanho_x(m1) == obter_tamanho_x(m2), obter_tamanho_y(m1) == obter_tamanho_y(m1),
           m1['r'] == m2['r'], m1['a'] == m2['a'], m1['p'] == m2['p']])


def prado_para_str(m):
    # Converte o prado numa imagem que o representa: prado --> str
    """O raciocinio aqui foi criar uma lista_coordenadas com todas as coordenadas do prado. Depois troca-se cada
    coordenada pela figura correspondente. Isto foi feito ora a verificar se a coordenada estava ocupada, ora vendo se
    ela estava numa lista de coordenadas conhecidas.
    Eu sei que há maneiras mil vezes melhores de fazer isto, mas esta foi a unica em que consegui pensar."""
    cantos = []
    cantos.append(cria_posicao(0, 0))
    cantos.append(cria_posicao(obter_tamanho_x(m) - 1, 0))
    cantos.append(cria_posicao(obter_tamanho_x(m) - 1, obter_tamanho_y(m) - 1))
    cantos.append(cria_posicao(0, obter_tamanho_y(m) - 1))

    lados_x = []
    for x in range(1, obter_tamanho_x(m) - 1):
        lados_x.append(cria_posicao(x, 0))
        lados_x.append(cria_posicao(x, obter_tamanho_y(m) - 1))

    lados_y = []
    for y in range(1, obter_tamanho_y(m) - 1):
        lados_y.append(cria_posicao(0, y))
        lados_y.append(cria_posicao(obter_tamanho_x(m) - 1, y))

    lista_cord = []
    for l in range(obter_tamanho_y(m) + 1 - 1):  # linha
        for c in range(obter_tamanho_x(m) + 1 - 1):
            lista_cord.append(cria_posicao(c, l))
        lista_cord.append('\n')
    # ^ é um mapa posições
    i = 0
    for pos in lista_cord:
        if pos in cantos:
            lista_cord.insert(i, '+')
            lista_cord.pop(i + 1)
            i += 1
        elif pos in lados_y:
            lista_cord.insert(i, '|')
            lista_cord.pop(i + 1)
            i += 1
        elif pos in lados_x:
            lista_cord.insert(i, '-')
            lista_cord.pop(i + 1)
            i += 1
        elif eh_posicao_obstaculo(m, pos):
            lista_cord.insert(i, '@')
            lista_cord.pop(i + 1)
            i += 1
        elif eh_posicao_animal(m, pos):
            lista_cord.insert(i, animal_para_char(obter_animal(m, pos)))
            lista_cord.pop(i + 1)
            i += 1
        elif pos != '\n':
            lista_cord.insert(i, '.')
            lista_cord.pop(i + 1)
            i += 1
        else:
            i += 1
    lista_cord = lista_cord[:-1]
    imagem_prado = ''.join(lista_cord)
    return imagem_prado


    # Funções de Alto nivel

def obter_valor_numerico(m, p):
    # Devolve o número de ordem de leitura correspondente à coordenada: prado x posicao --> int
    return (obter_tamanho_x(m)) * obter_pos_y(p) + obter_pos_x(p)


def obter_movimento(m, p):
    # Devolve a posição para que o animal se vai mover asseguir: prado x posicao --> posicao
    # Escolhi não fazer uma função interna porque os predadores precisão do for para contar as presas
    x = 0
    pa = list(obter_posicoes_adjacentes(p))  # posições adjacentes, numa lista
    pe = []
    for pos in pa:  # validar pa, porque pode ser a baixo do prado
        if not obter_pos_x(pos) < (obter_tamanho_x(m) - 1) or not obter_pos_y(pos) < (obter_tamanho_y(m) - 1):
            x += 1
        else:
            pe.append(pos)
            x += 1
    pa = pe
    if eh_predador(obter_animal(m, p)):
        x = 0
        presas = []
        pe = []
        for pos in pa:
            if not eh_posicao_obstaculo(m, pos):
                pe.append(pos)
            if eh_posicao_animal(m, pos):
                if not eh_predador(obter_animal(m, pos)):
                    pe.append(pos)
                if eh_presa(obter_animal(m, pos)):
                    presas.append(pos)
            x += 1
        pa = pe
        if len(presas) >= 1:
            n = obter_valor_numerico(m, p) % len(presas)
            return presas[n]
        elif len(pa) != 0:  # if len(presas) == 0
            n = obter_valor_numerico(m, p) % len(pa)
            return pa[n]
        else:
            return p

    if eh_presa(obter_animal(m, p)):  # é mais fácil entender o das presas primeiro
        x = 0
        pe = []
        for pos in pa:
            if not eh_posicao_obstaculo(m, pos) and not eh_posicao_animal(m, pos):
                pe.append(pos)
            x += 1
        pa = pe
        if len(pa) != 0:
            n = obter_valor_numerico(m, p) % len(pa)
            return pa[n]
        else:
            return p


# Funções adicionais

def geracao(m):
    val = []
    for pos in obter_posicao_animais(m):
        if pos not in val:
            aumenta_idade(obter_animal(m, pos))
            aumenta_fome(obter_animal(m, pos))
            if eh_animal_fertil(obter_animal(m, pos)):  # Nascimento
                if pos == obter_movimento(m, pos):
                    val.append(pos)
                    pos2 = pos
                elif eh_presa(obter_animal(m, pos)):
                    pos2 = obter_movimento(m, pos)
                    val.append(pos2)
                    val.append(pos)
                    mover_animal(m, pos, pos2)
                    inserir_animal(m, reproduz_animal(obter_animal(m, pos2)), pos)
                elif eh_predador(obter_animal(m, pos)):
                    pos2 = obter_movimento(m, pos)
                    val.append(pos2)
                    val.append(pos)
                    reproduz_animal(obter_animal(m, pos))
                    mover_animal(m, pos, pos2)  # houve aqui duvidas

            elif eh_posicao_animal(m, obter_movimento(m, pos)) and not posicoes_iguais(pos, obter_movimento(m, pos)):
                pos2 = obter_movimento(m, pos)
                if eh_presa(obter_animal(m, pos2)):  # Movimento + Comer
                    reset_fome(obter_animal(m, pos))
                    eliminar_animal(m, pos2)
                    mover_animal(m, pos, pos2)
                    val.append(pos2)

            else:
                pos2 = obter_movimento(m, pos)
                mover_animal(m, pos, pos2)
                val.append(pos2)

            if eh_animal_faminto(obter_animal(m, pos2)):  # Morte por fome
                eliminar_animal(m, pos2)  # referenced before assignment, mas como todos dão pos2 devia dar
    return m


def simula_ecossistema(f, g, v):
    # Simula o ecossistema e retorna o numero de predadores e presas: str x int x booblean --> tuple
    # f-> nome doc.txt, g-> nº gerações, -> modo verboso/quiet (verboso mostra o prado, os nº de animais e a geração
    # sempre que o nº de animais muda

    def str_inicial(npredadores, npresas):
        return print(f'Predadores: {npredadores} vs Presas: {npresas} (Gen. 0) \n{prado_para_str(m)}')


    with open(f, 'r') as file:
        dr = file.readline()
        d = dr.replace('(', '').replace(')', '').replace('\n', '')
        d = d.split(',')
        d = cria_posicao(int(d[0]), int(d[1]))  #___
        rr = file.readline()
        r = rr.replace('(', '').replace(')', '').replace('\n', '')
        r = r.split(',')
        pos = ()
        for n in range(0, len(r), 2):
            pos += (cria_posicao(int(r[n]), int(r[n + 1])),)
        r = pos
        a = ()
        p = ()
        for animal in file.readlines():
            anir = animal
            ani = anir.replace('\n', '').replace('(', '').replace(')', '').replace("'", '')
            ani = ani.split(',')
            a += (cria_animal(ani[0], int(ani[1]), int(ani[2])),)
            p += (cria_posicao(int(ani[3]), int(ani[4])),)
    m = cria_prado(d, r, a, p)
    npresas = obter_numero_presas(m)
    npredadores = obter_numero_predadores(m)  #___
    if v:
        str_inicial(npredadores, npresas)
        for i in range(1, g + 1):
            geracao(m)
            novpresas = obter_numero_presas(m)
            novpredadores = obter_numero_predadores(m)
            if novpresas != npresas or novpredadores != npredadores:
                print(f'Predadores: {novpredadores} vs Presas: {novpresas} (Gen. {i}) \n{prado_para_str(m)}')
                npresas = novpresas
                npredadores = novpredadores
        print((npredadores, npresas))
    else:
        str_inicial(npredadores, npresas)
        for i in range(1, g + 1):
            geracao(m)
        npredadores = obter_numero_predadores(m)
        npresas = obter_numero_presas(m)
        str_inicial(npredadores, npresas)
        print((npredadores, npresas))

simula_ecossistema('config.txt', 200, True)
