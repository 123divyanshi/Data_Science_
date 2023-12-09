#ASSOCIATION RULES
#How to Mine Association Rules Using Python

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

# Sample Transactions
transactions = [
    ['Milk', 'Onion', 'Nutmeg','Kidney Beans','Eggs','Yougurt'],
    ['Dill', 'Onion', 'Nutmeg','Kidney Beans','Eggs','Yougurt'],
    ['Milk', 'Apple','Kidney Beans','Eggs'],
    ['Milk', 'Unicorn', 'Corn','Kidney Beans','Yougurt'],
    ['Corn', 'Onion', 'Onion','Kidney Beans','Ice cream','Eggs']
]

# Convert transactions to a one-hot encoded DataFrame
te = TransactionEncoder()
one_hot_encoded = te.fit(transactions).transform(transactions)
df = pd.DataFrame(one_hot_encoded, columns=te.columns_)

'''Uses the apriori function to generate frequent itemsets from the one-hot encoded DataFrame.'''
# Generate frequent itemsets
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

#The Apriori algorithm is used to find frequent itemsets,
# and association rules are then extracted based on user-defined metrics and thresholds.
# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# Display the association rules
print(rules)

