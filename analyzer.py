import os


LOG_FILE = "logs.txt"


def garantir_arquivo(caminho):
    """Garante que o arquivo existe"""
    if not os.path.exists(caminho):
        print("⚠️ Arquivo não encontrado. Criando...")
        with open(caminho, "w"):
            pass


def ler_logs(caminho):
    """Lê os logs do arquivo"""
    with open(caminho, "r") as arquivo:
        return arquivo.readlines()


def adicionar_logs(caminho):
    """Adiciona logs manualmente"""
    print("\n✍️ Digite os logs (digite 'sair' para parar):")

    with open(caminho, "a") as arquivo:
        while True:
            entrada = input("Log: ")

            if entrada.lower() == "sair":
                break

            arquivo.write(entrada + "\n")


def contar_falhas(linhas):
    """Conta tentativas de login falhas por IP"""
    ips = {}

    for linha in linhas:
        linha = linha.strip()

        if "failed" in linha.lower():
            partes = linha.split(" - ")

            if len(partes) != 2:
                print(f"⚠️ Linha inválida: {linha}")
                continue

            ip = partes[0]
            ips[ip] = ips.get(ip, 0) + 1

    return ips


def detectar_suspeitos(ips, limite=3):
    """Filtra IPs suspeitos com base no limite"""
    return {ip: total for ip, total in ips.items() if total >= limite}


def exibir_resultados(ips, suspeitos):
    """Exibe os resultados no terminal"""
    print("\n📊 Resultado geral:")
    for ip, total in ips.items():
        print(f"{ip} -> {total} falhas")

    print("\n🚨 IPs suspeitos:")
    if suspeitos:
        for ip, total in suspeitos.items():
            print(f"{ip} ({total} tentativas)")
    else:
        print("Nenhum IP suspeito encontrado.")


def main():
    garantir_arquivo(LOG_FILE)

    print("\n=== LOG ANALYZER ===")
    print("1 - Adicionar logs")
    print("2 - Analisar logs")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_logs(LOG_FILE)

    linhas = ler_logs(LOG_FILE)

    if not linhas:
        print("📭 Arquivo vazio.")
        return

    ips = contar_falhas(linhas)
    suspeitos = detectar_suspeitos(ips)

    exibir_resultados(ips, suspeitos)


if __name__ == "__main__":
    main()