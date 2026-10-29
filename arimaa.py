from definiciones import *

#### Algunas funciones ya dadas

def son_posiciones_vecinas(pos1 : Posicion, pos2 : Posicion) -> bool: # pragma: no cover
    return (pos1.fila == pos2.fila and abs(pos1.columna - pos2.columna) == 1) \
        or (pos1.columna == pos2.columna and abs(pos1.fila - pos2.fila) == 1)

def direccion_desde_hasta(pos1 : Posicion, pos2 : Posicion) -> Direccion: # pragma: no cover
    assert son_posiciones_vecinas(pos1, pos2)
    if pos1.fila < pos2.fila:
       return NORTE
    elif pos1.fila > pos2.fila:
       return SUR
    elif pos1.columna < pos2.columna:
       return ESTE
    else:
       return OESTE

def pasar_turno(j : Juego) -> Juego: # pragma: no cover
    return Juego(j.tablero, oponente(j.turno), 0)

#### Ejercicio 1

def tableroBienFormado(t: Tablero)->bool:
    """
    Indica si el tablero t tiene exactamente Alto filas y cada fila tiene exactamente
    Ancho casillas.
    """
    res : bool = len(t) == ALTO
    i : int
    for i in range(len(t)): # Este for recore las filas del tablero mediante su indice
        if len(t[i]) != ANCHO:
            res = False
    return res


def tablero_bien_formado(t : Tablero) -> bool:
    """
    Indica si el tablero t está bien formado, es decir, si tiene Alto filas de Ancho
    casillas cada una.
    """
    return tableroBienFormado(t) 


def posicionEnTablero(pos:Posicion)->bool:
    """
    Indica si la posición pos está dentro del tablero, es decir, si su fila y su columna
    están entre 0 y 7.
    """
    return 0 <= pos.fila < ALTO and 0 <= pos.columna < ANCHO


def posicion_en_tablero(pos : Posicion) -> bool:
    """
    Indica si la posición pos está dentro del tablero.
    """
    return posicionEnTablero(pos) 


def movimientobienFormado(m : Movimiento) -> bool:
    """
    Indica si el movimiento m está bien formado: su origen está dentro del tablero y
    tiene un solo paso si es mover a secas o dos pasos si es arrastrar o empujar.
    """
    return (posicion_en_tablero(m.origen)
            and ((m.accion == MOVER_A_SECAS and len(m.pasos) == 1)
                 or (m.accion == EMPUJAR and len(m.pasos) == 2)
                 or (m.accion == ARRASTRAR and len(m.pasos) == 2)))

def movimiento_bien_formado(m : Movimiento) -> bool:
    """
    Indica si el movimiento m está bien formado.
    """
    return movimientobienFormado(m) 


def juegoBienFormado(j: Juego) ->bool:
    """
    Indica si el juego j está bien formado: su tablero está bien formado y los pasos
    consumidos están entre 0 y Max_pasos - 1.
    """
    return tablero_bien_formado(j.tablero) and 0 <= j.pasos_consumidos < MAX_PASOS #si es tablero esta bien formado y los pasos consumidos estan entre 0 y menor a 4 da True


def juego_bien_formado(j : Juego) -> bool:
    """
    Indica si el juego j está bien formado.
    """

    return juegoBienFormado(j) 


#### Ejercicio 2
def esPosicionVecinaHacia(pos:Posicion, d: Direccion, pos1: Posicion) -> bool:
    """
    Indica si pos1 es la posición vecina a pos en la dirección d, es decir, la que está
    a una casilla de distancia en esa dirección.
    """
    return ((d == NORTE and (pos1.fila == pos.fila + 1 and pos1.columna == pos.columna))
            or (d == SUR and (pos1.fila == pos.fila - 1 and pos1.columna == pos.columna))
            or (d == ESTE and (pos1.fila == pos.fila and pos1.columna == pos.columna + 1))
            or (d == OESTE and (pos1.fila == pos.fila and pos1.columna == pos.columna - 1)))


