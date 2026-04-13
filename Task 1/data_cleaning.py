import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the dataset
df = pd.read_csv('Titanic-Dataset.csv')

# 1. Explore basic info
print("Dataset shape:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())

# 2. Handle missing values
# Age: fill with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Cabin: too many missing, drop the column
df.drop('Cabin', axis=1, inplace=True)

# Embarked: fill with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

print("\nAfter handling missing values:")
print(df.isnull().sum())

# 3. Convert categorical features to numerical
# Sex: male=0, female=1
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Embarked: S=0, C=1, Q=2
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Drop unnecessary columns: PassengerId, Name, Ticket
df.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)

print("\nData types after encoding:")
print(df.dtypes)

# 4. Normalize/standardize numerical features
# Numerical features: Age, Fare, SibSp, Parch
scaler = StandardScaler()
numerical_features = ['Age', 'Fare', 'SibSp', 'Parch']
df[numerical_features] = scaler.fit_transform(df[numerical_features])

print("\nNumerical features standardized.")

# 5. Visualize outliers using boxplots and remove them
# For Age, Fare
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

sns.boxplot(x=df['Age'], ax=axes[0])
axes[0].set_title('Age Boxplot')

sns.boxplot(x=df['Fare'], ax=axes[1])
axes[1].set_title('Fare Boxplot')

plt.savefig('outliers_before.png')
plt.close()

print("Outliers plot saved as outliers_before.png")

# Remove outliers using IQR
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

df = remove_outliers(df, 'Age')
df = remove_outliers(df, 'Fare')

print("\nDataset shape after removing outliers:", df.shape)

# Final dataset
print("\nFinal dataset head:")
print(df.head())

# Save the cleaned dataset
df.to_csv('Titanic-Cleaned.csv', index=False)
print("\nCleaned dataset saved as Titanic-Cleaned.csv")