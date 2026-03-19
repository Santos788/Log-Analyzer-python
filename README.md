🔐 Log Analyzer - Python

Projeto simples de análise de logs com foco em cibersegurança.

📌 Funcionalidades

- Leitura de logs de um arquivo ".txt"
- Identificação de tentativas de login falhas
- Contagem de falhas por IP
- Detecção de IPs suspeitos (ataques de força bruta)

🧠 Conceitos aplicados

- Manipulação de arquivos
- Estruturas de dados (dicionários)
- Funções
- Tratamento básico de erros
- Lógica de detecção de ataques

🚀 Como usar

python main.py

Menu:

- 1 → Adicionar logs manualmente
- 2 → Analisar logs

📂 Exemplo de log

192.168.0.1 - login failed
192.168.0.1 - login failed
192.168.0.1 - login failed
192.168.0.2 - login success

🚨 Exemplo de saída

IP suspeito: 192.168.0.1 (3 tentativas)

🔥 Possíveis melhorias

- Interface gráfica
- Exportação de relatório
- Uso de regex para parsing
- Integração com API
- Dashboard web (Flask)

👨‍💻 Autor

Desenvolvido por Clayton 
