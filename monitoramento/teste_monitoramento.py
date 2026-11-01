
from registrador import monitorar_etapa

print("Iniciando teste de falha da Pessoa 4")

with monitorar_etapa("teste_falha_p4"):
    print("Simulando erro de qualidade...")
    raise ValueError("Falha de qualidade simulada")

print("Esta mensagem NAO deve aparecer!")
