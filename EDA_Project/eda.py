# ============================================================================
# EXPLORATORY DATA ANALYSIS (EDA) - TITANIC DATASET
# ============================================================================
# Project: Titanic Dataset Analysis
# Objective: Comprehensive Exploratory Data Analysis to understand patterns
# Date: 2026
# Author: Data Science Analyst
# ============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style for visualizations
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ============================================================================
# SECTION 1: LOAD DATASET
# ============================================================================

print("=" * 80)
print("SECTION 1: LOADING DATASET")
print("=" * 80)

# Load the dataset
df = pd.read_csv('Titanic-Dataset.csv')

# Display basic information
print("\n1.1 First 5 rows of the dataset:")
print(df.head())

print("\n1.2 Dataset Info:")
print(df.info())

# ============================================================================
# SECTION 2: DATA UNDERSTANDING
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 2: DATA UNDERSTANDING")
print("=" * 80)

print(f"\n2.1 Shape of Dataset: {df.shape}")
print(f"    - Rows (Passengers): {df.shape[0]}")
print(f"    - Columns (Features): {df.shape[1]}")

print("\n2.2 Column Names:")
print(df.columns.tolist())

print("\n2.3 Data Types:")
print(df.dtypes)

print("\n2.4 Missing Values:")
missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing_Count': missing,
    'Percentage': missing_percent
})
print(missing_df[missing_df['Missing_Count'] > 0])

print("\n2.5 Unique Values per Column:")
unique_counts = df.nunique()
print(unique_counts)

# ============================================================================
# SECTION 3: SUMMARY STATISTICS
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 3: SUMMARY STATISTICS")
print("=" * 80)

print("\n3.1 Descriptive Statistics using df.describe():")
print(df.describe())

print("\n3.2 Mean Values:")
print(df.mean(numeric_only=True))

print("\n3.3 Median Values:")
print(df.median(numeric_only=True))

print("\n3.4 Standard Deviation:")
print(df.std(numeric_only=True))

print("\n3.5 Percentiles (25%, 50%, 75%):")
print(df.quantile([0.25, 0.5, 0.75]))

# ============================================================================
# SECTION 4: DATA CLEANING
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 4: DATA CLEANING")
print("=" * 80)

# Create a copy for cleaning
df_clean = df.copy()

print(f"\n4.1 Initial duplicate rows: {df_clean.duplicated().sum()}")

# Remove duplicates
df_clean = df_clean.drop_duplicates()
print(f"4.2 Duplicates after removal: {df_clean.duplicated().sum()}")

# Handle missing values
print("\n4.3 Handling Missing Values:")
print(f"    - Age missing: {df_clean['Age'].isnull().sum()}")
print(f"    - Cabin missing: {df_clean['Cabin'].isnull().sum()}")
print(f"    - Embarked missing: {df_clean['Embarked'].isnull().sum()}")

# Fill Age with median
df_clean['Age'].fillna(df_clean['Age'].median(), inplace=True)
print(f"    - Age filled with median: {df_clean['Age'].isnull().sum()}")

# Fill Embarked with mode
df_clean['Embarked'].fillna(df_clean['Embarked'].mode()[0], inplace=True)
print(f"    - Embarked filled with mode: {df_clean['Embarked'].isnull().sum()}")

# Drop Cabin (too many missing)
df_clean.drop('Cabin', axis=1, inplace=True)
print(f"    - Cabin column dropped")

print(f"\n4.4 Final missing values:\n{df_clean.isnull().sum().sum()} total missing values")

print(f"\n4.5 Dataset shape after cleaning: {df_clean.shape}")

# ============================================================================
# SECTION 5: DATA VISUALIZATION
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 5: DATA VISUALIZATION")
print("=" * 80)

# Create figure for histograms
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Distribution Analysis', fontsize=16, fontweight='bold')

