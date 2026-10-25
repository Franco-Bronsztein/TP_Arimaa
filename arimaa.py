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
    if len(t) != 8: #len(t) da la catidad de filas del tablero si es distinto a 8 da False
        return False
    for i in range(len(t)): # Este for recore las filas del tablero mediante su indice
        if len(t[i]) !=8: #El len(t[i]) va verificando que la fila correspondiente al indice i que viene del for tenga efectivamente 8 indices(8 columnas)
            return False # si el tamblero no tiene 8 columnas da False
    return True


def tablero_bien_formado(t : Tablero) -> bool: #Recibe el tablero y comprueba si esta bien formado llamando a la auxiliar tablerobienformado
    return tableroBienFormado(t) 


def posicionEnTablero(pos:Posicion)->bool: #Esta funcion combrueba si la posicion se cumple tanto en fila como en columnas, si no hay una cordenada fuera de rango
    return 0<= pos.fila < 8 and 0<= pos.columna < 8 


def posicion_en_tablero(pos : Posicion) -> bool: #Recibe la posicion:pos y llama a la funcion auxuliar para devolver un bool
    return posicionEnTablero(pos) 


def movimientobienFormado(m : Movimiento) -> bool:

    if posicion_en_tablero (m.origen) and m.accion== MOVER_A_SECAS and len(m.pasos)==1: #Este if verifica si la coordenada es true, si la anccion es mover a secar y la longitud de pasos es 1 da True
        return True
    if posicion_en_tablero (m.origen) and m.accion== EMPUJAR and len(m.pasos)==2: #Este if verifica si la coordenada es true, si la anccion es Empujar y la longitud de pasos es 2 da True
            return True
    if posicion_en_tablero(m.origen) and m.accion== ARRASTRAR and len(m.pasos)==2: #Este if verifica si la coordenada es true, si la anccion es Arrastrar y la longitud de pasos es 2 da True
                return True
    return False

def movimiento_bien_formado(m : Movimiento) -> bool:#Recibe el movimiento:m y llama a la funcion auxiliar para devolver un bool
    return movimientobienFormado(m) 


def juegoBienFormado(j: Juego) ->bool:
    if tablero_bien_formado(j.tablero) and 0<= j.pasos_consumidos < MAX_PASOS: #si es tablero esta bien formado y los pasos consumidos estan entre 0 y menor a 4 da True
        return True
    return False


def juego_bien_formado(j : Juego) -> bool:#Recibe los parametros del juego y devuelve un bool si pasa juegoBienFormado

    return juegoBienFormado(j) 


#### Ejercicio 2
def esPosicionVecinaHacia(pos:Posicion, d: Direccion, pos1: Posicion) -> bool: #esta funcion recibe una posicion y verifica si hay 1 casilla de distancia en la direccion indicada
    if  d==NORTE and (pos1.fila == pos.fila + 1 and pos1.columna==pos.columna): 
        return True
    if  d==SUR and (pos1.fila == pos.fila -1 and pos1.columna ==pos.columna):
        return True
    if  d==ESTE and (pos1.fila ==pos.fila and pos1.columna == pos.columna + 1):
        return True
    if d==OESTE and (pos1.fila == pos.fila and pos1.columna ==pos.columna -1):
        return True
    return False


def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion: #devuelve la posición vecina al origen en la dirección indicada.
    if d==NORTE:
        return Posicion(pos.fila + 1, pos.columna)
    if d==SUR:
        return Posicion(pos.fila - 1, pos.columna)
    if d==ESTE:
        return Posicion(pos.fila, pos.columna + 1)
    else:
        return Posicion(pos.fila, pos.columna - 1)


def casilla_en_posicion(t : Tablero, p : Posicion) -> Casilla: #Devuelve la casilla de la posicion indicada 
    return t[p.fila][p.columna]

    
def hayCasillaVacia(t:Tablero, pos:Posicion) -> bool: #Indica si la casilla esta vacia, si no lo esta devuelve un False
    if posicionEnTablero(pos) and t[pos.fila][pos.columna]== CasillaVacia.VACIA:
        return True
    return False


def hay_casilla_vacia(t : Tablero, pos : Posicion) -> bool: #Llama a la funcion auxiliar con el tablero y la posicion indicada, devulve un bool
    return hayCasillaVacia(t,pos)

def hayFiguraDeColor(t:Tablero, pos:Posicion, f: Figura, col: Color) -> bool: #Agarra una casilla y verifica si ha una figura de color, si la figura concuerda con el parametro y es del mismo color, la funcion da True
    if posicionEnTablero(pos) and not hayCasillaVacia(t, pos) and t[pos.fila][pos.columna].figura == f  and t[pos.fila][pos.columna].color == col:
        return True
    return False

