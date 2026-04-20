🏎️ Projeto: Otimização de Logística Interna Automotiva (JIT)
Este projeto apresenta uma modelagem técnica para a transição de um sistema de abastecimento de peças "Push" (Empurrado) para um sistema "Pull" (Puxado/Just-in-Time) em uma planta automotiva.
🎯 Objetivo
Implementar um sistema de Abastecimento Horário (Internal Milk Run) para sincronizar o almoxarifado interno com o ritmo da linha de montagem (Takt Time), visando eficiência operacional e redução de custos.
🚀 Principais Ganhos (KPIs)
Redução de Inventário: Diminuição da autonomia de borda de linha de 12h para 2h (redução de 83%).
Otimização de Espaço: Liberação de área fabril estratégica para novos processos.
Ruptura Zero: Garantia de abastecimento contínuo através de rotas fixas de rebocadores.
Ergonomia e Qualidade: Uso de kits sequenciados e embalagens padronizadas (KLT).
🛠️ Tecnologias Utilizadas
Python: Utilizado para o cálculo de dimensionamento de frota e geração de gráficos de performance.
Metodologias Lean: Kanban, Heijunka (nivelamento) e Milk Run.
📊 Estrutura do Código
O arquivo main.py contém o script para:
Calcular a distribuição do tempo de ciclo do rebocador (janela de 60 min).
Gerar o comparativo de estoque antes vs. depois da implementação.
