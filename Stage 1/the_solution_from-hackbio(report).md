# Genomics of Drug Sensitivity in Cancer (GDSC): Exploratory Analysis Report
---
## 1. Dataset Overview
The GDSC dataset contains 162,103 drug-cell line sensitivity measurements across 246 drugs, 737 cancer cell lines, and 30 TCGA cancer types. Each row represents a single drug tested on a single cell line, with the following key variables:

---

|Column	|Description|
|-------|-----------|
|COSMIC_ID	|Unique cell line identifier (COSMIC database)
|CELL_LINE_NAME	|Name of the cancer cell line
|TCGA_DESC	|TCGA cancer type abbreviation
|DRUG_NAME	|Drug name
|LN_IC50	|Natural log of IC50 (µM); lower = more potent
|AUC	|Area under dose-response curve; lower = more sensitive
|Z_SCORE	|Standardized sensitivity score across all cell lines
|TISSUE_1 / TISSUE_2	|Tissue of origin descriptors
|MSI_STATUS	|Microsatellite instability status (MSI-H vs MSS/MSI-L)
|GROWTH_PROPS	|Cell growth type (Adherent, Suspension, Semi-Adherent)
|CNA	|Whether copy number alteration data is available (Y/N flag)
|Gene Expression	|Whether gene expression data is available (Y/N flag)
|Methylation	|Whether methylation data is available (Y/N flag)
|TARGET	|Drug molecular target
|TARGET_PATHWAY	|Biological pathway targeted by the drug

> Important note on genomic columns: CNA, Gene Expression, and Methylation are binary availability flags (Y/N), not continuous genomic measurements. This limits mechanistic genomic analysis; comparisons reflect data-availability differences across cell lines.

---

## 2. Data Quality & Cleaning
- Missing values: None detected across all 162,103 rows and 19 columns
- Duplicate rows: None (exact duplicates or drug–cell line pair duplicates)
- AUC validity: All values fall within [0, 1] as expected
- LN_IC50 range: −8.64 to +13.82 (median = 3.27); 2% of values fall outside the 1st–99th percentile range
- Preprocessing steps: Columns renamed for clarity; IC50_uM back-transformed from LN_IC50; binary flags converted to boolean

---

## 3. Drug Sensitivity Patterns
### 3.1 Global Distributions
The LN_IC50 distribution is approximately normal with a slight right skew (median = 3.27), indicating that most drugs require relatively high concentrations to achieve 50% inhibition. The AUC distribution is heavily left-skewed (median = 0.94), with most cell lines showing high AUC values — meaning most drugs do not fully suppress growth at tested concentrations. The Z-score distribution is symmetric around zero by construction.

**Figure 1** — Global distributions of LN_IC50, AUC, and Z-Score

### 3.2 Most Effective Drugs
The 15 most potent drugs (lowest median LN_IC50) are dominated by mitosis inhibitors and DNA replication inhibitors:

|Drug	|Median LN_IC50	|Target Pathway
|-------|---------------|---------------
|Romidepsin	|−5.32	|Chromatin histone acetylation (HDAC inhibitor)
|Bortezomib	|−4.91	|Protein stability and degradation (proteasome)
|Sepantronium bromide	|−4.21	|Apoptosis regulation
|Docetaxel	|−3.99	|Mitosis (taxane)
|Daporinad	|−3.90	|Metabolism (NAMPT inhibitor)
|Vinblastine	|−3.78	|Mitosis (vinca alkaloid)
|SN-38	|−3.51	|DNA replication (topoisomerase I)

These are well-established cytotoxic agents with broad-spectrum activity, consistent with their clinical use.

### 3.3 Least Effective Drugs
The least effective drugs include antioxidants (Vitamin C, N-acetyl cysteine, glutathione, alpha-lipoic acid) — these are not conventional cancer drugs and their high IC50 values are biologically expected. Among conventional agents, Temozolomide (alkylating agent, median LN_IC50 = 6.51) and Motesanib (RTK inhibitor) show the lowest potency.


### 3.4 Most Variable (Selective) Drugs
Drugs with the highest standard deviation of LN_IC50 across cell lines are the most cancer-type-selective — they work very well in some contexts and poorly in others:

