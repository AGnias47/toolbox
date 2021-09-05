HREF=$(cat ahmad.json | jq ".artists.href")
echo $HREF
GENRES=$(cat ahmad.json | jq ".artists.items"[0]".genres")
echo $GENRES
