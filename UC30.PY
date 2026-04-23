
PONTOS_POR_KG = {
    "plastico": 10,
    "papel":     8,
    "metal":    15,
    "vidro":    12,
    "organico":  5,
}

DICAS_RECICLAGEM = {
    "plastico": "Lave antes de descartar e retire tampas.",
    "papel":    "Mantenha seco e sem gordura.",
    "metal":    "Amasse latas para economizar espaço.",
    "vidro":    "Cuidado com vidros quebrados; embale com jornal.",
    "organico": "Pode virar adubo na escola!",
}

META_KG = 50.0 
registros = []      
def exibir_menu():
    """Mostra o menu principal."""
    print("\n" + "=" * 45)
    print(" COLETA SELETIVA ESCOLAR ")
    print("=" * 45)
    print("  1. Registrar entrega de material")
    print("  2. Consultar entregas")
    print("  3. Ranking de participantes")
    print("  4. Progresso da meta coletiva")
    print("  5. Sair")
    print("=" * 45)


def validar_float(mensagem):
    """Lê um número decimal positivo, rejeitando entradas inválidas."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
            if valor <= 0:
                print("  Digite um número maior que zero.")
            else:
                return valor
        except ValueError:
            print("  Entrada inválida. Use apenas números (ex.: 1.5).")

def validar_material():
    """Apresenta os tipos disponíveis e valida a escolha."""
    tipos = list(PONTOS_POR_KG.keys())
    print("\n  Tipos de material:")
    for i, t in enumerate(tipos, 1):
        print(f"  {i}. {t.capitalize()}")
    while True:
        opcao = input("  Escolha o número do material: ").strip()
        if opcao.isdigit() and 1 <= int(opcao) <= len(tipos):
            return tipos[int(opcao) - 1]
        print("  Opção inválida.")

def validar_nome():
    """Garante que o nome não esteja em branco."""
    while True:
        nome = input("  Seu nome: ").strip()
        if nome:
            return nome.title()
        print("   O nome não pode estar vazio.")


def registrar_entrega():
    """Recebe os dados de uma entrega e salva no sistema."""
    print("\n--- REGISTRAR ENTREGA ---")
    nome     = validar_nome()
    material = validar_material()
    peso_kg  = validar_float("  Quantidade em kg: ")

    pontos = round(peso_kg * PONTOS_POR_KG[material])

    entrega = {
        "nome":     nome,
        "material": material,
        "peso_kg":  peso_kg,
        "pontos":   pontos,
    }
    registros.append(entrega)

    print(f"\n   Registrado! Você ganhou {pontos} pontos.")
    print(f"   Dica: {DICAS_RECICLAGEM[material]}")


def consultar_entregas():
    """Lista todas as entregas realizadas."""
    print("\n--- ENTREGAS REGISTRADAS ---")
    if not registros:
        print("  Nenhuma entrega registrada ainda.")
        return

    print(f"  {'#':<4} {'Nome':<20} {'Material':<10} {'Kg':>6} {'Pts':>6}")
    print("  " + "-" * 50)
    for i, e in enumerate(registros, 1):
        print(f"  {i:<4} {e['nome']:<20} {e['material'].capitalize():<10}"
              f" {e['peso_kg']:>6.2f} {e['pontos']:>6}")

def ranking():
    """Exibe os participantes ordenados por pontuação total."""
    print("\n--- RANKING DE PARTICIPANTES ---")
    if not registros:
        print("  Nenhuma entrega registrada ainda.")
        return

    placar = {}
    for e in registros:
        placar[e["nome"]] = placar.get(e["nome"], 0) + e["pontos"]

    ordenado = sorted(placar.items(), key=lambda x: x[1], reverse=True)
    medalhas = ["🥇", "🥈", "🥉"]

    for i, (nome, pts) in enumerate(ordenado):
        simbolo = medalhas[i] if i < 3 else f"  {i+1}."
        print(f"  {simbolo} {nome:<20} {pts} pontos")

def progresso_meta():
    """Mostra o total coletado e o percentual da meta."""
    total_kg = sum(e["peso_kg"] for e in registros)
    percentual = min((total_kg / META_KG) * 100, 100)
    barras = int(percentual / 5)   

    print("\n--- PROGRESSO DA META COLETIVA ---")
    print(f"  Meta: {META_KG:.0f} kg  |  Coletado: {total_kg:.2f} kg")
    print(f"  [{'' * barras}{'' * (20 - barras)}] {percentual:.1f}%")

    if total_kg >= META_KG:
        print("   META ATINGIDA! Parabéns à escola!")
    else:
        falta = META_KG - total_kg
        print(f"  Faltam {falta:.2f} kg para atingir a meta.")

def main():
    print("\nBem-vindo ao Sistema de Coleta Seletiva Escolar!")
    print("Contribua com o meio ambiente e ganhe pontos. ")

    while True:
        exibir_menu()
        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            registrar_entrega()
        elif opcao == "2":
            consultar_entregas()
        elif opcao == "3":
            ranking()
        elif opcao == "4":
            progresso_meta()
        elif opcao == "5":
            print("\n  Até logo! Continue reciclando. \n")
            break
        else:
            print("   Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()