def hayPiezaDeColor(t:Tablero, pos:Posicion, col:Color) -> bool: #Comprueba si en la posición indicada hay una pieza del color especificado, sin importar qué figura sea.
    if hayFiguraDeColor(t,pos, ELEFANTE,col):
        return True
    if hayFiguraDeColor(t, pos, CAMELLO, col):
        return True
    if hayFiguraDeColor(t, pos, CABALLO, col):
        return True
    if hayFiguraDeColor(t, pos, PERRO, col):
        return True
    if hayFiguraDeColor (t, pos, GATO, col):
        return True
    if hayFiguraDeColor (t, pos, CONEJO, col):
        return True
    return False


def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool: #Llama a la función auxiliar pasándole el tablero, la posición y el color. Devuelve el mismo resultado que obtiene de ella.
    return hayPiezaDeColor(t, pos, col)

#### Ejercicio 3

def hay_casilla_vacia_hacia(t: Tablero, pos: Posicion, d: Direccion) -> bool: #Indica si la casilla vecina a pos en la dirección d existe y está vacía.
    return hay_casilla_vacia(t, posicion_vecina_hacia(pos, d))


def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool: ## comrpueba si hay una pieza vecina a la que se va a jugar
    return hayPiezaAmigaVecina(t, pos)

def hayPiezaAmigaHacia (t : Tablero , pos : Posicion , d : Direccion ) -> bool: ## Indica si alguna de las 4 vecinas de pos tiene una pieza del mismo color que la pieza que está en pos.
    col : Color = casilla_en_posicion(t,pos).color 
    vecina :  Posicion = posicion_vecina_hacia(pos,d)
    return hay_pieza_de_color(t, vecina, col)

def hayPiezaAmigaVecina(t: Tablero, pos: Posicion) -> bool: ## indica si hay una pieza (de cualquier figura y color) en pos vecina
    return (hayPiezaAmigaHacia(t, pos, NORTE)
            or hayPiezaAmigaHacia(t, pos, SUR)
            or hayPiezaAmigaHacia(t, pos, ESTE)
            or hayPiezaAmigaHacia(t, pos, OESTE))

def hayPieza(t: Tablero, pos: Posicion) -> bool: ##Indica si hay una pieza (de cualquier figura y color) en la posición pos. 
    return posicionEnTablero(pos) and not hayCasillaVacia(t, pos)

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool: # Indica si la pieza vecina a pos en la dirección d es del oponente y es más débil que la pieza ubicada en pos.
    mia = casilla_en_posicion(t, pos)
    pos_enemiga = posicion_vecina_hacia(pos, d)
    return (hay_pieza_de_color(t, pos_enemiga, oponente(mia.color)) and fuerza(mia.figura) > fuerza(casilla_en_posicion(t, pos_enemiga).figura))


def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool: # Indica si alguna de las 4 posiciones vecinas a pos tiene una pieza del oponente más fuerte que la pieza ubicada en pos.
    return hayPiezaEnemigaMasFuerteVecina(t, pos)


def hayPiezaEnemigaMasFuerteHacia(t : Tablero, pos : Posicion, d : Direccion) -> bool: # Indica si la pieza vecina a pos en la dirección d es del oponente y es más fuerte que la pieza ubicada en pos.
    mia : Casilla = casilla_en_posicion(t, pos)
    pos_enemiga : Posicion = posicion_vecina_hacia(pos, d)
    return (hay_pieza_de_color(t, pos_enemiga, oponente(mia.color))
            and fuerza(mia.figura) < fuerza(casilla_en_posicion(t, pos_enemiga).figura))


def hayPiezaEnemigaMasFuerteVecina(t : Tablero, pos : Posicion) -> bool: # Indica si alguna de las 4 posiciones vecinas a pos tiene una pieza del oponente más fuerte que la pieza ubicada en pos.
    return (hayPiezaEnemigaMasFuerteHacia(t, pos, NORTE)
            or hayPiezaEnemigaMasFuerteHacia(t, pos, SUR)
            or hayPiezaEnemigaMasFuerteHacia(t, pos, ESTE)
            or hayPiezaEnemigaMasFuerteHacia(t, pos, OESTE))



def hay_pieza_congelada(t : Tablero, pos : Posicion) -> bool: # Indica si hay una pieza en pos que está congelada, es decir, que tiene una pieza enemiga más fuerte vecina y no tiene ninguna pieza amiga vecina.
    return (hayPieza(t, pos)
            and hay_pieza_enemiga_mas_fuerte_vecina(t, pos)
            and not hay_pieza_amiga_vecina(t, pos))

#### Ejercicio 4

