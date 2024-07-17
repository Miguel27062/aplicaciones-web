def elegir_metodo_pago(monto):

  if monto < 150000:
    return "Efectivo"
  elif 150000 <= monto < 300000:
    return "Dinero electrónico (celular)"
  elif 300000 <= monto < 600000:
    return "Tarjeta de débito"
  else:
    return "Tarjeta de crédito"


monto_total = float(input("Ingrese el monto total a pagar: $"))


metodo_pago = elegir_metodo_pago(monto_total)
print("Se recomienda pagar con:", metodo_pago)

