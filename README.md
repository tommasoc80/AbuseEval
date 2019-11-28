# AbuseEval
Data set for LREC 2020 paper "I Feel Offended, Don't Be Abusive!"

The repository is structured as follows:

- data/ : the folder contains the enriched versions of the OffenseEval/OLID dataset with the distinction of explicit/implicit offensive messages (./data/offenseval_explicit_implicit) and the newly proposed annotations of abusive messages (./data/abuseval_labels)
- dictionary-based_experiments/ : the folder contains the script to replicate the dictionary experiments reported in the paper (OffenseEval sub-task A and AbuseEval binary classification)
- keywords/ : the folder contains the list of the top 50 keywords from the OffenseEval training and test data for sub-task A per class (list of keywords for offensive and not offensive messages)

OLID/OffenseEval Data: https://competitions.codalab.org/competitions/20011

# References
```
@inproceedings{zampierietal2019, 
    title={{Predicting the Type and Target of Offensive Posts in Social Media}}, 
    author={Zampieri, Marcos and Malmasi, Shervin and Nakov, Preslav and Rosenthal, Sara and Farra, Noura and Kumar, Ritesh}, 
    booktitle={Proceedings of NAACL}, 
    year={2019}
} 
``` 


<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
