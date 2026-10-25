import unittest
from arimaa import *

# Las piezas se representan con las siguientes letras:
#   E : elefante
#   M : camello
#   H : caballo
#   D : perro
#   C : gato
#   R : ratón
# donde
#   mayúscula : dorado
#   minúscula : plateado

def tablero_8x8_vacio():
    return leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])

def tablero_8x8_inicial_ejemplo():
    return leer_tablero([
              'hcdmedch', #7
              'rrrrrrrr', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              'RRRRRRRR', #1
              'HCDMEDCH', #0
              #01234567
            ])

#### Ejercicio 1

class test_tablero_bien_formado(unittest.TestCase):

    def test_8x8_lleno(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(tablero_bien_formado(t))

    def test_tablero_vacio_sin_filas(self):
        self.assertFalse(tablero_bien_formado(leer_tablero([])))

    def test_pocas_filas(self):
        self.assertFalse(tablero_bien_formado(leer_tablero(['--------'] * 7)))

    def test_demasiadas_filas(self):
        self.assertFalse(tablero_bien_formado(leer_tablero(['--------'] * 9)))

    def test_fila_con_pocas_columnas(self):
        self.assertFalse(tablero_bien_formado(leer_tablero(['--------'] * 7 + ['-------'])))

    def test_fila_con_demasiadas_columnas(self):
        self.assertFalse(tablero_bien_formado(leer_tablero(['---------'] + ['--------'] * 7)))

class test_posicion_en_tablero(unittest.TestCase):

    def test_posicion_ok(self):
        self.assertTrue(posicion_en_tablero(Posicion(5, 3)))

    def test_posiciones_en_las_esquinas(self):
        self.assertTrue(posicion_en_tablero(Posicion(0, 0)))
        self.assertTrue(posicion_en_tablero(Posicion(7, 7)))

    def test_fila_negativa(self):
        self.assertFalse(posicion_en_tablero(Posicion(-1, 0)))

    def test_fila_igual_al_alto(self):
        self.assertFalse(posicion_en_tablero(Posicion(8, 0)))

    def test_columna_negativa(self):
        self.assertFalse(posicion_en_tablero(Posicion(0, -1)))

    def test_columna_igual_al_ancho(self):
        self.assertFalse(posicion_en_tablero(Posicion(0, 8)))

class test_movimiento_bien_formado(unittest.TestCase):

    def test_movimiento_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])))

    def test_empujar_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(2, 2), [NORTE, ESTE])))

    def test_arrastrar_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(2, 2), [SUR, OESTE])))

    def test_mover_a_secas_con_dos_pasos(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(2, 2), [NORTE, ESTE])))

    def test_mover_a_secas_sin_pasos(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(2, 2), [])))

    def test_empujar_con_un_paso(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(2, 2), [NORTE])))

    def test_empujar_con_tres_pasos(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(2, 2), [NORTE, ESTE, SUR])))

    def test_arrastrar_con_un_paso(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(2, 2), [NORTE])))

    def test_arrastrar_con_tres_pasos(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(2, 2), [NORTE, ESTE, SUR])))

    def test_origen_fuera_del_tablero(self):
        self.assertFalse(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(8, 0), [NORTE])))
        self.assertFalse(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(0, -1), [NORTE, ESTE])))

class test_juego_bien_formado(unittest.TestCase):

    def test_juego_ok(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 0)
        self.assertTrue(juego_bien_formado(j))

    def test_juego_con_el_maximo_de_pasos_menos_uno(self):
        j = Juego(tablero_8x8_vacio(), PLATEADO, 3)
        self.assertTrue(juego_bien_formado(j))

    def test_juego_con_todos_los_pasos_consumidos(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 4)
        self.assertFalse(juego_bien_formado(j))

    def test_juego_con_pasos_negativos(self):
        j = Juego(tablero_8x8_vacio(), DORADO, -1)
        self.assertFalse(juego_bien_formado(j))

    def test_juego_con_tablero_mal_formado(self):
        j = Juego(leer_tablero(['--------'] * 7), DORADO, 0)
        self.assertFalse(juego_bien_formado(j))

#### Ejercicio 2

