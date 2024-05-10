# README

Use this project to search Google Trends website for downloading the frequency or usage of keywords (search terms) that
are of your interest (max 5 at a time).

### Note:

- This is a project built very quickly as per my requirement. So, please modify as per your need.
- The resolution of trends searched will be at <u>city</u> level
- The <u>Include low search volume regions</u> checkbox will be selected by default
- If you don't want the driver browser in action, then in the file `src/scrape_gtrends.py` uncomment the line: _# options.add_argument('--headless')_ 

In the `main.py` file, under the section <u>User Inputs</u>, modify the values as per your need and save it.

```python
# At least 1 and max of 5 keywords
keywords = ["bitcoin", "ethereum", "tether", "solana", "dogecoin"]

start_date = "2024-04-09"
end_date = "2024-05-09"

# For list of country names and their geocodes, check the file "utils/country_geo_codes.csv"
geo = "GB"

# Change this to actual path on your system to folder "Data_Output"
# Adjust the path format style based on the OS you are using (Linux, Windows, Mac)
csv_directory_location = '/home/xxxxx/xxxxx/GoogleTrends/Data_Output'
```

Open your terminal, run the following lines:

```shell
$ cd GoogleTrends

# It is highly recommended to create a virtual environment and install the following libraries
$ pip3 install -r requirements.txt

# Run the script
$ python3 main,py
```

In the above example:

1. the following csv files will be downloaded from Google Trends website to the folder `Data_Output`

|   | File                                             | Notes                                  |
|---|--------------------------------------------------|----------------------------------------|
| 1 | _Data_Output/kwds_score_relative_each_other.csv_ | Compared breakdown by city             |
| 2 | _Data_Output/scores_for_kwd_bitcoin.csv_         | Interest by city for the word bitcoin  |
| 3 | _Data_Output/scores_for_kwd_ethereum.csv_        | Interest by city for the word ethereum |
| 4 | _Data_Output/scores_for_kwd_tether.csv_          | Interest by city for the word tether   |
| 5 | _Data_Output/scores_for_kwd_solana.csv_          | Interest by city for the word solana   |
| 6 | _Data_Output/scores_for_kwd_dogecoin.csv_        | Interest by city for the word dogecoin |

2. the files (above) will be parsed/cleaned and saved as two addition files

|   | File                                                     | Notes                                                   |
|---|----------------------------------------------------------|---------------------------------------------------------|
| 7 | _Data_Output/cleaned_kwds_score_relative_each_other.csv_ | Compared breakdown by city (cleaned)                    |
| 8 | _Data_Output/scores_for_kwds_combined.csv_               | Interest by city for each key word (cleaned and merged) |


