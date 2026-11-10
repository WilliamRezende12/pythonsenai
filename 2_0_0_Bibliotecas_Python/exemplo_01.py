from datetime import datetime

# Obtém hora e data atual
agora = datetime.now()

# Exibe os resultados
print("Data e hora atual:", agora)

print("Data:", agora.strftime("%d/%m/%Y"))

print("Hora:", agora.strftime("%H:%M:%S"))