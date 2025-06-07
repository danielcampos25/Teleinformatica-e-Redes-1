# modulacao_portadora.py
import numpy as np

def encode_ASK(bits, freq=5, sample_rate=100):
    """
    Amplitude Shift Keying: codifica bits em uma onda com amplitude variável.
    """
    t = np.linspace(0, 1, sample_rate, endpoint=False)
    signal = []

    for bit in bits:
        amplitude = 1 if bit == '1' else 0
        wave = amplitude * np.sin(2 * np.pi * freq * t)
        signal.extend(wave)

    return np.array(signal)

def encode_FSK(bits, freq0=3, freq1=7, sample_rate=100):
    """
    Frequency Shift Keying: codifica bits em diferentes frequências.
    """
    t = np.linspace(0, 1, sample_rate, endpoint=False)
    signal = []

    for bit in bits:
        freq = freq1 if bit == '1' else freq0
        wave = np.sin(2 * np.pi * freq * t)
        signal.extend(wave)

    return np.array(signal)

def encode_8QAM(bits, sample_rate=100):
    original_length = len(bits)  # Guarda o tamanho original pra ajudar no decode
    if len(bits) % 3 != 0:
        bits += '0' * (3 - len(bits) % 3)
    t = np.linspace(0, 1, sample_rate, endpoint=False)
    signal = []

    # Mapeamento consistente com a decodificação (I, Q)
    mapping = {
        '000': (1, 0), '001': (0, 1),
        '010': (-1, 0), '011': (0, -1),
        '100': (2, 0), '101': (0, 2),
        '110': (-2, 0), '111': (0, -2),
    }

    for i in range(0, len(bits), 3):
        group = bits[i:i+3]
        I, Q = mapping[group]
        # Criar a onda modulada (portadora em fase e quadratura)
        wave = I * np.cos(2 * np.pi * 5 * t) - Q * np.sin(2 * np.pi * 5 * t)
        signal.extend(wave)

    return np.array(signal), original_length  # Retorna o tamanho original
