import os
import matplotlib.pyplot as plt
from .import modulacao_portadora
from CamadaFisica.ModulacaoBandaBase import modulacao_banda_base


def plot_signal(signal, title, sample_rate, is_baseband=False):
    if is_baseband:
        time = []
        level = []
        for i, val in enumerate(signal):
            time.extend([i, i+1])
            level.extend([val, val])
    else:
        time = [i / sample_rate for i in range(len(signal))]
        level = signal

    plt.plot(time, level)
    plt.title(title)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)

def main():
    bits = "1011001"
    sample_rate = 100

    nrz = modulacao_banda_base.encode_NRZ(bits)

    ask = modulacao_portadora.encode_ASK(bits, sample_rate=sample_rate)
    fsk = modulacao_portadora.encode_FSK(bits, sample_rate=sample_rate)
    qam = modulacao_portadora.encode_8QAM(bits, sample_rate=sample_rate)

    plt.figure(figsize=(12, 12))

    plt.subplot(4, 1, 1)
    plot_signal(nrz, "Sinal original (NRZ)", sample_rate, is_baseband=True)

    plt.subplot(4, 1, 2)
    plot_signal(ask, "Amplitude Shift Keying (ASK)", sample_rate)

    plt.subplot(4, 1, 3)
    plot_signal(fsk, "Frequency Shift Keying (FSK)", sample_rate)

    plt.subplot(4, 1, 4)
    plot_signal(qam, "8-QAM (Quadrature Amplitude Modulation)", sample_rate)

    plt.tight_layout()

    os.makedirs("Resultados", exist_ok=True)

    plt.savefig("Resultados/modulacoes_portadora_com_sinal.png")
    print("Gráfico salvo em Resultados/modulacoes_portadora_com_sinal.png")

if __name__ == "__main__":
    main()
