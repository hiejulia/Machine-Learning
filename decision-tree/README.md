## Decision 
- pandas, numpy, seaborn

- data clean 
- data prepare 

- build model and evaluation 
    - prevent overlifting issue in DT 
- tuning 



## Income prediction wiht DT 
- Attributes : age, working class type, marital status, gender, race 
- build DT with hyperparameters 
- tune
- choose optima hyperparameters using grid search cross validation 


- data preparation 
    - encode the categorical vars into a standard format so that sklearn can understand and build the tree 
    - `LabelEncoder()`



- model building and evaluation  



- plot decision tree (graphviz )


- tune : cross validation 

- Hyperparameter tuning 

- get parameters in DT `help(DecisionTreeClassifier)`
    - criterion 
    - splitter 
    - max_features
    - max_depth
    - min_samples_split
    - min_sample_leaf
    - max_leaf_node 


- tuning max_depth 
    - create dataframe with max_depth in range 1 - 80 and check accuracy score to each max_depth 

    - to reiterate, a grid search scheme 
        - an estimator : classifier such as SVC() or DT
        - parameter space
        - method for searching or sampling candidates 
        - cross validation scheme
        - score function with accuracy, roc_auc etc 



- tuning min_samples_leaf
    - indicate the min number of samples required to be at a leaf
    - less -> overfit 


- tune min_samples_split 
    - min no. of samples required to split an internal node 
    - default = 2 
    

- Grid search to find optimal hyperparameters 
    - find multiple optimal hyperparameters together with GridSearchCV 
    - gini/entropy or IG 





- DEMO 
<a href="https://imgur.com/5CO54Fi"><img src="https://i.imgur.com/5CO54Fi.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/WdO9kfE"><img src="https://i.imgur.com/WdO9kfE.png" title="source: imgur.com" /></a>
<a href="https://imgur.com/xaR9XgU"><img src="https://i.imgur.com/xaR9XgU.png" title="source: imgur.com" /></a>
<a href="https://imgur.com/7qbPT8S"><img src="https://i.imgur.com/7qbPT8S.png" title="source: imgur.com" /></a>
<a href="https://imgur.com/ztwgvTC"><img src="https://i.imgur.com/ztwgvTC.png" title="source: imgur.com" /></a>
<a href="https://imgur.com/5ere7lX"><img src="https://i.imgur.com/5ere7lX.png" title="source: imgur.com" /></a>
<a href="https://imgur.com/jGNSklG"><img src="https://i.imgur.com/jGNSklG.png" title="source: imgur.com" /></a>
<a href="https://imgur.com/2Ptzrbq"><img src="https://i.imgur.com/2Ptzrbq.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/09U8tR1"><img src="https://i.imgur.com/09U8tR1.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/QLc12uN"><img src="https://i.imgur.com/QLc12uN.png" title="source: imgur.com" /></a>

<a href="https://imgur.com/WhFhC0S"><img src="https://i.imgur.com/WhFhC0S.png" title="source: imgur.com" /></a>
