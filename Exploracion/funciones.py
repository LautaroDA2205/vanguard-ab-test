
import pandas as pd
import scipy.stats as st

def valida_segmento(df_segmento, ranking, nombre):
    """
    Realiza un test de hipótesis (t-test) para comparar la tasa de conversión
    entre el grupo Control y Test de un segmento dado.
    
    Args:
        df_segmento (pd.DataFrame): DataFrame filtrado con los datos del segmento.
        ranking (int): Número para ordenar la salida.
        nombre (str): Nombre descriptivo del segmento.
    """
    if len(df_segmento) < 10: return
    
    control = df_segmento[df_segmento["experiment_group"] == "Control"]["converted"]
    test = df_segmento[df_segmento["experiment_group"] == "Test"]["converted"]
    
    # Test de hipótesis (alternative='greater' porque queremos saber si Test > Control)
    stat, p = st.ttest_ind(test, control, equal_var=False, alternative='greater')
    
    decision = "Aceptamos H1" if p < 0.05 else "Aceptamos H0"
    print(f"Top {ranking} | {nombre:<25} | Control: {control.mean():.1%} -> Test: {test.mean():.1%} | P-Value: {p:.5f} | {decision}")


