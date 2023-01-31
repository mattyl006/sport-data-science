from statsbombpy import sb
import sys

if len(sys.argv) > 1:
    season_id = int(sys.argv[1])
else:
    season_id = 235

competitions = sb.competitions()
matches = sb.matches(competition_id=38, season_id=235)
matches.to_csv("matches.csv", encoding="utf-8", index=False)