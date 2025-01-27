import pandas as pd
import numpy as np
from faker import Faker
import random



#####################################################
# Classic Generating Data Strategy
#####################################################


fake = Faker()

total_players = 30672
players_unfinished_game = 5414
recent_players_24h = 148
inconsistent_data = 4
used_players = 25106
num_churners = 10465
num_non_churners = used_players - num_churners

data = []

for _ in range(used_players):
    fbid = fake.uuid4()
    total_session = random.randint(1,20) #Session period
    total_play = random.randint(1,total_session * 3) #number of sessions
    total_half_game = random.randint(0,int(total_play * 0.5)) #Number of Unfinished Game
    session_with_noplay = random.randint(0,total_session//2) #Number of Game without Playing
    sequential_win = random.randint(0, 10)

    total_chip = random.uniform(100, 10000)
    total_pishti = random.randint(0, total_play // 2)
    total_vpishti = random.randint(0, total_pishti // 2)
    avg_pot = random.uniform(5, 50)
    total_level = random.randint(1, 50)
    sequential_pishti = random.randint(0, 10)


    max_chip_played = random.uniform(50, total_chip)
    total_create = random.randint(0, 10)
    total_sit = random.randint(total_create, total_create + 20)
    total_join = random.randint(0, total_play)
    total_play_now = random.randint(0, 20)
    want_buy = random.randint(0, 5)

    # Churn durumu
    is_churn = 1 if len(data) < num_churners else 0  # İlk churners, sonra non-churners

    # Oyuncu verisini listeye ekle
    data.append([
        fbid, total_session, total_play, total_half_game, session_with_noplay,
        sequential_win, total_chip, total_pishti, total_vpishti, avg_pot,
        total_level, sequential_pishti, max_chip_played, total_create, total_sit,
        total_join, total_play_now, want_buy, is_churn
    ])


columns = [
    "fbid", "total_session", "total_play", "total_half_game", "session_with_no_play",
    "sequential_win", "total_chip", "total_pishti", "total_vpishti", "avg_pot",
    "total_level", "sequential_pishti", "max_chip_played", "total_create",
    "total_sit", "total_join", "total_play_now", "want_buy", "is_churn"
]

df = pd.DataFrame(data,columns= columns)


df = df.sample(frac=1, random_state=42).reset_index(drop=True)




print(df.head())



# Save as CSV
df.to_csv("mobile_game_churn_dataset_with_random.csv", index=False)
print("Veri seti 'mobile_game_churn_dataset_with_info.csv' olarak kaydedildi!")


