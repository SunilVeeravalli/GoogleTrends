from src.parse_csv_files import clean_kwds_score_relative_each_other_file, \
    merge_scores_for_keyword_files
from src.scrape_gtrends import scrape_gtrends

# -----------------------------------------------------------------------------
# User inputs
# -----------------------------------------------------------------------------

keywords = ["bitcoin", "ethereum", "tether", "solana", "dogecoin"]
start_date = "2024-04-09"
end_date = "2024-05-09"
geo = "GB"
csv_directory_location = '/home/xxxxx/xxxxx/GoogleTrends/Data_Output'

# -----------------------------------------------------------------------------
# Scraping Google trends and downloading csv files
# -----------------------------------------------------------------------------

scrape_gtrends(keywords = keywords,
               start_date = start_date,
               end_date = end_date,
               geo = geo,
               csv_directory_location = csv_directory_location)

# -----------------------------------------------------------------------------
# Cleaning and merging csv files
# -----------------------------------------------------------------------------

merge_scores_for_keyword_files(keywords = keywords)
clean_kwds_score_relative_each_other_file(keywords = keywords)
