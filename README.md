# Cyber_AgileHawks
 
---
## Team : Agile_Hawks
## Team Members : Mayank Bhatt, Ansh Karki

---

## To use this repo 
<pre>1. CLone the repo
2.Download the model from :
</pre>
 [https://drive.google.com/file/d/1OG4n-6pX81fsfoWUzyTOu14-MCbaMzBA/view?usp=drive_link](https://drive.google.com/file/d/1OG4n-6pX81fsfoWUzyTOu14-MCbaMzBA/view?usp=drive_link)
 <pre>
3. Put the model in same folder where the repo is cloned.
4. DOwnload necessary pip files.
4. Run the command : streamlit run app.py.
You are good to go .
</pre>

---

Basically we did EDA and found the following details : 

### EDA SUMMARY REPORT: 
<pre>
  Total rows              : 1,775,435
  Total features          : 79
  Numeric features        : 70
  Missing value columns   : 14
  Duplicate rows          : 1,445
  Inf-value columns       : 2
  Zero-variance features  : 0
  Near-zero-var features  : 6
  High-corr pairs (>0.9)  : 20
  Unique labels           : 1588
  Class imbalance ratio   : 1180520.0x
</pre>

#### Key observations from EDA:

Dataset is extremely imbalanced, which is a major challenge
Some features had very high correlation (>0.9) → reduced redundancy
Presence of missing and infinite values → handled carefully during preprocessing
No zero-variance features, but near-zero variance features were removed
Large number of unique labels (multi-class problem)

---

 ### Feature Engineering summary : 
 <pre>
   Final rows        : 1,768,131
  Final features    : 85
  Label classes     : 1589
  Saved to          : engineered_dataset.csv
  Label map saved   : label_map.csv
   </pre>

  #### What we did in Feature Engineering:

Cleaned missing and infinite values
Removed duplicates and noisy data
Handled high correlation features
Created additional meaningful features to improve model learning
Encoded labels properly and saved mapping for reproducibility
Ensured dataset is optimized for training ML models

---- 

## Our engineered dataset link :
<pre> And we created this new dataset 
It has 2 files : 
engineered_dataset.csv 
label_map.csv
</pre>
[https://www.kaggle.com/datasets/anshkarki/engineered-dataset](https://www.kaggle.com/datasets/anshkarki/engineered-dataset-1)


