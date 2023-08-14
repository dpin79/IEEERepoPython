"""Write a program that stores the subjects 
of a course (e.g. Mathematics, Physics, 
Chemistry, History and Language) in a list
 and displays it on the screen."""

def subjects():
    ans= []
    loop = None
    qs = input("Do you want add any subject?(Y/N):\n")
    if qs == "Y":
        loop = True
        while loop == True:
            sub = str((input("Write subject-NONE to stop write subjects-:\n")))
            if sub == "NONE":
                loop = False
            else:
                grade = str(input("Write the grade in the signed subject:\n"))
                tuple = f"The subject is: {sub} and the grade is: {grade}\n"
                ans.append(tuple)
    print("")
    return f"The subjects list is: {ans}"

#print(subjects())

"""
Write a program that stores the subjects of a course (e.g. Mathematics, 
Physics, Chemistry, History and Language) in a list, asks the user the 
grade he/she got in each subject, and then displays them on the screen 
with the message In <subject> you got <grade> where <subject> is each 
of the subjects in the list and <grade> is each of the corresponding 
grades entered by the user.
"""
def subs():
    ans = []
    loop = input("Write down any subject?(Y/N): ")      #INCOMPLETE
    print("")
    sub = str(input("Write a subject"))
    grade = str(input("Write a grade"))
    tuple = (sub,grade)

    ans.append(tuple)
























#1 PROGRAM TO SOLVE THE OUTSTANDING INVOICES / PENDING BILLS
dictExample = {'01':50,
               'D02':50,
               'C03':'CANCELED',
               '04':50,
               'D05':50,
               'D06':50,
               'C07':'CANCELED',
               '08':50,
               '09':50,
               '10':50}

import time
def pendBills(dict):
    
    CantidadRecolectada=0
    CantidadCobrar=0
    for each in dict.keys():
        if each.find("C") != -1:
            continue
        elif each.find("D") != -1:
            value = dict.get(each)
            CantidadRecolectada += value
        else:
            value = dict.get(each)
            CantidadCobrar += value

    print(f"Cantidad reco: {CantidadRecolectada}")
    print(f"Cantidad cobrar: {CantidadCobrar}")
    print("")
    
    dict['Cantidad recolectada']=CantidadRecolectada
    dict['Cantidad por cobrar']=CantidadCobrar
    
    advice = "En la siguiente opción ingrese según requiera:\n*(Y)Pagar o cancelar una factura\n*No hacer cambios(N)\n"
    print(advice)
    option = str(input("Ingrese opción(Y/N): "))
    if option == "N":
        print("No se harán modificaciones")
    else:
        suboption = str(input("Pagar(P) o Cancelar(C) una factura: "))
        if suboption == "P":
            factNumb = str(input("Ingrese el número de la factuar a pagar: "))
            oldNumb = factNumb
            try:
                valueToPay = dict.get(factNumb)
                print(f"Value to be pay: {valueToPay}")
                print("")
                print("---Procesando pago---")
                print("")
                time.sleep(2)

                dict.pop(factNumb)

                newNumb = "D"+oldNumb

                dict[newNumb] = valueToPay

                dict['Cantidad recolectada']+=valueToPay
                dict['Cantidad por cobrar']-=valueToPay

            except:
                print("El número de factura no fue encontrado")
        elif suboption == "C":
            factNumb = str(input("Ingrese el número de la factuar a cancelar: "))
            oldNumb = factNumb
            try:
                valueToCancel= dict.get(factNumb)
                print(f"Value on the cancel invoice is: {valueToCancel}")
                print("")
                print("---Processing cancellation---")
                print("")
                time.sleep(2)

                dict.pop(factNumb)

                newNumb = "C"+oldNumb

                dict[newNumb] = 'CANCELED'

                dict['Cantidad por cobrar']-=valueToCancel

            except:
                print("El número de factura no fue encontrado")
        else:
            print("No se seleccionó una opción válida")
    invoicesNumb = len(dict) - 2
    reco = dict.get('Cantidad recolectada')
    cob = dict.get('Cantidad por cobrar')
    print(f"RESUMEN DE EJECUCIÓN\n")

    print(f"El número de facturas es de: {invoicesNumb}\n")
    print(f"Cantidad de dinero recolectado: {reco}")
    print(f"Cantidad de dinero por cobrar: {cob}")
    print("")
    print(f"Diccionario de facturas:\n{dict}")


