import argparse
import pickle
import numpy as np

def load_model(model_file):
    with open(model_file, 'rb') as f:
        model = pickle.load(f)
        return model

def predict_single_sample(model, features):
    predicted_prob = model.predict(features, num_iteration=model.best_iteration)
    predicted_label = 1 if predicted_prob > 0.5 else 0
    return predicted_label, predicted_prob

def main():
    parser = argparse.ArgumentParser(description="Load pickle model and make predictions")
    parser.add_argument("model_file", type=str, help="Path to the pickled model")
    parser.add_argument("features", type=float, nargs="+",help="Features for predictino")

    args = parser.parse_args()

    model = load_model(args.model_file)
    features = np.array(args.features).reshape(1, -1)

    predicted_label, predicted_prob = predict_single_sample(model, features)

    print("Predicted probability:", predicted_prob)
    print("Predicted Label", predicted_label)

if __name__ == "__main__":
    main()