def direccionDeMovimientoHabilitada(t : Tablero, pos : Posicion, d : Direccion) -> bool: # Indica si la pieza ubicada en pos puede moverse en la dirección d. Los conejos no pueden retroceder: el dorado no puede ir al sur y el plateado no puede ir al norte.
    pieza : Casilla = casilla_en_posicion(t, pos)
    retrocede : bool = ((pieza.figura == CONEJO and pieza.color == DORADO and d == SUR)
                        or (pieza.figura == CONEJO and pieza.color == PLATEADO and d == NORTE))
    return not retrocede


def puedeMoverASecas(t : Tablero, pos : Posicion, d : Direccion) -> bool: # Indica si la pieza ubicada en pos puede moverse a secas en la dirección d, es decir, si la casilla vecina en esa dirección está vacía.
    return hay_casilla_vacia_hacia(t, pos, d)


def puedeArrastrar(t : Tablero, pos : Posicion, d : Direccion, d_arrastre : Direccion) -> bool: # Indica si la pieza ubicada en pos puede moverse en la dirección d arrastrando a una pieza enemiga más débil, ubicada del lado opuesto a d_arrastre, que se mueve hacia pos.
    return (hay_casilla_vacia_hacia(t, pos, d)
            and hay_pieza_enemiga_mas_debil_hacia(t, pos, opuesta(d_arrastre)))


def puedeEmpujar(t : Tablero, pos : Posicion, d : Direccion, d_empuje : Direccion) -> bool: # Indica si la pieza ubicada en pos puede moverse en la dirección d empujando hacia d_empuje a la pieza enemiga más débil que está en esa dirección.
    return (hay_pieza_enemiga_mas_debil_hacia(t, pos, d)
            and hay_casilla_vacia_hacia(t, posicion_vecina_hacia(pos, d), d_empuje))


def puedeRealizarAccion(t : Tablero, m : Movimiento) -> bool: # Indica si, en el tablero t, la acción del movimiento m (mover a secas, arrastrar o empujar) se puede realizar desde su posición de origen.
    return ((m.accion == MOVER_A_SECAS and puedeMoverASecas(t, m.origen, m.pasos[0]))
            or (m.accion == ARRASTRAR and puedeArrastrar(t, m.origen, m.pasos[0], m.pasos[1]))
            or (m.accion == EMPUJAR and puedeEmpujar(t, m.origen, m.pasos[0], m.pasos[1])))


def puedeRealizarMovimiento(j : Juego, m : Movimiento) -> bool: # Indica si el jugador al que le toca jugar en j puede realizar el movimiento m.
    return (hay_pieza_de_color(j.tablero, m.origen, j.turno)
            and not hay_pieza_congelada(j.tablero, m.origen)
            and direccionDeMovimientoHabilitada(j.tablero, m.origen, m.pasos[0])
            and j.pasos_consumidos + len(m.pasos) <= MAX_PASOS
            and puedeRealizarAccion(j.tablero, m))


def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool: # Indica si el jugador al que le toca jugar en j puede realizar el movimiento m.
    return puedeRealizarMovimiento(j, m)

#### Ejercicio 5

def copiarTablero(t : Tablero) -> Tablero: # Devuelve un tablero nuevo con las mismas casillas que t pero independiente de él.
    copia : Tablero = []
    for fila in t:
        fila_nueva : list[Casilla] = []
        for casilla in fila:
            fila_nueva.append(casilla)
        copia.append(fila_nueva)
    return copia


def sacarPieza(t : Tablero, pos : Posicion) -> None: # Deja vacía la casilla en pos del tablero t, sin tocar ninguna otra. Modifica el tablero t en lugar de devolver uno nuevo.
    t[pos.fila][pos.columna] = VACIA


def activarTrampa(t : Tablero, pos : Posicion) -> None: # Activa la casilla trampa en pos sobre t. Si la pieza de pos no tiene ninguna pieza amiga vecina, la retira. Si tiene alguna, o si la casilla está vacía, el tablero queda igual.
    tiene_amiga_vecina : bool = hayPieza(t, pos) and hay_pieza_amiga_vecina(t, pos)
    if not tiene_amiga_vecina:
        sacarPieza(t, pos)


def activarTrampas(t : Tablero) -> Tablero: # Devuelve el tablero que resulta de activar las cuatro casillas trampa sobre t, sin modificar t.
    res : Tablero = copiarTablero(t)
    for pos_trampa in POSICIONES_TRAMPA:
        activarTrampa(res, pos_trampa)
    return res


def activar_trampas(t : Tablero) -> Tablero: # Devuelve el tablero que resulta de activar las cuatro casillas trampa sobre t.
    return activarTrampas(t)

#### Ejercicio 6

