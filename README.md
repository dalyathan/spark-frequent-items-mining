## Frequent Itemset Mining on Large-Scale Retail Data Using the SON Algorithm

Name: Surafel Melese Tariku
ID: VR526858
Masters in AI

# Objectives
Build a scalable pipeline for mining frequent itemsets from transactional data leveraging Apache Spark’s distributed, in‑memory processing (RDD / MLlib) to efficiently implement SON—enabling parallel local mining and fast global aggregation based on [6.4.4 The SON Algorithm and MapReduce](http://infolab.stanford.edu/~ullman/mmds/ch6.pdf)

# Motivation
Mining frequent itemsets from massive retail data using SON enables scalable pattern discovery through distributed candidate generation and verification—offering actionable insights and improved cross-selling strategies.

# Methdology
- Implement a single machine verison using the `mlxtend` library
- Implement a single machine verison using the `PyFIM` library
- Implement a multi machine verison using `Pyspark` library

# Dataset
I'm planning to do increasingly challenging datasets on this order
1. [T40I10D100K,  Retail Dataset (from FIMI)](http://fimi.uantwerpen.be/data/T10I4D100K.dat),  88,162 transactions, 16,470 items
2. [Kosarak](http://fimi.uantwerpen.be/data/kosarak.dat), ~1 million transactions, 41,270 distinct items
3. [Instacart Dataset](https://www.instacart.com/datasets/grocery-shopping-2017), ~3 million orders from 200k users, 50k products



# Expected Results:
- As the database becomes more challening, the single machine implementation should progressively become slowe while the pyspark implementation doesn't get as slow, (but is expected to still get slower)
- Some hyperparameter experimentation, for example minimum support threshold during the apriori stage
- The result of the single machine verison of the pyspark version should be the same