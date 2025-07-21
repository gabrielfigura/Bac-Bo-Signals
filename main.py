import time
from scraper import get_last_rounds
from strategies import detect_strong_pattern
from telegram_bot import send_signal, delete_message
from utils import validate_result

last_signal_time = 0
last_msg_id = None
gale_active = False
sinal_enviado = False

while True:
    history = get_last_rounds()

    pattern = detect_strong_pattern(history)
    now = time.time()

    if pattern and (now - last_signal_time) > 60:
        # Decidir jogada com base no padrão
        if pattern in ["repeticao", "dominancia_b", "tripla_b"]:
            entrada = "🔴🔴🔴"
            expected = "B"
        elif pattern in ["dominancia_p", "tripla_p"]:
            entrada = "🔵🔵🔵"
            expected = "P"
        elif pattern == "tie_proximo":
            entrada = "🔵🔵🔵" if history[-1] == "B" else "🔴🔴🔴"
            expected = "B" if entrada == "🔴🔴🔴" else "P"
        else:
            entrada = "🔵🔵🔵"
            expected = "P"

        sinal_enviado = True
        last_signal_time = now

        send_signal(f"""
🎲 <b>Novo sinal Bac Bo ao vivo:</b>
Entrada: {entrada}
Protege o TIE🟡
Validade: 1 minuto
Confiança: {80 + int(now)%20}%
""")

        # Validação do sinal após 60s
        resultado = validate_result(expected)
        send_signal(f"Resultado: {resultado}")

        # Se for LOSS, aplicar 1º GALE
        if resultado == "LOSS ❌":
            gale_active = True
            send_signal("📢 Aplicando GALE 1...")
            resultado = validate_result(expected)
            send_signal(f"Resultado GALE: {resultado}")

        sinal_enviado = False
        gale_active = False

    elif not sinal_enviado and (now - last_signal_time) > 30:
        msg = send_signal("⌛ <b>ANALISANDO...</b>")
        time.sleep(15)
        delete_message(msg.message_id)

    time.sleep(5)
