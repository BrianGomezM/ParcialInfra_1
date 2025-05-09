from utils import cargar_configuracion
from pipeline import simulacion_secuencial, simulacion_pipeline, calcular_speedup
import matplotlib.pyplot as plt

def ejecutar_simulacion(M_list, config_path):
    etapas = cargar_configuracion(config_path)
    config_name = config_path.split(".")[0]
    print(f"\nConfiguración: {config_name}")
    print(f"{'M':<10} {'T_Secuencial':<15} {'T_Pipeline':<15} {'Speedup':<10}")
    
    resultados = []
    for M in M_list:
        t_sec = simulacion_secuencial(etapas, M)
        t_pipe = simulacion_pipeline(etapas, M)
        speedup = calcular_speedup(t_sec, t_pipe)
        resultados.append([config_name, M, t_sec, t_pipe, round(speedup, 2)])
        print(f"{M:<10} {t_sec:<15} {t_pipe:<15} {round(speedup, 2):<10}")
    
    return resultados

if __name__ == "__main__":
    M_list = [5, 10, 20]
    configuraciones = ["config_1.json", "config_2.json", "config_3.json", "config_4.json", "config_5.json", "config_6.json", "config_7.json", "config_8.json", "config_9.json", "config_10.json"]
    todos_resultados = []
    
    for config in configuraciones:
        resultados = ejecutar_simulacion(M_list, config)
        todos_resultados.extend(resultados)
    
    # Preparamos los datos para la gráfica
    etapas = list(range(1, len(configuraciones) + 1))
    
    # Graficamos los speedups para cada valor de M
    plt.figure(figsize=(10, 6))
    
    for M in M_list:
        speedups = [r[4] for r in todos_resultados if r[1] == M]
        plt.plot(etapas, speedups, marker='o', linestyle='-', label=f'M = {M}')
    
    plt.title("Evolución del Speedup con diferentes valores de M")
    plt.xlabel("Número de etapas del pipeline")
    plt.ylabel("Speedup")
    plt.grid(True)
    plt.xticks(etapas)
    plt.legend(title="Valor de M")
    plt.tight_layout()
    plt.show()
