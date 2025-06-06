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
    """
    8-QAM (Quadrature Amplitude Modulation) para grupos de 3 bits.
    Combina fase e amplitude.
    """
    if len(bits) % 3 != 0:
        bits += '0' * (3 - len(bits) % 3)  # Padding

    t = np.linspace(0, 1, sample_rate, endpoint=False)
    signal = []

    mapping = {
        '000': (1, 0),    # amplitude=1, phase=0
        '001': (1, 90),
        '010': (1, 180),
        '011': (1, 270),
        '100': (2, 0),
        '101': (2, 90),
        '110': (2, 180),
        '111': (2, 270),
    }

    for i in range(0, len(bits), 3):
        group = bits[i:i+3]
        amp, phase_deg = mapping[group]
        phase_rad = np.deg2rad(phase_deg)
        wave = amp * np.cos(2 * np.pi * 5 * t + phase_rad)
        signal.extend(wave)

    return np.array(signal)
