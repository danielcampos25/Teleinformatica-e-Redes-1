import os
import matplotlib.pyplot as plt
from . import modulacao_banda_base

def plot_signal(signal, title, bits, samples_per_bit=1):
    time = []
    level = []
    
    for i, value in enumerate(signal):
        t_begin = i
        t_end = i + 1

        time.extend([t_begin, t_end])
        level.extend([value, value])
    
    plt.step(time, level, where='post')
    plt.ylim(-1.5, 1.5)
    plt.title(f"{title} - bits: {bits}")
    plt.xlabel("Tempo (amostras)")
    plt.ylabel("Nível")
    plt.grid(True)

def main():
    bits = "1011001"

    nrz = modulacao_banda_base.encode_NRZ(bits)
    manchester = modulacao_banda_base.encode_manchester(bits)
    bipolar = modulacao_banda_base.encode_bipolar(bits)

    plt.figure(figsize=(10, 8))

    plt.subplot(3, 1, 1)
    plot_signal(nrz, "NRZ-Polar", bits)

    plt.subplot(3, 1, 2)
    plot_signal(manchester, "Manchester", bits)

    plt.subplot(3, 1, 3)
    plot_signal(bipolar, "Bipolar (AMI)", bits)

    plt.tight_layout()

    # Criar pasta Resultados se não existir
    os.makedirs("Resultados", exist_ok=True)

    plt.savefig("Resultados/modulacoes_banda_base.png")
    print("Gráfico salvo em Resultados/modulacoes_banda_base.png")

if __name__ == "__main__":
    main()
