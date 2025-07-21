def detect_strong_pattern(history):
    if len(history) < 5:
        return None

    # Estratégia 1: Alternância
    if all(history[i] != history[i+1] for i in range(len(history)-1)):
        return "alternancia"

    # Estratégia 2: Repetição
    if len(set(history[-5:])) == 1:
        return "repeticao"

    # Estratégia 3: ZigZag curto
    if history[-3:] in [["P", "B", "P"], ["B", "P", "B"]]:
        return "zigzag"

    # Estratégia 4: Dominância Player
    if history[-6:].count("P") >= 5:
        return "dominancia_p"

    # Estratégia 5: Dominância Banker
    if history[-6:].count("B") >= 5:
        return "dominancia_b"

    # Estratégia 6: Tripla
    if history[-3:] == ["B", "B", "B"]:
        return "tripla_b"
    if history[-3:] == ["P", "P", "P"]:
        return "tripla_p"

    # Estratégia 7: Espelhamento
    if history[-6:-3] == history[-3:]:
        return "espelhamento"

    # Estratégia 8: TIE frequente
    if history.count("T") >= 3 and history[-1] != "T":
        return "tie_proximo"

    # Adicione +22 padrões aqui...
    # Por simplicidade vamos retornar aleatório entre padrões detectados
    return None
