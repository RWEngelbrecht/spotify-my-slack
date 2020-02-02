"""
Emoji-related utlities
"""

# Map of lowercase strings to emojis. Ordered in decending preference
# https://www.webpagefx.com/tools/emoji-cheat-sheet/
EMOJI_MAP = {
  "alien": ":alien:",
  "ufo": ":alien:",
  "heartbreak": ":broken_heart:",
  "heart break": ":broken_heart:",
  "broken heart": ":broken_heart:",
  "space": ":alien:",
  "innocent": ":innocent:",
  "evil": ":smiling_imp:",
  "yum": ":yum:",
  "yummy": ":yum:",
  "delicious": ":yum:",
  "cupid": ":cupid:",
  "sweat": ":sweat:",
  "sweaty": ":sweat:",
  "workout": ":muscle:",
  "work out": ":muscle:",
  "star": ":star:",
  "cat": ":cat:",
  "kitty": ":cat:",
  "pig": ":pig:",
  "monkey": ":monkey:",
  "sheep": ":sheep:",
  "boom": ":boom:",
  "explosion": ":boom:",
  "crash": ":boom:",
  "fart": ":dash:",
  "poop": ":poop:",
  "shit": ":poop:",
  "muscle": ":muscle:",
  "run": ":runner:",
  "running": ":runner:",
  "runner": ":runner:",
  "clap": ":clap:",
  "kiss": ":kiss:",
  "lips": ":lips:",
  "sleeping": ":sleeping:",
  "sleep": ":sleeping:",
  "sea": ":ocean:",
  "ocean": ":ocean:",
  "wave": ":ocean:",
  "waves": ":ocean:",
  "water": ":ocean:",
  "waters": ":ocean:",
  "tired": ":sleeping:",
  "looking": ":eyes:",
  "money": ":money_with_wings:",
  "millionaire": ":money_with_wings:",
  "billionaire": ":money_with_wings:",
  "rage": ":rage:",
  "angry": ":angry:",
  "anger": ":angry:",
  "mad": ":angry:",
  "hate": ":angry:",
  "sunny": ":sunny:",
  "sun": ":sunny:",
  "snow": ":snowflake:",
  "snowflake": ":snowflake:",
  "snowy": ":snowflake:",
  "rain": ":droplet:",
  "rainy": ":droplet:",
  "raining": ":droplet:",
  "cloud": ":cloud:",
  "cloudy": ":cloud:",
  "moon": ":full_moon:",
  "cool": ":sunglasses:",
  "wind": ":dash:",
  "fast": ":dash:",
  "eyes": ":eyes:",
  "eye": ":eyes:",
  "hello": ":wave:",
  "love": ":heart:",
  "heart": ":heart:",
  "ghost": ":ghost:",
  "scary": ":ghost:",
  "halloween": ":ghost:",
  "fire": ":fire:",
  "hot": ":fire:",
  "burn": ":fire:",
  "night": ":sparkles:",
  "forest": ":evergreen_tree:",
  "tree": ":evergreen_tree:",
  "hug": ":hugging_face:",
  "hugging": ":hugging_face:",
  "party": ":tada:",
  "parties": ":tada:",
  "peach": ":peach:",
  "peaches": ":peach:",
  "lemon": ":lemon:",
  "lemons": ":lemon:",
  "lemonade": ":lemon:",
  "smile": ":grin:",
  "smiles": ":grin:",
  "smiling": ":grin:",
  "laugh": ":laughing:",
  "laughing": ":laughing:",
  "laughs": ":laughing:",
  "laughed": ":laughing:",
  "cowboy": ":face_with_cowboy_hat:",
  "cowboys": ":face_with_cowboy_hat:",
  "star struck": ":star-struck:",
  "clown": ":clown_face:",
  "clowns": ":clown_face:",
  "skull": ":skull:",
  "skulls": ":skull:",
  "robot": ":robot_face:",
  "robots": ":robot_face:",
  "die": ":skull:",
  "dies": ":skull:",
  "dead": ":skull:",
  "died": ":skull:",
  "dying": ":skull:",
  "angel": ":angel:",
  "angels": ":angel:",
  "dance": ":dancer:",
  "dancing": ":dancer:",
  "dances": ":dancer:",
  "dancer": ":dancer:",
  "dancers": ":dancer:",
  "danced": ":dancer:",
  "stars": ":star:",
  "selfie": ":selfie:",
  "selfies": ":selfie:",
  "strong": ":muscle:",
  "stronger": ":muscle:",
  "write": ":writing_hand:",
  "writer": ":writing_hand:",
  "letter": ":love_letter:",
  "letters": ":love_letter:",
  "talk": ":speech_balloon:",
  "talks": ":speech_balloon:",
  "talking": ":speech_balloon:",
  "say": ":speech_balloon:",
  "sunglasses": ":dark_sunglasses:",
  "jeans": ":jeans:",
  "dress": ":dress:",
  "dresses": ":dress:",
  "kimono": ":kimono:",
  "kimonos": ":kimono:",
  "bikini": ":bikini:",
  "bikinis": ":bikini:",
  "crown": ":crown:",
  "crowns": ":crown:",
  "princess": ":princess:",
  "prince": ":prince:",
  "ring": ":ring:",
  "rings": ":ring:",
  "diamond": ":gem:",
  "gem": ":gem:",
  "diamonds": ":gem:",
  "lipstick": ":lipstick:",
  "dog": ":dog:",
  "dogs": ":dog:",
  "puppy": ":dog:",
  "puppies": ":dog:",
  "wolf": ":wolf:",
  "wolves": ":wolf:",
  "fox": ":fox_face:",
  "foxes": ":fox_face:",
  "lion": ":lion_face:",
  "lions": ":lion_face:",
  "tiger": ":tiger:",
  "tigers": ":tiger:",
  "horse": ":horse:",
  "horses": ":horse:",
  "unicorn": ":unicorn_face:",
  "unicorns": ":unicorn_face:",
  "zebra": ":zebra_face:",
  "zebras": ":zebra_face:",
  "deer": ":deer:",
  "cow": ":cow:",
  "cows": ":cow:",
  "goat": ":goat:",
  "goats": ":goat:",
  "camel": ":dromedary_camel:",
  "camels": ":dromedary_camel:",
  "giraffe": ":giraffe_face:",
  "elephant": ":elephant:",
  "elephants": ":elephant:",
  "gorilla": ":gorilla:",
  "gorillas": ":gorilla:",
  "mouse": ":mouse:",
  "mice": ":mouse:",
  "feet": ":footprints:",
  "foot": ":footprints:",
  "footprints": ":footprints:",
  "footsteps": ":footsteps:",
  "footstep": ":footstep:",
  "whale": ":whale:",
  "dolphin": ":dolphin:",
  "fish": ":fish:",
  "shark": ":shark:",
  "sharks": ":shark:",
  "octopus": ":octopus:",
  "shell": ":shell:",
  "shells": ":shell:",
  "crab": ":crab:",
  "crabs": ":crab:",
  "shrimp": ":shrimp:",
  "squid": ":squid:",
  "snail": ":snail:",
  "butterfly": ":butterfly:",
  "butterflies": ":butterfly:",
  "bee": ":bee:",
  "bees": ":bee:",
  "spider": ":spider:",
  "spiders": ":spider:",
  "spiderweb": ":spider_web:",
  "spiderwebs": ":spider_web:",
  "spider web": ":spider_web:",
  "spider webs": ":spider_web:",
  "scorpion": ":scorpion:",
  "scorpions": ":scorpion:",
  "flower": ":cherry_blossom:",
  "rose": ":rose:",
  "roses": ":rose:",
  "sunflower": ":sunflower:",
  "sunflowers": ":sunflower:",
  "flowers": ":bouquet:",
  "leaves": ":leaves:",
  "leaf": ":leaves:",
  "pray": ":pray:",
  "prays": ":pray:",
  "punch": ":facepunch:",
  "fist": ":facepunch:",
  "grape": ":grape:",
  "grapes": ":grape:",
  "watermelon": ":watermelon:",
  "orange": ":tangerine:",
  "oranges": ":tangerine:",
  "banana": ":banana:",
  "bananas": ":banana:",
  "pineapple": ":pineapple:",
  "apple": ":apple:",
  "cherry": ":cherries:",
  "cherries": ":cherries:",
  "strawberry": ":strawberry:",
  "strawberres": ":strawberry:",
  "kiwi": ":kiwifruit:",
  "tomato": ":tomato:",
  "pepper": ":hot_pepper:",
  "peppers": ":hot_pepper:",
  "broccoli": ":broccoli:",
  "bread": ":bread:",
  "cheese": ":cheese_wedge:",
  "cheesy": ":cheese_wedge:",
  "taco": ":taco:",
  "tacos": ":taco:",
  "burrito": ":burrito:",
  "burritos": ":burrito:",
  "egg": ":egg:",
  "eggs": ":egg:",
  "icecream": ":icecream:",
  "ice cream": ":icecream:",
  "middle finger": ":middle_finger:",
  "cookie": ":cookie:",
  "cookies": ":cookie:",
  "birthday": ":birthday:",
  "birthdays": ":birthday:",
  "cake": ":cake:",
  "pie": ":pie:",
  "pies": ":pie:",
  "chocolate": ":chocolate_bar:",
  "candy": ":candy:",
  "candies": ":candy:",
  "lollipop": ":lollipop:",
  "honey": ":honey_pot:",
  "tea": ":tea:",
  "coffee": ":coffee:",
  "champagne": ":champagne:",
  "wine": ":wine_glass:",
  "cocktail": ":cocktail:",
  "cocktails": ":cocktail:",
  "beer": ":beer:",
  "beers": ":beer:",
  "knife": ":knife:",
  "balloon": ":balloon:",
  "balloons": ":balloon:",
  "win": ":trophy:",
  "winner": ":trophy:",
  "winning": ":trophy:",
  "video game": ":video_game:",
  "video games": ":video_game:",
  "gamble": ":game_die:",
  "gambles": ":game_die:",
  "gambler": ":game_die:",
  "gambling": ":game_die:",
  "world": ":earth_americas:",
  "worlds": ":earth_americas:",
  "earth": ":earth_americas:",
  "island": ":desert_island:",
  "islands": ":desert_island:",
  "tropical": ":desert_island:",
  "tropic": ":desert_island:",
  "tropics": ":desert_island:",
  "mountain": ":mountain:",
  "mountains": ":mountain:",
  "home": ":house:",
  "homeward": ":house:",
  "house": ":house:",
  "lightning": ":zap:",
  "electric": ":zap:",
  "electricity": ":zap:",
  "rainbow": ":rainbow:",
  "umbrella": ":umbrella:",
  "bell": ":bell:",
  "call": ":phone:",
  "phone": ":phone:",
  "sing": ":microphone:",
  "sings": ":microphone:",
  "singing": ":microphone:",
  "light": ":bulb:",
  "lights": ":bulb:",
  "lock": ":lock:",
  "scale": ":scales:",
  "key": ":key:",
  "keys": ":key:",
  "scissors": ":scissors:",
  "cut": ":scissors:",
  "cuts": ":scissors:",
  "america": ":us:",
  "american": ":us:",
  "pill": ":pill:",
  "pills": ":pill:",
  "chain": ":chains:",
  "chains": ":chains:",
  "movie": ":clapper:",
  "movies": ":clapper:",
  "hush": ":shushing_face:",
  "shh": ":shushing_face:",
  "quiet": ":shushing_face:",
  "cry": ":cry:",
  "cries": ":cry:",
  "cried": ":cry:",
  "crying": ":cry:",
  "nerd": ":nerd_face:",
  "up": ":point_up:",
  "down": ":point_down:",
  "snake": ":snake:",
  "snakes": ":snake:",
  "firework": ":fireworks:",
  "fireworks": ":fireworks:",
  "gift": ":gift:",
  "gifts": ":gift:",
  "tennis": ":tennis:",
  "roller coaster": ":roller_coaster:",
  "rollercoaster": ":roller_coaster:",
  "carousel": ":carousel_horse:",
  "circus": ":circus_tent:",
  "art": ":art:",
  "church": ":church:",
  "churches": ":church:",
  "tent": ":tent:",
  "wait": ":hourglass_flowing_sand:",
  "waiting": ":hourglass_flowing_sand:",
  "waits": ":hourglass_flowing_sand:",
  "time": ":alarm_clock:",
  "pancake": ":pancakes:",
  "pancakes": ":pancakes:",
  "bird": ":bird:",
  "birds": ":bird:",
  "bed": ":bed:",
  "beds": ":bed:",
  "bride": ":bride_with_veil:",
  "wedding": ":wedding:",
  "marry": ":wedding:",
  "weddings": ":wedding:",
}
DEFAULT_EMOJIS = [":headphones:", ":notes:", ":musical_note:"]
