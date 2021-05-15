from datetime import datetime,timedelta

def FuncFechaCorte(mes=None):

    if mes == None:
        fecha_ref = datetime.now().date().replace(day=1) 
    else:
        fecha_ref = datetime.now().date().replace(day=1,month=int(mes))
    
    mespasado = fecha_ref + timedelta(days=-1)
    return str(mespasado)

resultado = FuncFechaCorte("01")
print(resultado)