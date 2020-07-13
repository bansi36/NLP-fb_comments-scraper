# facebook-comments-scraper
- facebook comments scraping using bs4 or Beautifulsoup
- the very first step is to specify your credentials and profile urls to the main scraper code which is faceboksdata_scraper
- run facebooksdata_scraper code
- profile_data.json which is the output of the first code, convert it into the csv file using the json_to_csv_conv.py and get profile_data.csv file.
- Then in text processing there are tokenization, part of speech tagging, stop word removal, stemming and lemmatization steps performed.
- Feature Extraction

-->The raw data or a sequence of symbols cannot be fed directly to the algorithms themselves as most of them expect numerical feature vectors with a fixed size rather than the raw text documents with variable length.

--> scikit-learn provides utilities for the most common ways to extract numerical features from text content, namely:

    - tokenizing strings and giving an integer id for each possible token, for instance by using white-spaces and punctuation as token separators.

    - counting the occurrences of tokens in each document.

    - normalizing and weighting with diminishing importance tokens that occur in the majority of samples / documents.
    
--> each individual token occurrence frequency (normalized or not) is treated as a feature.

--> vectorization, the general process of turning a collection of text documents into numerical feature vectors.