#print(pendBills(dictExample))      #ELIMINAR NUMERAL PARA PROBAR EL PROGRAMA EN LA FUNCIÓN

    
#2 PROGRAM TO MANAGE A DATABASE OF CLIENTS

dataBaseExample = {'100-00-0000':{'name':'Pepe Garcia','Address':'Cll 17','Telephone':'3101234567','mail':'pg@gmail.com','Preferential':True},
                   '210-00-0000':{'name':'Mauricio Lopez','Address':'Av 74','Telephone':'3101234567','mail':'ml@gmail.com','Preferential':True},
                   '301-00-0000':{'name':'Alejandro Perez','Address':'Cll 22','Telephone':'3101234567','mail':'ap@gmail.com','Preferential':True},
                   '400-10-0000':{'name':'Sofia Flores','Address':'Av 80','Telephone':'3101234567','mail':'sf@gmail.com','Preferential':False},
                   '500-01-0000':{'name':'Mateo Ramirez','Address':'Cll 30','Telephone':'3101234567','mail':'mr@gmail.com','Preferential':True},
                   '600-00-1000':{'name':'Valentina Sanchez','Address':'Av 12','Telephone':'3101234567','mail':'vs@gmail.com','Preferential':False},
                   '700-00-0100':{'name':'Andres Blanco','Address':'Cll 45','Telephone':'3101234567','mail':'ab@gmail.com','Preferential':True},
                   '800-00-0010':{'name':'Camilo Martinez','Address':'Av 40','Telephone':'3101234567','mail':'cm@gmail.com','Preferential':False},
                   '900-00-0001':{'name':'Sebastián Gonzalez','Address':'Cll 72','Telephone':'3101234567','mail':'sg@gmail.com','Preferential':True},
                   '999-00-0000':{'name':'Isabela Pardo','Address':'Av 50','Telephone':'3101234567','mail':'ip@gmail.com','Preferential':False},}


def dbGestor(dict):
    keep = True
    while keep == True:
            
        print(f"Seleccione la opción requerida: \n1.Agregar cliente\n2.Eliminar Cliente\n3.Mostrar cliente\n4.Listar todos los clientes\n5.Listar clientes preferenciales\n6.Finalizar ejecución")
        print("")
        option = int(input("Opción: "))

        if option == 6:
            keep = False
        elif option == 1:
            id = str(input("Ingrese el número de identificación del cliente: \n"))
            name = str(input("Ingrese el nombre del cliente: \n"))
            address = str(input("Ingrese la dirección del cliente: \n"))
            cellphone = str(input("Ingrese el telefono del cliente: \n"))
            mail = str(input("Ingrese el correo electronico del cliente: \n"))
            state = input("Ingrese si es cliente preferencial(Y) o no es cliente preferencial(N): \n")
            if state == 'Y':
                state = True
            elif state == 'N':
                state = False
            else:
                print("La opción seleccionada NO es válida se ha asignado un valor que no pertenece a ninguno")
                state = None
            dict[id] = {'name':name,'Address':address,'Telephone':cellphone,'mail':mail,'Preferential':state}
                    
        elif option == 2:
            idClient = str(input("Ingrese el ID exacto del cliente a eliminar: \n"))
            try:
                dict.pop(idClient)
            except:
                print("No se ha ingresado un ID que contenga la base de datos")
        elif option == 3:
            idClient = str(input("Ingrese el ID exacto del cliente a visualizar: \n"))
            try:
                visualizer = dict.get(idClient)
                print(f"Los datos del cliente identificado con el ID ingresado son: \n{visualizer}")
            except:
                print("No se ha ingresado un ID que contenga la base de datos")
        elif option == 4:
            print("La lista completa de clientes es: \n")
            lst = []
            for i in range(0,len(dict)):
                name = list(dataBaseExample.values())[i]['name']
                lst.append(name)
            print(f"Lista: {lst}")
        elif option == 5:
            print("La lista completa de clientes es: \n")
            lst = []
            for i in range(0,len(dict)):
                name = list(dataBaseExample.values())[i]['name']
                state = list(dataBaseExample.values())[i]['Preferential']
                if state == True:
                    lst.append(name)
            print(f"Lista: {lst}")
        else:
            print("Ha seleccionado una opción incorrecta")
    print(f"El número de clientes es: {len(dict)}")
    return f"La ejecución ha finalizado"

#print(dbGestor(dataBaseExample))       #ELIMINAR NUMERAL PARA PROBAR EL PROGRAMA EN LA FUNCIÓN