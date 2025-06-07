#demodulacao_portadora.py

from CamadaFisica.ModulacaoPortadora.modulacao_portadora import encode_8QAM
import numpy as np


#Obs: atentar para o sample_rate, que na demodulação deve ter a mesma taxa da respectiva modulação
def decode_ASK(signal, freq=5, sample_rate=100):
    """
    Demodula um sinal ASK e retorna a sequência de bits.
    """
    bit_duration = sample_rate
    num_bits = len(signal) // bit_duration
    bits = []

    for i in range(num_bits):
        segment = signal[i * bit_duration : (i + 1) * bit_duration]
        # Calcula a energia (ou potência) do sinal no segmento
        energy = np.sum(segment ** 2)

        # Limiar simples: se há energia, assume que é '1'; se não, '0'
        bit = '1' if energy > 0.1 else '0'
        bits.append(bit)

    return ''.join(bits)
# teste
# bits = "10101"
# sinal = encode_ASK(bits)
# recuperado = decode_ASK(sinal)
# print(recuperado)  # Deve imprimir: 10101 -->passou!


def decode_FSK(signal, freq0=3, freq1=7, sample_rate=100):
    """
    Demodula um sinal FSK e retorna a sequência de bits.
    """
    bit_duration = sample_rate
    num_bits = len(signal) // bit_duration
    bits = []

    # Geração das senóides de referência para correlação
    t = np.linspace(0, 1, sample_rate, endpoint=False)
    ref_wave0 = np.sin(2 * np.pi * freq0 * t)
    ref_wave1 = np.sin(2 * np.pi * freq1 * t)

    for i in range(num_bits):
        segment = signal[i * bit_duration : (i + 1) * bit_duration]
        
        # Correlação com cada onda de referência (detecção por energia)
        corr0 = np.dot(segment, ref_wave0)
        corr1 = np.dot(segment, ref_wave1)

        # Decide qual frequência predominou
        bit = '0' if abs(corr0) > abs(corr1) else '1'
        bits.append(bit)

    return ''.join(bits)

#pequeno teste
# bits = "10101"
# sinal = encode_FSK(bits)
# recuperado = decode_FSK(sinal)
# print(recuperado)  # Deve imprimir: 10101 --> passou



def decode_8QAM(signal,original_length=None, sample_rate=100): #por default tanto o encode qnt o decode tem sample_size = 100, devem ter valores iguais 
    symbol_size = sample_rate
    t = np.linspace(0, 1, sample_rate, endpoint=False)
    freq = 5
    cos_ref = np.cos(2 * np.pi * freq * t)
    sin_ref = -np.sin(2 * np.pi * freq * t)  # Note o sinal negativo para corresponder à fórmula de modulação

    symbols = []
    for i in range(0, len(signal), symbol_size):
        segment = signal[i:i+symbol_size]
        I = 2 * np.dot(segment, cos_ref) / sample_rate  # Fator 2 para compensar a energia
        Q = 2 * np.dot(segment, sin_ref) / sample_rate
        symbols.append((I, Q))

    # Mesmo mapeamento usado no encode
    mapping = {
        '000': (1, 0), '001': (0, 1),
        '010': (-1, 0), '011': (0, -1),
        '100': (2, 0), '101': (0, 2),
        '110': (-2, 0), '111': (0, -2),
    }

    # Inverter o dicionário
    reverse_mapping = {v: k for k, v in mapping.items()}

    # Função de quantização melhorada
    def quantize(val):
        thresholds = [-1.5, -0.75, 0.75, 1.5]
        if val < thresholds[0]:
            return -2
        elif val < thresholds[1]:
            return -1
        elif val < thresholds[2]:
            return 0
        elif val < thresholds[3]:
            return 1
        else:
            return 2

    bits = ''
    for I, Q in symbols:
        I_q = quantize(I)
        Q_q = quantize(Q)
        bits += reverse_mapping.get((I_q, Q_q), '000')  # Default para '000' se não encontrar

    if original_length is not None:
        bits = bits[:original_length]  # Corta os bits extras
    return bits





