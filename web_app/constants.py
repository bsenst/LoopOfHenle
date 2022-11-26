MODEL = "model_weighted.pkl"


USED_COLUMNS = ['Patient', 'Report','EntryDate', 'NCLP',
       'Analyte', 'ValueNumber', 'Unit',
       'pr_id']

USES_DIFF_FROM_LAST = False

if not USES_DIFF_FROM_LAST:
    FEATURE_COLUMNS = ['8574.0', '3086.0', '5254.0', '2688.0', '4769.0', '13808.0', '1675.0', '2419.0', '2099.0', '1991.0', '4726.0', '16263.0', '18895.0', '5272.0', '3078.0', '582.0', '17339.0', '921.0', '1961.0', '3410.0', '5143.0', '12367.0', '12348.0', '12347.0', '12369.0', '12365.0', '18029.0', '18027.0', '12449.0', '12460.0', '12483.0', '12478.0', '12471.0', '543.0']
else:
    FEATURE_COLUMNS = ['8574.0','8574.0_diff_from_last']

