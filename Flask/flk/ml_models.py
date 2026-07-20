from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np

X = np.array([
    [5.0], [5.2], [5.5], [5.8],
    [6.0], [6.2], [6.5], [6.8],
    [7.0], [7.2], [7.5], [7.8],
    [8.0], [8.2], [8.5], [8.8],
    [9.0], [9.2], [9.5], [9.8]
])
y = np.array([
    0, 0, 0, 0,
    0, 0, 1, 1,
    1, 1, 1, 1,
    1, 1, 1, 1,
    1, 1, 1, 1
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

models = {
    "logistic_regression": LogisticRegression(),
    "random_forest": RandomForestClassifier(n_estimators=10, random_state=42),
    "svm": SVC(probability=True),
    "decision_tree": DecisionTreeClassifier(random_state=42),
    "knn": KNeighborsClassifier(n_neighbors=3),
    "naive_bayes": GaussianNB(),
}

model_accuracies = {}

for name, m in models.items():
    m.fit(X_train, y_train)
    preds = m.predict(X_test)
    acc = round(accuracy_score(y_test, preds) * 100, 2)
    model_accuracies[name] = acc

model_display_names = {
    "logistic_regression": "Logistic Regression",
    "random_forest": "Random Forest",
    "svm": "Support Vector Machine",
    "decision_tree": "Decision Tree",
    "knn": "K-Nearest Neighbors",
    "naive_bayes": "Naive Bayes",
}

# ---- Linear Regression: CGPA -> Expected Package (LPA) ----
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
X_reg = np.array([
    [5.0], [5.5], [6.0], [6.5],
    [7.0], [7.5], [8.0], [8.5],
    [9.0], [9.5]
])
y_reg = np.array([
    2.5, 3.0, 3.5, 4.2,
    5.0, 6.0, 7.2, 8.5,
    10.0, 12.0
])

linear_model = LinearRegression()
linear_model.fit(X_reg, y_reg)
y_reg_pred = linear_model.predict(X_reg)
linear_r2 = round(r2_score(y_reg, y_reg_pred), 3)