class test_posicion_vecina_hacia(unittest.TestCase):

    def test_vecina_al_norte(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), NORTE), Posicion(1, 0))

    def test_vecina_al_sur(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(3, 3), SUR), Posicion(2, 3))

    def test_vecina_al_este(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(3, 3), ESTE), Posicion(3, 4))

    def test_vecina_al_oeste(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(3, 3), OESTE), Posicion(3, 2))

    def test_vecina_fuera_del_tablero(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), SUR), Posicion(-1, 0))

class test_es_posicion_vecina_hacia(unittest.TestCase):

    def test_vecina_al_norte(self):
        self.assertTrue(esPosicionVecinaHacia(Posicion(3, 3), NORTE, Posicion(4, 3)))

    def test_vecina_al_sur(self):
        self.assertTrue(esPosicionVecinaHacia(Posicion(3, 3), SUR, Posicion(2, 3)))

    def test_vecina_al_este(self):
        self.assertTrue(esPosicionVecinaHacia(Posicion(3, 3), ESTE, Posicion(3, 4)))

    def test_vecina_al_oeste(self):
        self.assertTrue(esPosicionVecinaHacia(Posicion(3, 3), OESTE, Posicion(3, 2)))

    def test_vecina_en_otra_direccion(self):
        self.assertFalse(esPosicionVecinaHacia(Posicion(3, 3), NORTE, Posicion(2, 3)))
        self.assertFalse(esPosicionVecinaHacia(Posicion(3, 3), SUR, Posicion(4, 3)))
        self.assertFalse(esPosicionVecinaHacia(Posicion(3, 3), ESTE, Posicion(3, 2)))
        self.assertFalse(esPosicionVecinaHacia(Posicion(3, 3), OESTE, Posicion(3, 4)))

    def test_posicion_que_no_es_vecina(self):
        self.assertFalse(esPosicionVecinaHacia(Posicion(3, 3), NORTE, Posicion(5, 3)))
        self.assertFalse(esPosicionVecinaHacia(Posicion(3, 3), ESTE, Posicion(4, 4)))
        self.assertFalse(esPosicionVecinaHacia(Posicion(3, 3), NORTE, Posicion(3, 3)))

class test_son_posiciones_vecinas(unittest.TestCase):

    def test_vecinas(self):
        self.assertTrue(son_posiciones_vecinas(Posicion(0, 0), Posicion(1, 0)))

class test_casilla_en_posicion(unittest.TestCase):

    def test_casilla_en_posicion(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(0, 0)), Pieza(CABALLO, DORADO))

    def test_casilla_en_posicion_pieza_plateada(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(7, 0)), Pieza(CABALLO, PLATEADO))

    def test_casilla_en_posicion_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(3, 3)), VACIA)

class test_hay_casilla_vacia(unittest.TestCase):

    def test_casilla_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_casilla_vacia(t, Posicion(2, 1)))

    def test_casilla_ocupada(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_casilla_vacia(t, Posicion(0, 0)))

    def test_posicion_fuera_del_tablero(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_casilla_vacia(t, Posicion(-1, 0)))
        self.assertFalse(hay_casilla_vacia(t, Posicion(0, 8)))

class test_hay_pieza_de_color(unittest.TestCase):

    def test_hay_pieza_de_color_ok(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_pieza_de_color(t, Posicion(1, 4), DORADO))

    def test_cada_figura_dorada(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_pieza_de_color(t, Posicion(0, 4), DORADO)) # elefante
        self.assertTrue(hay_pieza_de_color(t, Posicion(0, 3), DORADO)) # camello
        self.assertTrue(hay_pieza_de_color(t, Posicion(0, 0), DORADO)) # caballo
        self.assertTrue(hay_pieza_de_color(t, Posicion(0, 2), DORADO)) # perro
        self.assertTrue(hay_pieza_de_color(t, Posicion(0, 1), DORADO)) # gato
        self.assertTrue(hay_pieza_de_color(t, Posicion(1, 0), DORADO)) # conejo

    def test_pieza_plateada(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_pieza_de_color(t, Posicion(7, 0), PLATEADO))

    def test_pieza_de_otro_color(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza_de_color(t, Posicion(0, 0), PLATEADO))
        self.assertFalse(hay_pieza_de_color(t, Posicion(7, 0), DORADO))

    def test_casilla_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza_de_color(t, Posicion(3, 3), DORADO))

    def test_posicion_fuera_del_tablero(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza_de_color(t, Posicion(-1, 0), DORADO))
        self.assertFalse(hay_pieza_de_color(t, Posicion(8, 0), PLATEADO))

