import matplotlib.pyplot as plt
import numpy as np

# Configuração Visual
plt.rcParams['font.size'] = 12
plt.rcParams['font.weight'] = 'bold'

# 1. Comparativo de Estoque
labels = ['Estoque em Linha']
antes = 12  # horas
depois = 2  # horas

# 2. Ciclo de Tempo do Rebocador (Total 60 min)
fases = ['Picking', 'Trânsito', 'Troca (Linha)', 'Retorno']
tempos = [25, 10, 15, 10]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Gráfico de Barras
bars = ax1.bar(['Antes (Push)', 'Depois (JIT)'], [antes, depois], color=['#e74c3c', '#27ae60'])
ax1.set_ylabel('Horas de Autonomia')
ax1.set_title('Impacto no Inventário de Borda', pad=20)
ax1.bar_label(bars, padding=3)

# Gráfico de Pizza
ax2.pie(tempos, labels=fases, autopct='%1.1f%%', startangle=140, colors=['#3498db', '#f1c40f', '#2ecc71', '#95a5a6'], explode=(0.1, 0, 0.1, 0))
ax2.set_title('Distribuição da Janela Horária', pad=20)

plt.tight_layout()
plt.savefig('logistica_results.png')
print("✅ Projeto modelado e gráfico salvo como 'logistica_results.png'")
