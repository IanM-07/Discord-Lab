from tools import *


def resolver(consulta):

    consulta = consulta.lower()

    # ==========================
    # UNIDAD 1
    # ==========================

    if (
        "importancia de los lenguajes" in consulta
        or "importancia de los lenguajes de programación" in consulta
        or "por qué son importantes los lenguajes" in consulta
        or "porque son importantes los lenguajes" in consulta
    ):
        return importancia_lenguajes(), "importancia de los lenguajes"

    elif (
        "compilación e interpretación" in consulta
        or "compilacion e interpretacion" in consulta
        or ("compilación" in consulta and "interpretación" in consulta)
        or ("compilacion" in consulta and "interpretacion" in consulta)
    ):
        return compilacion_interpretacion(), "compilación e interpretación"

    elif (
    "lenguaje de programación" in consulta
    or "lenguajes de programación" in consulta
    or consulta.strip() == "lenguaje"
    or consulta.strip() == "lenguajes"
):
        return lenguaje_programacion(), "lenguaje de programación"

    elif "alto nivel" in consulta:
        return alto_nivel(), "alto nivel"

    elif "bajo nivel" in consulta:
        return bajo_nivel(), "bajo nivel"

    elif "compilador" in consulta or "compiladores" in consulta:
        return compilador(), "compilador"

    elif (
        "intérprete" in consulta
        or "interprete" in consulta
        or "intérpretes" in consulta
        or "interpretes" in consulta
    ):
        return interprete(), "intérprete"

    # ==========================
    # UNIDAD 2
    # ==========================

    elif (
    consulta.strip() in [
        "ide",
        "ides",
        "que es un ide",
        "qué es un ide",
        "que es un ide?",
        "¿que es un ide?",
        "¿qué es un ide?"
    ]
):
        return ides(), "IDE"

    elif (
    "estructura de un programa" in consulta
    or "estructura del programa" in consulta
):
        return estructura_programa(), "estructura de un programa"

    elif (
    "identificador" in consulta
    or "identificadores" in consulta
):
        return identificadores(), "identificadores"

    elif (
        "palabra reservada" in consulta
        or "palabras reservadas" in consulta
    ):
        return palabras_reservadas(), "palabras reservadas"

    elif "variable" in consulta or "variables" in consulta:
        return variables(), "variables"

    elif "constante" in consulta or "constantes" in consulta:
        return constantes(), "constantes"

    elif (
        "tipo de dato simple" in consulta
        or "tipos de datos simples" in consulta
    ):
        return tipos_datos_simples(), "tipos de datos simples"

    elif (
        "tipo de dato compuesto" in consulta
        or "tipos de datos compuestos" in consulta
    ):
        return tipos_datos_compuestos(), "tipos de datos compuestos"

    elif (
        "tipo de dato" in consulta
        or "tipos de datos" in consulta
    ):
        return tipos_datos(), "tipos de datos"

    elif (
        "operador aritmético" in consulta
        or "operador aritmetico" in consulta
        or "operadores aritméticos" in consulta
        or "operadores aritmeticos" in consulta
    ):
        return operadores_aritmeticos(), "operadores aritméticos"

    elif (
        "operador lógico" in consulta
        or "operador logico" in consulta
        or "operadores lógicos" in consulta
        or "operadores logicos" in consulta
    ):
        return operadores_logicos(), "operadores lógicos"

    elif "operador" in consulta or "operadores" in consulta:
        return operadores(), "operadores"

    # ==========================
    # UNIDAD 3
    # ==========================

    elif (
        "estructura de control" in consulta
        or "estructuras de control" in consulta
    ):
        return estructuras_control(), "estructuras de control"

    elif (
        "estructura de selección" in consulta
        or "estructura de seleccion" in consulta
        or "estructuras de selección" in consulta
        or "estructuras de seleccion" in consulta
    ):
        return estructuras_seleccion(), "estructuras de selección"

    elif "if else" in consulta or "if-else" in consulta:
        return if_else(), "if else"

    elif "then" in consulta:
        return then(), "then"

    elif (
    "if" in consulta
    and "if else" not in consulta
    and "if-else" not in consulta
):
        return if_condicional(), "if"

    elif "switch" in consulta:
        return switch(), "switch"

    elif (
        "estructura de repetición" in consulta
        or "estructura de repeticion" in consulta
        or "estructuras de repetición" in consulta
        or "estructuras de repeticion" in consulta
    ):
        return estructuras_repeticion(), "estructuras de repetición"

    elif "do while" in consulta:
        return do_while(), "do while"

    elif (
    consulta.strip() == "while"
    or "ciclo while" in consulta
):
        return ciclo_while(), "while"

    elif (
    consulta.strip() == "for"
    or "ciclo for" in consulta
    or "bucle for" in consulta
):
        return ciclo_for(), "for"

    elif (
        "aplicación de algoritmos" in consulta
        or "aplicacion de algoritmos" in consulta
        or "algoritmos usando estructuras de control" in consulta
    ):
        return aplicacion_algoritmos(), "aplicación de algoritmos"

    # ==========================
    # UNIDAD 4
    # ==========================

    elif "procedimiento" in consulta or "procedimientos" in consulta:
        return procedimientos(), "procedimientos"

    elif (
        "función de usuario" in consulta
        or "funcion de usuario" in consulta
    ):
        return funciones_usuario(), "funciones de usuario"

    elif (
        "función externa" in consulta
        or "funcion externa" in consulta
        or "funciones externas" in consulta
    ):
        return funciones_externas(), "funciones externas"

    elif "invocación" in consulta or "invocacion" in consulta:
        return invocacion(), "invocación"

    elif (
        "parámetro de entrada" in consulta
        or "parametro de entrada" in consulta
    ):
        return parametros_entrada(), "parámetros de entrada"

    elif (
        "parámetro de salida" in consulta
        or "parametro de salida" in consulta
    ):
        return parametros_salida(), "parámetros de salida"

    elif (
        "parámetro" in consulta
        or "parametro" in consulta
        or "parámetros" in consulta
        or "parametros" in consulta
    ):
        return parametros(), "parámetros"

    elif "biblioteca" in consulta or "bibliotecas" in consulta:
        return bibliotecas(), "bibliotecas"

    elif (
        "diferencia entre función y procedimiento" in consulta
        or "diferencia entre funcion y procedimiento" in consulta
    ):
        return diferencias_funciones(), "diferencias"

    elif (
        "función" in consulta
        or "funcion" in consulta
        or "funciones" in consulta
    ):
        return funciones(), "funciones"

    # ==========================
    # UNIDAD 5
    # ==========================

    elif (
        "declaración de arreglos" in consulta
        or "declaracion de arreglos" in consulta
    ):
        return declaracion_arreglos(), "declaración de arreglos"

    elif (
        "lectura y escritura" in consulta
        or "lectura de arreglos" in consulta
        or "escritura de arreglos" in consulta
    ):
        return lectura_escritura(), "lectura y escritura"

    elif "operaciones con arreglos" in consulta:
        return operaciones_arreglos(), "operaciones con arreglos"

    elif "arreglo" in consulta or "arreglos" in consulta:
        return arreglos(), "arreglos"

    elif "vector" in consulta or "vectores" in consulta:
        return vectores(), "vectores"

    elif "matriz" in consulta or "matrices" in consulta:
        return matrices(), "matrices"

    # ==========================
    # SI NO ENCUENTRA EL TEMA
    # ==========================

    else:
        return (
            "Lo siento, todavía no tengo información sobre ese tema. "
            "Intenta preguntar sobre alguno de los temas de Programación Estructurada.",
            None
        )