|Drug	|Std LN_IC50	|Target Pathway
|-------|---------------|--------------
|Gemcitabine	|2.94	|DNA replication
|AZD5991	|2.76	|Apoptosis regulation (MCL1 inhibitor)
|Daporinad	|2.74	|Metabolism
|Docetaxel	|2.55	|Mitosis
|BI-2536	|2.46	|Cell cycle (PLK1 inhibitor)
|Dasatinib	|2.39	|Other kinases (BCR-ABL/SRC)
|Trametinib	|2.30	|ERK MAPK signalling (MEK inhibitor)

High variability in Dasatinib and Trametinib is clinically meaningful — these drugs have known biomarker-driven indications (BCR-ABL fusions, BRAF/RAS mutations).

**Figure 2** — Boxplots: most vs least effective drugs

**Figure 3** — Most variable drugs and pathway-level sensitivity overview

---

## 4. Cancer Cell Line Analysis
### 4.1 Overall Sensitivity by Cancer Type
Hematologic malignancies are consistently the most drug-sensitive cancer types:

|Cancer Type	|Median LN_IC50	|n Cell Lines	|Notes
|---------------|---------------|---------------|------
|CLL	|1.55	|2	|⚠ Very small sample
|LAML (AML)	|2.04	|24	|Robust
|ALL	|2.06	|26	|Robust
|DLBC (DLBCL)	|2.10	|33	|Robust
|LCML (CML)	|2.16	|10	|Moderate
|MM (Myeloma)	|2.47	|16	|Moderate

The most drug-resistant cancer types are PAAD (pancreatic, median LN_IC50 = 4.17), UCEC (endometrial), and LIHC (liver) — consistent with the known clinical challenge of treating these cancers.

> Caveat: CLL (n=2) and ACC (n=1) results should be interpreted with extreme caution due to very small sample sizes.

### 4.2 Cancer-Type-Selective Drug Responses
The most cancer-type-selective drugs (largest LN_IC50 range across cancer types):

|Drug	|Most Sensitive Cancer	|LN_IC50	|Least Sensitive	|LN_IC50	Pathway
|-------|-----------------------|-----------|-------------------|------------------
|AZD5991 (MCL1i)	|MM	|−1.80	|PAAD	|+6.22	|Apoptosis
|Trametinib (MEKi)	|SKCM	|−3.48	|SCLC	|+2.46	|ERK MAPK
|Gemcitabine	|DLBC	|−4.76	|BRCA	|+2.71	|DNA replication
|Cytarabine	|ALL	|−2.63	|BRCA	|+3.32	|Other
|BI-2536 (PLK1i)	|ALL	|−4.51	|BRCA	|+1.25	|Cell cycle
|PD0325901 (MEKi)	|SKCM	|−2.31	|SCLC	|+3.13	|ERK MAPK

Biological interpretation:

- Trametinib/PD0325901 in SKCM: Melanoma is enriched for BRAF V600E mutations, which activate the MAPK pathway — MEK inhibitors are a standard-of-care treatment
- AZD5991 in MM: Multiple myeloma is highly dependent on MCL1 for survival
- Cytarabine/BI-2536 in ALL: Acute lymphoblastic leukemia is highly sensitive to nucleoside analogues and mitotic inhibitors
- Gemcitabine in DLBC: Diffuse large B-cell lymphoma shows high sensitivity to nucleoside analogues

**Figure 4** — Cancer type sensitivity boxplot and drug × cancer type heatmap

**Figure 5** — Top 6 most cancer-type-selective drugs

---

## 5. Genomic & Molecular Influences on Drug Response
### 5.1 LN_IC50 vs AUC Correlation
LN_IC50 and AUC are strongly correlated (Pearson r = 0.756, Spearman ρ = 0.776, n = 5,000 sample), confirming that both metrics capture similar information about drug sensitivity. The correlation is not perfect, reflecting that AUC captures the full dose-response shape while IC50 captures only the midpoint.

### 5.2 MSI Status
MSI-H (microsatellite instability-high) tumors are significantly more drug-sensitive than MSS/MSI-L tumors (Mann-Whitney U, p < 0.001):
- MSI-H: median LN_IC50 = 2.997
- MSS/MSI-L: median LN_IC50 = 3.293

After Bonferroni correction across 233 drugs, 10 drugs show significant MSI-H selectivity:

|Drug	|Delta LN_IC50 (MSI-H minus MSS)	|Pathway
|-------|-----------------------------------|---------
|Methotrexate	|−2.43	|DNA replication
|VE821 (ATRi)	|−1.37	|Genome integrity
|AZD6738 (ATRi)	|−1.08	|Genome integrity
|Oxaliplatin	|−0.90	|DNA replication
|Uprosertib (AKTi)	|−0.86	|PI3K/MTOR
|5-Fluorouracil	|−1.10	|Other