def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:
    """
    Devuelve la posición vecina a pos en la dirección d. La posición devuelta puede
    quedar fuera del tablero.
    """
    res : Posicion
    if d == NORTE:
        res = Posicion(pos.fila + 1, pos.columna)
    elif d == SUR:
        res = Posicion(pos.fila - 1, pos.columna)
    elif d == ESTE:
        res = Posicion(pos.fila, pos.columna + 1)
    else:
        res = Posicion(pos.fila, pos.columna - 1)
    return res


def casilla_en_posicion(t : Tablero, p : Posicion) -> Casilla:
    """
    Devuelve la casilla ubicada en la posición p del tablero t.
    """
    return t[p.fila][p.columna]

    
def hayCasillaVacia(t:Tablero, pos:Posicion) -> bool:
    """
    Indica si la posición pos está dentro del tablero y su casilla está vacía.
    """
    return posicionEnTablero(pos) and t[pos.fila][pos.columna] == CasillaVacia.VACIA


def hay_casilla_vacia(t : Tablero, pos : Posicion) -> bool:
    """
    Indica si la posición pos está dentro del tablero y su casilla está vacía.
    """
    return hayCasillaVacia(t,pos)

def hayFiguraDeColor(t:Tablero, pos:Posicion, f: Figura, col: Color) -> bool:
    """
    Indica si en la posición pos hay una pieza de figura f y de color col.
    """
    return (posicionEnTablero(pos)
            and not hayCasillaVacia(t, pos)
            and t[pos.fila][pos.columna].figura == f
            and t[pos.fila][pos.columna].color == col)

def hayPiezaDeColor(t:Tablero, pos:Posicion, col:Color) -> bool:
    """
    Indica si en la posición pos hay una pieza del color col, sin importar su figura.
    """
    return (hayFiguraDeColor(t, pos, ELEFANTE, col)
            or hayFiguraDeColor(t, pos, CAMELLO, col)
            or hayFiguraDeColor(t, pos, CABALLO, col)
            or hayFiguraDeColor(t, pos, PERRO, col)
            or hayFiguraDeColor(t, pos, GATO, col)
            or hayFiguraDeColor(t, pos, CONEJO, col))


def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
    """
    Indica si en la posición pos hay una pieza del color col, sin importar su figura.
    """
    return hayPiezaDeColor(t, pos, col)

#### Ejercicio 3