#### Ejercicio 3

def tablero_esquinas():
    return leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '-R------', #1
              'R-------', #0
              #01234567
            ])

def tablero_con_amigas():
    return leer_tablero([
              'r-------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '---r----', #3
              '-rrR----', #2
              '-------R', #1
              '-------R', #0
              #01234567
            ])

def tablero_con_debiles():
    return leer_tablero([
              '--------', #7
              '------Rc', #6
              '--------', #5
              '---c----', #4
              '--REe---', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])

def tablero_con_fuertes():
    return leer_tablero([
              '--------', #7
              '-Mm-----', #6
              '-----cR-', #5
              '--------', #4
              '-rD-----', #3
              '--r-----', #2
              '-e------', #1
              '-----RE-', #0
              #01234567
            ])

def tablero_con_congelables():
    return leer_tablero([
              '-------E', #7
              '--------', #6
              '-rC-----', #5
              '--------', #4
              '-----r--', #3
              '-----rC-', #2
              '--------', #1
              '--Mm----', #0
              #01234567
            ])

class test_hay_casilla_vacia_hacia(unittest.TestCase):

    def test_hay_casilla_vacia_hacia(self):
        t = leer_tablero([
              '-r----rr', #7
              '-mrh----', #6
              '-r---r--', #5
              'd-EH---c', #4
              '-M--hD-d', #3
              '-R-e----', #2
              '---H-R-C', #1
              'R-R---RR', #0
              #01234567
            ])
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(0, 0), NORTE))

    def test_casilla_vacia_hacia_el_este(self):
        self.assertTrue(hay_casilla_vacia_hacia(tablero_esquinas(), Posicion(0, 0), ESTE))

    def test_casilla_ocupada_hacia_el_norte(self):
        self.assertFalse(hay_casilla_vacia_hacia(tablero_esquinas(), Posicion(0, 1), NORTE))

    def test_fuera_del_tablero_hacia_el_sur(self):
        self.assertFalse(hay_casilla_vacia_hacia(tablero_esquinas(), Posicion(0, 0), SUR))

    def test_fuera_del_tablero_hacia_el_oeste(self):
        self.assertFalse(hay_casilla_vacia_hacia(tablero_esquinas(), Posicion(0, 0), OESTE))

    def test_fuera_del_tablero_hacia_el_norte(self):
        self.assertFalse(hay_casilla_vacia_hacia(tablero_esquinas(), Posicion(7, 7), NORTE))

    def test_fuera_del_tablero_hacia_el_este(self):
        self.assertFalse(hay_casilla_vacia_hacia(tablero_esquinas(), Posicion(7, 7), ESTE))

class test_hay_pieza_amiga_vecina(unittest.TestCase):

    def test_hay_pieza_amiga_vecina(self):
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(4, 3)))

    def test_amiga_al_este(self):
        self.assertTrue(hay_pieza_amiga_vecina(tablero_con_amigas(), Posicion(2, 1)))

    def test_amiga_al_oeste(self):
        self.assertTrue(hay_pieza_amiga_vecina(tablero_con_amigas(), Posicion(2, 2)))

    def test_amiga_al_norte(self):
        self.assertTrue(hay_pieza_amiga_vecina(tablero_con_amigas(), Posicion(0, 7)))

    def test_amiga_al_sur(self):
        self.assertTrue(hay_pieza_amiga_vecina(tablero_con_amigas(), Posicion(1, 7)))

    def test_solo_vecinas_enemigas(self):
        self.assertFalse(hay_pieza_amiga_vecina(tablero_con_amigas(), Posicion(2, 3)))

    def test_sin_vecinas(self):
        self.assertFalse(hay_pieza_amiga_vecina(tablero_con_amigas(), Posicion(3, 3)))

    def test_pieza_en_la_esquina_sin_vecinas(self):
        self.assertFalse(hay_pieza_amiga_vecina(tablero_con_amigas(), Posicion(7, 0)))