The enrichment of DNA replication and genome integrity drugs among MSI-H-sensitive agents is biologically coherent: MSI-H tumors have defective mismatch repair, making them more vulnerable to DNA-damaging agents and replication stress.

### 5.3 Growth Properties (Adherent vs Suspension)
Suspension-growing cells (predominantly hematologic cancers) are significantly more drug-sensitive than adherent cells (solid tumors):

- Suspension: median LN_IC50 = 2.44
- Adherent: median LN_IC50 = 3.52

Top drugs preferentially effective in suspension (hematologic) cells include AZD5991, BI-2536, ABT737, Navitoclax, Cytarabine, and Methotrexate — all with established clinical use in hematologic malignancies.

> Confounding note: The growth property effect largely reflects cancer type composition (hematologic vs solid tumors) rather than a direct mechanistic effect of growth properties on drug sensitivity.

### 5.4 Genomic Data Availability
CNA and Gene Expression data availability are statistically associated with LN_IC50 differences (p < 0.01), but effect sizes are small (delta median < 0.5 LN_IC50 units). This likely reflects cancer type composition bias — cell lines with genomic data available may be enriched for certain cancer types — rather than a direct causal relationship.

**Figure 6** — Genomic and molecular feature influences on drug sensitivity

**Figure 7a** — LN_IC50 vs AUC scatter plot

**Figure 7b** — Mean Z-Score heatmap (cancer type × target pathway)

---
## 6. Key Biological Insights
1. Hematologic cancers are broadly drug-sensitive — LAML, ALL, DLBC, and MM show the lowest median LN_IC50 values, consistent with their clinical responsiveness to chemotherapy and targeted agents.

2. Pancreatic cancer (PAAD) is the most drug-resistant — median LN_IC50 = 4.17, the highest of all cancer types, consistent with the poor prognosis and limited treatment options in clinical practice.

3. MEK inhibitors are highly selective for melanoma — Trametinib and PD0325901 show the strongest SKCM selectivity, directly reflecting the high prevalence of BRAF/RAS mutations in melanoma.

4. MSI-H tumors are more drug-sensitive, particularly to DNA-damaging agents and ATR inhibitors — supporting the clinical rationale for using DNA damage response inhibitors in MSI-H cancers.

5. Mitosis and DNA replication inhibitors are the most broadly potent — these pathways represent fundamental vulnerabilities in rapidly dividing cancer cells.

6. Antioxidants (Vitamin C, NAC, glutathione) show the highest IC50 values — these are not cytotoxic agents and their inclusion in the dataset reflects the breadth of the GDSC screening effort.

---
7. Limitations
- Binary genomic flags: CNA, Gene Expression, and Methylation columns indicate data availability, not actual genomic values. Continuous genomic data would enable far richer mechanistic analysis.
- Small sample sizes: CLL (n=2), ACC (n=1), MB (n=4) cancer type results are unreliable.
- Confounding: Growth property and genomic availability effects are likely confounded by cancer type composition.
- In vitro context: All data comes from cell line experiments. Drug sensitivity in cell lines does not always translate to clinical efficacy.
- Drug concentration range: IC50 values outside the tested concentration range are extrapolated and may be less reliable.

---
## 8. Figures Summary
|Figure	|Description
|-------|-----------
|fig1_global_distributions	|LN_IC50, AUC, and Z-Score global distributions
|fig2_most_least_effective_drugs	|Boxplots: top 15 most vs least effective drugs
|fig3_variability_pathway	|Most variable drugs and pathway-level sensitivity
|fig4_cancer_type_sensitivity	|Cancer type sensitivity boxplot + drug × cancer heatmap
|fig5_selective_drug_cancer	|Top 6 cancer-type-selective drugs (bar charts)
|fig6_genomic_influence	|MSI, growth properties, and genomic flag effects
|fig7a_scatter_ic50_auc	|LN_IC50 vs AUC scatter with Z-Score coloring
|fig7b_zscore_heatmap	|Mean Z-Score heatmap (cancer type × target pathway)

---
*Analysis performed using Python (pandas, numpy, scipy, matplotlib, seaborn). Dataset: GDSC public dataset via HackBio Internship GitHub repository*.
