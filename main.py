def comenzar():
    prestamo = dict()
    # prestamo['id_prestamo'] #N/A str código único alfanumérico que identifica el prestamo
    # prestamo['casado'] # N/A str Aplicante es casado (Si / No)
    # prestamo['dependientes'] # N/A int / str Cantidad de personas dependientes del aplicante(0 / 1 / 2/ ‘3+’)
    # prestamo['educacion'] # N/A str Nivel de educación de la persona (Graduado / No Graduado)
    # prestamo['independiente'] # N/A str Aplicante es independiente (Si / No)
    # prestamo['ingreso_deudor'] # i_d float Ingreso del aplicante
    # prestamo['ingreso_codeudor'] # i_c float Ingreso del codeudor
    # prestamo['cantidad_prestamo'] # c_p float Cantidad decrédito solicitada
    # prestamo['plazo_prestamo'] # p_p int Plazo del crédito
    # prestamo['historia_credito'] # N/A int Aplicante cuenta con historia crediticia favorable (1 / 0)
    # prestamo['tipo_propiedad'] # N/A str Urbana / Rural / Semi Urbana
    prestamo['id_prestamo'] = 'RETOS2_002'
    prestamo['casado']  = 'No'
    prestamo['dependientes'] = 4
    prestamo['educacion']  = 'No Graduado'
    prestamo['independiente'] = 'No'
    prestamo['ingreso_deudor'] = 1830
    prestamo['ingreso_codeudor'] = 0
    prestamo['cantidad_prestamo'] = 100
    prestamo['plazo_prestamo']  = 360
    prestamo['historia_credito']  = 0
    prestamo['tipo_propiedad']  = 'Urbano'
    res = calcularCredito(prestamo)
    print(res)



def calcularCredito(prestamo:dict)->dict:
    response = dict()
    response['id_prestamo'] = prestamo['id_prestamo']
    response['aprobado'] = False
    if prestamo['historia_credito']:
        if prestamo['ingreso_codeudor'] > 0 and (prestamo['ingreso_deudor'] / 9) > prestamo['cantidad_prestamo']:
            response['aprobado'] = True
            return response
        else:
            if prestamo['dependientes'] > 2 and prestamo['independiente']:
                if (prestamo['ingreso_codeudor']/12) >  prestamo['cantidad_prestamo']:
                    response['aprobado'] = True
                    return response
            else:
                if prestamo['cantidad_prestamo'] < 200:
                    response['aprobado'] = True
                    return response
    else:
        if prestamo['independiente']:
            if not (prestamo['casado'] and prestamo['dependientes'] > 1):
                if prestamo['ingreso_deudor']/10 >  prestamo['cantidad_prestamo'] or prestamo['ingreso_codeudor']/10 > prestamo['cantidad_prestamo']:
                    if prestamo['cantidad_prestamo'] < 180:
                        response['aprobado'] = True
                        return response
                else:
                    response['aprobado'] = False
                    return response
            else:
                response['aprobado'] = False
                return response
        else:
            if prestamo['tipo_propiedad'] != 'Semi Urbana' and prestamo['dependientes'] < 2:
                if prestamo['educacion'] == 'Graduado':
                    if prestamo['ingreso_deudor'] / 11 > prestamo['cantidad_prestamo'] and prestamo['ingreso_codeudor'] / 11 > prestamo['cantidad_prestamo']:
                        response['aprobado'] = True
                        return response
                else:
                    response['aprobado'] = False
                    return response
            else:
                response['aprobado'] = False
                return response
    return response

comenzar()