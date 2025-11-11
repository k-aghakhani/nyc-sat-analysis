# NYC Public Schools SAT Performance Analysis

An in-depth exploration of SAT performance across New York City public
high schools, highlighting top-performing institutions, borough-level
trends, and meaningful insights into student achievement.\
This project combines data analysis, visualization, and educational
insight to support educators, policymakers, families, and researchers.

------------------------------------------------------------------------

## 🎯 Project Overview

Every year, thousands of NYC high school students take the SAT---a
standardized exam evaluating **Math**, **Reading**, and **Writing**
(each scored out of 800).\
This project analyzes SAT performance to address three key questions:

1.  **Which schools excel in Mathematics?**\
    (Identifying schools scoring at least 80% of the maximum math
    score.)
2.  **Which schools rank among the Top 10 overall SAT performers?**
3.  **Which borough shows the highest variability in SAT performance?**

The analysis uses: - **Pandas** for data cleaning & aggregation
- **Matplotlib** / **Seaborn** for clear and compelling visualizations

Dataset Source: NYC Department of Education (via DataCamp)

------------------------------------------------------------------------

## 🔍 Key Findings

  -----------------------------------------------------------------------
  Metric               Highlight                        Value
  -------------------- -------------------------------- -----------------
  **Top Math School**  Stuyvesant High School           **754 (Math
                                                        Score)**

  **Highest Total      Stuyvesant High School           **2,144 Total
  SAT**                                                 Score**

  **Most Variable      Manhattan                        **Std. Dev: \~230
  Borough**                                             (Avg: \~1340)**
  -----------------------------------------------------------------------

**Insights:** 
- Specialized schools lead performance citywide,
particularly in Math.
- Top 10 schools significantly outperform the city
average.
- Manhattan exhibits the widest performance range, indicating
unequal school resources and outcomes.

------------------------------------------------------------------------

## 📊 Visualizations

This project generates publication-ready visualizations:

-   **Top 10 Schools Bar Chart**
-   **Borough SAT Score Distribution (Boxplots)**
-   **Math Score vs. Total SAT Scatter Plot**

All figures are automatically saved in the `plots/` directory.

------------------------------------------------------------------------

## 📁 Repository Structure

    nyc-sat-analysis/
    │
    ├── data/                       
    │   └── schools.csv          
    │
    ├── src/                       
    │   └── analysis.py           
    │
    ├── results/                   
    │   ├── best_math_schools.csv     
    │   ├── top_10_schools.csv        
    │   └── largest_std_dev.csv       
    │
    ├── plots/                    
    │   ├── top_10_schools_bar.png
    │   ├── borough_sat_distribution.png
    │   └── math_vs_total_scatter.png
    │
    ├── README.md                
    ├── requirements.txt         
    └── run_analysis.py          

------------------------------------------------------------------------

## 🚀 Getting Started

### Prerequisites

-   Python **3.8+**
-   Git

### Installation & Run

``` bash
git clone https://github.com/k-aghakhani/nyc-sat-analysis.git
cd nyc-sat-analysis
pip install -r requirements.txt
python run_analysis.py
```

Outputs will be stored in `results/` and `plots/`.

------------------------------------------------------------------------

## 🧩 Customization

-   Modify analysis thresholds in `src/analysis.py`
-   Convert to Jupyter Notebook for interactive exploration
-   Extend with demographic or multi-year datasets

------------------------------------------------------------------------

## 📈 Future Enhancements

-   Predictive modeling of SAT scores
-   Streamlit-based interactive dashboard
-   Equity-based analysis tied to socioeconomic data

------------------------------------------------------------------------

## 📝 License & Attribution

-   **License:** MIT (free to use & modify)
-   **Data:** NYC Department of Education (via DataCamp)

------------------------------------------------------------------------

## 👨‍💻 Author

**Kiarash Aghakhani**\
GitHub: https://github.com/k-aghakhani
Email: kiarash1988@gmail.com

------------------------------------------------------------------------

> Built with a passion for educational insight and data-driven
> storytelling. 🌍📊
