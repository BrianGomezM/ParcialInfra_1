def simulacion_secuencial(etapas, M):
    return sum(etapas.values()) * M

def simulacion_pipeline(etapas, M):
    etapa_lenta = max(etapas.values())
    K = len(etapas)
    return etapa_lenta * (K + M - 1)

def calcular_speedup(t_secuencial, t_pipeline):
    return t_secuencial / t_pipeline
