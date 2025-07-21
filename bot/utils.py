import time
from bot.scraper import get_last_rounds

def validate_result(expected):
    time.sleep(60)  # espera nova rodada

    rounds = get_last_rounds(1)
    real = rounds[-1]

    if real == expected:
        return "WIN ✅"
    elif real == "T":
        return "EMPATE (VALIDA WIN) ✅"
    else:
        return "LOSS ❌"