class test_hay_pieza_enemiga_mas_debil_hacia(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_debil_hacia(self):
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhC--', #6
              'e---R-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RRcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(1, 3), OESTE))

    def test_enemiga_mas_debil_al_norte(self):
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(tablero_con_debiles(), Posicion(3, 3), NORTE))

    def test_enemiga_de_igual_fuerza(self):
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(tablero_con_debiles(), Posicion(3, 3), ESTE))

    def test_vecina_amiga(self):
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(tablero_con_debiles(), Posicion(3, 3), OESTE))

    def test_vecina_vacia(self):
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(tablero_con_debiles(), Posicion(3, 3), SUR))

    def test_enemiga_mas_fuerte(self):
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(tablero_con_debiles(), Posicion(6, 6), ESTE))

    def test_plateada_con_enemiga_dorada_mas_debil(self):
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(tablero_con_debiles(), Posicion(6, 7), OESTE))

    def test_vecina_fuera_del_tablero(self):
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(tablero_con_debiles(), Posicion(6, 7), ESTE))

class test_hay_pieza_enemiga_mas_fuerte_vecina(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_fuerte_vecina(self):
        t = leer_tablero([
              'R-e--mRr', #7
              '------dE', #6
              'h--Rr-RR', #5
              'c--R-C--', #4
              '-rCHDrr-', #3
              '----rc--', #2
              'h-R-M-R-', #1
              'rr-D-dH-', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(3, 1)))

    def test_enemiga_mas_fuerte_al_este(self):
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(tablero_con_fuertes(), Posicion(3, 1)))

    def test_enemiga_mas_fuerte_al_norte(self):
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(tablero_con_fuertes(), Posicion(2, 2)))

    def test_enemiga_mas_fuerte_al_oeste(self):
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(tablero_con_fuertes(), Posicion(5, 6)))

    def test_solo_vecinas_enemigas_mas_debiles(self):
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(tablero_con_fuertes(), Posicion(3, 2)))
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(tablero_con_fuertes(), Posicion(5, 5)))

    def test_sin_vecinas(self):
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(tablero_con_fuertes(), Posicion(1, 1)))

    def test_vecina_amiga_mas_fuerte_no_cuenta(self):
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(tablero_con_fuertes(), Posicion(0, 5)))

    def test_enemigas_de_igual_fuerza_no_cuentan(self):
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(tablero_con_fuertes(), Posicion(6, 1)))
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(tablero_con_fuertes(), Posicion(6, 2)))

class test_hay_pieza_congelada(unittest.TestCase):

    def test_hay_pieza_congelada(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_congelada(t, Posicion(6, 1)))

    def test_congelada_sin_amigas(self):
        self.assertTrue(hay_pieza_congelada(tablero_con_congelables(), Posicion(5, 1)))

    def test_no_congelada_por_tener_una_amiga_vecina(self):
        self.assertFalse(hay_pieza_congelada(tablero_con_congelables(), Posicion(2, 5)))

    def test_no_congelada_sin_enemigas_mas_fuertes(self):
        self.assertFalse(hay_pieza_congelada(tablero_con_congelables(), Posicion(5, 2)))
        self.assertFalse(hay_pieza_congelada(tablero_con_congelables(), Posicion(3, 5)))
        self.assertFalse(hay_pieza_congelada(tablero_con_congelables(), Posicion(7, 7)))

    def test_no_congelada_por_enemiga_de_igual_fuerza(self):
        self.assertFalse(hay_pieza_congelada(tablero_con_congelables(), Posicion(0, 2)))
        self.assertFalse(hay_pieza_congelada(tablero_con_congelables(), Posicion(0, 3)))

    def test_casilla_vacia_no_esta_congelada(self):
        self.assertFalse(hay_pieza_congelada(tablero_con_congelables(), Posicion(4, 4)))

#### Ejercicio 4

def tablero_para_movimientos():
    return leer_tablero([
              '--------', #7
              '--------', #6
              '--r--R--', #5
              '---rr---', #4
              '---Ec---', #3
              '--------', #2
              'c-------', #1
              'R-------', #0
              #01234567
            ])

