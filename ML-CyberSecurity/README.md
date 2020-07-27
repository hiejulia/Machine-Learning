# Malware classification
- PE header 
- Dataset : malicious file PE samples dataset 
- Automate analysis of samples in VM is Cuckoo Sandbox 
- Detect & classify file type based on feature extract from PE header & features derived from N grams 


## Feature extraction techniques
- N-grams features (hash n grams)
- PE headers fetures (sections names & imports) -> vectorized using NLP approach (hashing vector)


## 
- Imbalance datasets(class imbalance techniques) -> weighted, unsample the minor class, downsampling major class 

## Tune
- Threshold, XGBoost

## Tools & Tech 
- YARA 
- pefile 

