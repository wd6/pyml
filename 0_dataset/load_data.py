from sklearn import datasets

# regression dataset
boston = datasets.load_boston(return_X_y=True)

# binary classification dataset
cancer = datasets.load_breast_cancer(return_X_y=True)

# mutiple classification dataset
digits = datasets.load_digits(return_X_y=True)

