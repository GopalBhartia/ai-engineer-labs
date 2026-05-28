# Day 7 - ML Workflow Notes

## Supervised vs Unsupervised Learning

### 1. Supervised learning uses labeled data

Supervised learning is a machine learning approach where the model learns from examples that already have correct answers.

Example:

text Input: "This product is amazing" Label: positive 

The model learns the relationship between the input and the correct output.

---

### 2. Unsupervised learning uses unlabeled data

Unsupervised learning is a machine learning approach where the model gets data without correct answers.

Example:

text Customer A buys laptop, mouse, keyboard Customer B buys shoes, jacket, watch Customer C buys laptop, monitor, keyboard 

The model tries to find hidden patterns or groups on its own.

---

### 3. Main goal of supervised learning

The goal of supervised learning is prediction.

The model learns from past labeled examples so it can predict labels for new unseen examples.

Examples:

- Predict whether an email is spam or not spam
- Predict whether a review is positive or negative
- Predict house prices
- Predict whether a transaction is fraudulent

---

### 4. Main goal of unsupervised learning

The goal of unsupervised learning is pattern discovery.

The model is not told the correct answer. It tries to discover structure in the data.

Examples:

- Group similar customers together
- Find topics in a collection of documents
- Detect unusual behavior
- Reduce many features into fewer important dimensions

---

### 5. Supervised learning has clearer evaluation

Supervised learning is usually easier to evaluate because we have true labels.

If the model predicts:

text positive 

and the actual label is:

text positive 

then the prediction is correct.

Common supervised learning metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Mean squared error for regression

---

### 6. Unsupervised learning is harder to evaluate

Unsupervised learning is harder to evaluate because there are usually no correct labels.

For example, if a clustering algorithm groups customers into 3 groups, we may not immediately know whether those groups are correct.

Evaluation often depends on:

- Business usefulness
- Human inspection
- Cluster quality metrics
- Whether the discovered patterns are actionable

---

### 7. Classification and regression are supervised learning tasks

Supervised learning has two common task types.

Classification predicts a category.

Examples:

text spam or not spam positive or negative fraud or not fraud 

Regression predicts a number.

Examples:

text house price salary temperature sales revenue 

---

### 8. Clustering and dimensionality reduction are unsupervised learning tasks

Unsupervised learning has common task types like clustering and dimensionality reduction.

Clustering means grouping similar data points.

Example:

text Group customers based on buying behavior 

Dimensionality reduction means reducing the number of features while keeping important information.

Example:

text Compress 500 features into 2 or 3 important dimensions for visualization 

---

### 9. Supervised learning needs labeled data, which can be expensive

Supervised learning can be powerful, but it needs labeled examples.

Creating labels may require humans, time, and money.

Example:

For sentiment analysis, someone may need to label thousands of reviews as:

text positive negative neutral 

This is why labeled datasets are valuable.

---

### 10. Unsupervised learning is useful when labels are not available

Unsupervised learning is useful when we have lots of data but no labels.

It can help explore data before building a supervised model.

Example:

A company may not know customer segments in advance. Unsupervised learning can group customers into segments such as:

text budget buyers premium buyers frequent buyers one-time buyers 

These groups can later be used for marketing, recommendations, or further supervised modeling.

---

## Quick Comparison Table

| Topic | Supervised Learning | Unsupervised Learning |
|---|---|---|
| Data type | Labeled data | Unlabeled data |
| Goal | Predict correct output | Discover hidden patterns |
| Output | Class or number | Groups, topics, compressed features |
| Examples | Classification, regression | Clustering, dimensionality reduction |
| Evaluation | Easier because true labels exist | Harder because no fixed answer |
| Common metrics | Accuracy, precision, recall, F1-score, MSE | Silhouette score, human review, business usefulness |
| Use cases | Spam detection, sentiment analysis, fraud detection | Customer segmentation, topic discovery, anomaly detection |

---

## Simple Interview Answer

Supervised learning is used when we have labeled data and want the model to predict an output, such as a class or a number. Examples include spam detection, sentiment analysis, fraud detection, and house price prediction.

Unsupervised learning is used when we do not have labeled data and want the model to discover hidden patterns. Examples include customer segmentation, topic discovery, anomaly detection, and dimensionality reduction.

The main difference is that supervised learning learns from correct answers, while unsupervised learning tries to find structure without correct answers.