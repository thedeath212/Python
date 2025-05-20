"""
Crear un programa que lea un archivo de texto que simula un log de accesos a un sistema, y que realice análisis útiles sobre el contenido
del archivo. El archivo contiene registros de acceso con la siguiente estructura:
"""

# Formato del archivo de log:
# fecha_hora, usuario, ip_origen, ip_destino, estado
# Ejemplo de contenido del archivo:
# 2023-10-01 12:00:00, juan,
# 

from collections import defaultdict, Counter
import os

# Leer archivo de log y cargar registros
def cargar_logs(nombre_archivo):
    registros = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            partes = linea.strip().split(', ')
            if len(partes) == 5:
                fecha_hora, usuario, ip_origen, ip_destino, estado = partes
                registros.append({
                    "fecha_hora": fecha_hora,
                    "usuario": usuario,
                    "ip_origen": ip_origen,
                    "ip_destino": ip_destino,
                    "estado": estado
                })
    return registros

# 1. Resumen de accesos por usuario
def resumen_por_usuario(registros):
    resumen = defaultdict(lambda: {"OK": 0, "FALLIDO": 0})
    for r in registros:
        resumen[r["usuario"]][r["estado"]] += 1
    return resumen

# 2. IP más usada
def ip_mas_usada(registros):
    ips = [r["ip_origen"] for r in registros]
    conteo_ips = Counter(ips)
    return conteo_ips.most_common(1)[0]

# 3. Detectar intentos fallidos consecutivos
def detectar_intrusiones(registros, max_fallos=3):
    intentos = defaultdict(list)
    for r in registros:
        intentos[r["usuario"]].append(r["estado"])

    sospechosos = []
    for usuario, acciones in intentos.items():
        consecutivos = 0
        for estado in acciones:
            if estado == "FALLIDO":
                consecutivos += 1
                if consecutivos >= max_fallos:
                    sospechosos.append(usuario)
                    break
            else:
                consecutivos = 0
    return sospechosos

# 4. Usuario con más accesos exitosos
def usuario_con_mas_ok(resumen):
    return max(resumen.items(), key=lambda x: x[1]["OK"])

# ======= Programa principal =======
if __name__ == "__main__":
    archivo = "accesos.log"

    # Crear el archivo si no existe con datos de ejemplo
    if not os.path.exists(archivo):
        with open(archivo, 'w') as f:
            f.write("""2023-10-01 12:00:00, juan, 192.168.0.2, 10.0.0.1, OK
2023-10-01 12:01:00, juan, 192.168.0.2, 10.0.0.1, FALLIDO
2023-10-01 12:02:00, juan, 192.168.0.2, 10.0.0.1, FALLIDO
2023-10-01 12:03:00, juan, 192.168.0.2, 10.0.0.1, FALLIDO
2023-10-01 12:04:00, maria, 192.168.0.3, 10.0.0.1, OK
2023-10-01 12:05:00, pedro, 192.168.0.4, 10.0.0.1, OK
2023-10-01 12:06:00, maria, 192.168.0.3, 10.0.0.1, FALLIDO""")
        print(f"✅ Archivo '{archivo}' creado con datos de ejemplo.")

    registros = cargar_logs(archivo)
    
    if not registros:
        print("No se encontraron registros válidos.")
        exit()

    resumen = resumen_por_usuario(registros)
    print("\n🔍 Resumen por usuario:")
    for usuario, datos in resumen.items():
        print(f" - {usuario}: OK = {datos['OK']}, FALLIDO = {datos['FALLIDO']}")

    ip, cantidad = ip_mas_usada(registros)
    print(f"\n📡 IP más usada: {ip} ({cantidad} veces)")

    sospechosos = detectar_intrusiones(registros)
    print("\n🚨 Posibles intentos de intrusión:")
    if sospechosos:
        for usuario in sospechosos:
            print(f" - {usuario}")
    else:
        print(" - Ningún usuario con intentos fallidos consecutivos sospechosos.")

    usuario_top, datos_top = usuario_con_mas_ok(resumen)
    print(f"\n🏆 Usuario con más accesos exitosos: {usuario_top} ({datos_top['OK']} veces)")
# Fin del programa
