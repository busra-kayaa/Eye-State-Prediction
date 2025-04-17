import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("dataset.csv")

x = data.iloc[:, :3].values
y = data.iloc[:, 3:].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

model = MultiOutputClassifier(LogisticRegression())

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

acc_sol = accuracy_score(y_test[:, 0], y_pred[:, 0])
acc_sag = accuracy_score(y_test[:, 1], y_pred[:, 1])

print("\nLogistic Regression")
print(f"  sol_label doğruluğu: {acc_sol:.2f}")
print(f"  sag_label doğruluğu: {acc_sag:.2f}")

print("\nTahminler (test seti):")
print(y_pred)

print("\nGerçek Değerler (test seti):")
print(y_test)
