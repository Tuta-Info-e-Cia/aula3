"""
18.	Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho_arquivo_mb = float(input("Informe o tamanho do arquivo (em MB): "))
velocidade_mbps = float(input("Informe a velocidade da internet (em Mbps): "))
velocidade_MBps = velocidade_mbps / 8
tempo_segundos = tamanho_arquivo_mb / velocidade_MBps
tempo_minutos = tempo_segundos / 60
print(f"\nTempo aproximado de download: {tempo_minutos:.2f} minutos")