# 5.1 Age Distribution Histogram
print("\n5.1 Creating Age Distribution Histogram...")
axes[0].hist(df_clean['Age'], bins=30, color='steelblue', edgecolor='black', alpha=0.7)
axes[0].set_xlabel('Age (years)', fontsize=11, fontweight='bold')
axes[0].set_ylabel('Frequency', fontsize=11, fontweight='bold')
axes[0].set_title('Age Distribution', fontsize=12, fontweight='bold')
axes[0].grid(axis='y', alpha=0.3)

# Add statistics text
age_mean = df_clean['Age'].mean()
age_median = df_clean['Age'].median()
axes[0].axvline(age_mean, color='red', linestyle='--', linewidth=2, label=f'Mean: {age_mean:.1f}')
axes[0].axvline(age_median, color='green', linestyle='--', linewidth=2, label=f'Median: {age_median:.1f}')
axes[0].legend()

# 5.2 Fare Distribution Histogram
print("5.2 Creating Fare Distribution Histogram...")
axes[1].hist(df_clean['Fare'], bins=30, color='coral', edgecolor='black', alpha=0.7)
axes[1].set_xlabel('Fare ($)', fontsize=11, fontweight='bold')
axes[1].set_ylabel('Frequency', fontsize=11, fontweight='bold')
axes[1].set_title('Fare Distribution', fontsize=12, fontweight='bold')
axes[1].grid(axis='y', alpha=0.3)

# Add statistics text
fare_mean = df_clean['Fare'].mean()
fare_median = df_clean['Fare'].median()
axes[1].axvline(fare_mean, color='red', linestyle='--', linewidth=2, label=f'Mean: {fare_mean:.2f}')
axes[1].axvline(fare_median, color='green', linestyle='--', linewidth=2, label=f'Median: {fare_median:.2f}')
axes[1].legend()

plt.tight_layout()
plt.savefig('histograms.png', dpi=300, bbox_inches='tight')
print("   ✓ Histogram saved as 'histograms.png'")
plt.show()

# 5.3 Boxplots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Boxplot Analysis', fontsize=16, fontweight='bold')

print("\n5.3 Creating Age vs Survival Boxplot...")
df_clean.boxplot(column='Age', by='Survived', ax=axes[0])
axes[0].set_xlabel('Survived (0=No, 1=Yes)', fontsize=11, fontweight='bold')
axes[0].set_ylabel('Age (years)', fontsize=11, fontweight='bold')
axes[0].set_title('Age Distribution by Survival Status', fontsize=12, fontweight='bold')
plt.sca(axes[0])
plt.xticks([1, 2], ['Did Not Survive', 'Survived'])

print("5.4 Creating Fare vs Class Boxplot...")
df_clean.boxplot(column='Fare', by='Pclass', ax=axes[1])
axes[1].set_xlabel('Passenger Class', fontsize=11, fontweight='bold')
axes[1].set_ylabel('Fare ($)', fontsize=11, fontweight='bold')
axes[1].set_title('Fare Distribution by Passenger Class', fontsize=12, fontweight='bold')
plt.sca(axes[1])
plt.xticks([1, 2, 3], ['1st Class', '2nd Class', '3rd Class'])

plt.tight_layout()
plt.savefig('boxplots.png', dpi=300, bbox_inches='tight')
print("   ✓ Boxplots saved as 'boxplots.png'")
plt.show()

# 5.5 Countplots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Categorical Distribution Analysis', fontsize=16, fontweight='bold')

print("\n5.5 Creating Gender vs Survival Countplot...")
sex_survived = pd.crosstab(df_clean['Sex'], df_clean['Survived'])
sex_survived.plot(kind='bar', ax=axes[0], color=['#d62728', '#2ca02c'])
axes[0].set_xlabel('Gender', fontsize=11, fontweight='bold')
axes[0].set_ylabel('Count', fontsize=11, fontweight='bold')
axes[0].set_title('Gender Distribution by Survival Status', fontsize=12, fontweight='bold')
axes[0].legend(['Did Not Survive', 'Survived'], loc='upper right')
plt.setp(axes[0].xaxis.get_majorticklabels(), rotation=0)

