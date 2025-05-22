# Predict Calorie Expenditure
## Playground Series - Season 5, Episode 5

**Predict Calorie Expenditure**

---

### Overview
Welcome to the 2025 Kaggle Playground Series! We plan to continue in the spirit of previous playgrounds, providing interesting and approachable datasets for our community to practice their machine learning skills, and anticipate a competition each month.

**Your Goal:** Your goal is to predict how many calories were burned during a workout.

* **Start:** 21 days ago
* **Close:** 10 days to go

---

### Evaluation
The evaluation metric for this competition is **Root Mean Squared Logarithmic Error (RMSLE)**.

The RMSLE is calculated as:

$$ \text{RMSLE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (\log(p_i + 1) - \log(a_i+1))^2} $$

where:
* $n$ is the total number of observations in the test set,
* $p_i$ is the predicted value of the target for instance (i),
* $a_i$ is the actual value of the target for instance (i), and,
* $\log$ is the natural logarithm.

---

### Submission File
For each `id` row in the test set, you must predict the continuous target, `Calories`. The file should contain a header and have the following format:

```csv
id,Calories
750000,93.27
50001,27.42
750002,103.8
etc.