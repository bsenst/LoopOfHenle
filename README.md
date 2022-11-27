# LoopOfHenle

Contribution to the European Health Hackathon 2022 Challenge 6 "Are you kidneying" https://hackhealth.eu/ . Collaborative work done by Roman Dusek, Francis Chemorion and Benjamin Senst.

Progress & ToDo GoogleDoc https://docs.google.com/document/d/1tdbptVnlwAC6p1nt4oPbzKTXhUuPqZB65h2o9GeFpvU

## Key findings

### Providing a Model (Task #2)

Different XGBoost models have been created as a result of the hackathon project. The model identified relevant features to different the presence/upcoming of chronic kidney disease. XGBoost is an open-source implementation of the gradient boosted trees algorithm. It is a type of supervised learning algorithm.

### XGBoost Model Interpretation (Identify Features, Task #2)

![image](https://user-images.githubusercontent.com/8211411/204102327-f222d19e-b6aa-4c99-8eb0-770912e9a600.png)

Blue colored data points represent a low feature value (i.e. decreased hemoglobine (Hb), which is Anemia as can be found as a consequence of Chronic Kidney Disease (CKD)) whereas red data points stand for increased feature value (i.e. inceased hemoglobine). Having a closer look on the hemoglobine feature one can observe that the red dots (i.e. higher Hb) are located left to the midline thus speaking against the presence/development of CKD. In contrast low hemoglobine as illustrated by blue points can be found to the right of the midline indicating the presence/development of CKD. The features further down the list have less impact on the model output as they are aligned midline.

![image](https://user-images.githubusercontent.com/8211411/204102346-a140b188-1197-449e-8b91-73e1b116065e.png)

The diagram showing the mean SHAP values illustrate the features with the most profound impact on the model output magnitude regardless of the direction the show (i.e. speaking for CKD or for non-CKD case). The diagram suggests features such as serum kreatinin, diffeence in absolute and relative granulocyte count, difference in thrombocyte level, hemoglobine and hematocrite, lymphocytes, neutrophiles, glomerular filtration rate, urine specific weight and erythrocyte anisocytosis.

The dataset reflects current clinical practice. Thus more frequent lab tests are overrepresented and might hide more rare features among other lab tests. From descriptive data analysis we propose the following features as candidates for further investigation which are not clinical routine for detecting kidney tissue damage:

```
1.25(OH)D                      B_ASPIRIN_VERIFY_p_ASPIRI[...] B_CD16_+_56                    
B_CD16_+_56                    B_CD19                         B_CD19_abs.počet               
B_CD3_abs.počet                B_CD4_abs.počet                B_CD8_abs.počet                
B_Lymfocyty_Lymfocyty_%_5[...] B_Lymfocyty_Lymfocyty_Lym[...] B_Lymfocyty_abs_Lymfocyty[...] 
B_Metamyelocyty_Metamyelocyty  B_NK_abs.počet                 B_NRBC_abs.počet               
B_RTC_mladé                    B_Sedimentace/1h_FW_/_1h_[...] B_Segmenty_Neutrofilní_se[...] 
B_Tyče_Neutrofilní_tyče_T[...] B_leukocyty                    B_poměr_CD4/CD8                
B_takrolimus                   CD19_Buňky_CD19+               CD19_Lymfocyty_CD19+           
CD20_Lymfocyty_CD20+           CKD-EPI_eGF_(CKD-EPI)_GF_[...] CVVH-vápník_ion.               
C_PEPTID_C-peptid              DHEAS                          DNA-A_HLA-A_(DNA)_(Pt;_HL[...] 
DNA-B_HLA-B_(DNA)_(Pt;_HL[...] Erytropoietin_Erytrocyty       GAD_M                          
GFR-CYSTC                      GFR-CYSTC-K                    GFR-KR                         
GFR-KRKOR                      GFR-KRKOR_Clearance/1.73_[...] GFR-KR_Clearance_kreat._C[...] 
GFR-MDRD-1P_MDRD_1P_GFR-M[...] GFR-MDRD-1P_MDRD_S_Odhad_[...] GFR-MDRD-3P                    
GFR-MDRD-3P                    Kappa+CD19+_Buňky_CD19+/kappa+ Kreatinin_S_Kreatinin_KREA     
NEESTER._MK                    NRBCau_technická_B_NRBCau[...] Normetanefrin                  
P-myoglobin                    PRADTT_Protilátky_Anti-HL[...] PRA_Protilátky_Anti-HLA_([...] 
ROMA                           S-PSA_PSA_PSA_celkový          S-free_PSA                     
S-triacylglyc._S_Triacylg[...] S_FSH                          S_LH                           
S_Prolaktin                    U_OSM_okamžitá                 U_OSM_sběr                     
U_albumin/kreat._V_Index_[...] U_albumin_ranní_U_Mikroal[...] U_albumin_sběr_U-mikroalb[...] 
U_albuminurie                  U_bakterie_U_bakterie_UF_[...] U_chloridy                     
U_draslík                      U_epitelie_jiné                U_epitelie_přechodné_UD_U[...] 
U_erytrocyty_Hamburger-er[...] U_erytrocyty_UD_U_Erytroc[...] U_fosfor_U-fosfor_(P)          
U_glukóza_Glukóza              U_hlen_UF_Hlen_v_sediment[...] U_hlen_U_hlen_UD_Hlen_U_H[...] 
U_kreatinin                    U_kreatinin_ran.               U_krev_Hemoglobin_Krev_Kr[...] 
U_kys.močová_U-kyselina_močová U_leukocyty_Hamburger-leu[...] U_protein/kreat.               
U_protein_celk._Bílkovina[...] U_protein_ranní                U_shluky_leukocytů_UF_Leu[...] 
U_sodík                        U_urea                         U_válce_hyalinní_U-válce_[...] 
U_válce_hyalinní_UD_Válce[...] U_válce_hyalinní_UF            U_válce_patol._UF              
U_válce_patolog._U_válce_[...] U_vápník_celk._U-vápník_(Ca)   Urea_S_Urea_-_močovina_Ur[...] 
Vitamin_D_Total_Vitamín_D[...] anti_TETANUS_IgG               dU-kortizol_volný/24_h_U-[...] 
dU_albumin_Mikroalbuminur[...] dU_kreatinin                   dU_protein_celk._Bílkovin[...] 
dU_urea                        dU_vápník_celk._dU-vápník/24h  dr_bilirub._celk               
dr_bilirub._přím               f_hemoglobin                   f_hemoglobin_f_hemogl._ko[...] 
objem_sbír_Moč_sběr_-_obj[...] p_ACTH                         p_ALT_ALT_P-ALT                
p_AMS_Amyláza                  p_AMS_pankreat.                p_AST_AST_P-AST                
p_Aldosteron                   p_Aldosteron                   p_Apixaban                     
p_BNP                          p_CK                           p_CMV_qRT_PCR                  
p_DDi_kvantit.                 p_DRVVT-sc1:1-RI               p_DRVVT_pacient                
p_DRVVT_pacient                p_DRVVT_ratio                  p_DRVVT_scr/konf               
p_DRVVT_scr_1:1                p_DRVVTkonf_paci               p_DRVVTkonf_rati               
p_Digoxin                      p_Digoxin                      p_Faktor_VIII                  
p_Faktor_XII                   p_GGT_GGT                      p_Gentamicin                   
p_LDH_LDH                      p_NT-proBNP                    p_PT_%                         
p_PT_INR_INR_PT_INR_Protr[...] p_PT_pacient                   p_PT_ratio_PT-ratio_Protr[...] 
p_Renin                        p_Renin                        p_aPTT-LA1:1-RI                
p_aPTT-LA_1:1                  p_aPTT-LA_pacien               p_aPTT-LA_ratio                
p_aPTT-konf.hex.               p_aPTT_scr/konf                p_aPTTnecit_rat                
p_amoniak                      p_bilirubin_celk               p_bilirubin_přím               
p_bilirubin_přím               p_fosfor_Fosfor                p_glukóza_(NaF)                
p_homocystein                  p_kreatinin_P-kreatinin        p_lipáza                       
p_prokalcitonin                p_prokalcitonin_s_prokalc[...] p_transfer._sat.               
p_urea_Urea_P-urea             p_železo_Železo                sTfR/F                         
s_AFP                          s_AMS_Amyláza_Alfa-amylas[...] s_AMS_pankreat.                
s_ANA_IF_ANA_IgG               s_ASCA_IgA                     s_ASCA_IgG                     
s_ASLO_ASLO_Antistreptoly[...] s_ApoC-III                     s_B12_aktivní                  
s_B12_aktivní                  s_Borrelia_IgG                 s_CA_125                       
s_CA_125                       s_CA_15-3                      s_CA_15-3                      
s_CA_72-4                      s_CA_72-4                      s_CIK_vazbou_C1q               
s_CIK_vazbou_C1q               s_CMV_IgM                      s_CMV_IgM                      
s_COVID-19_IgG_CLIA_s_COV[...] s_C_peptid                     s_C_peptid                     
s_Chl.pn.IgG                   s_Chl.pn.IgM                   s_Chl.sp.IgA_Anti_CHLAMYD[...] 
s_Chl.sp.IgM_Anti_CHLAMYD[...] s_Degradace_histaminu          s_Dermat.farinae               
s_Dermatoph.pter               s_EBNA_IgG                     s_EBV_EA_IgG                   
s_EBV_VCA_IgG                  s_EBV_VCA_IgM                  s_FSH                          
s_GX1-trávy_rané               s_GX4-trávy_poz.               s_HBsAg_kvantita               
s_HE4                          s_Herpes_IgG                   s_Herpes_IgM                   
s_IgG2                         s_IgG3                         s_IgM                          
s_Kortizol_Kortisol_(dopo[...] s_Kortizol_S_Kortizol          s_LH                           
s_Mycop.pneu.IgM               s_PSA                          s_TX10-stromy_s.               
s_TX10-stromy_s.               s_TX6-stromy_sm.               s_WX1-plevely_s.               
s_a-HBs                        s_a-HBs                        s_a-HBs                        
s_a-MPO_CIA                    s_a-MPO_CIA_s_a-MPO_ELISA      s_a-PR3_CIA                    
s_a-PR3_CIA_s_a-PR3_ELISA      s_a-PS_IgG                     s_a-PS_IgM                     
s_a-b-2GPI_IgG                 s_a-b-2GPI_IgM                 s_a-dsDNA_CIA                  
s_a-dsDNA_CIA_s_a-dsDNA_ELISA  s_a-gliadin_IgA_Gliadin_IgA    s_a-gliadin_IgG_Gliadin_IgG    
s_a-kardiol.IgG                s_a-kardiol.IgM                s_a-nukleosomy                 
s_a1_antitrypsin               s_anti-TG_Anti_tyreoglobulin   s_anti-TPO                     
s_anti-TSH_rec._TRAK_(ant[...] s_anti-tTG_IgA                 s_anti-tTG_IgA                 
s_anti-tTG_IgG                 s_anti-tTG_IgG                 s_anti-virus_hepatitidy_E_IgM  
s_anti_PI_IgG                  s_anti_PI_IgM                  s_b-2-mikroglob.               
s_b-CrossLaps                  s_b-CrossLaps_B_Beta-Cros[...] s_bilirubin_celk               
s_bilirubin_přím               s_ceruloplasmin                s_cystatin_C                   
s_fPSA                         s_fPSA                         s_ferritin                     
s_ferritin_Ferritin            s_ferritin_Ferritin_S_Ferritin s_hs-Troponin_T                
s_kočka                        s_kreatinin_kreatinin_S-k[...] s_lipoprotein(a)               
s_lipáza_Lipáza_Lipasa         s_parathormon_Parathormon_PTH  s_parathormon_s_PTH(1-84)      
s_pes                          s_prokalcitonin                s_prolaktin                    
s_propeptid_prokolagenu_1      s_propeptid_prokolagenu_1[...] s_rBetv2_profil._s_rBet_v2     
s_testosteron                  s_total_IgE_s_Total_IgE        s_total_IgE_s_Total_IgE        
s_urea_Urea_urea_S_Urea_S-urea v_3-OH-butyrát                 x_Frakční_exkrece_vody_Fr[...]
```

## Try the key features with the live app

https://huggingface.co/spaces/bsenst/CKD-Predictor

![image](https://user-images.githubusercontent.com/8211411/204114798-dfef4648-2d3a-416a-885c-d2091b800c6a.png)

## Further Resources as a result of the Friday Warm-up

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