class test_puede_realizar_movimiento(unittest.TestCase):

    def test_mover_a_secas_ok(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j, m))

    def test_mover_a_secas_a_casilla_vacia(self):
        j = Juego(tablero_para_movimientos(), DORADO, 0)
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(3, 3), [SUR])))
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(3, 3), [OESTE])))

    def test_mover_a_secas_a_casilla_ocupada(self):
        j = Juego(tablero_para_movimientos(), DORADO, 0)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(3, 3), [NORTE])))

    def test_no_se_puede_mover_pieza_del_oponente(self):
        j = Juego(tablero_para_movimientos(), PLATEADO, 0)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(3, 3), [SUR])))

    def test_no_se_puede_mover_desde_casilla_vacia(self):
        j = Juego(tablero_para_movimientos(), DORADO, 0)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(6, 6), [SUR])))

    def test_pasos_consumidos_con_un_solo_paso_disponible(self):
        j = Juego(tablero_para_movimientos(), DORADO, 3)
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(3, 3), [SUR])))

    def test_pasos_insuficientes_para_un_movimiento_de_dos_pasos(self):
        j = Juego(tablero_para_movimientos(), DORADO, 3)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(3, 3), [NORTE, NORTE])))

    def test_movimiento_de_dos_pasos_usando_todos_los_pasos(self):
        j = Juego(tablero_para_movimientos(), DORADO, 2)
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(3, 3), [NORTE, NORTE])))

    def test_pieza_congelada_no_puede_moverse(self):
        j = Juego(tablero_para_movimientos(), DORADO, 0)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(0, 0), [ESTE])))

    def test_conejo_dorado_no_puede_retroceder(self):
        j = Juego(tablero_para_movimientos(), DORADO, 0)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(5, 5), [SUR])))

    def test_conejo_dorado_puede_avanzar_y_moverse_de_costado(self):
        j = Juego(tablero_para_movimientos(), DORADO, 0)
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(5, 5), [NORTE])))
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(5, 5), [ESTE])))
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(5, 5), [OESTE])))

    def test_conejo_plateado_no_puede_retroceder(self):
        j = Juego(tablero_para_movimientos(), PLATEADO, 0)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(5, 2), [NORTE])))

    def test_conejo_plateado_puede_avanzar_y_moverse_de_costado(self):
        j = Juego(tablero_para_movimientos(), PLATEADO, 0)
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(5, 2), [SUR])))
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(5, 2), [ESTE])))

    def test_arrastrar_pieza_mas_debil(self):
        j = Juego(tablero_para_movimientos(), DORADO, 0)
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(ARRASTRAR, Posicion(3, 3), [SUR, SUR])))
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(ARRASTRAR, Posicion(3, 3), [SUR, OESTE])))

    def test_arrastrar_sin_pieza_enemiga_para_arrastrar(self):
        j = Juego(tablero_para_movimientos(), DORADO, 0)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(ARRASTRAR, Posicion(3, 3), [SUR, ESTE])))
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(ARRASTRAR, Posicion(3, 3), [SUR, NORTE])))

    def test_arrastrar_hacia_casilla_ocupada(self):
        j = Juego(tablero_para_movimientos(), DORADO, 0)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(ARRASTRAR, Posicion(3, 3), [NORTE, SUR])))

    def test_arrastrar_pieza_mas_fuerte(self):
        j = Juego(tablero_para_movimientos(), PLATEADO, 0)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(ARRASTRAR, Posicion(4, 3), [OESTE, NORTE])))

    def test_empujar_pieza_mas_debil(self):
        j = Juego(tablero_para_movimientos(), DORADO, 0)
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(3, 3), [NORTE, NORTE])))
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(3, 3), [NORTE, OESTE])))
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(3, 3), [ESTE, ESTE])))
        self.assertTrue(puede_realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(3, 3), [ESTE, SUR])))

    def test_empujar_hacia_casilla_ocupada(self):
        j = Juego(tablero_para_movimientos(), DORADO, 0)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(3, 3), [NORTE, ESTE])))
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(3, 3), [ESTE, NORTE])))
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(3, 3), [ESTE, OESTE])))

    def test_empujar_sin_pieza_enemiga(self):
        j = Juego(tablero_para_movimientos(), DORADO, 0)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(3, 3), [SUR, SUR])))

    def test_empujar_pieza_mas_fuerte(self):
        j = Juego(tablero_para_movimientos(), PLATEADO, 0)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(4, 3), [SUR, ESTE])))

#### Ejercicio 5

