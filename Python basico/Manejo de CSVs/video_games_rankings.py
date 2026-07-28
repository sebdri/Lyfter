import csv
def video_game_rank(file_path , data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:

         headers = data[0].keys()

         writer = csv.DictWriter(file , fieldnames=headers)

         writer.writeheader()

         writer.writerows(data)


games_ranked = [
     {
        'Name': 'Fortnite',
        'Genre': 'Shooter',
        'Developer':'Epic Games',
        'Classification ESRB':'T(teen)'
     },
     {
        'Name': 'Grand Theft Auto',
        'Genre': 'Action',
        'Developer':'Rockstar Games',
        'Classification ESRB':'T(teen)'     
     },
     {
        'Name': 'Valorant',
        'Genre':'Shooter',
        'Developer':'Riot Games',
        'Classification ESRB':'T(teen)'
     },
     {
    
        'Name': 'Minecraft',
        'Genre': 'Sandbox',
        'Developer': 'Mojang Studios',
        'Classification ESRB': 'E10+ (Everyone 10+)'

     }
     ]


video_game_rank("Rating_file.csv", games_ranked)