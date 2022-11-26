import pandas as pd
import pickle
from constants import FEATURE_COLUMNS, USES_DIFF_FROM_LAST, USED_COLUMNS

with open("analytes_nclp_mapping.pkl","rb") as f:
    analytes_nclp_mapping=pickle.load(f)

def ffill_na(df):
    return df.fillna(method="ffill")

def format_date(row):
    day, month, year = row.split(".")
    return f"{year}-{month}-{day}"

def prepare_labs_df(df):
    # prepare 
    df.EntryDate = pd.to_datetime(df.EntryDate.apply(format_date))
    df["pr_id"]= df.Patient.astype(str) + "_" +df.Report.astype(str)
    df = df[~df.ValueNumber.isna()]

    df_nan_nclp = df[df.NCLP.isna()].copy()
    df_nan_nclp.NCLP = df_nan_nclp.Analyte.apply(lambda x: analytes_nclp_mapping[x] if x in analytes_nclp_mapping else -999)

    df_new = pd.concat([df[~df.NCLP.isna()],df_nan_nclp[~(df_nan_nclp.NCLP == -999)]])

    return df_new

def preprocess_for_model(data):
    data = data.groupby("p_id").apply(ffill_na)
    return data

def preprocess_df(labs_df):

    labs_df = prepare_labs_df(labs_df)
    
    model_data = labs_df.pivot_table(index="pr_id",columns="NCLP", values="ValueNumber", aggfunc="first")

    model_data = model_data.merge(labs_df[["pr_id","EntryDate"]].drop_duplicates(), on="pr_id")

    model_data["p_id"] = model_data.pr_id.apply(lambda x: int(x.split("_")[0]))

    for col in model_data.columns[1:-1]:
        model_data[col] = model_data[col].apply(lambda x: pd.to_numeric(x, errors='coerce'))

    model_data_grouped = model_data.groupby(["p_id", pd.Grouper(key="EntryDate",freq="1M")]).mean()

    model_data_grouped = model_data_grouped[FEATURE_COLUMNS]

    model_data_grouped = model_data_grouped.groupby("p_id").apply(ffill_na)

    if USES_DIFF_FROM_LAST:
        model_data_lagged = model_data_grouped.copy()
        model_data_lagged.iloc[:,2:-1] = model_data_lagged.iloc[:,2:-1].shift(1).values - model_data_lagged.iloc[:,2:-1].values
        model_data_grouped = model_data_grouped.merge(model_data_lagged.iloc[1:,:-1], on=["p_id","EntryDate"], suffixes=("","_diff_from_last"))

    model_data_grouped = model_data_grouped.fillna(-999)

    return model_data_grouped

    