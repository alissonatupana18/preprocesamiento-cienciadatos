import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def cargar_datos(ruta_archivo):
    """
    Carga los datos desde el archivo CSV
    """
    return pd.read_csv(ruta_archivo)

def limpiar_datos_faltantes(df):
    """
    Limpia los valores faltantes del DataFrame
    """
    # Rellenar valores numéricos faltantes con la media
    df_numerico = df.select_dtypes(include=[np.number])
    df[df_numerico.columns] = df_numerico.fillna(df_numerico.mean())
    
    # Rellenar valores categóricos faltantes con la moda
    df_categorico = df.select_dtypes(exclude=[np.number])
    df[df_categorico.columns] = df_categorico.fillna(df_categorico.mode().iloc[0])
    
    return df

def normalizar_datos(df):
    """
    Normaliza las columnas numéricas del DataFrame
    """
    scaler = StandardScaler()
    columnas_numericas = df.select_dtypes(include=[np.number]).columns
    df[columnas_numericas] = scaler.fit_transform(df[columnas_numericas])
    return df

def main():
    try:
        # Ejemplo de uso
        ruta_archivo = "datos/ejemplo.csv"
        
        # Cargar datos
        print("Cargando datos...")
        df = cargar_datos(ruta_archivo)
        
        # Limpiar datos faltantes
        print("Limpiando datos faltantes...")
        df = limpiar_datos_faltantes(df)
        
        # Normalizar datos
        print("Normalizando datos...")
        df = normalizar_datos(df)
        
        print("¡Preprocesamiento completado!")
        return df
        
    except Exception as e:
        print(f"Error durante el preprocesamiento: {str(e)}")
        return None

if __name__ == "__main__":
    main()