def hay_casilla_vacia_hacia(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    """
    Indica si la casilla vecina a pos en la dirección d existe (está dentro del tablero)
    y está vacía.
    """
    return hay_casilla_vacia(t, posicion_vecina_hacia(pos, d))


def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    """
    Indica si alguna de las cuatro posiciones vecinas a pos tiene una pieza del mismo
    color que la pieza ubicada en pos.
    """
    return hayPiezaAmigaVecina(t, pos)

def hayPiezaAmigaHacia (t : Tablero , pos : Posicion , d : Direccion ) -> bool:
    """
    Indica si la posición vecina a pos en la dirección d tiene una pieza del mismo color
    que la pieza ubicada en pos.
    """
    col : Color = casilla_en_posicion(t,pos).color 
    vecina :  Posicion = posicion_vecina_hacia(pos,d)
    return hay_pieza_de_color(t, vecina, col)

def hayPiezaAmigaVecina(t: Tablero, pos: Posicion) -> bool:
    """
    Indica si alguna de las cuatro posiciones vecinas a pos tiene una pieza del mismo
    color que la pieza ubicada en pos.
    """
    return (hayPiezaAmigaHacia(t, pos, NORTE)
            or hayPiezaAmigaHacia(t, pos, SUR)
            or hayPiezaAmigaHacia(t, pos, ESTE)
            or hayPiezaAmigaHacia(t, pos, OESTE))

def hayPieza(t: Tablero, pos: Posicion) -> bool:
    """
    Indica si hay una pieza (de cualquier figura y color) en la posición pos.
    """
    return posicionEnTablero(pos) and not hayCasillaVacia(t, pos)

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Indica si la posición vecina a pos en la dirección d tiene una pieza del oponente
    más débil que la pieza ubicada en pos.
    """
    mia : Casilla = casilla_en_posicion(t, pos)
    pos_enemiga : Posicion = posicion_vecina_hacia(pos, d)
    return (hay_pieza_de_color(t, pos_enemiga, oponente(mia.color))
            and fuerza(mia.figura) > fuerza(casilla_en_posicion(t, pos_enemiga).figura))


def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool:
    """
    Indica si alguna de las cuatro posiciones vecinas a pos tiene una pieza del oponente
    más fuerte que la pieza ubicada en pos.
    """
    return hayPiezaEnemigaMasFuerteVecina(t, pos)


def hayPiezaEnemigaMasFuerteHacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Indica si la posición vecina a pos en la dirección d tiene una pieza del oponente
    más fuerte que la pieza ubicada en pos.
    """
    mia : Casilla = casilla_en_posicion(t, pos)
    pos_enemiga : Posicion = posicion_vecina_hacia(pos, d)
    return (hay_pieza_de_color(t, pos_enemiga, oponente(mia.color))
            and fuerza(mia.figura) < fuerza(casilla_en_posicion(t, pos_enemiga).figura))


def hayPiezaEnemigaMasFuerteVecina(t : Tablero, pos : Posicion) -> bool:
    """
    Indica si alguna de las cuatro posiciones vecinas a pos tiene una pieza del oponente
    más fuerte que la pieza ubicada en pos.
    """
    return (hayPiezaEnemigaMasFuerteHacia(t, pos, NORTE)
            or hayPiezaEnemigaMasFuerteHacia(t, pos, SUR)
            or hayPiezaEnemigaMasFuerteHacia(t, pos, ESTE)
            or hayPiezaEnemigaMasFuerteHacia(t, pos, OESTE))



def hay_pieza_congelada(t : Tablero, pos : Posicion) -> bool:
    """
    Indica si hay una pieza en pos y está congelada, es decir, si tiene alguna pieza
    enemiga más fuerte como vecina y ninguna pieza amiga como vecina.
    """
    return (hayPieza(t, pos)
            and hay_pieza_enemiga_mas_fuerte_vecina(t, pos)
            and not hay_pieza_amiga_vecina(t, pos))

#### Ejercicio 4

def direccionDeMovimientoHabilitada(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Indica si la pieza ubicada en pos puede moverse en la dirección d. Todas las piezas
    pueden moverse hacia cualquier dirección, salvo los conejos, que no pueden
    retroceder: el conejo dorado no puede ir al sur y el conejo plateado no puede ir al
    norte.
    """
    pieza : Casilla = casilla_en_posicion(t, pos)
    retrocede : bool = ((pieza.figura == CONEJO and pieza.color == DORADO and d == SUR)
                        or (pieza.figura == CONEJO and pieza.color == PLATEADO and d == NORTE))
    return not retrocede


def puedeMoverASecas(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Indica si la pieza ubicada en pos puede moverse a secas en la dirección d, es decir,
    si la casilla vecina en esa dirección está vacía.
    """
    return hay_casilla_vacia_hacia(t, pos, d)


def puedeArrastrar(t : Tablero, pos : Posicion, d : Direccion, d_arrastre : Direccion) -> bool:
    """
    Indica si la pieza ubicada en pos puede moverse en la dirección d arrastrando a una
    pieza enemiga más débil, que está del lado opuesto a d_arrastre y se mueve hacia
    pos.
    """
    return (hay_casilla_vacia_hacia(t, pos, d)
            and hay_pieza_enemiga_mas_debil_hacia(t, pos, opuesta(d_arrastre)))


def puedeEmpujar(t : Tablero, pos : Posicion, d : Direccion, d_empuje : Direccion) -> bool:
    """
    Indica si la pieza ubicada en pos puede moverse en la dirección d empujando hacia
    d_empuje a la pieza enemiga más débil que está en esa dirección.
    """
    return (hay_pieza_enemiga_mas_debil_hacia(t, pos, d)
            and hay_casilla_vacia_hacia(t, posicion_vecina_hacia(pos, d), d_empuje))


def puedeRealizarAccion(t : Tablero, m : Movimiento) -> bool:
    """
    Indica si la acción del movimiento m (mover a secas, arrastrar o empujar) se puede
    realizar en el tablero t desde la posición de origen de m.
    """
    return ((m.accion == MOVER_A_SECAS and puedeMoverASecas(t, m.origen, m.pasos[0]))
            or (m.accion == ARRASTRAR and puedeArrastrar(t, m.origen, m.pasos[0], m.pasos[1]))
            or (m.accion == EMPUJAR and puedeEmpujar(t, m.origen, m.pasos[0], m.pasos[1])))


def puedeRealizarMovimiento(j : Juego, m : Movimiento) -> bool:
    """
    Indica si el jugador al que le toca jugar en j puede realizar el movimiento m: la
    pieza de origen es suya y no está congelada, la dirección está habilitada, no se
    superan los pasos del turno y la acción se puede realizar.
    """
    return (hay_pieza_de_color(j.tablero, m.origen, j.turno)
            and not hay_pieza_congelada(j.tablero, m.origen)
            and direccionDeMovimientoHabilitada(j.tablero, m.origen, m.pasos[0])
            and j.pasos_consumidos + len(m.pasos) <= MAX_PASOS
            and puedeRealizarAccion(j.tablero, m))


def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:
    """
    Indica si el jugador al que le toca jugar en j puede realizar el movimiento m.
    """
    return puedeRealizarMovimiento(j, m)

#### Ejercicio 5

def copiarTablero(t : Tablero) -> Tablero:
    """
    Devuelve un tablero nuevo con las mismas casillas que t, independiente de t.
    """
    copia : Tablero = []
    fila : list[Casilla]
    casilla : Casilla
    for fila in t:
        fila_nueva : list[Casilla] = []
        for casilla in fila:
            fila_nueva.append(casilla)
        copia.append(fila_nueva)
    return copia


def sacarPieza(t : Tablero, pos : Posicion) -> None:
    """
    Deja vacía la casilla en la posición pos del tablero t, sin tocar ninguna otra.
    Modifica el tablero t en lugar de devolver uno nuevo.
    """
    t[pos.fila][pos.columna] = VACIA


def activarTrampa(t : Tablero, pos : Posicion) -> None:
    """
    Activa la casilla trampa en pos sobre t: si hay una pieza en pos y no tiene ninguna
    pieza amiga vecina, la retira. En cualquier otro caso el tablero queda igual.
    Modifica el tablero t.
    """
    tiene_amiga_vecina : bool = hayPieza(t, pos) and hay_pieza_amiga_vecina(t, pos)
    if not tiene_amiga_vecina:
        sacarPieza(t, pos)


def activarTrampas(t : Tablero) -> Tablero:
    """
    Devuelve el tablero que resulta de activar las cuatro casillas trampa sobre t, sin
    modificar t.
    """
    res : Tablero = copiarTablero(t)
    pos_trampa : Posicion
    for pos_trampa in POSICIONES_TRAMPA:
        activarTrampa(res, pos_trampa)
    return res


def activar_trampas(t : Tablero) -> Tablero:
    """
    Devuelve el tablero que resulta de activar las cuatro casillas trampa sobre t: se
    retira toda pieza ubicada en una trampa que no tenga ninguna pieza amiga vecina.
    """
    return activarTrampas(t)

#### Ejercicio 6

def tableroTrasladandoPieza(t0 : Tablero, posorigen : Posicion, posdestino : Posicion) -> Tablero:
    """
    Devuelve el tablero que resulta de trasladar la pieza ubicada en posorigen a
    posdestino: la casilla de origen queda vacía y la de destino pasa a tener esa pieza.
    No modifica t0.
    """
    res : Tablero = copiarTablero(t0)
    res[posdestino.fila][posdestino.columna] = casilla_en_posicion(t0, posorigen)
    sacarPieza(res, posorigen)
    return res


def tableroPostMoverASecas(t0 : Tablero, pos : Posicion, d : Direccion) -> Tablero:
    """
    Devuelve el tablero que resulta de mover a secas la pieza ubicada en pos una casilla
    hacia d y activar luego las trampas.
    """
    posdestino : Posicion = posicion_vecina_hacia(pos, d)
    tintermedio : Tablero = tableroTrasladandoPieza(t0, pos, posdestino)
    return activar_trampas(tintermedio)


def tableroPostArrastrar(t0 : Tablero, pos : Posicion, d : Direccion, darrastre : Direccion) -> Tablero:
    """
    Devuelve el tablero que resulta de mover la pieza ubicada en pos hacia d arrastrando
    a la pieza enemiga que está del lado opuesto a darrastre (que termina en pos), y de
    activar luego las trampas.
    """
    poshueco : Posicion = posicion_vecina_hacia(pos, d)
    posenemiga : Posicion = posicion_vecina_hacia(pos, opuesta(darrastre))
    tintermedio1 : Tablero = tableroTrasladandoPieza(t0, pos, poshueco)
    tintermedio2 : Tablero = tableroTrasladandoPieza(tintermedio1, posenemiga, pos)
    return activar_trampas(tintermedio2)


def tableroPostEmpujar(t0 : Tablero, pos : Posicion, d : Direccion, dempuje : Direccion) -> Tablero:
    """
    Devuelve el tablero que resulta de mover la pieza ubicada en pos hacia d empujando
    hacia dempuje a la pieza enemiga que está en esa dirección (la pieza que empuja
    termina donde estaba la empujada), y de activar luego las trampas.
    """
    posenemiga : Posicion = posicion_vecina_hacia(pos, d)
    poshueco : Posicion = posicion_vecina_hacia(posenemiga, dempuje)
    tintermedio1 : Tablero = tableroTrasladandoPieza(t0, posenemiga, poshueco)
    tintermedio2 : Tablero = tableroTrasladandoPieza(tintermedio1, pos, posenemiga)
    return activar_trampas(tintermedio2)


def tableroPostMovimiento(t0 : Tablero, m : Movimiento) -> Tablero:
    """
    Devuelve el tablero que resulta de realizar el movimiento m sobre t0 según su acción
    (mover a secas, arrastrar o empujar).
    """
    res : Tablero
    if m.accion == MOVER_A_SECAS:
        res = tableroPostMoverASecas(t0, m.origen, m.pasos[0])
    elif m.accion == ARRASTRAR:
        res = tableroPostArrastrar(t0, m.origen, m.pasos[0], m.pasos[1])
    else:
        res = tableroPostEmpujar(t0, m.origen, m.pasos[0], m.pasos[1])
    return res


def hayQueCambiarDeTurno(j : Juego, m : Movimiento) -> bool:
    """
    Indica si, al realizar el movimiento m en el juego j, el jugador agota los pasos de
    su turno y el turno debe pasar al oponente.
    """
    return j.pasos_consumidos + len(m.pasos) == MAX_PASOS


def juegoConTurnoPosiblementeAvanzado(j0 : Juego, m : Movimiento) -> Juego:
    """
    Devuelve un juego con el mismo tablero que j0 en el que ya se contaron los pasos del
    movimiento m. Si se agotan los pasos del turno, el turno pasa al oponente con 0
    pasos consumidos; si no, el turno se mantiene y se suman los pasos del movimiento.
    """
    res : Juego
    if hayQueCambiarDeTurno(j0, m):
        res = pasar_turno(j0)
    else:
        res = Juego(j0.tablero, j0.turno, j0.pasos_consumidos + len(m.pasos))
    return res


def juegoPostMovimiento(j0 : Juego, m : Movimiento) -> Juego:
    """
    Devuelve el juego que resulta de realizar el movimiento m en j0, con el tablero
    actualizado y con el turno y los pasos al día.
    """
    tablero_nuevo : Tablero = tableroPostMovimiento(j0.tablero, m)
    j_con_tablero_nuevo : Juego = Juego(tablero_nuevo, j0.turno, j0.pasos_consumidos)
    return juegoConTurnoPosiblementeAvanzado(j_con_tablero_nuevo, m)


def realizar_movimiento(j : Juego, m : Movimiento) -> Juego:
    """
    Devuelve el juego que resulta de realizar el movimiento m en j: se mueven las
    piezas, se activan las trampas y se actualizan el turno y los pasos consumidos.
    """
    return juegoPostMovimiento(j, m)

#### Ejercicio 7

def esInicioDeTurno(j : Juego, col : Color) -> bool:
    """
    Indica si en el juego j es el turno de col y todavía no consumió ningún paso, es
    decir, si el oponente de col acaba de terminar su jugada.
    """
    return j.turno == col and j.pasos_consumidos == 0


def hayConejoEnFila(j : Juego, fila : int, col : Color) -> bool:
    """
    Indica si hay algún conejo del color col en la fila fila del tablero de j.
    """
    hay_conejo : bool = False
    columna : int
    for columna in range(ANCHO):
        if hayFiguraDeColor(j.tablero, Posicion(fila, columna), CONEJO, col):
            hay_conejo = True
    return hay_conejo


def hayConejoEnTablero(j : Juego, col : Color) -> bool:
    """
    Indica si queda algún conejo del color col en el tablero de j.
    """
    hay_conejo : bool = False
    fila : int
    for fila in range(ALTO):
        if hayConejoEnFila(j, fila, col):
            hay_conejo = True
    return hay_conejo


def posicionEnFilaInicial(pos : Posicion, col : Color) -> bool:
    """
    Indica si pos está en la fila inicial del jugador de color col: la fila 0 para el
    dorado y la fila 7 para el plateado.
    """
    return (col == DORADO and pos.fila == 0) or (col == PLATEADO and pos.fila == ALTO - 1)


def hayConejoEnFilaInicialOponente(j : Juego, col : Color) -> bool:
    """
    Indica si hay algún conejo del color col en la fila inicial de su oponente.
    """
    hay_conejo : bool = False
    fila : int
    for fila in range(ALTO):
        if posicionEnFilaInicial(Posicion(fila, 0), oponente(col)) and hayConejoEnFila(j, fila, col):
            hay_conejo = True
    return hay_conejo


def reuneCondicionesDeGanar(j : Juego, col : Color) -> bool:
    """
    Indica si el jugador de color col cumple alguna condición de victoria: tiene un
    conejo en la fila inicial del oponente o el oponente se quedó sin conejos.
    """
    return hayConejoEnFilaInicialOponente(j, col) or not hayConejoEnTablero(j, oponente(col))


def reuneCondicionesDeGanarExclusivas(j : Juego, col : Color) -> bool:
    """
    Indica si el jugador de color col cumple alguna condición de victoria y su oponente
    no cumple ninguna.
    """
    return reuneCondicionesDeGanar(j, col) and not reuneCondicionesDeGanar(j, oponente(col))


def esJugadorGanador(j : Juego, col : Color) -> bool:
    """
    Indica si el jugador de color col ganó en j. Si el juego está al inicio del turno
    del oponente (col acaba de jugar), alcanza con que cumpla alguna condición de
    victoria. Si está al inicio del turno de col (el oponente acaba de jugar), solo gana
    si es el único que la cumple. En cualquier otro momento nadie gana.
    """
    return ((esInicioDeTurno(j, oponente(col)) and reuneCondicionesDeGanar(j, col))
            or (esInicioDeTurno(j, col) and reuneCondicionesDeGanarExclusivas(j, col)))


def hayGanadorDeterminado(j : Juego) -> bool:
    """
    Indica si alguno de los dos jugadores ganó en j.
    """
    return esJugadorGanador(j, DORADO) or esJugadorGanador(j, PLATEADO)


def hay_ganador_determinado(j : Juego) -> bool:
    """
    Indica si alguno de los dos jugadores ganó en j.
    """
    return hayGanadorDeterminado(j)


def ganador_del_juego(j : Juego) -> Color:
    """
    Devuelve el color del jugador que ganó en j. Solo tiene sentido si hay un ganador
    determinado.
    """
    res : Color
    if esJugadorGanador(j, DORADO):
        res = DORADO
    else:
        res = PLATEADO
    return res