"""
from googletrans import Translator, constants
from pprint import pprint


# init the Google API translator
translator = Translator()


# translate a spanish text to english text (by default)
translation = translator.translate("Hola Mundo")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
"""
do = True
dictionary = {'hola':'hello','mundo':'world','esto':'this','is':'es','un(a)':'a', 'prueba':'test'}
print('BIENVENIDO A DICCIONARIO Y TRADUCTOR\n')
while do:
    print('MENU:')
    print('0 VER DICCIONARIO ACTUAL')
    print('1 AGREGAR PAREJAS DE PALABRAS AL DICT')
    print('2 TRADUCIR ORACION')
    print('3 FINALIZAR\n')
    print('')
    opt = int(input('Ingrese opcion: '))
    if opt == 0:
        print(f"El diccionario actual es: {dictionary}")
    elif opt == 1:
        words = str(input('Ingrese las palabras a agregar en formato <PALABRA:TRADUCCION>: \n'))
        try:
            medLst= words.replace('<','')
            medLst= words.replace('>','')
            wordsLst = medLst.split(":")
            
            origWord = wordsLst[0]
            transWord = wordsLst[1]
            dictionary[origWord] = transWord

        except:
            print('ERROR, El formato NO ha sido el correcto\nEl formato es... \n<PALABRA:TRADUCCION>')

    elif opt == 2:
        try:
            chain = input('Ingrese una cadena a traducir: \n')
            print("")
            wordsLst = chain.split()
            finalTrans = ""
            for i in wordsLst:
                if i in dictionary.keys():
                    transWord = dictionary[i]
                    finalTrans += transWord+" "
                else:
                    finalTrans += i+" "
            print(finalTrans)
        except:
            print('ERROR, No ha sido el formato correcto')
    elif opt == 3:
        do = False
    else:
        print('Opcion incorrecta, porfavor verifique su entrada')


def translateChain(str):
    chain = input('Ingrese una cadena a traducir: \n')
    print("")
    wordsLst = chain.split()
    finalTrans = ""
    for i in wordsLst:
        if i in dictionary.keys():
            transWord = dictionary[i]
            finalTrans += transWord+" "
        else:
            finalTrans += i+" "
    print(finalTrans)


#print(wordsLst)