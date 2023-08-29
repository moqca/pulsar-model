# Pulsar Star Classification Model

This repository contains a trained machine learning model to predict whether a star is a pulsar or not based on certain features. The model is intended to be used within a Docker container.

## Prerequisites

- Docker installed on your local machine

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/pulsar-star-classification.git
```

1. Navigate to the project directory:

```bash
cd pulsar-star-classification
```

2. Build the Docker Image
```bash
docker build -t pulsar-prediction .
```

3. Run the Docker container:
```bash
docker run pulsar-predictor model.pkl 0.685166 0.398257 0.186306 0.021399 0.009040 0.059088 0.358474 0.122370

```

