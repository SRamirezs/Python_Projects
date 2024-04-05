import shutil
from pathlib import Path
import os


def mostrar_menu():
    print('1. Leer Receta')
    print('2. Crear Receta')
    print('3. Crear Categoria')
    print('4. Eliminar Receta')
    print('5. Eliminar Categoria')
    print('6. Finalizar Programa')
    pass


def mostrar_categorias():
    print('Estas son las opciones que tenemos,')
    directorio = Path('/Users/santiagoramirezsarmiento/Desktop/Recetas')
    carpetas = [carpeta.name for carpeta in directorio.iterdir() if carpeta.is_dir()]
    print('\n')
    print(carpetas)


def elegir_categoria():
    categoria = input('Elija una categoria (Escriba solo el nombre): ')
    recetas = Path(f'/Users/santiagoramirezsarmiento/Desktop/Recetas/{categoria}')
    abrir_recetas = [receta.name for receta in recetas.iterdir() if receta.is_file()]
    print('\n')
    print(abrir_recetas)
    return categoria


def abrir_receta(categoria_elegida):
    receta_elegida = input('¿Que receta desea abrir?: ')
    receta_path = Path(f'/Users/santiagoramirezsarmiento/Desktop/Recetas/{categoria_elegida}/{receta_elegida}')
    leer_receta = receta_path.read_text()
    print('\n')
    print(leer_receta)


def crear_receta(categoria):
    ruta_categoria = Path(f'/Users/santiagoramirezsarmiento/Desktop/Recetas/{categoria}/')
    nombre_receta = input('Nombre de tu receta') + '.txt'
    ruta_receta = ruta_categoria / nombre_receta
    with open(ruta_receta, 'w') as f:
        print('La receta ha sido creada')
        pass


def elimina_receta(categoria):
    ruta_categoria = Path(f'/Users/santiagoramirezsarmiento/Desktop/Recetas/{categoria}/')
    nombre_receta = input('Ingrese el nombre de la receta que eliminara: ')
    ruta = ruta_categoria / nombre_receta
    if os.path.exists(ruta):
        os.remove(ruta)
        print('La receta ha sido eliminada')
    else:
        print('La receta no existe')


def crear_categoria(nombre):
    ruta_recetas = Path('/Users/santiagoramirezsarmiento/Desktop/Recetas/') / nombre
    Path(ruta_recetas).mkdir()
    print('La categoria ha sido creada')


def elimina_categoria():
    ruta_recetas = Path(f'/Users/santiagoramirezsarmiento/Desktop/Recetas/')
    nombre_categoria = input('Ingrese la categoria que eliminara')
    ruta = ruta_recetas / nombre_categoria
    if os.path.exists(ruta):
        shutil.rmtree(ruta)
        print('La categoria ha sido eliminada')
    else:
        print('La categoria no existe')


print(f'Hola {input('Ingresa tu Nombre: ')} este es el MENU para tu recetario')
while True:
    print('\n')
    mostrar_menu()
    print('\n')
    menu = input('Seleccione una opción: ')

    if menu == '1':
        mostrar_categorias()
        categoria_seleccionada = elegir_categoria()
        abrir_receta(categoria_seleccionada)
        pass
    elif menu == '2':
        print('¿En que categoria desea crear su receta?')
        mostrar_categorias()
        categoria_receta = input('Escriba la categoria donde va a crear su receta')
        crear_receta(categoria_receta)
        pass
    elif menu == '3':
        nueva_categoria = input('Ingrese el nombre de la categoria que desea crear: ')
        crear_categoria(nueva_categoria)
        pass
    elif menu == '4':
        mostrar_categorias()
        categoria = elegir_categoria()
        elimina_receta(categoria)
        pass
    elif menu == '5':
        mostrar_categorias()
        elimina_categoria()
        pass
    elif menu == '6':
        print('Hasta luego')
        break
    else:
        print('Esta funcion no es valida, ingresa numeros del 1-6')
