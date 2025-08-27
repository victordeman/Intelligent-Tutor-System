from pyBKT.models import Model

def train_bkt(data):
    """Trains Bayesian Knowledge Tracing model."""
    model = Model()
    model.fit(data=data)
    return model

def predict_bkt(model, data):
    """Predicts learner knowledge states."""
    return model.predict(data)
