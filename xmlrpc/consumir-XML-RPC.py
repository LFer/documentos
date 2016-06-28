# -*- coding: utf_8 -*-

   #####
####
##   OOO    Declaraciones
##   OOOOO
##   OOO    Bibliotecas y módulos utilizados y variables  globales
####
   #####
import sys
import xmlrpclib

# OpenERP
oerp_base = 'LMO2'
oerp_user = 'admin'
oerp_pass = 'admin'

# Servicios XML-RPC
url_common = 'http://localhost:8069/xmlrpc/common'              # Login
url_object = 'http://localhost:8069/xmlrpc/object'              # ORM

   #####
####
##    OOO   main
##   OOOOO
##    OOO   Establece la conexión para obtener el UID, a continuación
##          ejecuta el procedimiento "hay_novedad" de la clase "xlab"
##          con los parámetros "proveedor" y "novedad", ambos enteros.
####
   #####
def main():

    # OpenERP: Obtener el uid (Login)
    sock_common = xmlrpclib.ServerProxy(url_common)
    oerp_uid = sock_common.login(oerp_base, oerp_user, oerp_pass)

    # OpenERP: Conector con los servicios ORM
    sock_object = xmlrpclib.ServerProxy(url_object)

    # Parámetros del método invocado (si no hay no se pone nada)
    # version ----------------------------------------------------------------------+
    # proveedor ----------------------------------------------------------------+   |
    #                                                                           |   |
    # Invocar el método 'hay_novedad' ---------------------------------+        |   |
    # Clase a la que pertenece el método -----------------+            |        |   |
    #                                                     |            |        |   |
    sock_object.execute(oerp_base, oerp_uid, oerp_pass, 'xlab', 'hay_novedad', 123, 1)

    return 0


if __name__ == "__main__":
    sys.exit(main())
