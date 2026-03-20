📊 Log Analyzer PRO

<p align="center">
  <b>Ferramenta simples para análise de logs de acesso por IP</b><br>
  <i>Projeto prático em Python com interface gráfica (Tkinter)</i>
</p>---

🚀 Sobre o Projeto

O Log Analyzer PRO é uma aplicação desktop desenvolvida em Python que permite registrar e analisar tentativas de acesso com base em logs.

O foco do projeto é demonstrar habilidades essenciais de um desenvolvedor júnior, incluindo:

- Manipulação de arquivos
- Estruturas de dados (dicionários)
- Interface gráfica com Tkinter
- Lógica de análise de dados
- Organização de código

---

🎯 Funcionalidades

✅ Adicionar logs manualmente
✅ Registro automático de data e hora
✅ Armazenamento em arquivo ".txt"
✅ Análise de falhas por IP
✅ Identificação de IPs suspeitos
✅ Interface gráfica simples e funcional

---

🧠 Regra de Negócio

Um IP é considerado suspeito quando:

Possui 3 ou mais tentativas com status "failed"

---

🖥️ Demonstração (Exemplo de uso)

📊 Resultado:
192.168.0.1 -> 3 falhas
192.168.0.2 -> 1 falha

🚨 Suspeitos:
192.168.0.1 (3)

---

📁 Estrutura do Projeto

📦 log-analyzer-pro
 ┣ 📄 main.py
 ┣ 📄 logs.txt
 ┗ 📄 README.md

---

▶️ Como Executar

🔧 Pré-requisitos

- Python 3.x instalado

▶️ Rodando o projeto

python main.py

📱 No Android (Pydroid):
Basta colar o código e executar normalmente.

---

📝 Exemplo de Log

192.168.0.1 - failed - 2026-03-20 14:30:10
192.168.0.1 - failed - 2026-03-20 14:31:05
192.168.0.1 - failed - 2026-03-20 14:32:22
192.168.0.2 - success - 2026-03-20 14:33:00

---

🛠️ Tecnologias Utilizadas

- Python 3
- Tkinter (interface gráfica)
- Manipulação de arquivos (".txt")
- Biblioteca "datetime"

---

📈 Possíveis Melhorias

- [ ] Interface moderna (CustomTkinter ou Web)
- [ ] Filtro por período (data/hora)
- [ ] Exportar relatórios (PDF/CSV)
- [ ] Integração com banco de dados (SQLite/PostgreSQL)
- [ ] Dashboard com gráficos
- [ ] Sistema de autenticação

---

💼 Valor para Recrutadores

Este projeto demonstra:

✔ Capacidade de construir uma aplicação completa
✔ Organização e clareza de código
✔ Uso de interface gráfica (diferencial para iniciantes)
✔ Implementação de lógica de análise de dados
✔ Pensamento em evolução (roadmap definido)

---

📌 Diferencial

Mesmo sendo um projeto simples, ele simula um cenário real de:

🔐 Monitoramento de tentativas de acesso
📊 Análise de comportamento suspeito
🧠 Base para sistemas de segurança

---

👨‍💻 Autor

Clayton Santos
🚀 Em evolução para Desenvolvedor Python

---

⭐ Contribuição

Sinta-se à vontade para clonar, estudar e melhorar o projeto!

git clone https://github.com/seu-usuario/log-analyzer-pro.git

---

📢 Observação

Este projeto tem fins educacionais e foi desenvolvido como parte da jornada de aprendizado em programação.

---

<p align="center">
  💡 <b>"Código simples, mas com mentalidade profissional."</b>
</p>
