# Synthetic Data Generation and Churn Prediction on Game Data

This post is an example of synthetic data I am preparing for LinkedIn. I wanted to do churn prediction on game data, so I started looking for a dataset. I wanted it to be challenging and not something I could easily replicate. Therefore, I decided to generate my own data.

## Data Generation

Initially, I referred to the project by Pelin Ercan, titled "DETECTION OF CHURNERS IN INTERNET GAMES USING CRM APPROACH: A CASE STUDY ON PISHTI PLUS," and advised by Prof. Dr. Ferda Nur Alpaslan. Based on this, I started generating data using the **random** and **faker** libraries.

However, I thought this dataset wouldn’t accurately reflect reality, so I decided to generate synthetic data from a project whose data I could access. I learned that synthetic data can be produced by identifying relationships between different data types even with a small amount of data. I also learned that big companies in the USA often obtain such data from small-scale firms.

## Synthetic Data Generation on World of Warcraft

For this task, I focused on the **World of Warcraft** game and used the **SDV (Synthetic Data Vault)** library. From a dataset of 37,000 rows, I created 20,000 rows using **GaussianCopulaSynthesizer** with an accuracy rate of 85.48%. Additionally, using **GAN**, I generated 20,000 rows with an accuracy rate of 86.60%.

I found that it was easier to measure accuracy with SDV compared to other synthetic data generation libraries. Therefore, I decided to continue using this method.

## Files

There are two main files in this project:

1. **Classic_Synthetic_Data.py**: This Python file contains the classic data generation methods using **random** and **faker** libraries. It represents a basic approach for generating synthetic data.



2. **SVD_Synhetic_Data.ipynb**: This Jupyter Notebook file includes synthetic data generation and analysis using the SDV library. It provides step-by-step explanations and visualizations, using more advanced techniques like **GaussianCopulaSynthesizer** and **GAN**.



## Features in the Dataset

Below are the features used in my synthetic data:

- **guild**: The community (guild) the player belongs to within the game. Guilds allow players to form groups and play together.
- **total_timestamps**: The total number of timestamps recorded for the player's activities in the game. This can indicate how often the player engages in game activities or how frequently they log in.
- **unique_days**: The number of unique days the player was active. For example, if a player only logged in on 5 different days during a month, this value would be 5.
- **max_level**: The highest level the player has reached. This represents the player's progression within the game.
- **min_month**: The earliest month the player was active in the game. For example, if a player first became active in January 2022, this value might be "2022-01."
- **max_month**: The most recent month the player was active in the game. This shows the player's latest activity (e.g., "2023-12").
- **Average_Hour**: The average hour the player plays the game. For example, if a player usually plays in the morning, this could range from 8-10 AM.
- **Average_Playing_density**: The density of the player's gaming activities. This could refer to how frequently the player plays during specific time periods (e.g., daily, weekly, or monthly). It can include metrics like average daily playtime or hourly activity distribution.