def tableros_coinciden_salvo_en_la_posicion(t1 : Tablero, t2 : Tablero, pos : Posicion) -> bool:
    coinciden : bool = True
    for fila in range(ALTO):
        for columna in range(ANCHO):
            if Posicion(fila, columna) != pos and t1[fila][columna] != t2[fila][columna]:
                coinciden = False
    return coinciden

def es_tablero_sacando_pieza(t0 : Tablero, t1 : Tablero, pos : Posicion) -> bool:
    return (tableros_coinciden_salvo_en_la_posicion(t0, t1, pos)
            and hay_casilla_vacia(t1, pos))

def es_tablero_despues_de_activar_trampa(t0 : Tablero, t1 : Tablero, pos_trampa : Posicion) -> bool:
    tiene_amiga_vecina : bool = hayPieza(t0, pos_trampa) and hay_pieza_amiga_vecina(t0, pos_trampa)
    primera_implicacion : bool = (not tiene_amiga_vecina) or t1 == t0
    segunda_implicacion : bool = tiene_amiga_vecina or es_tablero_sacando_pieza(t0, t1, pos_trampa)
    return primera_implicacion and segunda_implicacion

def es_tablero_despues_de_activar_todas_las_trampas(t0 : Tablero, t1 : Tablero) -> bool:
    t_intermedio1 : Tablero = copiarTablero(t0)
    activarTrampa(t_intermedio1, POSICIONES_TRAMPA[0])
    t_intermedio2 : Tablero = copiarTablero(t_intermedio1)
    activarTrampa(t_intermedio2, POSICIONES_TRAMPA[1])
    t_intermedio3 : Tablero = copiarTablero(t_intermedio2)
    activarTrampa(t_intermedio3, POSICIONES_TRAMPA[2])
    return (es_tablero_despues_de_activar_trampa(t0, t_intermedio1, POSICIONES_TRAMPA[0])
            and es_tablero_despues_de_activar_trampa(t_intermedio1, t_intermedio2, POSICIONES_TRAMPA[1])
            and es_tablero_despues_de_activar_trampa(t_intermedio2, t_intermedio3, POSICIONES_TRAMPA[2])
            and es_tablero_despues_de_activar_trampa(t_intermedio3, t1, POSICIONES_TRAMPA[3]))

def tablero_con_trampas_ocupadas():
    return leer_tablero([
              '--------', #7
              '--------', #6
              '--r-----', #5
              '--r-----', #4
              '--------', #3
              '----rE--', #2
              '--------', #1
              'R-------', #0
              #01234567
            ])

