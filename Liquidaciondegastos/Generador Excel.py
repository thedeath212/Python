import xml.etree.ElementTree as ET
import pandas as pd
import os

def extraer_datos_factura(archivo_xml):
    try:
        tree = ET.parse(archivo_xml)
        root = tree.getroot()

        # Extraemos el comprobante CDATA y lo parseamos
        comprobante_cdata = root.find('comprobante').text.strip()
        comprobante_root = ET.fromstring(comprobante_cdata)

        # Datos básicos
        razon_social = comprobante_root.find('infoTributaria/razonSocial').text if comprobante_root.find('infoTributaria/razonSocial') is not None else ''
        nombre_comercial = comprobante_root.find('infoTributaria/nombreComercial').text if comprobante_root.find('infoTributaria/nombreComercial') is not None else ''
        ruc = comprobante_root.find('infoTributaria/ruc').text if comprobante_root.find('infoTributaria/ruc') is not None else ''

        fecha_emision = comprobante_root.find('infoFactura/fechaEmision').text if comprobante_root.find('infoFactura/fechaEmision') is not None else ''
        fecha_emision = fecha_emision.split('T')[0] if 'T' in fecha_emision else fecha_emision

        importe_total = comprobante_root.find('infoFactura/importeTotal').text if comprobante_root.find('infoFactura/importeTotal') is not None else '0'

        infoTrib = comprobante_root.find('infoTributaria')
        if infoTrib is not None:
            estab = infoTrib.find('estab').text if infoTrib.find('estab') is not None else ''
            ptoEmi = infoTrib.find('ptoEmi').text if infoTrib.find('ptoEmi') is not None else ''
            secuencial = infoTrib.find('secuencial').text if infoTrib.find('secuencial') is not None else ''
            no_doc = f"{estab}-{ptoEmi}-{secuencial}"
        else:
            no_doc = ''

        # Gastos y Detalle siempre vacíos
        gastos = ''
        detalle = ''

        proveedor = razon_social

        teceb_otros = "Otros"

        doc_soporte = "Factura"

        return {
            "No": None,
            "Fecha Emisión": fecha_emision,
            "Gastos": gastos,
            "Proveedor": proveedor,
            "Detalle": detalle,
            "TECEB u otros": teceb_otros,
            "Documento soporte": doc_soporte,
            "No Doc": no_doc,
            "Valor": importe_total
        }

    except Exception as e:
        print(f"Error al procesar {archivo_xml}: {e}")
        return None

def procesar_carpeta_xml(carpeta):
    facturas = []
    contador = 1
    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith('.xml'):
            ruta_completa = os.path.join(carpeta, archivo)
            datos = extraer_datos_factura(ruta_completa)
            if datos:
                datos["No"] = contador
                contador += 1
                facturas.append(datos)

    if facturas:
        df = pd.DataFrame(facturas)
        excel_salida = os.path.join(carpeta, 'facturas_consolidadas.xlsx')
        df.to_excel(excel_salida, index=False)
        print(f"Archivo Excel generado: {excel_salida}")
    else:
        print("No se procesaron facturas.")

if __name__ == "__main__":
    carpeta_facturas = '.'  # Cambiar carpeta si quieres
    procesar_carpeta_xml(carpeta_facturas)
