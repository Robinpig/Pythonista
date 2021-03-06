import numpy as np


# 最小二乘法实现线性回归
class OLSLinearRegression:
    def _ols(self, X, y):
        '最小二乘法估算w'
        return np.linalg.inv(X.T @ X) @ X.T @ y

    def _preprocess_data_X(self, X):
        '数据预处理'
        # 扩展X，添加x0列并设置为1
        m, n = X.shape
        X_ = np.empty((m, n + 1))
        X_[:, 0] = 1
        X_[:, 1:] = X
        return X_

    def train(self, X_train, y_train):
        '训练模型'
        # 预处理X_train(添加x0=1)
        X_train = self._preprocess_data_X(X_train)
        # 使用最小二乘法估算w
        self.w = self._ols(X_train, y_train)

    def predict(self, X):
        '预测'
        # 预处理X_train(添加x0=1)
        X = self._preprocess_data_X(X)
        return np.matmul(X, self.w)