class test_activar_trampas(unittest.TestCase):

    def test_activar_trampas_ok(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r--E--', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-H--m--', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t1 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-------', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)

    def test_cumple_la_especificacion_del_ejemplo(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r--E--', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-H--m--', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        self.assertTrue(es_tablero_despues_de_activar_todas_las_trampas(t0, activar_trampas(t0)))
        self.assertFalse(es_tablero_despues_de_activar_todas_las_trampas(t0, t0))

    def test_la_pieza_con_amiga_vecina_se_queda_y_la_que_solo_tiene_enemigas_se_retira(self):
        esperado = leer_tablero([
              '--------', #7
              '--------', #6
              '--r-----', #5
              '--r-----', #4
              '--------', #3
              '----r---', #2
              '--------', #1
              'R-------', #0
              #01234567
            ])
        self.assertEqual(activar_trampas(tablero_con_trampas_ocupadas()), esperado)

    def test_no_modifica_el_tablero_original(self):
        t = tablero_con_trampas_ocupadas()
        activar_trampas(t)
        self.assertEqual(t, tablero_con_trampas_ocupadas())

    def test_tablero_sin_piezas_en_trampas_queda_igual(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(activar_trampas(t), tablero_8x8_inicial_ejemplo())

    def test_tablero_vacio_queda_vacio(self):
        self.assertEqual(activar_trampas(tablero_8x8_vacio()), tablero_8x8_vacio())

    def test_copiar_tablero_es_independiente_del_original(self):
        t = tablero_con_trampas_ocupadas()
        copia = copiarTablero(t)
        self.assertEqual(copia, t)
        sacarPieza(copia, Posicion(0, 0))
        self.assertEqual(casilla_en_posicion(copia, Posicion(0, 0)), VACIA)
        self.assertEqual(casilla_en_posicion(t, Posicion(0, 0)), Pieza(CONEJO, DORADO))

#### Ejercicio 6

def tablero_para_realizar():
    return leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---r----', #4
              '---Ec---', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])

class test_realizar_movimiento(unittest.TestCase):
 
    def test_mover_a_secas(self):
        t0 = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '--------', #5
               '---m----', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        tN = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '---m----', #5
               '--------', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        j0 = Juego(t0, PLATEADO, 0) 
        jN = Juego(tN, PLATEADO, 1) 
        mN = Movimiento(MOVER_A_SECAS, Posicion(4, 3), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)

    def test_mover_a_secas_suma_un_paso(self):
        j = Juego(tablero_para_realizar(), DORADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(3, 3), [OESTE])
        esperado = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---r----', #4
              '--E-c---', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertEqual(realizar_movimiento(j, m), Juego(esperado, DORADO, 1))

    def test_arrastrar(self):
        j = Juego(tablero_para_realizar(), DORADO, 0)
        m = Movimiento(ARRASTRAR, Posicion(3, 3), [SUR, SUR])
        esperado = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '---rc---', #3
              '---E----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertEqual(realizar_movimiento(j, m), Juego(esperado, DORADO, 2))

    def test_empujar_hacia_el_norte(self):
        j = Juego(tablero_para_realizar(), DORADO, 0)
        m = Movimiento(EMPUJAR, Posicion(3, 3), [NORTE, NORTE])
        esperado = leer_tablero([
              '--------', #7
              '--------', #6
              '---r----', #5
              '---E----', #4
              '----c---', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertEqual(realizar_movimiento(j, m), Juego(esperado, DORADO, 2))

    def test_empujar_hacia_el_sur(self):
        j = Juego(tablero_para_realizar(), DORADO, 0)
        m = Movimiento(EMPUJAR, Posicion(3, 3), [ESTE, SUR])
        esperado = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---r----', #4
              '----E---', #3
              '----c---', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertEqual(realizar_movimiento(j, m), Juego(esperado, DORADO, 2))

    def test_el_turno_pasa_al_oponente_al_agotar_los_pasos(self):
        j = Juego(tablero_para_realizar(), DORADO, 3)
        m = Movimiento(MOVER_A_SECAS, Posicion(3, 3), [OESTE])
        esperado = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '---r----', #4
              '--E-c---', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertEqual(realizar_movimiento(j, m), Juego(esperado, PLATEADO, 0))

    def test_el_turno_pasa_al_oponente_con_un_movimiento_de_dos_pasos(self):
        j = Juego(tablero_para_realizar(), DORADO, 2)
        m = Movimiento(ARRASTRAR, Posicion(3, 3), [SUR, SUR])
        resultado = realizar_movimiento(j, m)
        self.assertEqual(resultado.turno, PLATEADO)
        self.assertEqual(resultado.pasos_consumidos, 0)

    def test_la_pieza_que_se_mueve_a_una_trampa_sin_amigas_se_retira(self):
        t = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '---E----', #2
              '--------', #1
              'R-------', #0
              #01234567
            ])
        esperado = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '--------', #1
              'R-------', #0
              #01234567
            ])
        m = Movimiento(MOVER_A_SECAS, Posicion(2, 3), [OESTE])
        self.assertEqual(realizar_movimiento(Juego(t, DORADO, 0), m), Juego(esperado, DORADO, 1))

    def test_la_pieza_empujada_a_una_trampa_sin_amigas_se_retira(self):
        t = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--r-----', #4
              '--E-----', #3
              '--------', #2
              '--------', #1
              'R-------', #0
              #01234567
            ])
        esperado = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--E-----', #4
              '--------', #3
              '--------', #2
              '--------', #1
              'R-------', #0
              #01234567
            ])
        m = Movimiento(EMPUJAR, Posicion(3, 2), [NORTE, NORTE])
        self.assertEqual(realizar_movimiento(Juego(t, DORADO, 0), m), Juego(esperado, DORADO, 2))

    def test_no_modifica_el_juego_original(self):
        j = Juego(tablero_para_realizar(), DORADO, 0)
        realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(3, 3), [NORTE, NORTE]))
        self.assertEqual(j, Juego(tablero_para_realizar(), DORADO, 0))
