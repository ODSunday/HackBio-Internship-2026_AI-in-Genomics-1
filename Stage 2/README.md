# Predicting Drug Sensitivity in Cancer Cell Lines

Cancer cells do not respond uniformly to treatment. A drug that eliminates one tumour type may be entirely ineffective or actively harmful in another. Understanding why certain cell lines are sensitive or resistant to specific drugs is one of the central challenges of precision oncology.

The **Genomics of Drug Sensitivity in Cancer (GDSC)** database provides a large-scale pharmacogenomics resource: hundreds of cancer cell lines profiled with multi-omic data and systematically exposed to hundreds of anti-cancer compounds. The primary readout is the **IC50**, the concentration of a drug required to inhibit cell viability by 50%. A lower IC50 indicates greater sensitivity; a higher IC50 indicates resistance.

In this study, we frame drug sensitivity prediction as a **regression task**, using `LN_IC50` (the natural log of IC50) as our target variable. We train an **XGBoost** model on a rich set of biological and pharmacological features, evaluate predictive performance, and use both **model-intrinsic feature importance** and **permutation importance** to interpret which features drive predictions, grounding every finding in cancer biology.
