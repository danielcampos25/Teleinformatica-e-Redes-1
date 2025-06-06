import subprocess

def run_all():
    subprocess.run(['python3', '-m', 'CamadaFisica.ModulacaoBandaBase.plot_modulacao_banda_base'])
    subprocess.run(['python3', '-m', 'CamadaFisica.ModulacaoPortadora.plot_modulacao_portadora'])

if __name__ == "__main__":
    run_all()