def tableroTrasladandoPieza(t0 : Tablero, posorigen : Posicion, posdestino : Posicion) -> Tablero: # Devuelve el tablero que resulta de trasladar la pieza ubicada en posorigen a posdestino: la casilla de origen queda vacía y la de destino pasa a tener esa pieza. No modifica t0.
    res : Tablero = copiarTablero(t0)
    res[posdestino.fila][posdestino.columna] = casilla_en_posicion(t0, posorigen)
    sacarPieza(res, posorigen)
    return res


def tableroPostMoverASecas(t0 : Tablero, pos : Posicion, d : Direccion) -> Tablero: # Devuelve el tablero que resulta de mover a secas la pieza ubicada en pos una casilla hacia d y activar luego las trampas.
    posdestino : Posicion = posicion_vecina_hacia(pos, d)
    tintermedio : Tablero = tableroTrasladandoPieza(t0, pos, posdestino)
    return activar_trampas(tintermedio)


def tableroPostArrastrar(t0 : Tablero, pos : Posicion, d : Direccion, darrastre : Direccion) -> Tablero: # Devuelve el tablero que resulta de mover la pieza en pos hacia d arrastrando a la pieza enemiga que está del lado opuesto a darrastre (la pieza arrastrada termina en pos), y de activar luego las trampas.
    poshueco : Posicion = posicion_vecina_hacia(pos, d)
    posenemiga : Posicion = posicion_vecina_hacia(pos, opuesta(darrastre))
    tintermedio1 : Tablero = tableroTrasladandoPieza(t0, pos, poshueco)
    tintermedio2 : Tablero = tableroTrasladandoPieza(tintermedio1, posenemiga, pos)
    return activar_trampas(tintermedio2)


def tableroPostEmpujar(t0 : Tablero, pos : Posicion, d : Direccion, dempuje : Direccion) -> Tablero: # Devuelve el tablero que resulta de mover la pieza en pos hacia d empujando a la pieza enemiga que está en esa dirección hacia dempuje (la pieza que empuja termina donde estaba la empujada), y de activar luego las trampas.
    posenemiga : Posicion = posicion_vecina_hacia(pos, d)
    poshueco : Posicion = posicion_vecina_hacia(posenemiga, dempuje)
    tintermedio1 : Tablero = tableroTrasladandoPieza(t0, posenemiga, poshueco)
    tintermedio2 : Tablero = tableroTrasladandoPieza(tintermedio1, pos, posenemiga)
    return activar_trampas(tintermedio2)


def tableroPostMovimiento(t0 : Tablero, m : Movimiento) -> Tablero: # Devuelve el tablero que resulta de realizar el movimiento m sobre t0 según su acción (mover a secas, arrastrar o empujar).
    res : Tablero
    if m.accion == MOVER_A_SECAS:
        res = tableroPostMoverASecas(t0, m.origen, m.pasos[0])
    elif m.accion == ARRASTRAR:
        res = tableroPostArrastrar(t0, m.origen, m.pasos[0], m.pasos[1])
    else:
        res = tableroPostEmpujar(t0, m.origen, m.pasos[0], m.pasos[1])
    return res


def hayQueCambiarDeTurno(j : Juego, m : Movimiento) -> bool: # Indica si, al realizar el movimiento m en el juego j, el jugador agota sus pasos del turno y el turno debe pasar al oponente.
    return j.pasos_consumidos + len(m.pasos) == MAX_PASOS


def juegoConTurnoPosiblementeAvanzado(j0 : Juego, m : Movimiento) -> Juego: # Devuelve un juego con el mismo tablero que j0 en el que ya se contaron los pasos del movimiento m. Si se agotan los pasos del turno, el turno pasa al oponente con 0 pasos consumidos; si no, el turno se mantiene y se suman los pasos del movimiento.
    res : Juego
    if hayQueCambiarDeTurno(j0, m):
        res = pasar_turno(j0)
    else:
        res = Juego(j0.tablero, j0.turno, j0.pasos_consumidos + len(m.pasos))
    return res


def juegoPostMovimiento(j0 : Juego, m : Movimiento) -> Juego: # Devuelve el juego que resulta de realizar el movimiento m en j0, con el tablero actualizado y con el turno y los pasos al día.
    tablero_nuevo : Tablero = tableroPostMovimiento(j0.tablero, m)
    j_con_tablero_nuevo : Juego = Juego(tablero_nuevo, j0.turno, j0.pasos_consumidos)
    return juegoConTurnoPosiblementeAvanzado(j_con_tablero_nuevo, m)


def realizar_movimiento(j : Juego, m : Movimiento) -> Juego: # Devuelve el juego que resulta de realizar el movimiento m en j: se mueven las piezas, se activan las trampas y se actualizan el turno y los pasos consumidos.
    return juegoPostMovimiento(j, m)

#### Ejercicio 7

def hay_ganador_determinado(j : Juego) -> bool:
    raise Exception("No implementado")

def ganador_del_juego(j : Juego) -> Color:
    raise Exception("No implementado")