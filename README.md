# LoopOfHenle

Contribution to the European Healthcare Hackathon 2022 Challenge #6 "Are you kidneying" https://hackhealth.eu/ . Collaborative work done by [Roman Dusek](roman-dusek
), [Francis Chemorion](https://github.com/kchemorion) and Benjamin Senst.

***Disclaimer: The findings of this project have not been validated. Thus no medical advice can be concluded from the provided model and its deployed application.***

## Key findings

### Providing a Model (Task #2)

Different XGBoost models have been created as a result of the hackathon project. The model identified relevant features to differentiate the presence/upcoming of chronic kidney disease. XGBoost is an open-source implementation of the gradient boosted trees algorithm. It is a type of supervised learning algorithm.

### XGBoost Model Interpretation (Identify Features, Task #2)

![image](https://user-images.githubusercontent.com/8211411/204102327-f222d19e-b6aa-4c99-8eb0-770912e9a600.png)

Blue colored data points represent a low feature value (i.e. decreased hemoglobine (Hb), which is Anemia as can be found as a consequence of Chronic Kidney Disease (CKD)) whereas red data points stand for increased feature value (i.e. inceased hemoglobine). Having a closer look on the hemoglobine feature one can observe that the red dots (i.e. higher Hb) are located left to the midline thus speaking against the presence/development of CKD. In contrast low hemoglobine as illustrated by blue points can be found to the right of the midline indicating the presence/development of CKD. The features further down the list have less impact on the model output as they are aligned midline.

![image](https://user-images.githubusercontent.com/8211411/204102346-a140b188-1197-449e-8b91-73e1b116065e.png)

The diagram showing the mean SHAP values illustrate the features with the most profound impact on the model output magnitude regardless of the direction the show (i.e. speaking for CKD or for non-CKD case). The diagram suggests features such as serum kreatinin, diffeence in absolute and relative granulocyte count, difference in thrombocyte level, hemoglobine and hematocrite, lymphocytes, neutrophiles, glomerular filtration rate, urine specific weight and erythrocyte anisocytosis.

The dataset reflects current clinical practice. Thus more frequent lab tests are overrepresented and might hide more rare features among other lab tests. Beside creatinine, GFR and anemia (late markers in CKD) interestingly the model also identified granulocytes, platelet and lymphocyte changes. These lab findings might play a role as early markers as is suggested in clinical research:

* Agarwal R, Light RP. Patterns and prognostic value of total and differential leukocyte count in chronic kidney disease. Clin J Am Soc Nephrol. 2011 Jun;6(6):1393-9. doi: 10.2215/CJN.10521110. Epub 2011 May 5. PMID: 21551023; PMCID: PMC3109937.
* Yu, Y., Lin, Q., Ye, D. et al. Neutrophil count as a reliable marker for diabetic kidney disease in autoimmune diabetes. BMC Endocr Disord 20, 158 (2020). https://doi.org/10.1186/s12902-020-00597-2
* Umeres-Francia, G.E., Rojas-Fern??ndez, M.V., Herrera-A??azco, P. et al. Neutrophil-to-lymphocyte ratio and platelet-to-lymphocyte ratio as risk factors for mortality in Peruvian adults with chronic kidney disease. Ren Replace Ther 8, 30 (2022). https://doi.org/10.1186/s41100-022-00420-9
* Mizdrak M, Kumri?? M, Kurir TT, Bo??i?? J. Emerging Biomarkers for Early Detection of Chronic Kidney Disease. J Pers Med. 2022 Mar 31;12(4):548. doi: 10.3390/jpm12040548. PMID: 35455664; PMCID: PMC9025702.
* Kovesdy CP, Ureche V, Lu JL, Kalantar-Zadeh K. Outcome predictability of serum alkaline phosphatase in men with pre-dialysis CKD. Nephrol Dial Transplant. 2010 Sep;25(9):3003-11. doi: 10.1093/ndt/gfq144. Epub 2010 Mar 17. PMID: 20299338; PMCID: PMC2948834.
* Taliercio JJ, Schold JD, Simon JF, Arrigain S, Tang A, Saab G, Nally JV Jr, Navaneethan SD. Prognostic importance of serum alkaline phosphatase in CKD stages 3-4 in a clinical population. Am J Kidney Dis. 2013 Oct;62(4):703-10. doi: 10.1053/j.ajkd.2013.04.012. Epub 2013 Jun 12. PMID: 23769134; PMCID: PMC3783514.
* Gauckler P, Shin JI, Mayer G, Kronbichler A. Eosinophilia and Kidney Disease: More than Just an Incidental Finding? J Clin Med. 2018 Dec 8;7(12):529. doi: 10.3390/jcm7120529. PMID: 30544782; PMCID: PMC6306805.

## Try the key features with one of the live apps

https://bsenst-loopofhenle-web-appapp-yk9aez.streamlit.app/

![image](https://user-images.githubusercontent.com/8211411/204124133-48d2426b-3f1a-4c50-8ac6-7207b4c9f585.png)

## Further Resources as a result of the Friday Contest Warm-up

|URL|Description|
|---|---|
| https://pubmed.ncbi.nlm.nih.gov/35003242/ | Implementation of Machine Learning Models for the Prevention of Kidney Diseases (CKD) or Their Derivatives |
| https://pubmed.ncbi.nlm.nih.gov/35915457/ | Machine learning algorithms' accuracy in predicting kidney disease progression: a systematic review and meta-analysis | 
| https://pubmed.ncbi.nlm.nih.gov/32932685/ | Optimized Identification of Advanced Chronic Kidney Disease and Absence of Kidney Disease by Combining Different Electronic Health Data Resources and by Applying Machine Learning Strategies |
| https://pubmed.ncbi.nlm.nih.gov/33850243/ | Medical records-based chronic kidney disease phenotype for clinical care and "big data" observational and genetic studies | https://pubmed.ncbi.nlm.nih.gov/32424281/ | Integrated multi-omics approaches to improve classification of chronic kidney disease | 
| https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8048707/ | Machine learning, the kidney, and genotype-phenotype analysis |
| https://youtu.be/XOeoisg85pA | Chronic Kidney Disease Prediction using Machine learning |
| https://youtu.be/a0NlmSIYiEY | Chronic Kidney Disease prediction using Machine Learning |
| https://www.youtube.com/watch?v=lD63ZzmgQmg | https://github.com/pg815/Kidney_Cancer_Prediction_Using_Machine_Learning |
| https://www.youtube.com/watch?v=MUkn5FYnSac | Survey on Prediction of Chronic Kidney Disease Using Data Mining Classification Techniques and Feature Selection.International Conference on Advances in Computer Science, Engineering and Technology ??? ICACSET???18 |
| https://www.ijert.org/chronic-kidney-disease-prediction-using-machine-learning |
| https://www.youtube.com/watch?v=bgDdNM-D-TU | A Machine Learning Methodology for Diagnosing Chronic Kidney Disease | Python IEEE Project |
| https://www.youtube.com/watch?v=idXF9JFBjZY | Using machine learning for the early prediction of chronic kidney disease |
| https://www.youtube.com/watch?v=uxMvHSUOZzc | Chronic Kidney Disease Prediction Using Python & Machine Learning |
| https://www.youtube.com/watch?v=4C3dJmXnpkE | A Machine Learning Methodology for Diagnosing Chronic Kidney Disease: A Review |
| https://archive.ics.uci.edu/ml/datasets/chronic_kidney_disease |

### On Time series & Machine Learning

* https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html
* https://www.machinelearningplus.com/time-series/time-series-analysis-python/
* https://builtin.com/data-science/time-series-python
* https://machinelearningmastery.com/a-guide-to-obtaining-time-series-datasets-in-python/
* https://neptune.ai/blog/time-series-prediction-vs-machine-learning
* https://www.tensorflow.org/tutorials/structured_data/time_series
* https://github.com/yzhao062/Pyod Python Outlier Detection (PyOD)
