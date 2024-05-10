import pandas as pd


def merge_scores_for_keyword_files(keywords: list) -> None:
    """
    This function will clean the csv files (Data_Output/scores_for_kwd_*.csv)
    and saves as "Data_Output/scores_for_kwds_combined.csv" file.

    Parameters
    ----------
    keywords: list
        Example: ["bitcoin", "ethereum"]

    Returns
    -------
    None

    """
    df = pd.DataFrame()
    for kwd in keywords:
        temp_df = pd.read_csv(
            f"Data_Output/scores_for_kwd_{kwd}.csv",
            names = ["city", kwd],
            skiprows = 3,
            header = None)
        if df.empty:
            df = temp_df.copy()
        else:
            df = pd.merge(left = df,
                          right = temp_df,
                          how = 'outer',
                          on = 'city',
                          validate = "many_to_many")

    df.fillna(0).to_csv("Data_Output/scores_for_kwds_combined.csv",
                        index = False)

    return None


def clean_kwds_score_relative_each_other_file(keywords: list) -> None:
    """
    This function cleans "Data_Output/kwds_score_relative_each_other.csv"
    file and saves as "Data_Output/cleaned_kwds_score_relative_each_other
    .csv"

    Parameters
    ----------
    keywords: list
        Example: ["bitcoin", "ethereum"]

    Returns
    -------
    None

    """

    df = pd.read_csv(
        "Data_Output/kwds_score_relative_each_other.csv",
        names = ['city'] + keywords,
        skiprows = 3,
        header = None)
    for kwd in keywords:
        df[kwd] = df[kwd].apply(
            lambda x: (x.replace("%", "")
                       .replace("<", "")
                       if isinstance(x, str) else x))
    df.fillna(0) \
        .to_csv(
        "Data_Output/cleaned_kwds_score_relative_each_other.csv",
        index = False)

    return None