print("5.6 Creating Passenger Class Distribution...")
pclass_counts = df_clean['Pclass'].value_counts().sort_index()
axes[1].bar(pclass_counts.index, pclass_counts.values, color=['#1f77b4', '#ff7f0e', '#2ca02c'], edgecolor='black')
axes[1].set_xlabel('Passenger Class', fontsize=11, fontweight='bold')
axes[1].set_ylabel('Count', fontsize=11, fontweight='bold')
axes[1].set_title('Passenger Class Distribution', fontsize=12, fontweight='bold')
axes[1].set_xticks([1, 2, 3])
axes[1].set_xticklabels(['1st Class', '2nd Class', '3rd Class'])

for i, v in enumerate(pclass_counts.values):
    axes[1].text(pclass_counts.index[i], v + 5, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('countplots.png', dpi=300, bbox_inches='tight')
print("   ✓ Countplots saved as 'countplots.png'")
plt.show()

# 5.7 Correlation Matrix Heatmap
print("\n5.7 Creating Correlation Matrix Heatmap...")
numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
correlation_matrix = df_clean[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            fmt='.2f', square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix - Titanic Dataset', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("   ✓ Correlation heatmap saved as 'correlation_heatmap.png'")
plt.show()

# 5.8 Pairplot (Feature Relationships)
print("\n5.8 Creating Pairplot (Feature Relationships)...")
print("   Note: This may take a moment...")
# Select numeric columns for pairplot
numeric_cols_for_pair = ['Age', 'Fare', 'Pclass', 'Survived']
pairplot_data = df_clean[numeric_cols_for_pair].copy()
pairplot = sns.pairplot(pairplot_data, diag_kind='kde', plot_kws={'alpha': 0.6})
pairplot.fig.suptitle('Pairplot - Feature Relationships', fontsize=14, fontweight='bold', y=1.001)
plt.savefig('pairplot.png', dpi=300, bbox_inches='tight')
print("   ✓ Pairplot saved as 'pairplot.png'")
plt.show()

# ============================================================================
# SECTION 6: PATTERN DETECTION & ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 6: PATTERN DETECTION & ANALYSIS")
print("=" * 80)

print("\n6.1 SURVIVAL ANALYSIS:")
survival_rate = (df_clean['Survived'].sum() / len(df_clean)) * 100
print(f"   - Overall survival rate: {survival_rate:.2f}%")
print(f"   - Survived: {df_clean['Survived'].sum()} passengers")
print(f"   - Did not survive: {(df_clean['Survived'] == 0).sum()} passengers")

print("\n6.2 GENDER-BASED SURVIVAL:")
gender_survival = pd.crosstab(df_clean['Sex'], df_clean['Survived'], margins=True)
print(gender_survival)
female_survival = (df_clean[df_clean['Sex'] == 'female']['Survived'].sum() / 
                   len(df_clean[df_clean['Sex'] == 'female'])) * 100
male_survival = (df_clean[df_clean['Sex'] == 'male']['Survived'].sum() / 
                 len(df_clean[df_clean['Sex'] == 'male'])) * 100
print(f"   - Female survival rate: {female_survival:.2f}%")
print(f"   - Male survival rate: {male_survival:.2f}%")
print(f"   - Observation: Women had significantly higher survival rates (likely 'women and children first' policy)")

print("\n6.3 CLASS-BASED SURVIVAL:")
class_survival = pd.crosstab(df_clean['Pclass'], df_clean['Survived'], margins=True)
print(class_survival)
for pclass in [1, 2, 3]:
    surv_rate = (df_clean[df_clean['Pclass'] == pclass]['Survived'].sum() / 
                 len(df_clean[df_clean['Pclass'] == pclass])) * 100
    print(f"   - Class {pclass} survival rate: {surv_rate:.2f}%")
print(f"   - Observation: Higher class passengers had better survival chances")

print("\n6.4 AGE-BASED SURVIVAL:")
print("   - Age statistics for survivors:")
print(df_clean[df_clean['Survived'] == 1]['Age'].describe())
print("   - Age statistics for non-survivors:")
print(df_clean[df_clean['Survived'] == 0]['Age'].describe())
print(f"   - Observation: Children and younger passengers had higher survival rates")

print("\n6.5 OUTLIER DETECTION (Age):")
Q1_age = df_clean['Age'].quantile(0.25)
Q3_age = df_clean['Age'].quantile(0.75)
IQR_age = Q3_age - Q1_age
outliers_age = df_clean[(df_clean['Age'] < Q1_age - 1.5*IQR_age) | 
                        (df_clean['Age'] > Q3_age + 1.5*IQR_age)]
print(f"   - Outliers in Age: {len(outliers_age)} ({(len(outliers_age)/len(df_clean)*100):.2f}%)")

print("\n6.6 OUTLIER DETECTION (Fare):")
Q1_fare = df_clean['Fare'].quantile(0.25)
Q3_fare = df_clean['Fare'].quantile(0.75)
IQR_fare = Q3_fare - Q1_fare
outliers_fare = df_clean[(df_clean['Fare'] < Q1_fare - 1.5*IQR_fare) | 
                         (df_clean['Fare'] > Q3_fare + 1.5*IQR_fare)]
print(f"   - Outliers in Fare: {len(outliers_fare)} ({(len(outliers_fare)/len(df_clean)*100):.2f}%)")
print(f"   - Observation: High-fare passengers were outliers, likely luxury travelers")

print("\n6.7 CORRELATION INSIGHTS:")
print(f"   - Survived vs Pclass correlation: {correlation_matrix.loc['Survived', 'Pclass']:.3f}")
print(f"   - Survived vs Age correlation: {correlation_matrix.loc['Survived', 'Age']:.3f}")
print(f"   - Survived vs Fare correlation: {correlation_matrix.loc['Survived', 'Fare']:.3f}")
print(f"   - Observation: Negative correlation with Pclass (higher class = lower number = better survival)")

print("\n6.8 EMBARKED PORT ANALYSIS:")
embarked_counts = df_clean['Embarked'].value_counts()
print(embarked_counts)
print(f"   - Port S (Southampton) had most passengers: {embarked_counts['S']} ({embarked_counts['S']/len(df_clean)*100:.1f}%)")

# ============================================================================
# SECTION 7: FINAL SUMMARY & CONCLUSIONS
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 7: KEY FINDINGS & CONCLUSIONS")
print("=" * 80)

print("""
KEY OBSERVATIONS:

1. SURVIVAL FACTORS:
   ✓ Gender: "Women and children first" policy clearly observed
   ✓ Class: First class had best survival rate (~62%)
   ✓ Age: Younger passengers had higher survival chances
   
2. DATA CHARACTERISTICS:
   ✓ Dataset contains 891 passengers with 11 features
   ✓ Age and Cabin had significant missing values
   ✓ Fare distribution is right-skewed with premium prices for 1st class
   
3. NOTABLE PATTERNS:
   ✓ Strong socioeconomic factor: Class and Fare strongly correlate with survival
   ✓ Gender was primary survival predictor
   ✓ Outliers exist in fare prices (luxury travel)
   
4. CHALLENGES IDENTIFIED:
   ✓ Missing data in Age, Cabin, and Embarked columns
   ✓ Class imbalance in survival outcomes
   ✓ Categorical variables require encoding for ML models
   
5. RECOMMENDATIONS FOR MODELING:
   ✓ Engineer features from Name (titles), Age groups
   ✓ Create family size features from SibSp and Parch
   ✓ Use class-weighted models due to imbalance
   ✓ Feature selection based on correlation analysis
""")

print("=" * 80)
print("EDA ANALYSIS COMPLETE")
print("=" * 80)
