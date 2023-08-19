# Tribals-Wars-World-Data-Scrapper
Tribal Wars world data scrapper rekindled and updated from the old tw_bot repository. The purpose of this simple now standalone module is to create a wrapper around the tribalwars world statistics and jsonify the output.
The module is built around a single class 'World', 7 methods and 1 property. It uses the world "br130", "pt103" as input. It should work for every country.

<p align="center">
  <img src="images/classdiagram.png"/> 
</p>
<p align="center"> World class diagram </p>

There are 5 fundamental data types:
- object.get_player() -> players json
- object.get_villages() -> villages data
- object.get_ally() -> alliances data
- object.get_oda() -> player offensive points data
- object.get_odd() -> player defensive points data

### object.get_player()
Template output:
```json
   player_id:{
      "player_id": str,
      "name": str,
      "ally_id": int,
      "num_vill": int,
      "points":" int,
      "rank":" int,
      "datetime": datetime
   }
```

### object.get_ally()
Template:
```json
   ally_id:{
     'ally_id': int,
     'name': str,
     'tag': str,
     'members': int,
     'num_vill': int,
     'points': int,
     'total_points': int,
     'rank': int
   }
```

### object.get_odd()
Template:
```json
   'player_id': {
     'rank': int,
     'player_id': int,
     'points': int
  }
```

### object.get_oda()
Template:
```json
   'player_id': {
     'rank': int,
     'player_id': int,
     'points': int
  },
```
