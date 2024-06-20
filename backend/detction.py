import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies():
    data = pd.read_csv('gaia_data.csv')
    df_cleaned = data.dropna(subset=['phot_g_mean_mag'])
    df_normalized = (df_cleaned - df_cleaned.mean()) / df_cleaned.std()
    
    model = IsolationForest(contamination=0.01)
    anomalies = model.fit_predict(df_normalized[['phot_g_mean_mag', 'bp_rp']])
    df_cleaned['anomaly'] = anomalies
    anomalies_detected = df_cleaned[df_cleaned['anomaly'] == -1]
    
    anomalies_detected.to_csv('anomalies.csv', index=False)
    return anomalies_detected.to_dict(orient='records')
