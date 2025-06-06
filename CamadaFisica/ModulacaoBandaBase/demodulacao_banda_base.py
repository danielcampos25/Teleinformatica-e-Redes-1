# demodulacao_banda_base.py
"""
Funções para demodulação de sinais modulados na banda base:
- NRZ-Polar
- Manchester
- Bipolar (AMI)
"""

def decode_NRZ(signal):
    """
    Demodula sinal NRZ-Polar.
    Assume que sinal é lista de níveis (ex: +1, -1)
    Retorna string de bits.
    """
    bits = []
    for level in signal:
        if level > 0:
            bits.append('1')
        else:
            bits.append('0')
    return ''.join(bits)


def decode_manchester(signal):
    """
    Demodula sinal Manchester.
    Assume que sinal é lista de níveis com comprimento par,
    cada bit codificado em dois níveis consecutivos.
    Retorna string de bits.
    """
    bits = []
    if len(signal) % 2 != 0:
        raise ValueError("Sinal Manchester deve ter comprimento par")
    for i in range(0, len(signal), 2):
        first = signal[i]
        second = signal[i + 1]
        # Considerando: transição de alto para baixo = 1, baixo para alto = 0
        if first > second:
            bits.append('1')
        else:
            bits.append('0')
    return ''.join(bits)


def decode_bipolar(signal):
    """
    Demodula sinal Bipolar (AMI).
    bit 0 quando nível é 0,
    bit 1 quando nível é diferente de 0 (positivo ou negativo).
    Retorna string de bits.
    """
    bits = []
    for level in signal:
        if level == 0:
            bits.append('0')
        else:
            bits.append('1')
    return ''.join(bits)


# Testes simples

if __name__ == "__main__":
    # Testes rápidos para verificar a correção

    # Exemplo NRZ (1,0,1,1,0)
    nrz_signal = [1, -1, 1, 1, -1]
    print("NRZ Demodulado:", decode_NRZ(nrz_signal))  # Esperado: 10110

    # Exemplo Manchester para bits 1010
    # codificado como (1, -1) = 1, (-1, 1) = 0
    manchester_signal = [1, -1, -1, 1, 1, -1, -1, 1]
    print("Manchester Demodulado:", decode_manchester(manchester_signal))  # Esperado: 1010

    # Exemplo Bipolar (AMI) para bits 101001
    bipolar_signal = [1, 0, -1, 0, 0, 1]
    print("Bipolar Demodulado:", decode_bipolar(bipolar_signal))  # Esperado: 101001
