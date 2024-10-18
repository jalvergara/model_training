import pandas as pd


def summary_by_columns(df):
    """
    Generates a summary of each column in the provided DataFrame.

    The summary includes the data type, number of missing values, number of unique values,
    and number of duplicate values for each column.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to summarize.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the summary information for each column.
    """
    # Create an empty DataFrame to store the summary
    summary_df = pd.DataFrame(columns=['Column', 'Data Type', 'Missing Values', 'Unique Values', 'Duplicates'])

    try:
        # Loop through each column in the DataFrame
        for col in df.columns:
            data_type = df[col].dtype
            missing_values = df[col].isna().sum()
            num_unique_values = df[col].nunique()
            num_duplicates = df[col].duplicated().sum()

            # Add the results to the summary DataFrame

            row_summary = pd.DataFrame({
                'Column': [col],
                'Data Type': [data_type],
                'Missing Values': [missing_values],
                'Unique Values': [num_unique_values],
                'Duplicates': [num_duplicates],
                'Missing Values (%)': [round((missing_values / df.shape[0]) * 100, 2)]
            })

            # Concatenate the row summary to the summary DataFrame
            summary_df = pd.concat([summary_df, row_summary], ignore_index=True)
        return summary_df
    except Exception as e:
        print(f"An error occurred: {e}. In the column: {col}")


def unpack_json_columns(df):
    """
    Unpacks columns containing JSON objects in a DataFrame.

    This function identifies columns with dictionary-like (JSON) structures, normalizes them, 
    and adds the resulting nested data as new columns, while removing the original JSON columns.

    Args:
        df (pd.DataFrame): The input DataFrame containing JSON columns.

    Returns:
        pd.DataFrame: The DataFrame with JSON columns unpacked into separate columns.
    """
    # Identify columns that contain dictionaries (JSON)
    json_columns = [col for col in df.columns if isinstance(
        df[col].iloc[0], dict)]

    for col in json_columns:
        # Use json_normalize on each JSON column
        json_df = pd.json_normalize(df[col])

        # Rename columns with the corresponding prefix
        json_df.columns = [f'{col}_{subcol}' for subcol in json_df.columns]

        # Add the new unpacked columns to the original dataframe
        df = df.drop(col, axis=1).join(json_df)

    return df


def convert_lists_to_strings(df):
    """
    Converts all columns containing lists into strings in the DataFrame.

    This function iterates over each column in the DataFrame and checks if the column contains list-like objects.
    If a column contains lists, those lists are converted into their string representation.

    Args:
        df (pd.DataFrame): The input DataFrame with potential list columns.

    Returns:
        pd.DataFrame: The DataFrame with list columns converted to strings.
    """
    # Iteramos sobre las columnas del DataFrame
    for col in df.columns:
        # Verificamos si la primera entrada de la columna es una lista
        if isinstance(df[col].iloc[0], list):
            # Convertimos la columna de listas a cadenas
            df[col] = df[col].apply(lambda x: str(x))

    return df


def count_lists_size(col_list):
    """
    Returns the size of the list if the input is a list, otherwise returns 0.

    This function checks if the input is a list. If so, it returns the length of the list.
    If the input is not a list, it returns 0.

    Args:
        col_list (any): The input value which can be a list or any other type.

    Returns:
        int: The size of the list if the input is a list, otherwise 0.
    """
    if isinstance(col_list, list):
        return len(col_list)
    else:
        return 0
