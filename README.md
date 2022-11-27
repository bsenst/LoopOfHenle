# LoopOfHenle

Contribution to the European Health Hackathon 2022 Challenge 6 "Are you kidneying" https://hackhealth.eu/ . Collaborative work done by Roman Dusek, Francis Chemorion and Benjamin Senst.

Progress & ToDo GoogleDoc https://docs.google.com/document/d/1tdbptVnlwAC6p1nt4oPbzKTXhUuPqZB65h2o9GeFpvU

## Key findings

### Providing a Model (Task #2)

Different XGBoost models have been created as a result of the hackathon project. The model identified relevant features to differentiate the presence/upcoming of chronic kidney disease. XGBoost is an open-source implementation of the gradient boosted trees algorithm. It is a type of supervised learning algorithm.

### XGBoost Model Interpretation (Identify Features, Task #2)

![image](https://user-images.githubusercontent.com/8211411/204102327-f222d19e-b6aa-4c99-8eb0-770912e9a600.png)

Blue colored data points represent a low feature value (i.e. decreased hemoglobine (Hb), which is Anemia as can be found as a consequence of Chronic Kidney Disease (CKD)) whereas red data points stand for increased feature value (i.e. inceased hemoglobine). Having a closer look on the hemoglobine feature one can observe that the red dots (i.e. higher Hb) are located left to the midline thus speaking against the presence/development of CKD. In contrast low hemoglobine as illustrated by blue points can be found to the right of the midline indicating the presence/development of CKD. The features further down the list have less impact on the model output as they are aligned midline.

![image](https://user-images.githubusercontent.com/8211411/204102346-a140b188-1197-449e-8b91-73e1b116065e.png)

The diagram showing the mean SHAP values illustrate the features with the most profound impact on the model output magnitude regardless of the direction the show (i.e. speaking for CKD or for non-CKD case). The diagram suggests features such as serum kreatinin, diffeence in absolute and relative granulocyte count, difference in thrombocyte level, hemoglobine and hematocrite, lymphocytes, neutrophiles, glomerular filtration rate, urine specific weight and erythrocyte anisocytosis.

The dataset reflects current clinical practice. Thus more frequent lab tests are overrepresented and might hide more rare features among other lab tests. From descriptive data analysis we propose the following features as candidates for further investigation which are not clinical routine for detecting kidney tissue damage:

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
| https://www.youtube.com/watch?v=MUkn5FYnSac | Survey on Prediction of Chronic Kidney Disease Using Data Mining Classification Techniques and Feature Selection.International Conference on Advances in Computer Science, Engineering and Technology – ICACSET’18 |
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
