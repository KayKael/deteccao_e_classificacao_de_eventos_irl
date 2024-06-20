# deteccao_e_classificacao_de_eventos_irl

## Overview

Welcome to the Deteccao e Classificacao de Eventos IRL! This project leverages state-of-the-art machine learning techniques to detect and classify astronomical events using real data from the Gaia mission. It provides a user-friendly interface to interact with detected events in real-time.

This project demonstrates my skills in:

- Artificial Intelligence and Machine Learning
- Data Analysis and Manipulation
- API Development with Flask
- Real-time Data Processing with WebSockets
- Frontend Development with React
- Containerization with Docker

## Features

- **Data Fetching**: Retrieves real astronomical data from the Gaia mission.
- **Anomaly Detection**: Uses Isolation Forest to identify potential astronomical events.
- **Event Classification**: Classifies detected events using a neural network.
- **Real-time Notifications**: Utilizes WebSockets to notify users of new events in real-time.
- **Interactive Frontend**: React-based UI for easy interaction with detected events.

## Project Structure

deteccao_e_classificacao_de_eventos_irl/
├── backend/
│ ├── Dockerfile
│ ├── requirements.txt
│ ├── app.py
│ ├── data_fetch.py
│ ├── detection.py
│ ├── classification.py
│ └── notification.py
├── frontend/
│ ├── Dockerfile
│ ├── package.json
│ ├── public/
│ │ └── index.html
│ └── src/
│ ├── App.js
│ ├── index.js
│ └── components/
│ ├── EventList.js
│ └── Notification.js
└── docker-compose.yml


## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/deteccao_e_classificacao_de_eventos_irl.git
   cd deteccao_e_classificacao_de_eventos_irl
2. **Build and run the Docker containers:**
   ```sh
  docker-compose up --build
3. **Access Frontend:**
  
