import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def classify_events():
    data = pd.read_csv('anomalies.csv')
    df_normalized = (data[['phot_g_mean_mag', 'bp_rp']] - data[['phot_g_mean_mag', 'bp_rp']].mean()) / data[['phot_g_mean_mag', 'bp_rp']].std()
    
    X_train = df_normalized
    y_train = (data['anomaly'] == -1).astype(int)
    
    model = Sequential([
        Dense(64, activation='relu', input_shape=(2,)),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    model.fit(X_train, y_train, epochs=10, batch_size=32)
    
    predictions = model.predict(X_train)
    data['classification'] = predictions
    
    data.to_csv('classified_events.csv', index=False)
    return data.to_dict(orient='records')
