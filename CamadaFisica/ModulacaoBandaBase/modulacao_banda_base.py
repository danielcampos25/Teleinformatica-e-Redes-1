# modulacao_banda_base.py - Modulação de Banda Base - Camada Física
#As funções recebem um trem de bits (na forma de string) e retorna uma lista de floats do sinal codificado

# Codificação Non-return to Zero Polar (NRZ-Polar);
def encode_NRZ(bits: str) -> list[float]:
    """
    NRZ Polar: 1 → +1, 0 → -1
    """
    signal = []
    for bit in bits:
        if bit == '1':
            signal.append(1.0)
        else:
            signal.append(-1.0)
    return signal

#Codificação Manchester - De acordo com o slide de aula (G.E Thomas)
def encode_manchester(bits: str) -> list[float]: #Obs: usamos float para facilitar o uso das bibliotecas para plotar
    """
    Manchester: 
    - 0 → [-1, 1]
    - 1 → [1, -1]
    """
    signal = []
    for bit in bits:
        if bit == '1':
            signal.extend([1.0, -1.0])
        else:
            signal.extend([-1.0, 1.0])
    return signal


def encode_bipolar(bits: str) -> list[float]:
    """
    Bipolar (AMI): 
    - 0 → 0
    - 1 → alterna entre +1 e -1
    """
    signal = []
    nivel = 1.0  # Começa com +1
    for bit in bits:
        if bit == '0':
            signal.append(0.0)
        else:
            signal.append(nivel)
            nivel *= -1  # Alterna o nível
    return signal
