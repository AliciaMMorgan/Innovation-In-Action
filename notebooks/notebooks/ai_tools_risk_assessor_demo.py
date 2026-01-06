# AI Tools Risk Assessor Comparison Demo
# This script uses the ai_tools_risk_assessor_comparison.csv to create simple views for PM decision-making

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv('ai_tools_risk_assessor_comparison.csv')
print("First 5 rows:")
print(df.head())

# Map Compliance Focus to numbers
compliance_map = {
    'Very High': 3,
    'High': 2,
    'Medium': 1,
    'Low-Medium': 1.5
}

df['compliance_score'] = df['Compliance Focus'].map(compliance_map)

# Show ranking
print("\\nCompliance Score Ranking:")
print(df[['dimension', 'Claude', 'ChatGPT', 'Perplexity', 'Gemini', 'Copilot']].head(1))
print(df['compliance_score'].sort_values(ascending=False))

# Bar chart
plt.bar(df.index, df['compliance_score'])
plt.title('Compliance Score by AI Tool')
plt.ylabel('Score')
plt.show()
