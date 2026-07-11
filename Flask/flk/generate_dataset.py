import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

data = pd.DataFrame({
    "cgpa": np.round(np.random.uniform(5.0, 10.0, n), 2),
    "num_skills": np.random.randint(0, 8, n),
    "num_languages": np.random.randint(1, 5, n),
    "internships": np.random.randint(0, 3, n),
    "backlogs": np.random.randint(0, 4, n),
    "communication_score": np.random.randint(1, 10, n),  
})

def placed(row):
    score = (row["cgpa"] * 1.5) + (row["num_skills"] * 1.2) + (row["internships"] * 2) \
            + (row["communication_score"] * 0.8) - (row["backlogs"] * 2.5)
    prob = 1 / (1 + np.exp(-(score - 20) / 5))  
    return np.random.binomial(1, prob)

data["placed"] = data.apply(placed, axis=1)

data.to_csv("placement_data.csv", index=False)
print(data["placed"].value_counts())
print("Dataset saved as placement_data.csv")