import numpy as np
import torch


class AdamNumpy(object):
    def __init__(self, eta=0.01, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.momentum_dw, self.velocity_dw = 0, 0
        self.momentum_db, self.velocity_db = 0, 0
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.eta = eta

    def update(self, t, w, b, dw, db):
        ## dw, db are from current minibatch
        ## momentum beta 1
        # *** weights *** #
        self.momentum_dw = self.beta1 * self.momentum_dw + (1 - self.beta1) * dw
        # *** biases *** #
        self.momentum_db = self.beta1 * self.momentum_db + (1 - self.beta1) * db

        ## rms beta 2
        # *** weights *** #
        self.velocity_dw = self.beta2 * self.velocity_dw + (1 - self.beta2) * (dw**2)
        # *** biases *** #
        self.velocity_db = self.beta2 * self.velocity_db + (1 - self.beta2) * (db**2)

        ## bias correction
        momentum_dw_corr = self.momentum_dw / (1 - self.beta1**t)
        momentum_db_corr = self.momentum_db / (1 - self.beta1**t)
        velocity_dw_corr = self.velocity_dw / (1 - self.beta2**t)
        velocity_db_corr = self.velocity_db / (1 - self.beta2**t)

        ## update weights and biases
        w = w - self.eta * (
            momentum_dw_corr / (np.sqrt(velocity_dw_corr) + self.epsilon)
        )
        b = b - self.eta * (
            momentum_db_corr / (np.sqrt(velocity_db_corr) + self.epsilon)
        )

        return w, b


class AdamTorch(object):
    def __init__(self, eta=0.01, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.momentum_dw, self.velocity_dw = None, None
        self.momentum_db, self.velocity_db = torch.tensor(0.0), torch.tensor(0.0)
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.eta = eta

    def update(self, t, w, b, dw, db):
        if self.momentum_dw is None:
            self.momentum_dw = torch.zeros_like(w)
            self.velocity_dw = torch.zeros_like(w)

        ## dw, db are from current minibatch
        ## momentum beta 1
        # *** weights *** #
        self.momentum_dw = self.beta1 * self.momentum_dw + (1 - self.beta1) * dw
        self.momentum_db = self.beta1 * self.momentum_db + (1 - self.beta1) * db

        ## rms beta 2
        # *** weights *** #
        self.velocity_dw = self.beta2 * self.velocity_dw + (1 - self.beta2) * (dw ** 2)
        # *** biases *** #
        self.velocity_db = self.beta2 * self.velocity_db + (1 - self.beta2) * (db ** 2)

        ## bias correction
        momentum_dw_corr = self.momentum_dw / (1 - self.beta1 ** t)
        momentum_db_corr = self.momentum_db / (1 - self.beta1 ** t)
        velocity_dw_corr = self.velocity_dw / (1 - self.beta2 ** t)
        velocity_db_corr = self.velocity_db / (1 - self.beta2 ** t)
        
        ## update weights and biases
        w = w - self.eta * (
            momentum_dw_corr / (torch.sqrt(velocity_dw_corr) + self.epsilon)
        )
        b = b - self.eta * (
            momentum_db_corr / (torch.sqrt(velocity_db_corr) + self.epsilon)
        )

        return w, b


def model(w, b, x):
    return x @ w + b


def loss_function(y_true, y_pred):
    return (y_true - y_pred) ** 2


def grad_w(y_true, y_pred, x):
    return -2 * x.T @ (y_true - y_pred)


def grad_b(y_true, y_pred):
    return -2 * (y_true - y_pred).sum()


w_0 = torch.randn(100)
b_0 = torch.tensor(0.0)
adam = AdamTorch()
t = 1
x = torch.randn(10000, 100)   # Tensor 10000 rows, 100 columns
w_true = torch.ones(100) * 2  # Tensor 100x1 
b_true = torch.tensor(1.0)    # Tensor 1x1
y = x @ w_true + b_true

while True:
    y_pred = model(w_0, b_0, x)
    dw = grad_w(y, y_pred, x)
    db = grad_b(y, y_pred)
    w_0_old = w_0.clone()
    w_0, b_0 = adam.update(t, w=w_0, b=b_0, dw=dw, db=db)
    loss = loss_function(y, y_pred).mean()
    if t % 100 == 0:
        print(f"Iteration {t}: Loss = {loss:.6f}, Bias = {b_0:.6f}")
    if torch.allclose(w_0, w_0_old, atol=1e-6):
        print(
            f"Converged at iteration {t}: Loss = {loss:.6f}, Weight Mean = {w_0.mean():.6f}, Bias = {b_0:.6f}"
        )
        break
    t += 1

