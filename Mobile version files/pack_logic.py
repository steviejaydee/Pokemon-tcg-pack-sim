import random
import collections

# --- Set Data ---
# This dictionary holds all the data for each available Pokémon TCG set.
SETS_DATA = {
            "Scarlet & Violet - Base Set": {
        "pull_rates": {
            "P_DR": 1/8, "P_IR": 1/13, "P_UR": 1/15, "P_SIR": 1/30, "P_HR": 1/56
        },
        "card_database": {
            "Common": [
                ("Pineco", "SVI", "001", "Common", "Pokémon"), ("Shroomish", "SVI", "003", "Common", "Pokémon"),
                ("Cacnea", "SVI", "005", "Common", "Pokémon"), ("Tropius", "SVI", "007", "Common", "Pokémon"),
                ("Scatterbug", "SVI", "008", "Common", "Pokémon"), ("Spewpa", "SVI", "009", "Common", "Pokémon"),
                ("Skiddo", "SVI", "011", "Common", "Pokémon"), ("Gogoat", "SVI", "012", "Common", "Pokémon"),
                ("Sprigatito", "SVI", "013", "Common", "Pokémon"), ("Tarountula", "SVI", "016", "Common", "Pokémon"),
                ("Tarountula", "SVI", "017", "Common", "Pokémon"), ("Tarountula", "SVI", "018", "Common", "Pokémon"),
                ("Smoliv", "SVI", "020", "Common", "Pokémon"), ("Smoliv", "SVI", "021", "Common", "Pokémon"),
                ("Dolliv", "SVI", "022", "Common", "Pokémon"), ("Toedscool", "SVI", "024", "Common", "Pokémon"),
                ("Toedscool", "SVI", "025", "Common", "Pokémon"), ("Capsakid", "SVI", "027", "Common", "Pokémon"),
                ("Capsakid", "SVI", "028", "Common", "Pokémon"), ("Growlithe", "SVI", "030", "Common", "Pokémon"),
                ("Growlithe", "SVI", "031", "Common", "Pokémon"), ("Houndour", "SVI", "033", "Common", "Pokémon"),
                ("Houndoom", "SVI", "034", "Common", "Pokémon"), ("Fuecoco", "SVI", "036", "Common", "Pokémon"),
                ("Charcadet", "SVI", "039", "Common", "Pokémon"), ("Charcadet", "SVI", "040", "Common", "Pokémon"),
                ("Slowpoke", "SVI", "042", "Common", "Pokémon"), ("Magikarp", "SVI", "044", "Common", "Pokémon"),
                ("Buizel", "SVI", "046", "Common", "Pokémon"), ("Alomomola", "SVI", "048", "Common", "Pokémon"),
                ("Clauncher", "SVI", "049", "Common", "Pokémon"), ("Clawitzer", "SVI", "050", "Common", "Pokémon"),
                ("Bruxish", "SVI", "051", "Common", "Pokémon"), ("Quaxly", "SVI", "052", "Common", "Pokémon"),
                ("Wiglett", "SVI", "055", "Common", "Pokémon"), ("Wiglett", "SVI", "056", "Common", "Pokémon"),
                ("Cetoddle", "SVI", "058", "Common", "Pokémon"), ("Cetoddle", "SVI", "059", "Common", "Pokémon"),
                ("Magnemite", "SVI", "063", "Common", "Pokémon"), ("Magneton", "SVI", "064", "Common", "Pokémon"),
                ("Mareep", "SVI", "066", "Common", "Pokémon"), ("Rotom", "SVI", "069", "Common", "Pokémon"),
                ("Rotom", "SVI", "070", "Common", "Pokémon"), ("Toxel", "SVI", "071", "Common", "Pokémon"),
                ("Pawmi", "SVI", "073", "Common", "Pokémon"), ("Pawmi", "SVI", "074", "Common", "Pokémon"),
                ("Pawmo", "SVI", "075", "Common", "Pokémon"), ("Wattrel", "SVI", "077", "Common", "Pokémon"),
                ("Wattrel", "SVI", "078", "Common", "Pokémon"), ("Drowzee", "SVI", "082", "Common", "Pokémon"),
                ("Ralts", "SVI", "084", "Common", "Pokémon"), ("Kirlia", "SVI", "085", "Common", "Pokémon"),
                ("Shuppet", "SVI", "087", "Common", "Pokémon"), ("Drifloon", "SVI", "089", "Common", "Pokémon"),
                ("Flabébé", "SVI", "091", "Common", "Pokémon"), ("Floette", "SVI", "092", "Common", "Pokémon"),
                ("Dedenne", "SVI", "094", "Common", "Pokémon"), ("Dedenne", "SVI", "095", "Common", "Pokémon"),
                ("Fidough", "SVI", "097", "Common", "Pokémon"), ("Fidough", "SVI", "098", "Common", "Pokémon"),
                ("Flittle", "SVI", "100", "Common", "Pokémon"), ("Flittle", "SVI", "101", "Common", "Pokémon"),
                ("Flittle", "SVI", "102", "Common", "Pokémon"), ("Greavard", "SVI", "104", "Common", "Pokémon"),
                ("Greavard", "SVI", "105", "Common", "Pokémon"), ("Mankey", "SVI", "107", "Common", "Pokémon"),
                ("Primeape", "SVI", "108", "Common", "Pokémon"), ("Meditite", "SVI", "110", "Common", "Pokémon"),
                ("Riolu", "SVI", "112", "Common", "Pokémon"), ("Riolu", "SVI", "113", "Common", "Pokémon"),
                ("Sandile", "SVI", "115", "Common", "Pokémon"), ("Krokorok", "SVI", "116", "Common", "Pokémon"),
                ("Silicobra", "SVI", "119", "Common", "Pokémon"), ("Grimer", "SVI", "126", "Common", "Pokémon"),
                ("Seviper", "SVI", "128", "Common", "Pokémon"), ("Croagunk", "SVI", "130", "Common", "Pokémon"),
                ("Pawniard", "SVI", "132", "Common", "Pokémon"), ("Bisharp", "SVI", "133", "Common", "Pokémon"),
                ("Maschiff", "SVI", "135", "Common", "Pokémon"), ("Maschiff", "SVI", "136", "Common", "Pokémon"),
                ("Varoom", "SVI", "140", "Common", "Pokémon"), ("Varoom", "SVI", "141", "Common", "Pokémon"),
                ("Chansey", "SVI", "144", "Common", "Pokémon"), ("Zangoose", "SVI", "146", "Common", "Pokémon"),
                ("Starly", "SVI", "148", "Common", "Pokémon"), ("Staravia", "SVI", "149", "Common", "Pokémon"),
                ("Skwovet", "SVI", "151", "Common", "Pokémon"), ("Lechonk", "SVI", "154", "Common", "Pokémon"),
                ("Lechonk", "SVI", "155", "Common", "Pokémon"), ("Lechonk", "SVI", "156", "Common", "Pokémon"),
                ("Tandemaus", "SVI", "159", "Common", "Pokémon"), ("Tandemaus", "SVI", "160", "Common", "Pokémon"),
                ("Squawkabilly", "SVI", "162", "Common", "Pokémon"), ("Crushing Hammer", "SVI", "168", "Common", "Trainer"),
                ("Energy Retrieval", "SVI", "171", "Common", "Trainer"), ("Energy Search", "SVI", "172", "Common", "Trainer"),
                ("Energy Switch", "SVI", "173", "Common", "Trainer"), ("Nemona", "SVI", "180", "Common", "Trainer"),
                ("Pal Pad", "SVI", "182", "Common", "Trainer"), ("Poké Ball", "SVI", "185", "Common", "Trainer"),
                ("Pokégear 3.0", "SVI", "186", "Common", "Trainer"), ("Pokémon Catcher", "SVI", "187", "Common", "Trainer"),
                ("Potion", "SVI", "188", "Common", "Trainer"), ("Rare Candy", "SVI", "191", "Common", "Trainer"),
                ("Switch", "SVI", "194", "Common", "Trainer")
            ],
            "Uncommon": [
                ("Heracross", "SVI", "002", "Uncommon", "Pokémon"), ("Breloom", "SVI", "004", "Uncommon", "Pokémon"),
                ("Cacturne", "SVI", "006", "Uncommon", "Pokémon"), ("Vivillon", "SVI", "010", "Uncommon", "Pokémon"),
                ("Floragato", "SVI", "014", "Uncommon", "Pokémon"), ("Toedscruel", "SVI", "026", "Uncommon", "Pokémon"),
                ("Scovillain", "SVI", "029", "Uncommon", "Pokémon"), ("Torkoal", "SVI", "035", "Uncommon", "Pokémon"),
                ("Crocalor", "SVI", "037", "Uncommon", "Pokémon"), ("Floatzel", "SVI", "047", "Uncommon", "Pokémon"),
                ("Quaxwell", "SVI", "053", "Uncommon", "Pokémon"), ("Wugtrio", "SVI", "057", "Uncommon", "Pokémon"),
                ("Cetitan", "SVI", "060", "Uncommon", "Pokémon"), ("Tatsugiri", "SVI", "062", "Uncommon", "Pokémon"),
                ("Flaaffy", "SVI", "067", "Uncommon", "Pokémon"), ("Pachirisu", "SVI", "068", "Uncommon", "Pokémon"),
                ("Toxtricity", "SVI", "072", "Uncommon", "Pokémon"), ("Kilowattrel", "SVI", "079", "Uncommon", "Pokémon"),
                ("Hypno", "SVI", "083", "Uncommon", "Pokémon"), ("Drifblim", "SVI", "090", "Uncommon", "Pokémon"),
                ("Florges", "SVI", "093", "Uncommon", "Pokémon"), ("Dachsbun", "SVI", "099", "Uncommon", "Pokémon"),
                ("Espathra", "SVI", "103", "Uncommon", "Pokémon"), ("Medicham", "SVI", "111", "Uncommon", "Pokémon"),
                ("Lucario", "SVI", "114", "Uncommon", "Pokémon"), ("Krookodile", "SVI", "117", "Uncommon", "Pokémon"),
                ("Sandaconda", "SVI", "120", "Uncommon", "Pokémon"), ("Stonjourner", "SVI", "121", "Uncommon", "Pokémon"),
                ("Muk", "SVI", "127", "Uncommon", "Pokémon"), ("Spiritomb", "SVI", "129", "Uncommon", "Pokémon"),
                ("Mabosstiff", "SVI", "137", "Uncommon", "Pokémon"), ("Bombirdier", "SVI", "138", "Uncommon", "Pokémon"),
                ("Forretress", "SVI", "139", "Uncommon", "Pokémon"), ("Blissey", "SVI", "145", "Uncommon", "Pokémon"),
                ("Zangoose", "SVI", "147", "Uncommon", "Pokémon"), ("Staraptor", "SVI", "150", "Uncommon", "Pokémon"),
                ("Greedent", "SVI", "152", "Uncommon", "Pokémon"), ("Oinkologne", "SVI", "157", "Uncommon", "Pokémon"),
                ("Maushold", "SVI", "161", "Uncommon", "Pokémon"), ("Cyclizar", "SVI", "163", "Uncommon", "Pokémon"),
                ("Flamigo", "SVI", "165", "Uncommon", "Pokémon"), ("Arven", "SVI", "166", "Uncommon", "Trainer"),
                ("Beach Court", "SVI", "167", "Uncommon", "Trainer"), ("Defiance Band", "SVI", "169", "Uncommon", "Trainer"),
                ("Electric Generator", "SVI", "170", "Uncommon", "Trainer"), ("Exp. Share", "SVI", "174", "Uncommon", "Trainer"),
                ("Jacq", "SVI", "175", "Uncommon", "Trainer"), ("Judge", "SVI", "176", "Uncommon", "Trainer"),
                ("Katy", "SVI", "177", "Uncommon", "Trainer"), ("Mesagoza", "SVI", "178", "Uncommon", "Trainer"),
                ("Miriam", "SVI", "179", "Uncommon", "Trainer"), ("Nest Ball", "SVI", "181", "Uncommon", "Trainer"),
                ("Penny", "SVI", "183", "Uncommon", "Trainer"), ("Picnic Basket", "SVI", "184", "Uncommon", "Trainer"),
                ("Rock Chestplate", "SVI", "192", "Uncommon", "Trainer"), ("Rocky Helmet", "SVI", "193", "Uncommon", "Trainer"),
                ("Team Star Grunt", "SVI", "195", "Uncommon", "Trainer"), ("Ultra Ball", "SVI", "196", "Uncommon", "Trainer"),
                ("Vitality Band", "SVI", "197", "Uncommon", "Trainer"), ("Youngster", "SVI", "198", "Uncommon", "Trainer")
            ],
            "Rare": [
                ("Meowscarada", "SVI", "015", "Rare", "Pokémon"), ("Arboliva", "SVI", "023", "Rare", "Pokémon"),
                ("Skeledirge", "SVI", "038", "Rare", "Pokémon"), ("Armarouge", "SVI", "041", "Rare", "Pokémon"),
                ("Slowbro", "SVI", "043", "Rare", "Pokémon"), ("Quaquaval", "SVI", "054", "Rare", "Pokémon"),
                ("Dondozo", "SVI", "061", "Rare", "Pokémon"), ("Pawmot", "SVI", "076", "Rare", "Pokémon"),
                ("Miraidon", "SVI", "080", "Rare", "Pokémon"), ("Klefki", "SVI", "096", "Rare", "Pokémon"),
                ("Houndstone", "SVI", "106", "Rare", "Pokémon"), ("Annihilape", "SVI", "109", "Rare", "Pokémon"),
                ("Hawlucha", "SVI", "118", "Rare", "Pokémon"), ("Klawf", "SVI", "122", "Rare", "Pokémon"),
                ("Koraidon", "SVI", "124", "Rare", "Pokémon"), ("Kingambit", "SVI", "134", "Rare", "Pokémon"),
                ("Revavroom", "SVI", "142", "Rare", "Pokémon"), ("Indeedee", "SVI", "153", "Rare", "Pokémon"),
                ("Cyclizar", "SVI", "164", "Rare", "Pokémon"), ("Professor’s Research", "SVI", "189", "Rare", "Trainer"),
                ("Professor’s Research", "SVI", "190", "Rare", "Trainer")
            ],
            "Double Rare": [
                ("Spidops ex", "SVI", "019", "Double Rare", "Pokémon"), ("Arcanine ex", "SVI", "032", "Double Rare", "Pokémon"),
                ("Gyarados ex", "SVI", "045", "Double Rare", "Pokémon"), ("Magnezone ex", "SVI", "065", "Double Rare", "Pokémon"),
                ("Miraidon ex", "SVI", "081", "Double Rare", "Pokémon"), ("Gardevoir ex", "SVI", "086", "Double Rare", "Pokémon"),
                ("Banette ex", "SVI", "088", "Double Rare", "Pokémon"), ("Great Tusk ex", "SVI", "123", "Double Rare", "Pokémon"),
                ("Koraidon ex", "SVI", "125", "Double Rare", "Pokémon"), ("Toxicroak ex", "SVI", "131", "Double Rare", "Pokémon"),
                ("Iron Treads ex", "SVI", "143", "Double Rare", "Pokémon"), ("Oinkologne ex", "SVI", "158", "Double Rare", "Pokémon")
            ],
            "Illustration Rare": [
                ("Tarountula", "SVI", "199", "Illustration Rare", "Pokémon"), ("Dolliv", "SVI", "200", "Illustration Rare", "Pokémon"),
                ("Toedscool", "SVI", "201", "Illustration Rare", "Pokémon"), ("Scovillain", "SVI", "202", "Illustration Rare", "Pokémon"),
                ("Armarouge", "SVI", "203", "Illustration Rare", "Pokémon"), ("Slowpoke", "SVI", "204", "Illustration Rare", "Pokémon"),
                ("Clauncher", "SVI", "205", "Illustration Rare", "Pokémon"), ("Wiglett", "SVI", "206", "Illustration Rare", "Pokémon"),
                ("Dondozo", "SVI", "207", "Illustration Rare", "Pokémon"), ("Pachirisu", "SVI", "208", "Illustration Rare", "Pokémon"),
                ("Pawmot", "SVI", "209", "Illustration Rare", "Pokémon"), ("Drowzee", "SVI", "210", "Illustration Rare", "Pokémon"),
                ("Ralts", "SVI", "211", "Illustration Rare", "Pokémon"), ("Kirlia", "SVI", "212", "Illustration Rare", "Pokémon"),
                ("Fidough", "SVI", "213", "Illustration Rare", "Pokémon"), ("Greavard", "SVI", "214", "Illustration Rare", "Pokémon"),
                ("Riolu", "SVI", "215", "Illustration Rare", "Pokémon"), ("Sandile", "SVI", "216", "Illustration Rare", "Pokémon"),
                ("Klawf", "SVI", "217", "Illustration Rare", "Pokémon"), ("Mabosstiff", "SVI", "218", "Illustration Rare", "Pokémon"),
                ("Bombirdier", "SVI", "219", "Illustration Rare", "Pokémon"), ("Kingambit", "SVI", "220", "Illustration Rare", "Pokémon"),
                ("Starly", "SVI", "221", "Illustration Rare", "Pokémon"), ("Skwovet", "SVI", "222", "Illustration Rare", "Pokémon")
            ],
            "Ultra Rare": [
                ("Spidops ex", "SVI", "223", "Ultra Rare", "Pokémon"), ("Arcanine ex", "SVI", "224", "Ultra Rare", "Pokémon"),
                ("Gyarados ex", "SVI", "225", "Ultra Rare", "Pokémon"), ("Magnezone ex", "SVI", "226", "Ultra Rare", "Pokémon"),
                ("Miraidon ex", "SVI", "227", "Ultra Rare", "Pokémon"), ("Gardevoir ex", "SVI", "228", "Ultra Rare", "Pokémon"),
                ("Banette ex", "SVI", "229", "Ultra Rare", "Pokémon"), ("Great Tusk ex", "SVI", "230", "Ultra Rare", "Pokémon"),
                ("Koraidon ex", "SVI", "231", "Ultra Rare", "Pokémon"), ("Toxicroak ex", "SVI", "232", "Ultra Rare", "Pokémon"),
                ("Iron Treads ex", "SVI", "233", "Ultra Rare", "Pokémon"), ("Oinkologne ex", "SVI", "234", "Ultra Rare", "Pokémon"),
                ("Arven", "SVI", "235", "Ultra Rare", "Trainer"), ("Jacq", "SVI", "236", "Ultra Rare", "Trainer"),
                ("Katy", "SVI", "237", "Ultra Rare", "Trainer"), ("Miriam", "SVI", "238", "Ultra Rare", "Trainer"),
                ("Penny", "SVI", "239", "Ultra Rare", "Trainer"), ("Professor’s Research", "SVI", "240", "Ultra Rare", "Trainer"),
                ("Professor’s Research", "SVI", "241", "Ultra Rare", "Trainer"), ("Team Star Grunt", "SVI", "242", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Spidops ex", "SVI", "243", "Special Illustration Rare", "Pokémon"), ("Miraidon ex", "SVI", "244", "Special Illustration Rare", "Pokémon"),
                ("Gardevoir ex", "SVI", "245", "Special Illustration Rare", "Pokémon"), ("Great Tusk ex", "SVI", "246", "Special Illustration Rare", "Pokémon"),
                ("Koraidon ex", "SVI", "247", "Special Illustration Rare", "Pokémon"), ("Iron Treads ex", "SVI", "248", "Special Illustration Rare", "Pokémon"),
                ("Arven", "SVI", "249", "Special Illustration Rare", "Trainer"), ("Jacq", "SVI", "250", "Special Illustration Rare", "Trainer"),
                ("Miriam", "SVI", "251", "Special Illustration Rare", "Trainer"), ("Penny", "SVI", "252", "Special Illustration Rare", "Trainer")
            ],
            "Hyper Rare": [
                ("Miraidon ex", "SVI", "253", "Hyper Rare", "Pokémon"), ("Koraidon ex", "SVI", "254", "Hyper Rare", "Pokémon"),
                ("Nest Ball", "SVI", "255", "Hyper Rare", "Trainer"), ("Rare Candy", "SVI", "256", "Hyper Rare", "Trainer"),
                ("Basic Lightning Energy", "SVI", "257", "Hyper Rare", "Energy"), ("Basic Fighting Energy", "SVI", "258", "Hyper Rare", "Energy")
            ]
        }
    },
        "Paldea Evolved": {
        "pull_rates": {
            "P_DR": 1/7, "P_IR": 1/13, "P_UR": 1/15, "P_SIR": 1/31, "P_HR": 1/53
        },
        "card_database": {
            "Common": [
                ("Hoppip", "PAL", "001", "Common", "Pokémon"), ("Pineco", "PAL", "004", "Common", "Pokémon"),
                ("Tropius", "PAL", "007", "Common", "Pokémon"), ("Combee", "PAL", "008", "Common", "Pokémon"),
                ("Snover", "PAL", "010", "Common", "Pokémon"), ("Sprigatito", "PAL", "012", "Common", "Pokémon"),
                ("Sprigatito", "PAL", "013", "Common", "Pokémon"), ("Tarountula", "PAL", "016", "Common", "Pokémon"),
                ("Tarountula", "PAL", "017", "Common", "Pokémon"), ("Nymble", "PAL", "019", "Common", "Pokémon"),
                ("Nymble", "PAL", "020", "Common", "Pokémon"), ("Bramblin", "PAL", "022", "Common", "Pokémon"),
                ("Bramblin", "PAL", "023", "Common", "Pokémon"), ("Rellor", "PAL", "025", "Common", "Pokémon"),
                ("Rellor", "PAL", "026", "Common", "Pokémon"), ("Litleo", "PAL", "031", "Common", "Pokémon"),
                ("Fuecoco", "PAL", "034", "Common", "Pokémon"), ("Fuecoco", "PAL", "035", "Common", "Pokémon"),
                ("Charcadet", "PAL", "038", "Common", "Pokémon"), ("Charcadet", "PAL", "039", "Common", "Pokémon"),
                ("Magikarp", "PAL", "042", "Common", "Pokémon"), ("Marill", "PAL", "044", "Common", "Pokémon"),
                ("Delibird", "PAL", "046", "Common", "Pokémon"), ("Luvdisc", "PAL", "047", "Common", "Pokémon"),
                ("Quaxly", "PAL", "049", "Common", "Pokémon"), ("Quaxly", "PAL", "050", "Common", "Pokémon"),
                ("Cetoddle", "PAL", "053", "Common", "Pokémon"), ("Cetoddle", "PAL", "054", "Common", "Pokémon"),
                ("Frigibax", "PAL", "057", "Common", "Pokémon"), ("Frigibax", "PAL", "058", "Common", "Pokémon"),
                ("Pikachu", "PAL", "062", "Common", "Pokémon"), ("Magnemite", "PAL", "065", "Common", "Pokémon"),
                ("Voltorb", "PAL", "066", "Common", "Pokémon"), ("Shinx", "PAL", "068", "Common", "Pokémon"),
                ("Shinx", "PAL", "069", "Common", "Pokémon"), ("Pincurchin", "PAL", "072", "Common", "Pokémon"),
                ("Pawmi", "PAL", "074", "Common", "Pokémon"), ("Tadbulb", "PAL", "077", "Common", "Pokémon"),
                ("Tadbulb", "PAL", "078", "Common", "Pokémon"), ("Wattrel", "PAL", "080", "Common", "Pokémon"),
                ("Wattrel", "PAL", "081", "Common", "Pokémon"), ("Jigglypuff", "PAL", "083", "Common", "Pokémon"),
                ("Slowpoke", "PAL", "085", "Common", "Pokémon"), ("Misdreavus", "PAL", "087", "Common", "Pokémon"),
                ("Gothita", "PAL", "090", "Common", "Pokémon"), ("Sandygast", "PAL", "095", "Common", "Pokémon"),
                ("Tinkatink", "PAL", "100", "Common", "Pokémon"), ("Tinkatink", "PAL", "101", "Common", "Pokémon"),
                ("Tinkatink", "PAL", "102", "Common", "Pokémon"), ("Mankey", "PAL", "106", "Common", "Pokémon"),
                ("Larvitar", "PAL", "110", "Common", "Pokémon"), ("Makuhita", "PAL", "112", "Common", "Pokémon"),
                ("Croagunk", "PAL", "114", "Common", "Pokémon"), ("Rockruff", "PAL", "116", "Common", "Pokémon"),
                ("Falinks", "PAL", "119", "Common", "Pokémon"), ("Nacli", "PAL", "120", "Common", "Pokémon"),
                ("Nacli", "PAL", "121", "Common", "Pokémon"), ("Glimmet", "PAL", "124", "Common", "Pokémon"),
                ("Glimmet", "PAL", "125", "Common", "Pokémon"), ("Paldean Wooper", "PAL", "128", "Common", "Pokémon"),
                ("Paldean Wooper", "PAL", "129", "Common", "Pokémon"), ("Murkrow", "PAL", "131", "Common", "Pokémon"),
                ("Sneasel", "PAL", "133", "Common", "Pokémon"), ("Deino", "PAL", "138", "Common", "Pokémon"),
                ("Maschiff", "PAL", "141", "Common", "Pokémon"), ("Maschiff", "PAL", "142", "Common", "Pokémon"),
                ("Shroodle", "PAL", "144", "Common", "Pokémon"), ("Shroodle", "PAL", "145", "Common", "Pokémon"),
                ("Cufant", "PAL", "149", "Common", "Pokémon"), ("Noibat", "PAL", "152", "Common", "Pokémon"),
                ("Girafarig", "PAL", "154", "Common", "Pokémon"), ("Dunsparce", "PAL", "156", "Common", "Pokémon"),
                ("Wingull", "PAL", "158", "Common", "Pokémon"), ("Slakoth", "PAL", "160", "Common", "Pokémon"),
                ("Fletchling", "PAL", "163", "Common", "Pokémon"), ("Rookidee", "PAL", "164", "Common", "Pokémon"),
                ("Tandemaus", "PAL", "166", "Common", "Pokémon"), ("Tandemaus", "PAL", "167", "Common", "Pokémon"),
                ("Clavell", "PAL", "177", "Common", "Trainer"), ("Great Ball", "PAL", "183", "Common", "Trainer"),
                ("Super Rod", "PAL", "188", "Common", "Trainer")
            ],
            "Uncommon": [
                ("Skiploom", "PAL", "002", "Uncommon", "Pokémon"), ("Heracross", "PAL", "006", "Uncommon", "Pokémon"),
                ("Vespiquen", "PAL", "009", "Uncommon", "Pokémon"), ("Floragato", "PAL", "014", "Uncommon", "Pokémon"),
                ("Spidops", "PAL", "018", "Uncommon", "Pokémon"), ("Brambleghast", "PAL", "024", "Uncommon", "Pokémon"),
                ("Paldean Tauros", "PAL", "028", "Uncommon", "Pokémon"), ("Fletchinder", "PAL", "029", "Uncommon", "Pokémon"),
                ("Talonflame", "PAL", "030", "Uncommon", "Pokémon"), ("Pyroar", "PAL", "032", "Uncommon", "Pokémon"),
                ("Crocalor", "PAL", "036", "Uncommon", "Pokémon"), ("Paldean Tauros", "PAL", "041", "Uncommon", "Pokémon"),
                ("Azumarill", "PAL", "045", "Uncommon", "Pokémon"), ("Eiscue", "PAL", "048", "Uncommon", "Pokémon"),
                ("Quaxwell", "PAL", "051", "Uncommon", "Pokémon"), ("Cetitan", "PAL", "055", "Uncommon", "Pokémon"),
                ("Arctibax", "PAL", "059", "Uncommon", "Pokémon"), ("Raichu", "PAL", "064", "Uncommon", "Pokémon"),
                ("Electrode", "PAL", "067", "Uncommon", "Pokémon"), ("Luxio", "PAL", "070", "Uncommon", "Pokémon"),
                ("Pincurchin", "PAL", "073", "Uncommon", "Pokémon"), ("Pawmo", "PAL", "075", "Uncommon", "Pokémon"),
                ("Kilowattrel", "PAL", "082", "Uncommon", "Pokémon"), ("Mismagius", "PAL", "088", "Uncommon", "Pokémon"),
                ("Gothorita", "PAL", "091", "Uncommon", "Pokémon"), ("Gothitelle", "PAL", "092", "Uncommon", "Pokémon"),
                ("Oranguru", "PAL", "094", "Uncommon", "Pokémon"), ("Palossand", "PAL", "096", "Uncommon", "Pokémon"),
                ("Tinkatuff", "PAL", "103", "Uncommon", "Pokémon"), ("Tinkatuff", "PAL", "104", "Uncommon", "Pokémon"),
                ("Primeape", "PAL", "107", "Uncommon", "Pokémon"), ("Paldean Tauros", "PAL", "108", "Uncommon", "Pokémon"),
                ("Sudowoodo", "PAL", "109", "Uncommon", "Pokémon"), ("Pupitar", "PAL", "111", "Uncommon", "Pokémon"),
                ("Toxicroak", "PAL", "115", "Uncommon", "Pokémon"), ("Passimian", "PAL", "118", "Uncommon", "Pokémon"),
                ("Naclstack", "PAL", "122", "Uncommon", "Pokémon"), ("Honchkrow", "PAL", "132", "Uncommon", "Pokémon"),
                ("Seviper", "PAL", "137", "Uncommon", "Pokémon"), ("Zweilous", "PAL", "139", "Uncommon", "Pokémon"),
                ("Mabosstiff", "PAL", "143", "Uncommon", "Pokémon"), ("Grafaiai", "PAL", "146", "Uncommon", "Pokémon"),
                ("Bombirdier", "PAL", "147", "Uncommon", "Pokémon"), ("Corviknight", "PAL", "148", "Uncommon", "Pokémon"),
                ("Farigiraf", "PAL", "155", "Uncommon", "Pokémon"), ("Dudunsparce", "PAL", "157", "Uncommon", "Pokémon"),
                ("Pelipper", "PAL", "159", "Uncommon", "Pokémon"), ("Vigoroth", "PAL", "161", "Uncommon", "Pokémon"),
                ("Corvisquire", "PAL", "165", "Uncommon", "Pokémon"), ("Maushold", "PAL", "168", "Uncommon", "Pokémon"),
                ("Flamigo", "PAL", "170", "Uncommon", "Pokémon"), ("Artazon", "PAL", "171", "Uncommon", "Trainer"),
                ("Bravery Charm", "PAL", "173", "Uncommon", "Trainer"), ("Calamitous Snowy Mountain", "PAL", "174", "Uncommon", "Trainer"),
                ("Calamitous Wasteland", "PAL", "175", "Uncommon", "Trainer"), ("Choice Belt", "PAL", "176", "Uncommon", "Trainer"),
                ("Delivery Drone", "PAL", "178", "Uncommon", "Trainer"), ("Dendra", "PAL", "179", "Uncommon", "Trainer"),
                ("Falkner", "PAL", "180", "Uncommon", "Trainer"), ("Fighting Au Lait", "PAL", "181", "Uncommon", "Trainer"),
                ("Giacomo", "PAL", "182", "Uncommon", "Trainer"), ("Grusha", "PAL", "184", "Uncommon", "Trainer"),
                ("Iono", "PAL", "185", "Uncommon", "Trainer"), ("Practice Studio", "PAL", "186", "Uncommon", "Trainer"),
                ("Saguaro", "PAL", "187", "Uncommon", "Trainer"), ("Superior Energy Retrieval", "PAL", "189", "Uncommon", "Trainer"),
                ("Jet Energy", "PAL", "190", "Uncommon", "Energy"), ("Luminous Energy", "PAL", "191", "Uncommon", "Energy"),
                ("Reversal Energy", "PAL", "192", "Uncommon", "Energy"), ("Therapeutic Energy", "PAL", "193", "Uncommon", "Energy")
            ],
            "Rare": [
                ("Jumpluff", "PAL", "003", "Rare", "Pokémon"), ("Abomasnow", "PAL", "011", "Rare", "Pokémon"),
                ("Lokix", "PAL", "021", "Rare", "Pokémon"), ("Oricorio", "PAL", "033", "Rare", "Pokémon"),
                ("Gyarados", "PAL", "043", "Rare", "Pokémon"), ("Veluza", "PAL", "056", "Rare", "Pokémon"),
                ("Baxcalibur", "PAL", "060", "Rare", "Pokémon"), ("Luxray", "PAL", "071", "Rare", "Pokémon"),
                ("Pawmot", "PAL", "076", "Rare", "Pokémon"), ("Wigglytuff", "PAL", "084", "Rare", "Pokémon"),
                ("Spiritomb", "PAL", "089", "Rare", "Pokémon"), ("Mimikyu", "PAL", "097", "Rare", "Pokémon"),
                ("Ceruledge", "PAL", "098", "Rare", "Pokémon"), ("Rabsca", "PAL", "099", "Rare", "Pokémon"),
                ("Tinkaton", "PAL", "105", "Rare", "Pokémon"), ("Hariyama", "PAL", "113", "Rare", "Pokémon"),
                ("Garganacl", "PAL", "123", "Rare", "Pokémon"), ("Glimmora", "PAL", "126", "Rare", "Pokémon"),
                ("Weavile", "PAL", "134", "Rare", "Pokémon"), ("Tyranitar", "PAL", "135", "Rare", "Pokémon"),
                ("Sableye", "PAL", "136", "Rare", "Pokémon"), ("Hydreigon", "PAL", "140", "Rare", "Pokémon"),
                ("Orthworm", "PAL", "151", "Rare", "Pokémon"), ("Slaking", "PAL", "162", "Rare", "Pokémon"),
                ("Boss’s Orders", "PAL", "172", "Rare", "Trainer")
            ],
            "Double Rare": [
                ("Forretress ex", "PAL", "005", "Double Rare", "Pokémon"), ("Meowscarada ex", "PAL", "015", "Double Rare", "Pokémon"),
                ("Wo-Chien ex", "PAL", "027", "Double Rare", "Pokémon"), ("Skeledirge ex", "PAL", "037", "Double Rare", "Pokémon"),
                ("Chi-Yu ex", "PAL", "040", "Double Rare", "Pokémon"), ("Quaquaval ex", "PAL", "052", "Double Rare", "Pokémon"),
                ("Chien-Pao ex", "PAL", "061", "Double Rare", "Pokémon"), ("Pikachu ex", "PAL", "063", "Double Rare", "Pokémon"),
                ("Bellibolt ex", "PAL", "079", "Double Rare", "Pokémon"), ("Slowking ex", "PAL", "086", "Double Rare", "Pokémon"),
                ("Dedenne ex", "PAL", "093", "Double Rare", "Pokémon"), ("Lycanroc ex", "PAL", "117", "Double Rare", "Pokémon"),
                ("Ting-Lu ex", "PAL", "127", "Double Rare", "Pokémon"), ("Paldean Clodsire ex", "PAL", "130", "Double Rare", "Pokémon"),
                ("Copperajah ex", "PAL", "150", "Double Rare", "Pokémon"), ("Noivern ex", "PAL", "153", "Double Rare", "Pokémon"),
                ("Squawkabilly ex", "PAL", "169", "Double Rare", "Pokémon")
            ],
            "Illustration Rare": [
                ("Heracross", "PAL", "194", "Illustration Rare", "Pokémon"), ("Tropius", "PAL", "195", "Illustration Rare", "Pokémon"),
                ("Sprigatito", "PAL", "196", "Illustration Rare", "Pokémon"), ("Floragato", "PAL", "197", "Illustration Rare", "Pokémon"),
                ("Bramblin", "PAL", "198", "Illustration Rare", "Pokémon"), ("Fletchinder", "PAL", "199", "Illustration Rare", "Pokémon"),
                ("Pyroar", "PAL", "200", "Illustration Rare", "Pokémon"), ("Fuecoco", "PAL", "201", "Illustration Rare", "Pokémon"),
                ("Crocalor", "PAL", "202", "Illustration Rare", "Pokémon"), ("Magikarp", "PAL", "203", "Illustration Rare", "Pokémon"),
                ("Marill", "PAL", "204", "Illustration Rare", "Pokémon"), ("Eiscue", "PAL", "205", "Illustration Rare", "Pokémon"),
                ("Quaxly", "PAL", "206", "Illustration Rare", "Pokémon"), ("Quaxwell", "PAL", "207", "Illustration Rare", "Pokémon"),
                ("Frigibax", "PAL", "208", "Illustration Rare", "Pokémon"), ("Arctibax", "PAL", "209", "Illustration Rare", "Pokémon"),
                ("Baxcalibur", "PAL", "210", "Illustration Rare", "Pokémon"), ("Raichu", "PAL", "211", "Illustration Rare", "Pokémon"),
                ("Mismagius", "PAL", "212", "Illustration Rare", "Pokémon"), ("Gothorita", "PAL", "213", "Illustration Rare", "Pokémon"),
                ("Sandygast", "PAL", "214", "Illustration Rare", "Pokémon"), ("Rabsca", "PAL", "215", "Illustration Rare", "Pokémon"),
                ("Tinkatink", "PAL", "216", "Illustration Rare", "Pokémon"), ("Tinkatuff", "PAL", "217", "Illustration Rare", "Pokémon"),
                ("Paldean Tauros", "PAL", "218", "Illustration Rare", "Pokémon"), ("Sudowoodo", "PAL", "219", "Illustration Rare", "Pokémon"),
                ("Nacli", "PAL", "220", "Illustration Rare", "Pokémon"), ("Paldean Wooper", "PAL", "221", "Illustration Rare", "Pokémon"),
                ("Tyranitar", "PAL", "222", "Illustration Rare", "Pokémon"), ("Grafaiai", "PAL", "223", "Illustration Rare", "Pokémon"),
                ("Orthworm", "PAL", "224", "Illustration Rare", "Pokémon"), ("Rookidee", "PAL", "225", "Illustration Rare", "Pokémon"),
                ("Maushold", "PAL", "226", "Illustration Rare", "Pokémon"), ("Flamigo", "PAL", "227", "Illustration Rare", "Pokémon"),
                ("Farigiraf", "PAL", "228", "Illustration Rare", "Pokémon"), ("Dudunsparce", "PAL", "229", "Illustration Rare", "Pokémon")
            ],
            "Ultra Rare": [
                ("Forretress ex", "PAL", "230", "Ultra Rare", "Pokémon"), ("Meowscarada ex", "PAL", "231", "Ultra Rare", "Pokémon"),
                ("Wo-Chien ex", "PAL", "232", "Ultra Rare", "Pokémon"), ("Skeledirge ex", "PAL", "233", "Ultra Rare", "Pokémon"),
                ("Chi-Yu ex", "PAL", "234", "Ultra Rare", "Pokémon"), ("Quaquaval ex", "PAL", "235", "Ultra Rare", "Pokémon"),
                ("Chien-Pao ex", "PAL", "236", "Ultra Rare", "Pokémon"), ("Bellibolt ex", "PAL", "237", "Ultra Rare", "Pokémon"),
                ("Slowking ex", "PAL", "238", "Ultra Rare", "Pokémon"), ("Dedenne ex", "PAL", "239", "Ultra Rare", "Pokémon"),
                ("Tinkaton ex", "PAL", "240", "Ultra Rare", "Pokémon"), ("Lycanroc ex", "PAL", "241", "Ultra Rare", "Pokémon"),
                ("Annihilape ex", "PAL", "242", "Ultra Rare", "Pokémon"), ("Ting-Lu ex", "PAL", "243", "Ultra Rare", "Pokémon"),
                ("Paldean Clodsire ex", "PAL", "244", "Ultra Rare", "Pokémon"), ("Copperajah ex", "PAL", "245", "Ultra Rare", "Pokémon"),
                ("Noivern ex", "PAL", "246", "Ultra Rare", "Pokémon"), ("Squawkabilly ex", "PAL", "247", "Ultra Rare", "Pokémon"),
                ("Boss’s Orders", "PAL", "248", "Ultra Rare", "Trainer"), ("Clavell", "PAL", "249", "Ultra Rare", "Trainer"),
                ("Dendra", "PAL", "250", "Ultra Rare", "Trainer"), ("Falkner", "PAL", "251", "Ultra Rare", "Trainer"),
                ("Giacomo", "PAL", "252", "Ultra Rare", "Trainer"), ("Grusha", "PAL", "253", "Ultra Rare", "Trainer"),
                ("Iono", "PAL", "254", "Ultra Rare", "Trainer"), ("Saguaro", "PAL", "255", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Meowscarada ex", "PAL", "256", "Special Illustration Rare", "Pokémon"), ("Wo-Chien ex", "PAL", "257", "Special Illustration Rare", "Pokémon"),
                ("Skeledirge ex", "PAL", "258", "Special Illustration Rare", "Pokémon"), ("Chi-Yu ex", "PAL", "259", "Special Illustration Rare", "Pokémon"),
                ("Quaquaval ex", "PAL", "260", "Special Illustration Rare", "Pokémon"), ("Chien-Pao ex", "PAL", "261", "Special Illustration Rare", "Pokémon"),
                ("Tinkaton ex", "PAL", "262", "Special Illustration Rare", "Pokémon"), ("Ting-Lu ex", "PAL", "263", "Special Illustration Rare", "Pokémon"),
                ("Squawkabilly ex", "PAL", "264", "Special Illustration Rare", "Pokémon"), ("Boss’s Orders", "PAL", "265", "Special Illustration Rare", "Trainer"),
                ("Dendra", "PAL", "266", "Special Illustration Rare", "Trainer"), ("Giacomo", "PAL", "267", "Special Illustration Rare", "Trainer"),
                ("Grusha", "PAL", "268", "Special Illustration Rare", "Trainer"), ("Iono", "PAL", "269", "Special Illustration Rare", "Trainer"),
                ("Saguaro", "PAL", "270", "Special Illustration Rare", "Trainer")
            ],
            "Hyper Rare": [
                ("Meowscarada ex", "PAL", "271", "Hyper Rare", "Pokémon"), ("Skeledirge ex", "PAL", "272", "Hyper Rare", "Pokémon"),
                ("Quaquaval ex", "PAL", "273", "Hyper Rare", "Pokémon"), ("Chien-Pao ex", "PAL", "274", "Hyper Rare", "Pokémon"),
                ("Ting-Lu ex", "PAL", "275", "Hyper Rare", "Pokémon"), ("Super Rod", "PAL", "276", "Hyper Rare", "Trainer"),
                ("Superior Energy Retrieval", "PAL", "277", "Hyper Rare", "Trainer"), ("Basic Grass Energy", "PAL", "278", "Hyper Rare", "Energy"),
                ("Basic Water Energy", "PAL", "279", "Hyper Rare", "Energy")
            ]
        }
    },
        "Obsidian Flames": {
        "pull_rates": {
            "P_DR": 1/7, "P_IR": 1/13, "P_UR": 1/15, "P_SIR": 1/32, "P_HR": 1/52
        },
        "card_database": {
            "Common": [
                ("Oddish", "OBF", "001", "Common", "Pokémon"), ("Gloom", "OBF", "002", "Common", "Pokémon"),
                ("Scyther", "OBF", "004", "Common", "Pokémon"), ("Shuckle", "OBF", "005", "Common", "Pokémon"),
                ("Surskit", "OBF", "006", "Common", "Pokémon"), ("Combee", "OBF", "008", "Common", "Pokémon"),
                ("Foongus", "OBF", "009", "Common", "Pokémon"), ("Phantump", "OBF", "011", "Common", "Pokémon"),
                ("Rowlet", "OBF", "013", "Common", "Pokémon"), ("Bounsweet", "OBF", "016", "Common", "Pokémon"),
                ("Steenee", "OBF", "017", "Common", "Pokémon"), ("Smoliv", "OBF", "019", "Common", "Pokémon"),
                ("Dolliv", "OBF", "020", "Common", "Pokémon"), ("Capsakid", "OBF", "023", "Common", "Pokémon"),
                ("Capsakid", "OBF", "024", "Common", "Pokémon"), ("Charmander", "OBF", "026", "Common", "Pokémon"),
                ("Vulpix", "OBF", "028", "Common", "Pokémon"), ("Numel", "OBF", "031", "Common", "Pokémon"),
                ("Darumaka", "OBF", "034", "Common", "Pokémon"), ("Litwick", "OBF", "036", "Common", "Pokémon"),
                ("Lampent", "OBF", "037", "Common", "Pokémon"), ("Heatmor", "OBF", "039", "Common", "Pokémon"),
                ("Larvesta", "OBF", "040", "Common", "Pokémon"), ("Charcadet", "OBF", "043", "Common", "Pokémon"),
                ("Carvanha", "OBF", "046", "Common", "Pokémon"), ("Buizel", "OBF", "048", "Common", "Pokémon"),
                ("Tympole", "OBF", "050", "Common", "Pokémon"), ("Palpitoad", "OBF", "051", "Common", "Pokémon"),
                ("Cubchoo", "OBF", "053", "Common", "Pokémon"), ("Froakie", "OBF", "056", "Common", "Pokémon"),
                ("Wiglett", "OBF", "058", "Common", "Pokémon"), ("Finizen", "OBF", "060", "Common", "Pokémon"),
                ("Finizen", "OBF", "061", "Common", "Pokémon"), ("Magnemite", "OBF", "063", "Common", "Pokémon"),
                ("Magneton", "OBF", "064", "Common", "Pokémon"), ("Tynamo", "OBF", "067", "Common", "Pokémon"),
                ("Eelektrik", "OBF", "068", "Common", "Pokémon"), ("Toxel", "OBF", "071", "Common", "Pokémon"),
                ("Tadbulb", "OBF", "074", "Common", "Pokémon"), ("Tadbulb", "OBF", "075", "Common", "Pokémon"),
                ("Tadbulb", "OBF", "076", "Common", "Pokémon"), ("Cleffa", "OBF", "080", "Common", "Pokémon"),
                ("Clefairy", "OBF", "081", "Common", "Pokémon"), ("Togepi", "OBF", "083", "Common", "Pokémon"),
                ("Snubbull", "OBF", "087", "Common", "Pokémon"), ("Mawile", "OBF", "089", "Common", "Pokémon"),
                ("Spoink", "OBF", "090", "Common", "Pokémon"), ("Baltoy", "OBF", "094", "Common", "Pokémon"),
                ("Sinistea", "OBF", "097", "Common", "Pokémon"), ("Greavard", "OBF", "099", "Common", "Pokémon"),
                ("Greavard", "OBF", "100", "Common", "Pokémon"), ("Diglett", "OBF", "103", "Common", "Pokémon"),
                ("Larvitar", "OBF", "105", "Common", "Pokémon"), ("Nosepass", "OBF", "107", "Common", "Pokémon"),
                ("Barboach", "OBF", "108", "Common", "Pokémon"), ("Bonsly", "OBF", "110", "Common", "Pokémon"),
                ("Drilbur", "OBF", "111", "Common", "Pokémon"), ("Crabrawler", "OBF", "114", "Common", "Pokémon"),
                ("Rockruff", "OBF", "116", "Common", "Pokémon"), ("Toedscool", "OBF", "118", "Common", "Pokémon"),
                ("Glimmet", "OBF", "121", "Common", "Pokémon"), ("Glimmet", "OBF", "122", "Common", "Pokémon"),
                ("Paldean Wooper", "OBF", "126", "Common", "Pokémon"), ("Paldean Wooper", "OBF", "127", "Common", "Pokémon"),
                ("Houndour", "OBF", "131", "Common", "Pokémon"), ("Houndour", "OBF", "132", "Common", "Pokémon"),
                ("Inkay", "OBF", "137", "Common", "Pokémon"), ("Salandit", "OBF", "139", "Common", "Pokémon"),
                ("Bronzor", "OBF", "144", "Common", "Pokémon"), ("Pawniard", "OBF", "148", "Common", "Pokémon"),
                ("Bisharp", "OBF", "149", "Common", "Pokémon"), ("Togedemaru", "OBF", "151", "Common", "Pokémon"),
                ("Meltan", "OBF", "152", "Common", "Pokémon"), ("Varoom", "OBF", "154", "Common", "Pokémon"),
                ("Varoom", "OBF", "155", "Common", "Pokémon"), ("Dratini", "OBF", "157", "Common", "Pokémon"),
                ("Pidgey", "OBF", "162", "Common", "Pokémon"), ("Eevee", "OBF", "166", "Common", "Pokémon"),
                ("Zigzagoon", "OBF", "167", "Common", "Pokémon"), ("Swablu", "OBF", "169", "Common", "Pokémon"),
                ("Lillipup", "OBF", "170", "Common", "Pokémon"), ("Herdier", "OBF", "171", "Common", "Pokémon"),
                ("Audino", "OBF", "173", "Common", "Pokémon"), ("Bunnelby", "OBF", "175", "Common", "Pokémon"),
                ("Yungoos", "OBF", "176", "Common", "Pokémon"), ("Skwovet", "OBF", "178", "Common", "Pokémon"),
                ("Lechonk", "OBF", "180", "Common", "Pokémon"), ("Lechonk", "OBF", "181", "Common", "Pokémon"),
                ("Lechonk", "OBF", "182", "Common", "Pokémon"), ("Ryme", "OBF", "194", "Common", "Trainer"),
                ("Town Store", "OBF", "196", "Common", "Trainer")
            ],
            "Uncommon": [
                ("Bellossom", "OBF", "003", "Uncommon", "Pokémon"), ("Masquerain", "OBF", "007", "Uncommon", "Pokémon"),
                ("Amoonguss", "OBF", "010", "Uncommon", "Pokémon"), ("Trevenant", "OBF", "012", "Uncommon", "Pokémon"),
                ("Dartrix", "OBF", "014", "Uncommon", "Pokémon"), ("Tsareena", "OBF", "018", "Uncommon", "Pokémon"),
                ("Arboliva", "OBF", "021", "Uncommon", "Pokémon"), ("Charmeleon", "OBF", "027", "Uncommon", "Pokémon"),
                ("Ninetales", "OBF", "029", "Uncommon", "Pokémon"), ("Camerupt", "OBF", "032", "Uncommon", "Pokémon"),
                ("Darmanitan", "OBF", "035", "Uncommon", "Pokémon"), ("Chandelure", "OBF", "038", "Uncommon", "Pokémon"),
                ("Volcarona", "OBF", "041", "Uncommon", "Pokémon"), ("Armarouge", "OBF", "044", "Uncommon", "Pokémon"),
                ("Lapras", "OBF", "045", "Uncommon", "Pokémon"), ("Sharpedo", "OBF", "047", "Uncommon", "Pokémon"),
                ("Floatzel", "OBF", "049", "Uncommon", "Pokémon"), ("Seismitoad", "OBF", "052", "Uncommon", "Pokémon"),
                ("Beartic", "OBF", "054", "Uncommon", "Pokémon"), ("Frogadier", "OBF", "057", "Uncommon", "Pokémon"),
                ("Wugtrio", "OBF", "059", "Uncommon", "Pokémon"), ("Magnezone", "OBF", "065", "Uncommon", "Pokémon"),
                ("Eelektross", "OBF", "069", "Uncommon", "Pokémon"), ("Bellibolt", "OBF", "077", "Uncommon", "Pokémon"),
                ("Bellibolt", "OBF", "078", "Uncommon", "Pokémon"), ("Togetic", "OBF", "084", "Uncommon", "Pokémon"),
                ("Espeon", "OBF", "086", "Uncommon", "Pokémon"), ("Granbull", "OBF", "088", "Uncommon", "Pokémon"),
                ("Grumpig", "OBF", "091", "Uncommon", "Pokémon"), ("Lunatone", "OBF", "092", "Uncommon", "Pokémon"),
                ("Solrock", "OBF", "093", "Uncommon", "Pokémon"), ("Polteageist", "OBF", "098", "Uncommon", "Pokémon"),
                ("Houndstone", "OBF", "101", "Uncommon", "Pokémon"), ("Dugtrio", "OBF", "104", "Uncommon", "Pokémon"),
                ("Pupitar", "OBF", "106", "Uncommon", "Pokémon"), ("Whiscash", "OBF", "109", "Uncommon", "Pokémon"),
                ("Stunfisk", "OBF", "112", "Uncommon", "Pokémon"), ("Diggersby", "OBF", "113", "Uncommon", "Pokémon"),
                ("Crabominable", "OBF", "115", "Uncommon", "Pokémon"), ("Lycanroc", "OBF", "117", "Uncommon", "Pokémon"),
                ("Toedscruel", "OBF", "119", "Uncommon", "Pokémon"), ("Paldean Clodsire", "OBF", "128", "Uncommon", "Pokémon"),
                ("Paldean Clodsire", "OBF", "129", "Uncommon", "Pokémon"), ("Umbreon", "OBF", "130", "Uncommon", "Pokémon"),
                ("Houndoom", "OBF", "133", "Uncommon", "Pokémon"), ("Malamar", "OBF", "138", "Uncommon", "Pokémon"),
                ("Salazzle", "OBF", "140", "Uncommon", "Pokémon"), ("Skarmory", "OBF", "142", "Uncommon", "Pokémon"),
                ("Mawile", "OBF", "143", "Uncommon", "Pokémon"), ("Bronzong", "OBF", "145", "Uncommon", "Pokémon"),
                ("Probopass", "OBF", "146", "Uncommon", "Pokémon"), ("Excadrill", "OBF", "147", "Uncommon", "Pokémon"),
                ("Kingambit", "OBF", "150", "Uncommon", "Pokémon"), ("Dragonair", "OBF", "158", "Uncommon", "Pokémon"),
                ("Altaria", "OBF", "160", "Uncommon", "Pokémon"), ("Drampa", "OBF", "161", "Uncommon", "Pokémon"),
                ("Pidgeotto", "OBF", "163", "Uncommon", "Pokémon"), ("Kangaskhan", "OBF", "165", "Uncommon", "Pokémon"),
                ("Linoone", "OBF", "168", "Uncommon", "Pokémon"), ("Stoutland", "OBF", "172", "Uncommon", "Pokémon"),
                ("Bouffalant", "OBF", "174", "Uncommon", "Pokémon"), ("Gumshoos", "OBF", "177", "Uncommon", "Pokémon"),
                ("Oinkologne", "OBF", "183", "Uncommon", "Pokémon"), ("Oinkologne", "OBF", "184", "Uncommon", "Pokémon"),
                ("Flamigo", "OBF", "185", "Uncommon", "Pokémon"), ("Arven", "OBF", "186", "Uncommon", "Trainer"),
                ("Brassius", "OBF", "187", "Uncommon", "Trainer"), ("Letter of Encouragement", "OBF", "189", "Uncommon", "Trainer"),
                ("Ortega", "OBF", "190", "Uncommon", "Trainer"), ("Patrol Cap", "OBF", "191", "Uncommon", "Trainer"),
                ("Pokémon League Headquarters", "OBF", "192", "Uncommon", "Trainer"), ("Poppy", "OBF", "193", "Uncommon", "Trainer"),
                ("Team Star Grunt", "OBF", "195", "Uncommon", "Trainer"), ("Vengeful Punch", "OBF", "197", "Uncommon", "Trainer")
            ],
            "Rare": [
                ("Scovillain", "OBF", "025", "Rare", "Pokémon"), ("Entei", "OBF", "030", "Rare", "Pokémon"),
                ("Palafin", "OBF", "062", "Rare", "Pokémon"), ("Thundurus", "OBF", "070", "Rare", "Pokémon"),
                ("Toxtricity", "OBF", "072", "Rare", "Pokémon"), ("Togekiss", "OBF", "085", "Rare", "Pokémon"),
                ("Claydol", "OBF", "095", "Rare", "Pokémon"), ("Darkrai", "OBF", "136", "Rare", "Pokémon"),
                ("Scizor", "OBF", "141", "Rare", "Pokémon"), ("Geeta", "OBF", "188", "Rare", "Trainer")
            ],
            "Double Rare": [
                ("Decidueye ex", "OBF", "015", "Double Rare", "Pokémon"), ("Toedscruel ex", "OBF", "022", "Double Rare", "Pokémon"),
                ("Victini ex", "OBF", "033", "Double Rare", "Pokémon"), ("Eiscue ex", "OBF", "042", "Double Rare", "Pokémon"),
                ("Tyranitar ex", "OBF", "066", "Double Rare", "Pokémon"), ("Pawmot ex", "OBF", "073", "Double Rare", "Pokémon"),
                ("Miraidon ex", "OBF", "079", "Double Rare", "Pokémon"), ("Clefable ex", "OBF", "082", "Double Rare", "Pokémon"),
                ("Vespiquen ex", "OBF", "096", "Double Rare", "Pokémon"), ("Houndstone ex", "OBF", "102", "Double Rare", "Pokémon"),
                ("Klawf ex", "OBF", "120", "Double Rare", "Pokémon"), ("Glimmora ex", "OBF", "123", "Double Rare", "Pokémon"),
                ("Koraidon ex", "OBF", "124", "Double Rare", "Pokémon"), ("Charizard ex", "OBF", "125", "Double Rare", "Pokémon"),
                ("Houndoom ex", "OBF", "134", "Double Rare", "Pokémon"), ("Absol ex", "OBF", "135", "Double Rare", "Pokémon"),
                ("Melmetal ex", "OBF", "153", "Double Rare", "Pokémon"), ("Revavroom ex", "OBF", "156", "Double Rare", "Pokémon"),
                ("Dragonite ex", "OBF", "159", "Double Rare", "Pokémon"), ("Pidgeot ex", "OBF", "164", "Double Rare", "Pokémon"),
                ("Greedent ex", "OBF", "179", "Double Rare", "Pokémon")
            ],
            "Illustration Rare": [
                ("Gloom", "OBF", "198", "Illustration Rare", "Pokémon"), ("Ninetales", "OBF", "199", "Illustration Rare", "Pokémon"),
                ("Palafin", "OBF", "200", "Illustration Rare", "Pokémon"), ("Bellibolt", "OBF", "201", "Illustration Rare", "Pokémon"),
                ("Cleffa", "OBF", "202", "Illustration Rare", "Pokémon"), ("Larvitar", "OBF", "203", "Illustration Rare", "Pokémon"),
                ("Houndour", "OBF", "204", "Illustration Rare", "Pokémon"), ("Scizor", "OBF", "205", "Illustration Rare", "Pokémon"),
                ("Varoom", "OBF", "206", "Illustration Rare", "Pokémon"), ("Pidgey", "OBF", "207", "Illustration Rare", "Pokémon"),
                ("Pidgeotto", "OBF", "208", "Illustration Rare", "Pokémon"), ("Lechonk", "OBF", "209", "Illustration Rare", "Pokémon")
            ],
            "Ultra Rare": [
                ("Eiscue ex", "OBF", "210", "Ultra Rare", "Pokémon"), ("Tyranitar ex", "OBF", "211", "Ultra Rare", "Pokémon"),
                ("Vespiquen ex", "OBF", "212", "Ultra Rare", "Pokémon"), ("Glimmora ex", "OBF", "213", "Ultra Rare", "Pokémon"),
                ("Absol ex", "OBF", "214", "Ultra Rare", "Pokémon"), ("Charizard ex", "OBF", "215", "Ultra Rare", "Pokémon"),
                ("Revavroom ex", "OBF", "216", "Ultra Rare", "Pokémon"), ("Pidgeot ex", "OBF", "217", "Ultra Rare", "Pokémon"),
                ("Geeta", "OBF", "218", "Ultra Rare", "Trainer"), ("Ortega", "OBF", "219", "Ultra Rare", "Trainer"),
                ("Poppy", "OBF", "220", "Ultra Rare", "Trainer"), ("Ryme", "OBF", "221", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Eiscue ex", "OBF", "222", "Special Illustration Rare", "Pokémon"), ("Charizard ex", "OBF", "223", "Special Illustration Rare", "Pokémon"),
                ("Revavroom ex", "OBF", "224", "Special Illustration Rare", "Pokémon"), ("Pidgeot ex", "OBF", "225", "Special Illustration Rare", "Pokémon"),
                ("Geeta", "OBF", "226", "Special Illustration Rare", "Trainer"), ("Poppy", "OBF", "227", "Special Illustration Rare", "Trainer")
            ],
            "Hyper Rare": [
                ("Charizard ex", "OBF", "228", "Hyper Rare", "Pokémon"), ("Artazon", "OBF", "229", "Hyper Rare", "Trainer"),
                ("Basic Fire Energy", "OBF", "230", "Hyper Rare", "Energy")
            ]
        }
    },
    "Scarlet & Violet—151": {
        "pull_rates": {
            "P_DR": 1/8, "P_IR": 1/12, "P_UR": 1/16, "P_SIR": 1/32, "P_HR": 1/51
        },
        "card_database": {
            "Common": [
                ("Bulbasaur", "MEW", "001", "Common", "Pokémon"), ("Charmander", "MEW", "004", "Common", "Pokémon"),
                ("Squirtle", "MEW", "007", "Common", "Pokémon"), ("Caterpie", "MEW", "010", "Common", "Pokémon"),
                ("Metapod", "MEW", "011", "Common", "Pokémon"), ("Weedle", "MEW", "013", "Common", "Pokémon"),
                ("Kakuna", "MEW", "014", "Common", "Pokémon"), ("Pidgey", "MEW", "016", "Common", "Pokémon"),
                ("Pidgeotto", "MEW", "017", "Common", "Pokémon"), ("Rattata", "MEW", "019", "Common", "Pokémon"),
                ("Spearow", "MEW", "021", "Common", "Pokémon"), ("Ekans", "MEW", "023", "Common", "Pokémon"),
                ("Pikachu", "MEW", "025", "Common", "Pokémon"), ("Sandshrew", "MEW", "027", "Common", "Pokémon"),
                ("Nidoran Female", "MEW", "029", "Common", "Pokémon"), ("Nidoran Male", "MEW", "032", "Common", "Pokémon"),
                ("Clefairy", "MEW", "035", "Common", "Pokémon"), ("Vulpix", "MEW", "037", "Common", "Pokémon"),
                ("Jigglypuff", "MEW", "039", "Common", "Pokémon"), ("Zubat", "MEW", "041", "Common", "Pokémon"),
                ("Oddish", "MEW", "043", "Common", "Pokémon"), ("Paras", "MEW", "046", "Common", "Pokémon"),
                ("Venonat", "MEW", "048", "Common", "Pokémon"), ("Diglett", "MEW", "050", "Common", "Pokémon"),
                ("Meowth", "MEW", "052", "Common", "Pokémon"), ("Psyduck", "MEW", "054", "Common", "Pokémon"),
                ("Mankey", "MEW", "056", "Common", "Pokémon"), ("Growlithe", "MEW", "058", "Common", "Pokémon"),
                ("Poliwag", "MEW", "060", "Common", "Pokémon"), ("Poliwhirl", "MEW", "061", "Common", "Pokémon"),
                ("Abra", "MEW", "063", "Common", "Pokémon"), ("Machop", "MEW", "066", "Common", "Pokémon"),
                ("Bellsprout", "MEW", "069", "Common", "Pokémon"), ("Weepinbell", "MEW", "070", "Common", "Pokémon"),
                ("Tentacool", "MEW", "072", "Common", "Pokémon"), ("Geodude", "MEW", "074", "Common", "Pokémon"),
                ("Ponyta", "MEW", "077", "Common", "Pokémon"), ("Slowpoke", "MEW", "079", "Common", "Pokémon"),
                ("Magnemite", "MEW", "081", "Common", "Pokémon"), ("Farfetch’d", "MEW", "083", "Common", "Pokémon"),
                ("Doduo", "MEW", "084", "Common", "Pokémon"), ("Seel", "MEW", "086", "Common", "Pokémon"),
                ("Grimer", "MEW", "088", "Common", "Pokémon"), ("Shellder", "MEW", "090", "Common", "Pokémon"),
                ("Gastly", "MEW", "092", "Common", "Pokémon"), ("Drowzee", "MEW", "096", "Common", "Pokémon"),
                ("Krabby", "MEW", "098", "Common", "Pokémon"), ("Voltorb", "MEW", "100", "Common", "Pokémon"),
                ("Exeggcute", "MEW", "102", "Common", "Pokémon"), ("Cubone", "MEW", "104", "Common", "Pokémon"),
                ("Lickitung", "MEW", "108", "Common", "Pokémon"), ("Koffing", "MEW", "109", "Common", "Pokémon"),
                ("Rhyhorn", "MEW", "111", "Common", "Pokémon"), ("Tangela", "MEW", "114", "Common", "Pokémon"),
                ("Horsea", "MEW", "116", "Common", "Pokémon"), ("Goldeen", "MEW", "118", "Common", "Pokémon"),
                ("Staryu", "MEW", "120", "Common", "Pokémon"), ("Electabuzz", "MEW", "125", "Common", "Pokémon"),
                ("Magmar", "MEW", "126", "Common", "Pokémon"), ("Magikarp", "MEW", "129", "Common", "Pokémon"),
                ("Eevee", "MEW", "133", "Common", "Pokémon"), ("Porygon", "MEW", "137", "Common", "Pokémon"),
                ("Dratini", "MEW", "147", "Common", "Pokémon"), ("Antique Dome Fossil", "MEW", "152", "Common", "Trainer"),
                ("Antique Helix Fossil", "MEW", "153", "Common", "Trainer"), ("Antique Old Amber", "MEW", "154", "Common", "Trainer")
            ],
            "Uncommon": [
                ("Ivysaur", "MEW", "002", "Uncommon", "Pokémon"), ("Charmeleon", "MEW", "005", "Uncommon", "Pokémon"),
                ("Wartortle", "MEW", "008", "Uncommon", "Pokémon"), ("Butterfree", "MEW", "012", "Uncommon", "Pokémon"),
                ("Pidgeot", "MEW", "018", "Uncommon", "Pokémon"), ("Raticate", "MEW", "020", "Uncommon", "Pokémon"),
                ("Fearow", "MEW", "022", "Uncommon", "Pokémon"), ("Sandslash", "MEW", "028", "Uncommon", "Pokémon"),
                ("Nidorina", "MEW", "030", "Uncommon", "Pokémon"), ("Nidoqueen", "MEW", "031", "Uncommon", "Pokémon"),
                ("Nidorino", "MEW", "033", "Uncommon", "Pokémon"), ("Clefable", "MEW", "036", "Uncommon", "Pokémon"),
                ("Golbat", "MEW", "042", "Uncommon", "Pokémon"), ("Gloom", "MEW", "044", "Uncommon", "Pokémon"),
                ("Parasect", "MEW", "047", "Uncommon", "Pokémon"), ("Venomoth", "MEW", "049", "Uncommon", "Pokémon"),
                ("Dugtrio", "MEW", "051", "Uncommon", "Pokémon"), ("Persian", "MEW", "053", "Uncommon", "Pokémon"),
                ("Golduck", "MEW", "055", "Uncommon", "Pokémon"), ("Primeape", "MEW", "057", "Uncommon", "Pokémon"),
                ("Arcanine", "MEW", "059", "Uncommon", "Pokémon"), ("Poliwrath", "MEW", "062", "Uncommon", "Pokémon"),
                ("Kadabra", "MEW", "064", "Uncommon", "Pokémon"), ("Machoke", "MEW", "067", "Uncommon", "Pokémon"),
                ("Victreebel", "MEW", "071", "Uncommon", "Pokémon"), ("Tentacruel", "MEW", "073", "Uncommon", "Pokémon"),
                ("Graveler", "MEW", "075", "Uncommon", "Pokémon"), ("Rapidash", "MEW", "078", "Uncommon", "Pokémon"),
                ("Slowbro", "MEW", "080", "Uncommon", "Pokémon"), ("Magneton", "MEW", "082", "Uncommon", "Pokémon"),
                ("Dewgong", "MEW", "087", "Uncommon", "Pokémon"), ("Muk", "MEW", "089", "Uncommon", "Pokémon"),
                ("Cloyster", "MEW", "091", "Uncommon", "Pokémon"), ("Haunter", "MEW", "093", "Uncommon", "Pokémon"),
                ("Onix", "MEW", "095", "Uncommon", "Pokémon"), ("Hypno", "MEW", "097", "Uncommon", "Pokémon"),
                ("Kingler", "MEW", "099", "Uncommon", "Pokémon"), ("Exeggutor", "MEW", "103", "Uncommon", "Pokémon"),
                ("Hitmonlee", "MEW", "106", "Uncommon", "Pokémon"), ("Hitmonchan", "MEW", "107", "Uncommon", "Pokémon"),
                ("Rhydon", "MEW", "112", "Uncommon", "Pokémon"), ("Seadra", "MEW", "117", "Uncommon", "Pokémon"),
                ("Seaking", "MEW", "119", "Uncommon", "Pokémon"), ("Scyther", "MEW", "123", "Uncommon", "Pokémon"),
                ("Pinsir", "MEW", "127", "Uncommon", "Pokémon"), ("Tauros", "MEW", "128", "Uncommon", "Pokémon"),
                ("Lapras", "MEW", "131", "Uncommon", "Pokémon"), ("Omanyte", "MEW", "138", "Uncommon", "Pokémon"),
                ("Kabuto", "MEW", "140", "Uncommon", "Pokémon"), ("Snorlax", "MEW", "143", "Uncommon", "Pokémon"),
                ("Dragonair", "MEW", "148", "Uncommon", "Pokémon"), ("Big Air Balloon", "MEW", "155", "Uncommon", "Trainer"),
                ("Bill’s Transfer", "MEW", "156", "Uncommon", "Trainer"), ("Cycling Road", "MEW", "157", "Uncommon", "Trainer"),
                ("Daisy’s Help", "MEW", "158", "Uncommon", "Trainer"), ("Energy Sticker", "MEW", "159", "Uncommon", "Trainer"),
                ("Erika’s Invitation", "MEW", "160", "Uncommon", "Trainer"), ("Giovanni’s Charisma", "MEW", "161", "Uncommon", "Trainer"),
                ("Grabber", "MEW", "162", "Uncommon", "Trainer"), ("Leftovers", "MEW", "163", "Uncommon", "Trainer"),
                ("Protective Goggles", "MEW", "164", "Uncommon", "Trainer"), ("Rigid Band", "MEW", "165", "Uncommon", "Trainer")
            ],
            "Rare": [
                ("Beedrill", "MEW", "015", "Rare", "Pokémon"), ("Raichu", "MEW", "026", "Rare", "Pokémon"),
                ("Nidoking", "MEW", "034", "Rare", "Pokémon"), ("Vileplume", "MEW", "045", "Rare", "Pokémon"),
                ("Machamp", "MEW", "068", "Rare", "Pokémon"), ("Dodrio", "MEW", "085", "Rare", "Pokémon"),
                ("Gengar", "MEW", "094", "Rare", "Pokémon"), ("Electrode", "MEW", "101", "Rare", "Pokémon"),
                ("Marowak", "MEW", "105", "Rare", "Pokémon"), ("Weezing", "MEW", "110", "Rare", "Pokémon"),
                ("Chansey", "MEW", "113", "Rare", "Pokémon"), ("Starmie", "MEW", "121", "Rare", "Pokémon"),
                ("Mr. Mime", "MEW", "122", "Rare", "Pokémon"), ("Gyarados", "MEW", "130", "Rare", "Pokémon"),
                ("Ditto", "MEW", "132", "Rare", "Pokémon"), ("Vaporeon", "MEW", "134", "Rare", "Pokémon"),
                ("Jolteon", "MEW", "135", "Rare", "Pokémon"), ("Flareon", "MEW", "136", "Rare", "Pokémon"),
                ("Omastar", "MEW", "139", "Rare", "Pokémon"), ("Kabutops", "MEW", "141", "Rare", "Pokémon"),
                ("Aerodactyl", "MEW", "142", "Rare", "Pokémon"), ("Articuno", "MEW", "144", "Rare", "Pokémon"),
                ("Moltres", "MEW", "146", "Rare", "Pokémon"), ("Dragonite", "MEW", "149", "Rare", "Pokémon"),
                ("Mewtwo", "MEW", "150", "Rare", "Pokémon")
            ],
            "Holo Rare": [],
            "Double Rare": [
                ("Venusaur ex", "MEW", "003", "Double Rare", "Pokémon"), ("Charizard ex", "MEW", "006", "Double Rare", "Pokémon"),
                ("Blastoise ex", "MEW", "009", "Double Rare", "Pokémon"), ("Arbok ex", "MEW", "024", "Double Rare", "Pokémon"),
                ("Ninetales ex", "MEW", "038", "Double Rare", "Pokémon"), ("Wigglytuff ex", "MEW", "040", "Double Rare", "Pokémon"),
                ("Alakazam ex", "MEW", "065", "Double Rare", "Pokémon"), ("Golem ex", "MEW", "076", "Double Rare", "Pokémon"),
                ("Kangaskhan ex", "MEW", "115", "Double Rare", "Pokémon"), ("Jynx ex", "MEW", "124", "Double Rare", "Pokémon"),
                ("Zapdos ex", "MEW", "145", "Double Rare", "Pokémon"), ("Mew ex", "MEW", "151", "Double Rare", "Pokémon")
            ],
            "Illustration Rare": [
                ("Bulbasaur", "MEW", "166", "Illustration Rare", "Pokémon"), ("Ivysaur", "MEW", "167", "Illustration Rare", "Pokémon"),
                ("Charmander", "MEW", "168", "Illustration Rare", "Pokémon"), ("Charmeleon", "MEW", "169", "Illustration Rare", "Pokémon"),
                ("Squirtle", "MEW", "170", "Illustration Rare", "Pokémon"), ("Wartortle", "MEW", "171", "Illustration Rare", "Pokémon"),
                ("Caterpie", "MEW", "172", "Illustration Rare", "Pokémon"), ("Pikachu", "MEW", "173", "Illustration Rare", "Pokémon"),
                ("Nidoking", "MEW", "174", "Illustration Rare", "Pokémon"), ("Psyduck", "MEW", "175", "Illustration Rare", "Pokémon"),
                ("Poliwhirl", "MEW", "176", "Illustration Rare", "Pokémon"), ("Machoke", "MEW", "177", "Illustration Rare", "Pokémon"),
                ("Tangela", "MEW", "178", "Illustration Rare", "Pokémon"), ("Mr. Mime", "MEW", "179", "Illustration Rare", "Pokémon"),
                ("Omanyte", "MEW", "180", "Illustration Rare", "Pokémon"), ("Dragonair", "MEW", "181", "Illustration Rare", "Pokémon")
            ],
            "Ultra Rare": [
                ("Venusaur ex", "MEW", "182", "Ultra Rare", "Pokémon"), ("Charizard ex", "MEW", "183", "Ultra Rare", "Pokémon"),
                ("Blastoise ex", "MEW", "184", "Ultra Rare", "Pokémon"), ("Arbok ex", "MEW", "185", "Ultra Rare", "Pokémon"),
                ("Ninetales ex", "MEW", "186", "Ultra Rare", "Pokémon"), ("Wigglytuff ex", "MEW", "187", "Ultra Rare", "Pokémon"),
                ("Alakazam ex", "MEW", "188", "Ultra Rare", "Pokémon"), ("Golem ex", "MEW", "189", "Ultra Rare", "Pokémon"),
                ("Kangaskhan ex", "MEW", "190", "Ultra Rare", "Pokémon"), ("Jynx ex", "MEW", "191", "Ultra Rare", "Pokémon"),
                ("Zapdos ex", "MEW", "192", "Ultra Rare", "Pokémon"), ("Mew ex", "MEW", "193", "Ultra Rare", "Pokémon"),
                ("Bill’s Transfer", "MEW", "194", "Ultra Rare", "Trainer"), ("Daisy’s Help", "MEW", "195", "Ultra Rare", "Trainer"),
                ("Erika’s Invitation", "MEW", "196", "Ultra Rare", "Trainer"), ("Giovanni’s Charisma", "MEW", "197", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Venusaur ex", "MEW", "198", "Special Illustration Rare", "Pokémon"), ("Charizard ex", "MEW", "199", "Special Illustration Rare", "Pokémon"),
                ("Blastoise ex", "MEW", "200", "Special Illustration Rare", "Pokémon"), ("Alakazam ex", "MEW", "201", "Special Illustration Rare", "Pokémon"),
                ("Zapdos ex", "MEW", "202", "Special Illustration Rare", "Pokémon"), ("Erika’s Invitation", "MEW", "203", "Special Illustration Rare", "Trainer"),
                ("Giovanni’s Charisma", "MEW", "204", "Special Illustration Rare", "Trainer")
            ],
            "Hyper Rare": [
                ("Mew ex", "MEW", "205", "Hyper Rare", "Pokémon"), ("Switch", "MEW", "206", "Hyper Rare", "Trainer"),
                ("Basic Psychic Energy", "MEW", "207", "Hyper Rare", "Energy")
            ]
        }
    },
    "Paradox Rift": {
        "pull_rates": {
            "P_DR": 1/6, "P_IR": 1/13, "P_UR": 1/15, "P_SIR": 1/47, "P_HR": 1/82
        },
        "card_database": {
            "Common": [
                ("Surskit", "PAR", "001", "Common", "Pokémon"), ("Pansage", "PAR", "004", "Common", "Pokémon"),
                ("Dwebble", "PAR", "006", "Common", "Pokémon"), ("Crustle", "PAR", "007", "Common", "Pokémon"),
                ("Bounsweet", "PAR", "008", "Common", "Pokémon"), ("Blipbug", "PAR", "010", "Common", "Pokémon"),
                ("Dottler", "PAR", "011", "Common", "Pokémon"), ("Nymble", "PAR", "013", "Common", "Pokémon"),
                ("Nymble", "PAR", "014", "Common", "Pokémon"), ("Toedscool", "PAR", "015", "Common", "Pokémon"),
                ("Toedscool", "PAR", "016", "Common", "Pokémon"), ("Magby", "PAR", "019", "Common", "Pokémon"),
                ("Pansear", "PAR", "020", "Common", "Pokémon"), ("Fuecoco", "PAR", "023", "Common", "Pokémon"),
                ("Charcadet", "PAR", "025", "Common", "Pokémon"), ("Charcadet", "PAR", "026", "Common", "Pokémon"),
                ("Horsea", "PAR", "030", "Common", "Pokémon"), ("Seadra", "PAR", "031", "Common", "Pokémon"),
                ("Remoraid", "PAR", "033", "Common", "Pokémon"), ("Octillery", "PAR", "034", "Common", "Pokémon"),
                ("Feebas", "PAR", "035", "Common", "Pokémon"), ("Snorunt", "PAR", "037", "Common", "Pokémon"),
                ("Mantyke", "PAR", "039", "Common", "Pokémon"), ("Panpour", "PAR", "041", "Common", "Pokémon"),
                ("Vanillite", "PAR", "043", "Common", "Pokémon"), ("Vanillish", "PAR", "044", "Common", "Pokémon"),
                ("Wimpod", "PAR", "047", "Common", "Pokémon"), ("Wimpod", "PAR", "048", "Common", "Pokémon"),
                ("Wiglett", "PAR", "051", "Common", "Pokémon"), ("Wiglett", "PAR", "052", "Common", "Pokémon"),
                ("Elekid", "PAR", "059", "Common", "Pokémon"), ("Plusle", "PAR", "060", "Common", "Pokémon"),
                ("Minun", "PAR", "061", "Common", "Pokémon"), ("Blitzle", "PAR", "062", "Common", "Pokémon"),
                ("Joltik", "PAR", "064", "Common", "Pokémon"), ("Galvantula", "PAR", "065", "Common", "Pokémon"),
                ("Oricorio", "PAR", "067", "Common", "Pokémon"), ("Toxel", "PAR", "069", "Common", "Pokémon"),
                ("Natu", "PAR", "071", "Common", "Pokémon"), ("Yamask", "PAR", "075", "Common", "Pokémon"),
                ("Pumpkaboo", "PAR", "077", "Common", "Pokémon"), ("Flittle", "PAR", "079", "Common", "Pokémon"),
                ("Flittle", "PAR", "080", "Common", "Pokémon"), ("Tinkatink", "PAR", "082", "Common", "Pokémon"),
                ("Tinkatink", "PAR", "083", "Common", "Pokémon"), ("Tinkatuff", "PAR", "084", "Common", "Pokémon"),
                ("Gimmighoul", "PAR", "087", "Common", "Pokémon"), ("Gimmighoul", "PAR", "088", "Common", "Pokémon"),
                ("Onix", "PAR", "090", "Common", "Pokémon"), ("Gligar", "PAR", "091", "Common", "Pokémon"),
                ("Gible", "PAR", "094", "Common", "Pokémon"), ("Gabite", "PAR", "095", "Common", "Pokémon"),
                ("Mienfoo", "PAR", "096", "Common", "Pokémon"), ("Nacli", "PAR", "101", "Common", "Pokémon"),
                ("Nacli", "PAR", "102", "Common", "Pokémon"), ("Naclstack", "PAR", "103", "Common", "Pokémon"),
                ("Flamigo", "PAR", "106", "Common", "Pokémon"), ("Zubat", "PAR", "110", "Common", "Pokémon"),
                ("Golbat", "PAR", "111", "Common", "Pokémon"), ("Purrloin", "PAR", "114", "Common", "Pokémon"),
                ("Liepard", "PAR", "115", "Common", "Pokémon"), ("Trubbish", "PAR", "116", "Common", "Pokémon"),
                ("Nickit", "PAR", "119", "Common", "Pokémon"), ("Jirachi", "PAR", "126", "Common", "Pokémon"),
                ("Ferroseed", "PAR", "127", "Common", "Pokémon"), ("Honedge", "PAR", "130", "Common", "Pokémon"),
                ("Honedge", "PAR", "131", "Common", "Pokémon"), ("Doublade", "PAR", "132", "Common", "Pokémon"),
                ("Doublade", "PAR", "133", "Common", "Pokémon"), ("Porygon", "PAR", "142", "Common", "Pokémon"),
                ("Porygon2", "PAR", "143", "Common", "Pokémon"), ("Aipom", "PAR", "145", "Common", "Pokémon"),
                ("Miltank", "PAR", "147", "Common", "Pokémon"), ("Whismur", "PAR", "148", "Common", "Pokémon"),
                ("Loudred", "PAR", "149", "Common", "Pokémon"), ("Spinda", "PAR", "151", "Common", "Pokémon"),
                ("Swablu", "PAR", "152", "Common", "Pokémon"), ("Tandemaus", "PAR", "153", "Common", "Pokémon"),
                ("Tandemaus", "PAR", "154", "Common", "Pokémon"), ("Larry", "PAR", "165", "Common", "Trainer"),
                ("Parasol Lady", "PAR", "169", "Common", "Trainer")
            ],
            "Uncommon": [
                ("Masquerain", "PAR", "002", "Uncommon", "Pokémon"), ("Simisage", "PAR", "005", "Uncommon", "Pokémon"),
                ("Steenee", "PAR", "009", "Uncommon", "Pokémon"), ("Orbeetle", "PAR", "012", "Uncommon", "Pokémon"),
                ("Toedscruel", "PAR", "017", "Uncommon", "Pokémon"), ("Simisear", "PAR", "021", "Uncommon", "Pokémon"),
                ("Crocalor", "PAR", "024", "Uncommon", "Pokémon"), ("Simipour", "PAR", "042", "Uncommon", "Pokémon"),
                ("Vanilluxe", "PAR", "045", "Uncommon", "Pokémon"), ("Wugtrio", "PAR", "053", "Uncommon", "Pokémon"),
                ("Veluza", "PAR", "054", "Uncommon", "Pokémon"), ("Dondozo", "PAR", "055", "Uncommon", "Pokémon"),
                ("Iron Bundle", "PAR", "056", "Uncommon", "Pokémon"), ("Zebstrika", "PAR", "063", "Uncommon", "Pokémon"),
                ("Gourgeist", "PAR", "078", "Uncommon", "Pokémon"), ("Tinkaton", "PAR", "085", "Uncommon", "Pokémon"),
                ("Scream Tail", "PAR", "086", "Uncommon", "Pokémon"), ("Gliscor", "PAR", "092", "Uncommon", "Pokémon"),
                ("Mienshao", "PAR", "097", "Uncommon", "Pokémon"), ("Minior", "PAR", "099", "Uncommon", "Pokémon"),
                ("Klawf", "PAR", "105", "Uncommon", "Pokémon"), ("Slither Wing", "PAR", "107", "Uncommon", "Pokémon"),
                ("Crobat", "PAR", "112", "Uncommon", "Pokémon"), ("Absol", "PAR", "113", "Uncommon", "Pokémon"),
                ("Garbodor", "PAR", "117", "Uncommon", "Pokémon"), ("Ferrothorn", "PAR", "128", "Uncommon", "Pokémon"),
                ("Durant", "PAR", "129", "Uncommon", "Pokémon"), ("Orthworm", "PAR", "138", "Uncommon", "Pokémon"),
                ("Tatsugiri", "PAR", "141", "Uncommon", "Pokémon"), ("Ambipom", "PAR", "146", "Uncommon", "Pokémon"),
                ("Exploud", "PAR", "150", "Uncommon", "Pokémon"), ("Cyclizar", "PAR", "157", "Uncommon", "Pokémon"),
                ("Ancient Booster Energy Capsule", "PAR", "159", "Uncommon", "Trainer"), ("Counter Catcher", "PAR", "160", "Uncommon", "Trainer"),
                ("Cursed Duster", "PAR", "161", "Uncommon", "Trainer"), ("Defiance Vest", "PAR", "162", "Uncommon", "Trainer"),
                ("Earthen Vessel", "PAR", "163", "Uncommon", "Trainer"), ("Future Booster Energy Capsule", "PAR", "164", "Uncommon", "Trainer"),
                ("Luxurious Cape", "PAR", "166", "Uncommon", "Trainer"), ("Mela", "PAR", "167", "Uncommon", "Trainer"),
                ("Norman", "PAR", "168", "Uncommon", "Trainer"), ("Professor Sada’s Vitality", "PAR", "170", "Uncommon", "Trainer"),
                ("Professor Turo’s Scenario", "PAR", "171", "Uncommon", "Trainer"), ("Rika", "PAR", "172", "Uncommon", "Trainer"),
                ("Roark", "PAR", "173", "Uncommon", "Trainer"), ("Shauntal", "PAR", "174", "Uncommon", "Trainer"),
                ("Snorlax Doll", "PAR", "175", "Uncommon", "Trainer"), ("Technical Machine: Blindside", "PAR", "176", "Uncommon", "Trainer"),
                ("Technical Machine: Devolution", "PAR", "177", "Uncommon", "Trainer"), ("Technical Machine: Evolution", "PAR", "178", "Uncommon", "Trainer"),
                ("Technical Machine: Turbo Energize", "PAR", "179", "Uncommon", "Trainer"), ("Techno Radar", "PAR", "180", "Uncommon", "Trainer"),
                ("Tulip", "PAR", "181", "Uncommon", "Trainer"), ("Medical Energy", "PAR", "182", "Uncommon", "Energy")
            ],
            "Rare": [
                ("Wo-Chien", "PAR", "018", "Rare", "Pokémon"), ("Volcanion", "PAR", "022", "Rare", "Pokémon"),
                ("Iron Moth", "PAR", "028", "Rare", "Pokémon"), ("Chi-Yu", "PAR", "029", "Rare", "Pokémon"),
                ("Kingdra", "PAR", "032", "Rare", "Pokémon"), ("Milotic", "PAR", "036", "Rare", "Pokémon"),
                ("Palkia", "PAR", "040", "Rare", "Pokémon"), ("Golisopod", "PAR", "049", "Rare", "Pokémon"),
                ("Chien-Pao", "PAR", "057", "Rare", "Pokémon"), ("Zekrom", "PAR", "066", "Rare", "Pokémon"),
                ("Xatu", "PAR", "072", "Rare", "Pokémon"), ("Latios", "PAR", "073", "Rare", "Pokémon"),
                ("Deoxys", "PAR", "074", "Rare", "Pokémon"), ("Espathra", "PAR", "081", "Rare", "Pokémon"),
                ("Groudon", "PAR", "093", "Rare", "Pokémon"), ("Garganacl", "PAR", "104", "Rare", "Pokémon"),
                ("Ting-Lu", "PAR", "109", "Rare", "Pokémon"), ("Yveltal", "PAR", "118", "Rare", "Pokémon"),
                ("Thievul", "PAR", "120", "Rare", "Pokémon"), ("Morpeko", "PAR", "121", "Rare", "Pokémon"),
                ("Lokix", "PAR", "122", "Rare", "Pokémon"), ("Brute Bonnet", "PAR", "123", "Rare", "Pokémon"),
                ("Steelix", "PAR", "125", "Rare", "Pokémon"), ("Aegislash", "PAR", "134", "Rare", "Pokémon"),
                ("Zacian", "PAR", "136", "Rare", "Pokémon"), ("Porygon-Z", "PAR", "144", "Rare", "Pokémon"),
                ("Iron Jugulis", "PAR", "158", "Rare", "Pokémon")
            ],
            "Double Rare": [
                ("Froslass ex", "PAR", "003", "Double Rare", "Pokémon"), ("Armarouge ex", "PAR", "027", "Double Rare", "Pokémon"),
                ("Garchomp ex", "PAR", "038", "Double Rare", "Pokémon"), ("Tsareena ex", "PAR", "046", "Double Rare", "Pokémon"),
                ("Golisopod ex", "PAR", "050", "Double Rare", "Pokémon"), ("Mewtwo ex", "PAR", "058", "Double Rare", "Pokémon"),
                ("Tapu Koko ex", "PAR", "068", "Double Rare", "Pokémon"), ("Iron Hands ex", "PAR", "070", "Double Rare", "Pokémon"),
                ("Cofagrigus ex", "PAR", "076", "Double Rare", "Pokémon"), ("Iron Valiant ex", "PAR", "089", "Double Rare", "Pokémon"),
                ("Hoopa ex", "PAR", "098", "Double Rare", "Pokémon"), ("Toxtricity ex", "PAR", "100", "Double Rare", "Pokémon"),
                ("Sandy Shocks ex", "PAR", "108", "Double Rare", "Pokémon"), ("Roaring Moon ex", "PAR", "124", "Double Rare", "Pokémon"),
                ("Aegislash ex", "PAR", "135", "Double Rare", "Pokémon"), ("Skeledirge ex", "PAR", "137", "Double Rare", "Pokémon"),
                ("Gholdengo ex", "PAR", "139", "Double Rare", "Pokémon"), ("Altaria ex", "PAR", "140", "Double Rare", "Pokémon"),
                ("Maushold ex", "PAR", "155", "Double Rare", "Pokémon"), ("Bombirdier ex", "PAR", "156", "Double Rare", "Pokémon")
            ],
            "Illustration Rare": [
                ("Crustle", "PAR", "183", "Illustration Rare", "Pokémon"), ("Dottler", "PAR", "184", "Illustration Rare", "Pokémon"),
                ("Toedscruel", "PAR", "185", "Illustration Rare", "Pokémon"), ("Magby", "PAR", "186", "Illustration Rare", "Pokémon"),
                ("Iron Moth", "PAR", "187", "Illustration Rare", "Pokémon"), ("Snorunt", "PAR", "188", "Illustration Rare", "Pokémon"),
                ("Mantyke", "PAR", "189", "Illustration Rare", "Pokémon"), ("Vanillish", "PAR", "190", "Illustration Rare", "Pokémon"),
                ("Wimpod", "PAR", "191", "Illustration Rare", "Pokémon"), ("Veluza", "PAR", "192", "Illustration Rare", "Pokémon"),
                ("Plusle", "PAR", "193", "Illustration Rare", "Pokémon"), ("Minun", "PAR", "194", "Illustration Rare", "Pokémon"),
                ("Blitzle", "PAR", "195", "Illustration Rare", "Pokémon"), ("Joltik", "PAR", "196", "Illustration Rare", "Pokémon"),
                ("Espathra", "PAR", "197", "Illustration Rare", "Pokémon"), ("Gimmighoul", "PAR", "198", "Illustration Rare", "Pokémon"),
                ("Groudon", "PAR", "199", "Illustration Rare", "Pokémon"), ("Mienshao", "PAR", "200", "Illustration Rare", "Pokémon"),
                ("Minior", "PAR", "201", "Illustration Rare", "Pokémon"), ("Garganacl", "PAR", "202", "Illustration Rare", "Pokémon"),
                ("Slither Wing", "PAR", "203", "Illustration Rare", "Pokémon"), ("Garbodor", "PAR", "204", "Illustration Rare", "Pokémon"),
                ("Yveltal", "PAR", "205", "Illustration Rare", "Pokémon"), ("Morpeko", "PAR", "206", "Illustration Rare", "Pokémon"),
                ("Brute Bonnet", "PAR", "207", "Illustration Rare", "Pokémon"), ("Steelix", "PAR", "208", "Illustration Rare", "Pokémon"),
                ("Ferrothorn", "PAR", "209", "Illustration Rare", "Pokémon"), ("Aegislash", "PAR", "210", "Illustration Rare", "Pokémon"),
                ("Aipom", "PAR", "211", "Illustration Rare", "Pokémon"), ("Loudred", "PAR", "212", "Illustration Rare", "Pokémon"),
                ("Swablu", "PAR", "213", "Illustration Rare", "Pokémon"), ("Porygon-Z", "PAR", "214", "Illustration Rare", "Pokémon"),
                ("Cyclizar", "PAR", "215", "Illustration Rare", "Pokémon"), ("Iron Jugulis", "PAR", "216", "Illustration Rare", "Pokémon")
            ],
            "Ultra Rare": [
                ("Froslass ex", "PAR", "217", "Ultra Rare", "Pokémon"), ("Armarouge ex", "PAR", "218", "Ultra Rare", "Pokémon"),
                ("Garchomp ex", "PAR", "219", "Ultra Rare", "Pokémon"), ("Tsareena ex", "PAR", "220", "Ultra Rare", "Pokémon"),
                ("Golisopod ex", "PAR", "221", "Ultra Rare", "Pokémon"), ("Tapu Koko ex", "PAR", "222", "Ultra Rare", "Pokémon"),
                ("Iron Hands ex", "PAR", "223", "Ultra Rare", "Pokémon"), ("Cofagrigus ex", "PAR", "224", "Ultra Rare", "Pokémon"),
                ("Iron Valiant ex", "PAR", "225", "Ultra Rare", "Pokémon"), ("Hoopa ex", "PAR", "226", "Ultra Rare", "Pokémon"),
                ("Toxtricity ex", "PAR", "227", "Ultra Rare", "Pokémon"), ("Sandy Shocks ex", "PAR", "228", "Ultra Rare", "Pokémon"),
                ("Roaring Moon ex", "PAR", "229", "Ultra Rare", "Pokémon"), ("Aegislash ex", "PAR", "230", "Ultra Rare", "Pokémon"),
                ("Gholdengo ex", "PAR", "231", "Ultra Rare", "Pokémon"), ("Altaria ex", "PAR", "232", "Ultra Rare", "Pokémon"),
                ("Maushold ex", "PAR", "233", "Ultra Rare", "Pokémon"), ("Bombirdier ex", "PAR", "234", "Ultra Rare", "Pokémon"),
                ("Larry", "PAR", "235", "Ultra Rare", "Trainer"), ("Mela", "PAR", "236", "Ultra Rare", "Trainer"),
                ("Norman", "PAR", "237", "Ultra Rare", "Trainer"), ("Parasol Lady", "PAR", "238", "Ultra Rare", "Trainer"),
                ("Professor Sada’s Vitality", "PAR", "239", "Ultra Rare", "Trainer"), ("Professor Turo’s Scenario", "PAR", "240", "Ultra Rare", "Trainer"),
                ("Rika", "PAR", "241", "Ultra Rare", "Trainer"), ("Roark", "PAR", "242", "Ultra Rare", "Trainer"),
                ("Shauntal", "PAR", "243", "Ultra Rare", "Trainer"), ("Tulip", "PAR", "244", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Garchomp ex", "PAR", "245", "Special Illustration Rare", "Pokémon"), ("Golisopod ex", "PAR", "246", "Special Illustration Rare", "Pokémon"),
                ("Tapu Koko ex", "PAR", "247", "Special Illustration Rare", "Pokémon"), ("Iron Hands ex", "PAR", "248", "Special Illustration Rare", "Pokémon"),
                ("Iron Valiant ex", "PAR", "249", "Special Illustration Rare", "Pokémon"), ("Sandy Shocks ex", "PAR", "250", "Special Illustration Rare", "Pokémon"),
                ("Roaring Moon ex", "PAR", "251", "Special Illustration Rare", "Pokémon"), ("Gholdengo ex", "PAR", "252", "Special Illustration Rare", "Pokémon"),
                ("Altaria ex", "PAR", "253", "Special Illustration Rare", "Pokémon"), ("Mela", "PAR", "254", "Special Illustration Rare", "Trainer"),
                ("Parasol Lady", "PAR", "255", "Special Illustration Rare", "Trainer"), ("Professor Sada’s Vitality", "PAR", "256", "Special Illustration Rare", "Trainer"),
                ("Professor Turo’s Scenario", "PAR", "257", "Special Illustration Rare", "Trainer"), ("Rika", "PAR", "258", "Special Illustration Rare", "Trainer"),
                ("Tulip", "PAR", "259", "Special Illustration Rare", "Trainer")
            ],
            "Hyper Rare": [
                ("Garchomp ex", "PAR", "260", "Hyper Rare", "Pokémon"), ("Iron Valiant ex", "PAR", "261", "Hyper Rare", "Pokémon"),
                ("Roaring Moon ex", "PAR", "262", "Hyper Rare", "Pokémon"), ("Beach Court", "PAR", "263", "Hyper Rare", "Trainer"),
                ("Counter Catcher", "PAR", "264", "Hyper Rare", "Trainer"), ("Luxurious Cape", "PAR", "265", "Hyper Rare", "Trainer"),
                ("Reversal Energy", "PAR", "266", "Hyper Rare", "Energy")
            ]
        }
    },
    "Paldean Fates": {
        "pull_rates": {
            "P_DR": 1/6, "P_SR": 1/4, "P_SUR": 1/13, "P_IR": 1/14, "P_UR": 1/15, "P_SIR": 1/58, "P_HR": 1/62
        },
        "card_database": {
            "Common": [
                ("Pineco", "PAF", "001", "Common", "Pokémon"), ("Maractus", "PAF", "003", "Common", "Pokémon"),
                ("Toedscool", "PAF", "004", "Common", "Pokémon"), ("Charmander", "PAF", "007", "Common", "Pokémon"),
                ("Magmar", "PAF", "009", "Common", "Pokémon"), ("Numel", "PAF", "011", "Common", "Pokémon"),
                ("Charcadet", "PAF", "014", "Common", "Pokémon"), ("Lapras", "PAF", "016", "Common", "Pokémon"),
                ("Frigibax", "PAF", "017", "Common", "Pokémon"), ("Pikachu", "PAF", "018", "Common", "Pokémon"),
                ("Chinchou", "PAF", "020", "Common", "Pokémon"), ("Exeggcute", "PAF", "023", "Common", "Pokémon"),
                ("Natu", "PAF", "025", "Common", "Pokémon"), ("Ralts", "PAF", "027", "Common", "Pokémon"),
                ("Chimecho", "PAF", "030", "Common", "Pokémon"), ("Mime Jr.", "PAF", "031", "Common", "Pokémon"),
                ("Woobat", "PAF", "032", "Common", "Pokémon"), ("Cottonee", "PAF", "034", "Common", "Pokémon"),
                ("Dedenne", "PAF", "036", "Common", "Pokémon"), ("Fidough", "PAF", "038", "Common", "Pokémon"),
                ("Flittle", "PAF", "041", "Common", "Pokémon"), ("Greavard", "PAF", "042", "Common", "Pokémon"),
                ("Gimmighoul", "PAF", "044", "Common", "Pokémon"), ("Mankey", "PAF", "045", "Common", "Pokémon"),
                ("Phanpy", "PAF", "048", "Common", "Pokémon"), ("Barboach", "PAF", "050", "Common", "Pokémon"),
                ("Clobbopus", "PAF", "051", "Common", "Pokémon"), ("Gastly", "PAF", "055", "Common", "Pokémon"),
                ("Haunter", "PAF", "056", "Common", "Pokémon"), ("Paldean Wooper", "PAF", "058", "Common", "Pokémon"),
                ("Scraggy", "PAF", "060", "Common", "Pokémon"), ("Maschiff", "PAF", "062", "Common", "Pokémon"),
                ("Varoom", "PAF", "064", "Common", "Pokémon"), ("Noibat", "PAF", "068", "Common", "Pokémon"),
                ("Lechonk", "PAF", "071", "Common", "Pokémon"), ("Tandemaus", "PAF", "073", "Common", "Pokémon"),
                ("Nemona", "PAF", "082", "Common", "Trainer"), ("Paldean Student", "PAF", "085", "Common", "Trainer"),
                ("Paldean Student", "PAF", "086", "Common", "Trainer"), ("Rare Candy", "PAF", "089", "Common", "Trainer")
            ],
            "Uncommon": [
                ("Charmeleon", "PAF", "008", "Uncommon", "Pokémon"), ("Camerupt", "PAF", "012", "Uncommon", "Pokémon"),
                ("Lanturn", "PAF", "021", "Uncommon", "Pokémon"), ("Kilowattrel", "PAF", "022", "Uncommon", "Pokémon"),
                ("Kirlia", "PAF", "028", "Uncommon", "Pokémon"), ("Swoobat", "PAF", "033", "Uncommon", "Pokémon"),
                ("Whimsicott", "PAF", "035", "Uncommon", "Pokémon"), ("Dachsbun", "PAF", "039", "Uncommon", "Pokémon"),
                ("Primeape", "PAF", "046", "Uncommon", "Pokémon"), ("Donphan", "PAF", "049", "Uncommon", "Pokémon"),
                ("Grapploct", "PAF", "052", "Uncommon", "Pokémon"), ("Gengar", "PAF", "057", "Uncommon", "Pokémon"),
                ("Scrafty", "PAF", "061", "Uncommon", "Pokémon"), ("Oinkologne", "PAF", "072", "Uncommon", "Pokémon"),
                ("Maushold", "PAF", "074", "Uncommon", "Pokémon"), ("Artazon", "PAF", "076", "Uncommon", "Trainer"),
                ("Atticus", "PAF", "077", "Uncommon", "Trainer"), ("Clive", "PAF", "078", "Uncommon", "Trainer"),
                ("Electric Generator", "PAF", "079", "Uncommon", "Trainer"), ("Iono", "PAF", "080", "Uncommon", "Trainer"),
                ("Moonlit Hill", "PAF", "081", "Uncommon", "Trainer"), ("Nemona’s Backpack", "PAF", "083", "Uncommon", "Trainer"),
                ("Nest Ball", "PAF", "084", "Uncommon", "Trainer"), ("Technical Machine: Crisis Punch", "PAF", "090", "Uncommon", "Trainer"),
                ("Ultra Ball", "PAF", "091", "Uncommon", "Trainer")
            ],
            "Rare": [
                ("Magmortar", "PAF", "010", "Rare", "Pokémon"), ("Heat Rotom", "PAF", "013", "Rare", "Pokémon"),
                ("Armarouge", "PAF", "015", "Rare", "Pokémon"), ("Raichu", "PAF", "019", "Rare", "Pokémon"),
                ("Exeggutor", "PAF", "024", "Rare", "Pokémon"), ("Xatu", "PAF", "026", "Rare", "Pokémon"),
                ("Mimikyu", "PAF", "037", "Rare", "Pokémon"), ("Ceruledge", "PAF", "040", "Rare", "Pokémon"),
                ("Houndstone", "PAF", "043", "Rare", "Pokémon"), ("Annihilape", "PAF", "047", "Rare", "Pokémon"),
                ("Mabosstiff", "PAF", "063", "Rare", "Pokémon"), ("Revavroom", "PAF", "065", "Rare", "Pokémon"),
                ("Gholdengo", "PAF", "067", "Rare", "Pokémon"), ("Cyclizar", "PAF", "070", "Rare", "Pokémon"),
                ("Professor’s Research", "PAF", "087", "Rare", "Trainer"), ("Professor’s Research", "PAF", "088", "Rare", "Trainer")
            ],
            "Double Rare": [
                ("Forretress ex", "PAF", "002", "Double Rare", "Pokémon"), ("Toedscruel ex", "PAF", "005", "Double Rare", "Pokémon"),
                ("Espathra ex", "PAF", "006", "Double Rare", "Pokémon"), ("Gardevoir ex", "PAF", "029", "Double Rare", "Pokémon"),
                ("Great Tusk ex", "PAF", "053", "Double Rare", "Pokémon"), ("Charizard ex", "PAF", "054", "Double Rare", "Pokémon"),
                ("Paldean Clodsire ex", "PAF", "059", "Double Rare", "Pokémon"), ("Iron Treads ex", "PAF", "066", "Double Rare", "Pokémon"),
                ("Noivern ex", "PAF", "069", "Double Rare", "Pokémon"), ("Squawkabilly ex", "PAF", "075", "Double Rare", "Pokémon")
            ],
            "Shiny Rare": [
                ("Oddish", "PAF", "092", "Shiny Rare", "Pokémon"), ("Gloom", "PAF", "093", "Shiny Rare", "Pokémon"),
                ("Vileplume", "PAF", "094", "Shiny Rare", "Pokémon"), ("Scyther", "PAF", "095", "Shiny Rare", "Pokémon"),
                ("Hoppip", "PAF", "096", "Shiny Rare", "Pokémon"), ("Skiploom", "PAF", "097", "Shiny Rare", "Pokémon"),
                ("Jumpluff", "PAF", "098", "Shiny Rare", "Pokémon"), ("Pineco", "PAF", "099", "Shiny Rare", "Pokémon"),
                ("Snover", "PAF", "100", "Shiny Rare", "Pokémon"), ("Abomasnow", "PAF", "101", "Shiny Rare", "Pokémon"),
                ("Smoliv", "PAF", "102", "Shiny Rare", "Pokémon"), ("Dolliv", "PAF", "103", "Shiny Rare", "Pokémon"),
                ("Arboliva", "PAF", "104", "Shiny Rare", "Pokémon"), ("Toedscool", "PAF", "105", "Shiny Rare", "Pokémon"),
                ("Capsakid", "PAF", "106", "Shiny Rare", "Pokémon"), ("Scovillain", "PAF", "107", "Shiny Rare", "Pokémon"),
                ("Rellor", "PAF", "108", "Shiny Rare", "Pokémon"), ("Charmander", "PAF", "109", "Shiny Rare", "Pokémon"),
                ("Charmeleon", "PAF", "110", "Shiny Rare", "Pokémon"), ("Paldean Tauros", "PAF", "111", "Shiny Rare", "Pokémon"),
                ("Entei", "PAF", "112", "Shiny Rare", "Pokémon"), ("Oricorio", "PAF", "113", "Shiny Rare", "Pokémon"),
                ("Charcadet", "PAF", "114", "Shiny Rare", "Pokémon"), ("Armarouge", "PAF", "115", "Shiny Rare", "Pokémon"),
                ("Slowpoke", "PAF", "116", "Shiny Rare", "Pokémon"), ("Slowbro", "PAF", "117", "Shiny Rare", "Pokémon"),
                ("Staryu", "PAF", "118", "Shiny Rare", "Pokémon"), ("Starmie", "PAF", "119", "Shiny Rare", "Pokémon"),
                ("Paldean Tauros", "PAF", "120", "Shiny Rare", "Pokémon"), ("Wiglett", "PAF", "121", "Shiny Rare", "Pokémon"),
                ("Wugtrio", "PAF", "122", "Shiny Rare", "Pokémon"), ("Finizen", "PAF", "123", "Shiny Rare", "Pokémon"),
                ("Palafin", "PAF", "124", "Shiny Rare", "Pokémon"), ("Veluza", "PAF", "125", "Shiny Rare", "Pokémon"),
                ("Dondozo", "PAF", "126", "Shiny Rare", "Pokémon"), ("Tatsugiri", "PAF", "127", "Shiny Rare", "Pokémon"),
                ("Frigibax", "PAF", "128", "Shiny Rare", "Pokémon"), ("Arctibax", "PAF", "129", "Shiny Rare", "Pokémon"),
                ("Baxcalibur", "PAF", "130", "Shiny Rare", "Pokémon"), ("Pikachu", "PAF", "131", "Shiny Rare", "Pokémon"),
                ("Raichu", "PAF", "132", "Shiny Rare", "Pokémon"), ("Voltorb", "PAF", "133", "Shiny Rare", "Pokémon"),
                ("Electrode", "PAF", "134", "Shiny Rare", "Pokémon"), ("Shinx", "PAF", "135", "Shiny Rare", "Pokémon"),
                ("Luxio", "PAF", "136", "Shiny Rare", "Pokémon"), ("Luxray", "PAF", "137", "Shiny Rare", "Pokémon"),
                ("Pachirisu", "PAF", "138", "Shiny Rare", "Pokémon"), ("Thundurus", "PAF", "139", "Shiny Rare", "Pokémon"),
                ("Toxel", "PAF", "140", "Shiny Rare", "Pokémon"), ("Toxtricity", "PAF", "141", "Shiny Rare", "Pokémon"),
                ("Pawmi", "PAF", "142", "Shiny Rare", "Pokémon"), ("Pawmo", "PAF", "143", "Shiny Rare", "Pokémon"),
                ("Pawmot", "PAF", "144", "Shiny Rare", "Pokémon"), ("Wattrel", "PAF", "145", "Shiny Rare", "Pokémon"),
                ("Kilowattrel", "PAF", "146", "Shiny Rare", "Pokémon"), ("Wigglytuff", "PAF", "147", "Shiny Rare", "Pokémon"),
                ("Abra", "PAF", "148", "Shiny Rare", "Pokémon"), ("Kadabra", "PAF", "149", "Shiny Rare", "Pokémon"),
                ("Cleffa", "PAF", "150", "Shiny Rare", "Pokémon"), ("Natu", "PAF", "151", "Shiny Rare", "Pokémon"),
                ("Xatu", "PAF", "152", "Shiny Rare", "Pokémon"), ("Ralts", "PAF", "153", "Shiny Rare", "Pokémon"),
                ("Kirlia", "PAF", "154", "Shiny Rare", "Pokémon"), ("Drifloon", "PAF", "155", "Shiny Rare", "Pokémon"),
                ("Drifblim", "PAF", "156", "Shiny Rare", "Pokémon"), ("Mime Jr.", "PAF", "157", "Shiny Rare", "Pokémon"),
                ("Spiritomb", "PAF", "158", "Shiny Rare", "Pokémon"), ("Klefki", "PAF", "159", "Shiny Rare", "Pokémon"),
                ("Mimikyu", "PAF", "160", "Shiny Rare", "Pokémon"), ("Dachsbun", "PAF", "161", "Shiny Rare", "Pokémon"),
                ("Ceruledge", "PAF", "162", "Shiny Rare", "Pokémon"), ("Rabsca", "PAF", "163", "Shiny Rare", "Pokémon"),
                ("Flittle", "PAF", "164", "Shiny Rare", "Pokémon"), ("Tinkatink", "PAF", "165", "Shiny Rare", "Pokémon"),
                ("Tinkatuff", "PAF", "166", "Shiny Rare", "Pokémon"), ("Tinkaton", "PAF", "167", "Shiny Rare", "Pokémon"),
                ("Houndstone", "PAF", "168", "Shiny Rare", "Pokémon"), ("Mankey", "PAF", "169", "Shiny Rare", "Pokémon"),
                ("Primeape", "PAF", "170", "Shiny Rare", "Pokémon"), ("Annihilape", "PAF", "171", "Shiny Rare", "Pokémon"),
                ("Paldean Tauros", "PAF", "172", "Shiny Rare", "Pokémon"), ("Riolu", "PAF", "173", "Shiny Rare", "Pokémon"),
                ("Lucario", "PAF", "174", "Shiny Rare", "Pokémon"), ("Hawlucha", "PAF", "175", "Shiny Rare", "Pokémon"),
                ("Nacli", "PAF", "176", "Shiny Rare", "Pokémon"), ("Naclstack", "PAF", "177", "Shiny Rare", "Pokémon"),
                ("Garganacl", "PAF", "178", "Shiny Rare", "Pokémon"), ("Glimmet", "PAF", "179", "Shiny Rare", "Pokémon"),
                ("Paldean Wooper", "PAF", "180", "Shiny Rare", "Pokémon"), ("Murkrow", "PAF", "181", "Shiny Rare", "Pokémon"),
                ("Sneasel", "PAF", "182", "Shiny Rare", "Pokémon"), ("Weavile", "PAF", "183", "Shiny Rare", "Pokémon"),
                ("Sableye", "PAF", "184", "Shiny Rare", "Pokémon"), ("Pawniard", "PAF", "185", "Shiny Rare", "Pokémon"),
                ("Bisharp", "PAF", "186", "Shiny Rare", "Pokémon"), ("Kingambit", "PAF", "187", "Shiny Rare", "Pokémon"),
                ("Mabosstiff", "PAF", "188", "Shiny Rare", "Pokémon"), ("Shroodle", "PAF", "189", "Shiny Rare", "Pokémon"),
                ("Grafaiai", "PAF", "190", "Shiny Rare", "Pokémon"), ("Scizor", "PAF", "191", "Shiny Rare", "Pokémon"),
                ("Varoom", "PAF", "192", "Shiny Rare", "Pokémon"), ("Revavroom", "PAF", "193", "Shiny Rare", "Pokémon"),
                ("Noibat", "PAF", "194", "Shiny Rare", "Pokémon"), ("Cyclizar", "PAF", "195", "Shiny Rare", "Pokémon"),
                ("Pidgey", "PAF", "196", "Shiny Rare", "Pokémon"), ("Pidgeotto", "PAF", "197", "Shiny Rare", "Pokémon"),
                ("Jigglypuff", "PAF", "198", "Shiny Rare", "Pokémon"), ("Doduo", "PAF", "199", "Shiny Rare", "Pokémon"),
                ("Dodrio", "PAF", "200", "Shiny Rare", "Pokémon"), ("Ditto", "PAF", "201", "Shiny Rare", "Pokémon"),
                ("Snorlax", "PAF", "202", "Shiny Rare", "Pokémon"), ("Wingull", "PAF", "203", "Shiny Rare", "Pokémon"),
                ("Pelipper", "PAF", "204", "Shiny Rare", "Pokémon"), ("Skwovet", "PAF", "205", "Shiny Rare", "Pokémon"),
                ("Greedent", "PAF", "206", "Shiny Rare", "Pokémon"), ("Lechonk", "PAF", "207", "Shiny Rare", "Pokémon"),
                ("Oinkologne", "PAF", "208", "Shiny Rare", "Pokémon"), ("Tandemaus", "PAF", "209", "Shiny Rare", "Pokémon"),
                ("Maushold", "PAF", "210", "Shiny Rare", "Pokémon"), ("Flamigo", "PAF", "211", "Shiny Rare", "Pokémon")
            ],
            "Shiny Ultra Rare": [
                ("Forretress ex", "PAF", "212", "Shiny Ultra Rare", "Pokémon"), ("Toedscruel ex", "PAF", "213", "Shiny Ultra Rare", "Pokémon"),
                ("Espathra ex", "PAF", "214", "Shiny Ultra Rare", "Pokémon"), ("Alakazam ex", "PAF", "215", "Shiny Ultra Rare", "Pokémon"),
                ("Mew ex", "PAF", "216", "Shiny Ultra Rare", "Pokémon"), ("Gardevoir ex", "PAF", "217", "Shiny Ultra Rare", "Pokémon"),
                ("Glimmora ex", "PAF", "218", "Shiny Ultra Rare", "Pokémon"), ("Paldean Clodsire ex", "PAF", "219", "Shiny Ultra Rare", "Pokémon"),
                ("Noivern ex", "PAF", "220", "Shiny Ultra Rare", "Pokémon"), ("Pidgeot ex", "PAF", "221", "Shiny Ultra Rare", "Pokémon"),
                ("Wigglytuff ex", "PAF", "222", "Shiny Ultra Rare", "Pokémon"), ("Squawkabilly ex", "PAF", "223", "Shiny Ultra Rare", "Pokémon")
            ],
            "Illustration Rare": [
                ("Wugtrio", "PAF", "224", "Illustration Rare", "Pokémon"), ("Palafin", "PAF", "225", "Illustration Rare", "Pokémon"),
                ("Pawmi", "PAF", "226", "Illustration Rare", "Pokémon")
            ],
            "Ultra Rare": [
                ("Clive", "PAF", "227", "Ultra Rare", "Trainer"), ("Judge", "PAF", "228", "Ultra Rare", "Trainer"),
                ("Nemona", "PAF", "229", "Ultra Rare", "Trainer"), ("Paldean Student", "PAF", "230", "Ultra Rare", "Trainer"),
                ("Paldean Student", "PAF", "231", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Mew ex", "PAF", "232", "Special Illustration Rare", "Pokémon"), ("Gardevoir ex", "PAF", "233", "Special Illustration Rare", "Pokémon"),
                ("Charizard ex", "PAF", "234", "Special Illustration Rare", "Pokémon"), ("Arven", "PAF", "235", "Special Illustration Rare", "Trainer"),
                ("Clive", "PAF", "236", "Special Illustration Rare", "Trainer"), ("Iono", "PAF", "237", "Special Illustration Rare", "Trainer"),
                ("Nemona", "PAF", "238", "Special Illustration Rare", "Trainer"), ("Penny", "PAF", "239", "Special Illustration Rare", "Trainer")
            ],
            "Hyper Rare": [
                ("Wo-Chien ex", "PAF", "240", "Hyper Rare", "Pokémon"), ("Chi-Yu ex", "PAF", "241", "Hyper Rare", "Pokémon"),
                ("Chien-Pao ex", "PAF", "242", "Hyper Rare", "Pokémon"), ("Miraidon ex", "PAF", "243", "Hyper Rare", "Pokémon"),
                ("Ting-Lu ex", "PAF", "244", "Hyper Rare", "Pokémon"), ("Koraidon ex", "PAF", "245", "Hyper Rare", "Pokémon")
            ]
        }
    },
    "Temporal Forces": {
        "pull_rates": {
            "P_DR": 1/6, "P_ASR": 1/20, "P_IR": 1/13, "P_UR": 1/15, "P_SIR": 1/86, "P_HR": 1/139
        },
        "card_database": {
            "Common": [
                ("Scyther", "TEF", "001", "Common", "Pokémon"), ("Pineco", "TEF", "002", "Common", "Pokémon"),
                ("Seedot", "TEF", "003", "Common", "Pokémon"), ("Nuzleaf", "TEF", "004", "Common", "Pokémon"),
                ("Shroomish", "TEF", "006", "Common", "Pokémon"), ("Breloom", "TEF", "007", "Common", "Pokémon"),
                ("Roselia", "TEF", "008", "Common", "Pokémon"), ("Turtwig", "TEF", "010", "Common", "Pokémon"),
                ("Grotle", "TEF", "011", "Common", "Pokémon"), ("Cottonee", "TEF", "014", "Common", "Pokémon"),
                ("Deerling", "TEF", "016", "Common", "Pokémon"), ("Grubbin", "TEF", "018", "Common", "Pokémon"),
                ("Bramblin", "TEF", "020", "Common", "Pokémon"), ("Rellor", "TEF", "023", "Common", "Pokémon"),
                ("Ponyta", "TEF", "026", "Common", "Pokémon"), ("Slugma", "TEF", "028", "Common", "Pokémon"),
                ("Victini", "TEF", "030", "Common", "Pokémon"), ("Heatmor", "TEF", "031", "Common", "Pokémon"),
                ("Litten", "TEF", "032", "Common", "Pokémon"), ("Torracat", "TEF", "033", "Common", "Pokémon"),
                ("Turtonator", "TEF", "035", "Common", "Pokémon"), ("Sizzlipede", "TEF", "036", "Common", "Pokémon"),
                ("Totodile", "TEF", "039", "Common", "Pokémon"), ("Croconaw", "TEF", "040", "Common", "Pokémon"),
                ("Carvanha", "TEF", "042", "Common", "Pokémon"), ("Snom", "TEF", "045", "Common", "Pokémon"),
                ("Frosmoth", "TEF", "046", "Common", "Pokémon"), ("Wiglett", "TEF", "047", "Common", "Pokémon"),
                ("Finizen", "TEF", "048", "Common", "Pokémon"), ("Pikachu", "TEF", "051", "Common", "Pokémon"),
                ("Raichu", "TEF", "052", "Common", "Pokémon"), ("Electabuzz", "TEF", "053", "Common", "Pokémon"),
                ("Charjabug", "TEF", "055", "Common", "Pokémon"), ("Yamper", "TEF", "058", "Common", "Pokémon"),
                ("Mr. Mime", "TEF", "063", "Common", "Pokémon"), ("Marill", "TEF", "064", "Common", "Pokémon"),
                ("Azumarill", "TEF", "065", "Common", "Pokémon"), ("Girafarig", "TEF", "066", "Common", "Pokémon"),
                ("Bronzor", "TEF", "068", "Common", "Pokémon"), ("Solosis", "TEF", "070", "Common", "Pokémon"),
                ("Duosion", "TEF", "071", "Common", "Pokémon"), ("Elgyem", "TEF", "073", "Common", "Pokémon"),
                ("Cutiefly", "TEF", "075", "Common", "Pokémon"), ("Meditite", "TEF", "082", "Common", "Pokémon"),
                ("Medicham", "TEF", "083", "Common", "Pokémon"), ("Drilbur", "TEF", "085", "Common", "Pokémon"),
                ("Golett", "TEF", "087", "Common", "Pokémon"), ("Rockruff", "TEF", "089", "Common", "Pokémon"),
                ("Mudbray", "TEF", "091", "Common", "Pokémon"), ("Rolycoly", "TEF", "093", "Common", "Pokémon"),
                ("Carkol", "TEF", "094", "Common", "Pokémon"), ("Ekans", "TEF", "100", "Common", "Pokémon"),
                ("Arbok", "TEF", "101", "Common", "Pokémon"), ("Gastly", "TEF", "102", "Common", "Pokémon"),
                ("Haunter", "TEF", "103", "Common", "Pokémon"), ("Poochyena", "TEF", "105", "Common", "Pokémon"),
                ("Mightyena", "TEF", "106", "Common", "Pokémon"), ("Mawile", "TEF", "112", "Common", "Pokémon"),
                ("Beldum", "TEF", "113", "Common", "Pokémon"), ("Metang", "TEF", "114", "Common", "Pokémon"),
                ("Meltan", "TEF", "116", "Common", "Pokémon"), ("Lickitung", "TEF", "124", "Common", "Pokémon"),
                ("Lickilicky", "TEF", "125", "Common", "Pokémon"), ("Hoothoot", "TEF", "126", "Common", "Pokémon"),
                ("Noctowl", "TEF", "127", "Common", "Pokémon"), ("Dunsparce", "TEF", "128", "Common", "Pokémon"),
                ("Skitty", "TEF", "130", "Common", "Pokémon"), ("Chatot", "TEF", "132", "Common", "Pokémon"),
                ("Pidove", "TEF", "133", "Common", "Pokémon"), ("Tranquill", "TEF", "134", "Common", "Pokémon"),
                ("Minccino", "TEF", "136", "Common", "Pokémon")
            ],
            "Uncommon": [
                ("Shiftry", "TEF", "005", "Uncommon", "Pokémon"), ("Roserade", "TEF", "009", "Uncommon", "Pokémon"),
                ("Shaymin", "TEF", "013", "Uncommon", "Pokémon"), ("Sawsbuck", "TEF", "017", "Uncommon", "Pokémon"),
                ("Dhelmise", "TEF", "019", "Uncommon", "Pokémon"), ("Rabsca", "TEF", "024", "Uncommon", "Pokémon"),
                ("Rapidash", "TEF", "027", "Uncommon", "Pokémon"), ("Centiskorch", "TEF", "037", "Uncommon", "Pokémon"),
                ("Sharpedo", "TEF", "043", "Uncommon", "Pokémon"), ("Keldeo", "TEF", "044", "Uncommon", "Pokémon"),
                ("Palafin", "TEF", "049", "Uncommon", "Pokémon"), ("Electivire", "TEF", "054", "Uncommon", "Pokémon"),
                ("Vikavolt", "TEF", "056", "Uncommon", "Pokémon"), ("Zeraora", "TEF", "057", "Uncommon", "Pokémon"),
                ("Boltund", "TEF", "059", "Uncommon", "Pokémon"), ("Iron Hands", "TEF", "061", "Uncommon", "Pokémon"),
                ("Latias", "TEF", "067", "Uncommon", "Pokémon"), ("Bronzong", "TEF", "069", "Uncommon", "Pokémon"),
                ("Reuniclus", "TEF", "072", "Uncommon", "Pokémon"), ("Beheeyem", "TEF", "074", "Uncommon", "Pokémon"),
                ("Ribombee", "TEF", "076", "Uncommon", "Pokémon"), ("Scream Tail", "TEF", "077", "Uncommon", "Pokémon"),
                ("Iron Valiant", "TEF", "079", "Uncommon", "Pokémon"), ("Excadrill", "TEF", "086", "Uncommon", "Pokémon"),
                ("Golurk", "TEF", "088", "Uncommon", "Pokémon"), ("Lycanroc", "TEF", "090", "Uncommon", "Pokémon"),
                ("Mudsdale", "TEF", "092", "Uncommon", "Pokémon"), ("Coalossal", "TEF", "095", "Uncommon", "Pokémon"),
                ("Great Tusk", "TEF", "096", "Uncommon", "Pokémon"), ("Great Tusk", "TEF", "097", "Uncommon", "Pokémon"),
                ("Sandy Shocks", "TEF", "098", "Uncommon", "Pokémon"), ("Sableye", "TEF", "107", "Uncommon", "Pokémon"),
                ("Forretress", "TEF", "110", "Uncommon", "Pokémon"), ("Metagross", "TEF", "115", "Uncommon", "Pokémon"),
                ("Iron Treads", "TEF", "118", "Uncommon", "Pokémon"), ("Delcatty", "TEF", "131", "Uncommon", "Pokémon"),
                ("Unfezant", "TEF", "135", "Uncommon", "Pokémon"), ("Cinccino", "TEF", "137", "Uncommon", "Pokémon"),
                ("Iron Jugulis", "TEF", "139", "Uncommon", "Pokémon"), ("Ancient Booster Energy Capsule", "TEF", "140", "Uncommon", "Trainer"),
                ("Bianca’s Devotion", "TEF", "142", "Uncommon", "Trainer"), ("Boxed Order", "TEF", "143", "Uncommon", "Trainer"),
                ("Buddy-Buddy Poffin", "TEF", "144", "Uncommon", "Trainer"), ("Ciphermaniac’s Codebreaking", "TEF", "145", "Uncommon", "Trainer"),
                ("Eri", "TEF", "146", "Uncommon", "Trainer"), ("Explorer’s Guidance", "TEF", "147", "Uncommon", "Trainer"),
                ("Full Metal Lab", "TEF", "148", "Uncommon", "Trainer"), ("Future Booster Energy Capsule", "TEF", "149", "Uncommon", "Trainer"),
                ("Hand Trimmer", "TEF", "150", "Uncommon", "Trainer"), ("Heavy Baton", "TEF", "151", "Uncommon", "Trainer"),
                ("Morty’s Conviction", "TEF", "155", "Uncommon", "Trainer"), ("Perilous Jungle", "TEF", "156", "Uncommon", "Trainer"),
                ("Rescue Board", "TEF", "159", "Uncommon", "Trainer"), ("Salvatore", "TEF", "160", "Uncommon", "Trainer"),
                ("Mist Energy", "TEF", "161", "Uncommon", "Energy")
            ],
            "Rare": [
                ("Whimsicott", "TEF", "015", "Rare", "Pokémon"), ("Brambleghast", "TEF", "021", "Rare", "Pokémon"),
                ("Magcargo", "TEF", "029", "Rare", "Pokémon"), ("Iron Thorns", "TEF", "062", "Rare", "Pokémon"),
                ("Flutter Mane", "TEF", "078", "Rare", "Pokémon"), ("Iron Valiant", "TEF", "080", "Rare", "Pokémon"),
                ("Relicanth", "TEF", "084", "Rare", "Pokémon"), ("Roaring Moon", "TEF", "109", "Rare", "Pokémon"),
                ("Melmetal", "TEF", "117", "Rare", "Pokémon"), ("Koraidon", "TEF", "119", "Rare", "Pokémon"),
                ("Miraidon", "TEF", "121", "Rare", "Pokémon"), ("Dudunsparce", "TEF", "129", "Rare", "Pokémon"),
                ("Drampa", "TEF", "138", "Rare", "Pokémon")
            ],
            "Double Rare": [
                ("Torterra ex", "TEF", "012", "Double Rare", "Pokémon"), ("Scovillain ex", "TEF", "022", "Double Rare", "Pokémon"),
                ("Iron Leaves ex", "TEF", "025", "Double Rare", "Pokémon"), ("Incineroar ex", "TEF", "034", "Double Rare", "Pokémon"),
                ("Gouging Fire ex", "TEF", "038", "Double Rare", "Pokémon"), ("Walking Wake ex", "TEF", "050", "Double Rare", "Pokémon"),
                ("Wugtrio ex", "TEF", "060", "Double Rare", "Pokémon"), ("Iron Crown ex", "TEF", "081", "Double Rare", "Pokémon"),
                ("Iron Boulder ex", "TEF", "099", "Double Rare", "Pokémon"), ("Gengar ex", "TEF", "104", "Double Rare", "Pokémon"),
                ("Farigiraf ex", "TEF", "108", "Double Rare", "Pokémon"), ("Scizor ex", "TEF", "111", "Double Rare", "Pokémon"),
                ("Koraidon ex", "TEF", "120", "Double Rare", "Pokémon"), ("Miraidon ex", "TEF", "122", "Double Rare", "Pokémon"),
                ("Raging Bolt ex", "TEF", "123", "Double Rare", "Pokémon")
            ],
            "ACE SPEC Rare": [
                ("Awakening Drum", "TEF", "141", "ACE SPEC Rare", "Trainer"), ("Hero’s Cape", "TEF", "152", "ACE SPEC Rare", "Trainer"),
                ("Master Ball", "TEF", "153", "ACE SPEC Rare", "Trainer"), ("Maximum Belt", "TEF", "154", "ACE SPEC Rare", "Trainer"),
                ("Prime Catcher", "TEF", "157", "ACE SPEC Rare", "Trainer"), ("Reboot Pod", "TEF", "158", "ACE SPEC Rare", "Trainer"),
                ("Neo Upper Energy", "TEF", "162", "ACE SPEC Rare", "Energy")
            ],
            "Illustration Rare": [
                ("Shiftry", "TEF", "163", "Illustration Rare", "Pokémon"), ("Grotle", "TEF", "164", "Illustration Rare", "Pokémon"),
                ("Deerling", "TEF", "165", "Illustration Rare", "Pokémon"), ("Sawsbuck", "TEF", "166", "Illustration Rare", "Pokémon"),
                ("Litten", "TEF", "167", "Illustration Rare", "Pokémon"), ("Snom", "TEF", "168", "Illustration Rare", "Pokémon"),
                ("Charjabug", "TEF", "169", "Illustration Rare", "Pokémon"), ("Bronzor", "TEF", "170", "Illustration Rare", "Pokémon"),
                ("Reuniclus", "TEF", "171", "Illustration Rare", "Pokémon"), ("Cutiefly", "TEF", "172", "Illustration Rare", "Pokémon"),
                ("Relicanth", "TEF", "173", "Illustration Rare", "Pokémon"), ("Excadrill", "TEF", "174", "Illustration Rare", "Pokémon"),
                ("Mudsdale", "TEF", "175", "Illustration Rare", "Pokémon"), ("Arbok", "TEF", "176", "Illustration Rare", "Pokémon"),
                ("Gastly", "TEF", "177", "Illustration Rare", "Pokémon"), ("Metagross", "TEF", "178", "Illustration Rare", "Pokémon"),
                ("Meltan", "TEF", "179", "Illustration Rare", "Pokémon"), ("Lickitung", "TEF", "180", "Illustration Rare", "Pokémon"),
                ("Chatot", "TEF", "181", "Illustration Rare", "Pokémon"), ("Minccino", "TEF", "182", "Illustration Rare", "Pokémon"),
                ("Cinccino", "TEF", "183", "Illustration Rare", "Pokémon"), ("Drampa", "TEF", "184", "Illustration Rare", "Pokémon")
            ],
            "Ultra Rare": [
                ("Torterra ex", "TEF", "185", "Ultra Rare", "Pokémon"), ("Iron Leaves ex", "TEF", "186", "Ultra Rare", "Pokémon"),
                ("Incineroar ex", "TEF", "187", "Ultra Rare", "Pokémon"), ("Gouging Fire ex", "TEF", "188", "Ultra Rare", "Pokémon"),
                ("Walking Wake ex", "TEF", "189", "Ultra Rare", "Pokémon"), ("Wugtrio ex", "TEF", "190", "Ultra Rare", "Pokémon"),
                ("Iron Crown ex", "TEF", "191", "Ultra Rare", "Pokémon"), ("Iron Boulder ex", "TEF", "192", "Ultra Rare", "Pokémon"),
                ("Gengar ex", "TEF", "193", "Ultra Rare", "Pokémon"), ("Farigiraf ex", "TEF", "194", "Ultra Rare", "Pokémon"),
                ("Scizor ex", "TEF", "195", "Ultra Rare", "Pokémon"), ("Raging Bolt ex", "TEF", "196", "Ultra Rare", "Pokémon"),
                ("Bianca’s Devotion", "TEF", "197", "Ultra Rare", "Trainer"), ("Ciphermaniac’s Codebreaking", "TEF", "198", "Ultra Rare", "Trainer"),
                ("Eri", "TEF", "199", "Ultra Rare", "Trainer"), ("Explorer’s Guidance", "TEF", "200", "Ultra Rare", "Trainer"),
                ("Morty’s Conviction", "TEF", "201", "Ultra Rare", "Trainer"), ("Salvatore", "TEF", "202", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Iron Leaves ex", "TEF", "203", "Special Illustration Rare", "Pokémon"), ("Gouging Fire ex", "TEF", "204", "Special Illustration Rare", "Pokémon"),
                ("Walking Wake ex", "TEF", "205", "Special Illustration Rare", "Pokémon"), ("Iron Crown ex", "TEF", "206", "Special Illustration Rare", "Pokémon"),
                ("Iron Boulder ex", "TEF", "207", "Special Illustration Rare", "Pokémon"), ("Raging Bolt ex", "TEF", "208", "Special Illustration Rare", "Pokémon"),
                ("Bianca’s Devotion", "TEF", "209", "Special Illustration Rare", "Trainer"), ("Eri", "TEF", "210", "Special Illustration Rare", "Trainer"),
                ("Morty’s Conviction", "TEF", "211", "Special Illustration Rare", "Trainer"), ("Salvatore", "TEF", "212", "Special Illustration Rare", "Trainer")
            ],
            "Hyper Rare": [
                ("Iron Leaves ex", "TEF", "213", "Hyper Rare", "Pokémon"), ("Gouging Fire ex", "TEF", "214", "Hyper Rare", "Pokémon"),
                ("Walking Wake ex", "TEF", "215", "Hyper Rare", "Pokémon"), ("Iron Crown ex", "TEF", "216", "Hyper Rare", "Pokémon"),
                ("Iron Boulder ex", "TEF", "217", "Hyper Rare", "Pokémon"), ("Raging Bolt ex", "TEF", "218", "Hyper Rare", "Pokémon")
            ]
        }
    },
        "Twilight Masquerade": {
        "pull_rates": {
            "P_DR": 1/6, "P_ASR": 1/20, "P_IR": 1/13, "P_UR": 1/15, "P_SIR": 1/86, "P_HR": 1/146
        },
        "card_database": {
            "Common": [
                ("Tangela", "TWM", "001", "Common", "Pokémon"), ("Tangrowth", "TWM", "002", "Common", "Pokémon"),
                ("Pinsir", "TWM", "003", "Common", "Pokémon"), ("Spinarak", "TWM", "004", "Common", "Pokémon"),
                ("Sunkern", "TWM", "006", "Common", "Pokémon"), ("Volbeat", "TWM", "009", "Common", "Pokémon"),
                ("Illumise", "TWM", "010", "Common", "Pokémon"), ("Phantump", "TWM", "012", "Common", "Pokémon"),
                ("Trevenant", "TWM", "013", "Common", "Pokémon"), ("Grookey", "TWM", "014", "Common", "Pokémon"),
                ("Thwackey", "TWM", "015", "Common", "Pokémon"), ("Applin", "TWM", "017", "Common", "Pokémon"),
                ("Poltchageist", "TWM", "020", "Common", "Pokémon"), ("Poltchageist", "TWM", "021", "Common", "Pokémon"),
                ("Vulpix", "TWM", "026", "Common", "Pokémon"), ("Ninetales", "TWM", "027", "Common", "Pokémon"),
                ("Slugma", "TWM", "028", "Common", "Pokémon"), ("Torkoal", "TWM", "030", "Common", "Pokémon"),
                ("Chimchar", "TWM", "031", "Common", "Pokémon"), ("Monferno", "TWM", "032", "Common", "Pokémon"),
                ("Darumaka", "TWM", "034", "Common", "Pokémon"), ("Litwick", "TWM", "036", "Common", "Pokémon"),
                ("Lampent", "TWM", "037", "Common", "Pokémon"), ("Poliwag", "TWM", "041", "Common", "Pokémon"),
                ("Poliwhirl", "TWM", "042", "Common", "Pokémon"), ("Goldeen", "TWM", "044", "Common", "Pokémon"),
                ("Seaking", "TWM", "045", "Common", "Pokémon"), ("Jynx", "TWM", "046", "Common", "Pokémon"),
                ("Corphish", "TWM", "047", "Common", "Pokémon"), ("Crawdaunt", "TWM", "048", "Common", "Pokémon"),
                ("Feebas", "TWM", "049", "Common", "Pokémon"), ("Snorunt", "TWM", "051", "Common", "Pokémon"),
                ("Phione", "TWM", "055", "Common", "Pokémon"), ("Froakie", "TWM", "056", "Common", "Pokémon"),
                ("Frogadier", "TWM", "057", "Common", "Pokémon"), ("Finizen", "TWM", "059", "Common", "Pokémon"),
                ("Shinx", "TWM", "066", "Common", "Pokémon"), ("Luxio", "TWM", "067", "Common", "Pokémon"),
                ("Emolga", "TWM", "069", "Common", "Pokémon"), ("Helioptile", "TWM", "070", "Common", "Pokémon"),
                ("Heliolisk", "TWM", "071", "Common", "Pokémon"), ("Tadbulb", "TWM", "073", "Common", "Pokémon"),
                ("Wattrel", "TWM", "075", "Common", "Pokémon"), ("Clefairy", "TWM", "078", "Common", "Pokémon"),
                ("Abra", "TWM", "080", "Common", "Pokémon"), ("Kadabra", "TWM", "081", "Common", "Pokémon"),
                ("Girafarig", "TWM", "083", "Common", "Pokémon"), ("Chimecho", "TWM", "085", "Common", "Pokémon"),
                ("Flabébé", "TWM", "086", "Common", "Pokémon"), ("Floette", "TWM", "087", "Common", "Pokémon"),
                ("Swirlix", "TWM", "089", "Common", "Pokémon"), ("Sandygast", "TWM", "091", "Common", "Pokémon"),
                ("Palossand", "TWM", "092", "Common", "Pokémon"), ("Sandshrew", "TWM", "097", "Common", "Pokémon"),
                ("Hisuian Growlithe", "TWM", "099", "Common", "Pokémon"), ("Nosepass", "TWM", "101", "Common", "Pokémon"),
                ("Timburr", "TWM", "103", "Common", "Pokémon"), ("Gurdurr", "TWM", "104", "Common", "Pokémon"),
                ("Hawlucha", "TWM", "107", "Common", "Pokémon"), ("Glimmet", "TWM", "108", "Common", "Pokémon"),
                ("Poochyena", "TWM", "113", "Common", "Pokémon"), ("Venipede", "TWM", "115", "Common", "Pokémon"),
                ("Whirlipede", "TWM", "116", "Common", "Pokémon"), ("Skarmory", "TWM", "119", "Common", "Pokémon"),
                ("Aron", "TWM", "120", "Common", "Pokémon"), ("Lairon", "TWM", "121", "Common", "Pokémon"),
                ("Varoom", "TWM", "124", "Common", "Pokémon"), ("Applin", "TWM", "126", "Common", "Pokémon"),
                ("Dreepy", "TWM", "128", "Common", "Pokémon"), ("Drakloak", "TWM", "129", "Common", "Pokémon"),
                ("Farfetch’d", "TWM", "132", "Common", "Pokémon"), ("Chansey", "TWM", "133", "Common", "Pokémon"),
                ("Eevee", "TWM", "135", "Common", "Pokémon"), ("Aipom", "TWM", "137", "Common", "Pokémon"),
                ("Ducklett", "TWM", "139", "Common", "Pokémon"), ("Caretaker", "TWM", "144", "Common", "Trainer")
            ],
            "Uncommon": [
                ("Ariados", "TWM", "005", "Uncommon", "Pokémon"), ("Sunflora", "TWM", "007", "Uncommon", "Pokémon"),
                ("Heracross", "TWM", "008", "Uncommon", "Pokémon"), ("Leafeon", "TWM", "011", "Uncommon", "Pokémon"),
                ("Rillaboom", "TWM", "016", "Uncommon", "Pokémon"), ("Dipplin", "TWM", "018", "Uncommon", "Pokémon"),
                ("Darmanitan", "TWM", "035", "Uncommon", "Pokémon"), ("Chi-Yu", "TWM", "039", "Uncommon", "Pokémon"),
                ("Poliwrath", "TWM", "043", "Uncommon", "Pokémon"), ("Milotic", "TWM", "050", "Uncommon", "Pokémon"),
                ("Glalie", "TWM", "052", "Uncommon", "Pokémon"), ("Glaceon", "TWM", "054", "Uncommon", "Pokémon"),
                ("Cramorant", "TWM", "058", "Uncommon", "Pokémon"), ("Palafin", "TWM", "060", "Uncommon", "Pokémon"),
                ("Iron Bundle", "TWM", "062", "Uncommon", "Pokémon"), ("Morpeko", "TWM", "072", "Uncommon", "Pokémon"),
                ("Bellibolt", "TWM", "074", "Uncommon", "Pokémon"), ("Kilowattrel", "TWM", "076", "Uncommon", "Pokémon"),
                ("Clefable", "TWM", "079", "Uncommon", "Pokémon"), ("Farigiraf", "TWM", "084", "Uncommon", "Pokémon"),
                ("Florges", "TWM", "088", "Uncommon", "Pokémon"), ("Slurpuff", "TWM", "090", "Uncommon", "Pokémon"),
                ("Sandslash", "TWM", "098", "Uncommon", "Pokémon"), ("Probopass", "TWM", "102", "Uncommon", "Pokémon"),
                ("Conkeldurr", "TWM", "105", "Uncommon", "Pokémon"), ("Glimmora", "TWM", "109", "Uncommon", "Pokémon"),
                ("Mightyena", "TWM", "114", "Uncommon", "Pokémon"), ("Scolipede", "TWM", "117", "Uncommon", "Pokémon"),
                ("Brute Bonnet", "TWM", "118", "Uncommon", "Pokémon"), ("Aggron", "TWM", "122", "Uncommon", "Pokémon"),
                ("Revavroom", "TWM", "125", "Uncommon", "Pokémon"), ("Dipplin", "TWM", "127", "Uncommon", "Pokémon"),
                ("Tatsugiri", "TWM", "131", "Uncommon", "Pokémon"), ("Snorlax", "TWM", "136", "Uncommon", "Pokémon"),
                ("Ambipom", "TWM", "138", "Uncommon", "Pokémon"), ("Swanna", "TWM", "140", "Uncommon", "Pokémon"),
                ("Accompanying Flute", "TWM", "142", "Uncommon", "Trainer"), ("Bug Catching Set", "TWM", "143", "Uncommon", "Trainer"),
                ("Carmine", "TWM", "145", "Uncommon", "Trainer"), ("Community Center", "TWM", "146", "Uncommon", "Trainer"),
                ("Cook", "TWM", "147", "Uncommon", "Trainer"), ("Enhanced Hammer", "TWM", "148", "Uncommon", "Trainer"),
                ("Festival Grounds", "TWM", "149", "Uncommon", "Trainer"), ("Handheld Fan", "TWM", "150", "Uncommon", "Trainer"),
                ("Hassel", "TWM", "151", "Uncommon", "Trainer"), ("Jamming Tower", "TWM", "153", "Uncommon", "Trainer"),
                ("Kieran", "TWM", "154", "Uncommon", "Trainer"), ("Lana’s Aid", "TWM", "155", "Uncommon", "Trainer"),
                ("Love Ball", "TWM", "156", "Uncommon", "Trainer"), ("Lucian", "TWM", "157", "Uncommon", "Trainer"),
                ("Lucky Helmet", "TWM", "158", "Uncommon", "Trainer"), ("Ogre’s Mask", "TWM", "159", "Uncommon", "Trainer"),
                ("Perrin", "TWM", "160", "Uncommon", "Trainer"), ("Raifort", "TWM", "161", "Uncommon", "Trainer"),
                ("Boomerang Energy", "TWM", "166", "Uncommon", "Energy")
            ],
            "Rare": [
                ("Iron Leaves", "TWM", "019", "Rare", "Pokémon"), ("Sinistcha", "TWM", "022", "Rare", "Pokémon"),
                ("Teal Mask Ogerpon", "TWM", "024", "Rare", "Pokémon"), ("Infernape", "TWM", "033", "Rare", "Pokémon"),
                ("Chandelure", "TWM", "038", "Rare", "Pokémon"), ("Froslass", "TWM", "053", "Rare", "Pokémon"),
                ("Walking Wake", "TWM", "063", "Rare", "Pokémon"), ("Zapdos", "TWM", "065", "Rare", "Pokémon"),
                ("Alakazam", "TWM", "082", "Rare", "Pokémon"), ("Enamorus", "TWM", "093", "Rare", "Pokémon"),
                ("Munkidori", "TWM", "095", "Rare", "Pokémon"), ("Fezandipiti", "TWM", "096", "Rare", "Pokémon"),
                ("Hisuian Arcanine", "TWM", "100", "Rare", "Pokémon"), ("Ting-Lu", "TWM", "110", "Rare", "Pokémon"),
                ("Okidogi", "TWM", "111", "Rare", "Pokémon"), ("Heatran", "TWM", "123", "Rare", "Pokémon")
            ],
            "Double Rare": [
                ("Sinistcha ex", "TWM", "023", "Double Rare", "Pokémon"), ("Teal Mask Ogerpon ex", "TWM", "025", "Double Rare", "Pokémon"),
                ("Magcargo ex", "TWM", "029", "Double Rare", "Pokémon"), ("Hearthflame Mask Ogerpon ex", "TWM", "040", "Double Rare", "Pokémon"),
                ("Palafin ex", "TWM", "061", "Double Rare", "Pokémon"), ("Wellspring Mask Ogerpon ex", "TWM", "064", "Double Rare", "Pokémon"),
                ("Luxray ex", "TWM", "068", "Double Rare", "Pokémon"), ("Iron Thorns ex", "TWM", "077", "Double Rare", "Pokémon"),
                ("Scream Tail ex", "TWM", "094", "Double Rare", "Pokémon"), ("Greninja ex", "TWM", "106", "Double Rare", "Pokémon"),
                ("Cornerstone Mask Ogerpon ex", "TWM", "112", "Double Rare", "Pokémon"), ("Dragapult ex", "TWM", "130", "Double Rare", "Pokémon"),
                ("Blissey ex", "TWM", "134", "Double Rare", "Pokémon"), ("Bloodmoon Ursaluna ex", "TWM", "141", "Double Rare", "Pokémon")
            ],
            "ACE SPEC Rare": [
                ("Hyper Aroma", "TWM", "152", "ACE SPEC Rare", "Trainer"), ("Scoop Up Cyclone", "TWM", "162", "ACE SPEC Rare", "Trainer"),
                ("Secret Box", "TWM", "163", "ACE SPEC Rare", "Trainer"), ("Survival Brace", "TWM", "164", "ACE SPEC Rare", "Trainer"),
                ("Unfair Stamp", "TWM", "165", "ACE SPEC Rare", "Trainer"), ("Legacy Energy", "TWM", "167", "ACE SPEC Rare", "Energy")
            ],
            "Illustration Rare": [
                ("Pinsir", "TWM", "168", "Illustration Rare", "Pokémon"), ("Sunflora", "TWM", "169", "Illustration Rare", "Pokémon"),
                ("Dipplin", "TWM", "170", "Illustration Rare", "Pokémon"), ("Poltchageist", "TWM", "171", "Illustration Rare", "Pokémon"),
                ("Torkoal", "TWM", "172", "Illustration Rare", "Pokémon"), ("Infernape", "TWM", "173", "Illustration Rare", "Pokémon"),
                ("Froslass", "TWM", "174", "Illustration Rare", "Pokémon"), ("Phione", "TWM", "175", "Illustration Rare", "Pokémon"),
                ("Cramorant", "TWM", "176", "Illustration Rare", "Pokémon"), ("Heliolisk", "TWM", "177", "Illustration Rare", "Pokémon"),
                ("Wattrel", "TWM", "178", "Illustration Rare", "Pokémon"), ("Chimecho", "TWM", "179", "Illustration Rare", "Pokémon"),
                ("Enamorus", "TWM", "180", "Illustration Rare", "Pokémon"), ("Hisuian Growlithe", "TWM", "181", "Illustration Rare", "Pokémon"),
                ("Probopass", "TWM", "182", "Illustration Rare", "Pokémon"), ("Timburr", "TWM", "183", "Illustration Rare", "Pokémon"),
                ("Lairon", "TWM", "184", "Illustration Rare", "Pokémon"), ("Applin", "TWM", "185", "Illustration Rare", "Pokémon"),
                ("Tatsugiri", "TWM", "186", "Illustration Rare", "Pokémon"), ("Chansey", "TWM", "187", "Illustration Rare", "Pokémon"),
                ("Eevee", "TWM", "188", "Illustration Rare", "Pokémon")
            ],
            "Ultra Rare": [
                ("Sinistcha ex", "TWM", "189", "Ultra Rare", "Pokémon"), ("Teal Mask Ogerpon ex", "TWM", "190", "Ultra Rare", "Pokémon"),
                ("Magcargo ex", "TWM", "191", "Ultra Rare", "Pokémon"), ("Hearthflame Mask Ogerpon ex", "TWM", "192", "Ultra Rare", "Pokémon"),
                ("Palafin ex", "TWM", "193", "Ultra Rare", "Pokémon"), ("Wellspring Mask Ogerpon ex", "TWM", "194", "Ultra Rare", "Pokémon"),
                ("Luxray ex", "TWM", "195", "Ultra Rare", "Pokémon"), ("Iron Thorns ex", "TWM", "196", "Ultra Rare", "Pokémon"),
                ("Scream Tail ex", "TWM", "197", "Ultra Rare", "Pokémon"), ("Greninja ex", "TWM", "198", "Ultra Rare", "Pokémon"),
                ("Cornerstone Mask Ogerpon ex", "TWM", "199", "Ultra Rare", "Pokémon"), ("Dragapult ex", "TWM", "200", "Ultra Rare", "Pokémon"),
                ("Blissey ex", "TWM", "201", "Ultra Rare", "Pokémon"), ("Bloodmoon Ursaluna ex", "TWM", "202", "Ultra Rare", "Pokémon"),
                ("Caretaker", "TWM", "203", "Ultra Rare", "Trainer"), ("Carmine", "TWM", "204", "Ultra Rare", "Trainer"),
                ("Hassel", "TWM", "205", "Ultra Rare", "Trainer"), ("Kieran", "TWM", "206", "Ultra Rare", "Trainer"),
                ("Lana’s Aid", "TWM", "207", "Ultra Rare", "Trainer"), ("Lucian", "TWM", "208", "Ultra Rare", "Trainer"),
                ("Perrin", "TWM", "209", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Sinistcha ex", "TWM", "210", "Special Illustration Rare", "Pokémon"), ("Teal Mask Ogerpon ex", "TWM", "211", "Special Illustration Rare", "Pokémon"),
                ("Hearthflame Mask Ogerpon ex", "TWM", "212", "Special Illustration Rare", "Pokémon"), ("Wellspring Mask Ogerpon ex", "TWM", "213", "Special Illustration Rare", "Pokémon"),
                ("Greninja ex", "TWM", "214", "Special Illustration Rare", "Pokémon"), ("Cornerstone Mask Ogerpon ex", "TWM", "215", "Special Illustration Rare", "Pokémon"),
                ("Bloodmoon Ursaluna ex", "TWM", "216", "Special Illustration Rare", "Pokémon"), ("Carmine", "TWM", "217", "Special Illustration Rare", "Trainer"),
                ("Kieran", "TWM", "218", "Special Illustration Rare", "Trainer"), ("Lana’s Aid", "TWM", "219", "Special Illustration Rare", "Trainer"),
                ("Perrin", "TWM", "220", "Special Illustration Rare", "Trainer")
            ],
            "Hyper Rare": [
                ("Teal Mask Ogerpon ex", "TWM", "221", "Hyper Rare", "Pokémon"), ("Bloodmoon Ursaluna ex", "TWM", "222", "Hyper Rare", "Pokémon"),
                ("Buddy-Buddy Poffin", "TWM", "223", "Hyper Rare", "Trainer"), ("Enhanced Hammer", "TWM", "224", "Hyper Rare", "Trainer"),
                ("Rescue Board", "TWM", "225", "Hyper Rare", "Trainer"), ("Luminous Energy", "TWM", "226", "Hyper Rare", "Energy")
            ]
        }
    },
        "Shrouded Fable": {
        "pull_rates": {
            "P_DR": 1/6, "P_ASR": 1/20, "P_IR": 1/12, "P_UR": 1/15, "P_SIR": 1/67, "P_HR": 1/144
        },
        "card_database": {
            "Common": [
                ("Joltik", "SFA", "001", "Common", "Pokémon"), ("Rowlet", "SFA", "003", "Common", "Pokémon"),
                ("Dartrix", "SFA", "004", "Common", "Pokémon"), ("Houndour", "SFA", "007", "Common", "Pokémon"),
                ("Houndoom", "SFA", "008", "Common", "Pokémon"), ("Horsea", "SFA", "010", "Common", "Pokémon"),
                ("Seadra", "SFA", "011", "Common", "Pokémon"), ("Sneasel", "SFA", "013", "Common", "Pokémon"),
                ("Drowzee", "SFA", "016", "Common", "Pokémon"), ("Duskull", "SFA", "018", "Common", "Pokémon"),
                ("Dusclops", "SFA", "019", "Common", "Pokémon"), ("Croagunk", "SFA", "023", "Common", "Pokémon"),
                ("Toxicroak", "SFA", "024", "Common", "Pokémon"), ("Zubat", "SFA", "027", "Common", "Pokémon"),
                ("Golbat", "SFA", "028", "Common", "Pokémon"), ("Absol", "SFA", "030", "Common", "Pokémon"),
                ("Zorua", "SFA", "031", "Common", "Pokémon"), ("Inkay", "SFA", "033", "Common", "Pokémon"),
                ("Cufant", "SFA", "041", "Common", "Pokémon"), ("Varoom", "SFA", "043", "Common", "Pokémon"),
                ("Axew", "SFA", "044", "Common", "Pokémon"), ("Fraxure", "SFA", "045", "Common", "Pokémon"),
                ("Meowth", "SFA", "048", "Common", "Pokémon"), ("Persian", "SFA", "049", "Common", "Pokémon"),
                ("Eevee", "SFA", "050", "Common", "Pokémon"), ("Furfrou", "SFA", "051", "Common", "Pokémon"),
                ("Stufful", "SFA", "052", "Common", "Pokémon"), ("Bewear", "SFA", "053", "Common", "Pokémon")
            ],
            "Uncommon": [
                ("Galvantula", "SFA", "002", "Uncommon", "Pokémon"), ("Decidueye", "SFA", "005", "Uncommon", "Pokémon"),
                ("Iron Moth", "SFA", "009", "Uncommon", "Pokémon"), ("Weavile", "SFA", "014", "Uncommon", "Pokémon"),
                ("Hypno", "SFA", "017", "Uncommon", "Pokémon"), ("Sylveon", "SFA", "022", "Uncommon", "Pokémon"),
                ("Slither Wing", "SFA", "026", "Uncommon", "Pokémon"), ("Crobat", "SFA", "029", "Uncommon", "Pokémon"),
                ("Malamar", "SFA", "034", "Uncommon", "Pokémon"), ("Yveltal", "SFA", "035", "Uncommon", "Pokémon"),
                ("Genesect", "SFA", "040", "Uncommon", "Pokémon"), ("Kyurem", "SFA", "047", "Uncommon", "Pokémon"),
                ("Academy at Night", "SFA", "054", "Uncommon", "Trainer"), ("Binding Mochi", "SFA", "055", "Uncommon", "Trainer"),
                ("Cassiopeia", "SFA", "056", "Uncommon", "Trainer"), ("Colress’s Tenacity", "SFA", "057", "Uncommon", "Trainer"),
                ("Janine’s Secret Art", "SFA", "059", "Uncommon", "Trainer"), ("Night Stretcher", "SFA", "061", "Uncommon", "Trainer"),
                ("Powerglass", "SFA", "063", "Uncommon", "Trainer"), ("Xerosic’s Machinations", "SFA", "064", "Uncommon", "Trainer")
            ],
            "Rare": [
                ("Tapu Bulu", "SFA", "006", "Rare", "Pokémon"), ("Dusknoir", "SFA", "020", "Rare", "Pokémon"),
                ("Cresselia", "SFA", "021", "Rare", "Pokémon"), ("Bloodmoon Ursaluna", "SFA", "025", "Rare", "Pokémon"),
                ("Zoroark", "SFA", "032", "Rare", "Pokémon"), ("Copperajah", "SFA", "042", "Rare", "Pokémon"),
                ("Haxorus", "SFA", "046", "Rare", "Pokémon")
            ],
            "Double Rare": [
                ("Kingdra ex", "SFA", "012", "Double Rare", "Pokémon"), ("Revavroom ex", "SFA", "015", "Double Rare", "Pokémon"),
                ("Okidogi ex", "SFA", "036", "Double Rare", "Pokémon"), ("Munkidori ex", "SFA", "037", "Double Rare", "Pokémon"),
                ("Fezandipiti ex", "SFA", "038", "Double Rare", "Pokémon"), ("Pecharunt ex", "SFA", "039", "Double Rare", "Pokémon")
            ],
            "ACE SPEC Rare": [
                ("Dangerous Laser", "SFA", "058", "ACE SPEC Rare", "Trainer"), ("Neutralization Zone", "SFA", "060", "ACE SPEC Rare", "Trainer"),
                ("Poké Vital A", "SFA", "062", "ACE SPEC Rare", "Trainer")
            ],
            "Illustration Rare": [
                ("Tapu Bulu", "SFA", "065", "Illustration Rare", "Pokémon"), ("Houndoom", "SFA", "066", "Illustration Rare", "Pokémon"),
                ("Horsea", "SFA", "067", "Illustration Rare", "Pokémon"), ("Duskull", "SFA", "068", "Illustration Rare", "Pokémon"),
                ("Dusclops", "SFA", "069", "Illustration Rare", "Pokémon"), ("Dusknoir", "SFA", "070", "Illustration Rare", "Pokémon"),
                ("Cresselia", "SFA", "071", "Illustration Rare", "Pokémon"), ("Munkidori", "SFA", "072", "Illustration Rare", "Pokémon"),
                ("Fezandipiti", "SFA", "073", "Illustration Rare", "Pokémon"), ("Okidogi", "SFA", "074", "Illustration Rare", "Pokémon"),
                ("Zorua", "SFA", "075", "Illustration Rare", "Pokémon"), ("Cufant", "SFA", "076", "Illustration Rare", "Pokémon"),
                ("Fraxure", "SFA", "077", "Illustration Rare", "Pokémon"), ("Persian", "SFA", "078", "Illustration Rare", "Pokémon"),
                ("Bewear", "SFA", "079", "Illustration Rare", "Pokémon")
            ],
            "Ultra Rare": [
                ("Kingdra ex", "SFA", "080", "Ultra Rare", "Pokémon"), ("Revavroom ex", "SFA", "081", "Ultra Rare", "Pokémon"),
                ("Okidogi ex", "SFA", "082", "Ultra Rare", "Pokémon"), ("Munkidori ex", "SFA", "083", "Ultra Rare", "Pokémon"),
                ("Fezandipiti ex", "SFA", "084", "Ultra Rare", "Pokémon"), ("Pecharunt ex", "SFA", "085", "Ultra Rare", "Pokémon"),
                ("Cassiopeia", "SFA", "086", "Ultra Rare", "Trainer"), ("Colress’s Tenacity", "SFA", "087", "Ultra Rare", "Trainer"),
                ("Janine’s Secret Art", "SFA", "088", "Ultra Rare", "Trainer"), ("Xerosic’s Machinations", "SFA", "089", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Okidogi ex", "SFA", "090", "Special Illustration Rare", "Pokémon"), ("Munkidori ex", "SFA", "091", "Special Illustration Rare", "Pokémon"),
                ("Fezandipiti ex", "SFA", "092", "Special Illustration Rare", "Pokémon"), ("Pecharunt ex", "SFA", "093", "Special Illustration Rare", "Pokémon"),
                ("Cassiopeia", "SFA", "094", "Special Illustration Rare", "Trainer")
            ],
            "Hyper Rare": [
                ("Pecharunt ex", "SFA", "095", "Hyper Rare", "Pokémon"), ("Earthen Vessel", "SFA", "096", "Hyper Rare", "Trainer"),
                ("Powerglass", "SFA", "097", "Hyper Rare", "Trainer"), ("Basic Darkness Energy", "SFA", "098", "Hyper Rare", "Energy"),
                ("Basic Metal Energy", "SFA", "099", "Hyper Rare", "Energy")
            ]
        }
    },
        "Stellar Crown": {
        "pull_rates": {
            "P_DR": 1/6, "P_ASR": 1/20, "P_IR": 1/13, "P_UR": 1/15, "P_SIR": 1/90, "P_HR": 1/137
        },
        "card_database": {
            "Common": [
                ("Ledyba", "SCR", "002", "Common", "Pokémon"), ("Lileep", "SCR", "005", "Common", "Pokémon"),
                ("Carnivine", "SCR", "007", "Common", "Pokémon"), ("Mow Rotom", "SCR", "008", "Common", "Pokémon"),
                ("Grubbin", "SCR", "009", "Common", "Pokémon"), ("Gossifleur", "SCR", "010", "Common", "Pokémon"),
                ("Applin", "SCR", "012", "Common", "Pokémon"), ("Dipplin", "SCR", "013", "Common", "Pokémon"),
                ("Nymble", "SCR", "015", "Common", "Pokémon"), ("Lokix", "SCR", "016", "Common", "Pokémon"),
                ("Toedscool", "SCR", "017", "Common", "Pokémon"), ("Ponyta", "SCR", "019", "Common", "Pokémon"),
                ("Pansear", "SCR", "021", "Common", "Pokémon"), ("Salandit", "SCR", "023", "Common", "Pokémon"),
                ("Turtonator", "SCR", "025", "Common", "Pokémon"), ("Scorbunny", "SCR", "026", "Common", "Pokémon"),
                ("Raboot", "SCR", "027", "Common", "Pokémon"), ("Charcadet", "SCR", "029", "Common", "Pokémon"),
                ("Marill", "SCR", "033", "Common", "Pokémon"), ("Finneon", "SCR", "035", "Common", "Pokémon"),
                ("Tirtouga", "SCR", "037", "Common", "Pokémon"), ("Froakie", "SCR", "039", "Common", "Pokémon"),
                ("Chewtle", "SCR", "043", "Common", "Pokémon"), ("Electabuzz", "SCR", "046", "Common", "Pokémon"),
                ("Chinchou", "SCR", "048", "Common", "Pokémon"), ("Joltik", "SCR", "050", "Common", "Pokémon"),
                ("Charjabug", "SCR", "052", "Common", "Pokémon"), ("Pawmi", "SCR", "056", "Common", "Pokémon"),
                ("Slowpoke", "SCR", "057", "Common", "Pokémon"), ("Drifloon", "SCR", "060", "Common", "Pokémon"),
                ("Yamask", "SCR", "062", "Common", "Pokémon"), ("Comfey", "SCR", "063", "Common", "Pokémon"),
                ("Milcery", "SCR", "064", "Common", "Pokémon"), ("Fidough", "SCR", "066", "Common", "Pokémon"),
                ("Flittle", "SCR", "068", "Common", "Pokémon"), ("Espathra", "SCR", "069", "Common", "Pokémon"),
                ("Greavard", "SCR", "070", "Common", "Pokémon"), ("Cubone", "SCR", "072", "Common", "Pokémon"),
                ("Rhyhorn", "SCR", "074", "Common", "Pokémon"), ("Rhydon", "SCR", "075", "Common", "Pokémon"),
                ("Meditite", "SCR", "077", "Common", "Pokémon"), ("Meditite", "SCR", "078", "Common", "Pokémon"),
                ("Medicham", "SCR", "079", "Common", "Pokémon"), ("Riolu", "SCR", "081", "Common", "Pokémon"),
                ("Mienfoo", "SCR", "083", "Common", "Pokémon"), ("Pancham", "SCR", "085", "Common", "Pokémon"),
                ("Crabrawler", "SCR", "087", "Common", "Pokémon"), ("Falinks", "SCR", "088", "Common", "Pokémon"),
                ("Gulpin", "SCR", "091", "Common", "Pokémon"), ("Impidimp", "SCR", "094", "Common", "Pokémon"),
                ("Morgrem", "SCR", "095", "Common", "Pokémon"), ("Bombirdier", "SCR", "097", "Common", "Pokémon"),
                ("Klink", "SCR", "099", "Common", "Pokémon"), ("Klang", "SCR", "100", "Common", "Pokémon"),
                ("Meltan", "SCR", "102", "Common", "Pokémon"), ("Meltan", "SCR", "103", "Common", "Pokémon"),
                ("Duraludon", "SCR", "106", "Common", "Pokémon"), ("Varoom", "SCR", "108", "Common", "Pokémon"),
                ("Tauros", "SCR", "112", "Common", "Pokémon"), ("Eevee", "SCR", "113", "Common", "Pokémon"),
                ("Hoothoot", "SCR", "114", "Common", "Pokémon"), ("Glameow", "SCR", "116", "Common", "Pokémon"),
                ("Purugly", "SCR", "117", "Common", "Pokémon"), ("Fan Rotom", "SCR", "118", "Common", "Pokémon"),
                ("Fletchling", "SCR", "121", "Common", "Pokémon"), ("Fletchinder", "SCR", "122", "Common", "Pokémon"),
                ("Wooloo", "SCR", "124", "Common", "Pokémon"), ("Lechonk", "SCR", "126", "Common", "Pokémon"),
                ("Cyclizar", "SCR", "127", "Common", "Pokémon"), ("Antique Cover Fossil", "SCR", "129", "Common", "Trainer"),
                ("Antique Root Fossil", "SCR", "130", "Common", "Trainer")
            ],
            "Uncommon": [
                ("Celebi", "SCR", "004", "Uncommon", "Pokémon"), ("Eldegoss", "SCR", "011", "Uncommon", "Pokémon"),
                ("Toedscruel", "SCR", "018", "Uncommon", "Pokémon"), ("Rapidash", "SCR", "020", "Uncommon", "Pokémon"),
                ("Reshiram", "SCR", "022", "Uncommon", "Pokémon"), ("Salazzle", "SCR", "024", "Uncommon", "Pokémon"),
                ("Lapras", "SCR", "031", "Uncommon", "Pokémon"), ("Azumarill", "SCR", "034", "Uncommon", "Pokémon"),
                ("Lumineon", "SCR", "036", "Uncommon", "Pokémon"), ("Frogadier", "SCR", "040", "Uncommon", "Pokémon"),
                ("Crabominable", "SCR", "042", "Uncommon", "Pokémon"), ("Veluza", "SCR", "045", "Uncommon", "Pokémon"),
                ("Electivire", "SCR", "047", "Uncommon", "Pokémon"), ("Lanturn", "SCR", "049", "Uncommon", "Pokémon"),
                ("Vikavolt", "SCR", "053", "Uncommon", "Pokémon"), ("Togedemaru", "SCR", "054", "Uncommon", "Pokémon"),
                ("Slowking", "SCR", "058", "Uncommon", "Pokémon"), ("Mewtwo", "SCR", "059", "Uncommon", "Pokémon"),
                ("Drifblim", "SCR", "061", "Uncommon", "Pokémon"), ("Marowak", "SCR", "073", "Uncommon", "Pokémon"),
                ("Mienshao", "SCR", "084", "Uncommon", "Pokémon"), ("Diancie", "SCR", "086", "Uncommon", "Pokémon"),
                ("Koraidon", "SCR", "090", "Uncommon", "Pokémon"), ("Swalot", "SCR", "092", "Uncommon", "Pokémon"),
                ("Pangoro", "SCR", "093", "Uncommon", "Pokémon"), ("Jirachi", "SCR", "098", "Uncommon", "Pokémon"),
                ("Revavroom", "SCR", "109", "Uncommon", "Pokémon"), ("Tornadus", "SCR", "120", "Uncommon", "Pokémon"),
                ("Talonflame", "SCR", "123", "Uncommon", "Pokémon"), ("Dubwool", "SCR", "125", "Uncommon", "Pokémon"),
                ("Area Zero Underdepths", "SCR", "131", "Uncommon", "Trainer"), ("Briar", "SCR", "132", "Uncommon", "Trainer"),
                ("Crispin", "SCR", "133", "Uncommon", "Trainer"), ("Glass Trumpet", "SCR", "135", "Uncommon", "Trainer"),
                ("Gravity Gemstone", "SCR", "137", "Uncommon", "Trainer"), ("Kofu", "SCR", "138", "Uncommon", "Trainer"),
                ("Lacey", "SCR", "139", "Uncommon", "Trainer"), ("Occa Berry", "SCR", "140", "Uncommon", "Trainer"),
                ("Payapa Berry", "SCR", "141", "Uncommon", "Trainer")
            ],
            "Rare": [
                ("Ledian", "SCR", "003", "Rare", "Pokémon"), ("Cradily", "SCR", "006", "Rare", "Pokémon"),
                ("Iron Leaves", "SCR", "019", "Rare", "Pokémon"), ("Sinistcha", "SCR", "022", "Rare", "Pokémon"),
                ("Infernape", "SCR", "033", "Rare", "Pokémon"), ("Chandelure", "SCR", "038", "Rare", "Pokémon"),
                ("Carracosta", "SCR", "038", "Rare", "Pokémon"), ("Drednaw", "SCR", "044", "Rare", "Pokémon"),
                ("Zeraora", "SCR", "055", "Rare", "Pokémon"), ("Alcremie", "SCR", "065", "Rare", "Pokémon"),
                ("Iron Boulder", "SCR", "071", "Rare", "Pokémon"), ("Rhyperior", "SCR", "076", "Rare", "Pokémon"),
                ("Grimmsnarl", "SCR", "096", "Rare", "Pokémon"), ("Klinklang", "SCR", "101", "Rare", "Pokémon"),
                ("Melmetal", "SCR", "104", "Rare", "Pokémon"), ("Archaludon", "SCR", "107", "Rare", "Pokémon"),
                ("Raging Bolt", "SCR", "111", "Rare", "Pokémon"), ("Noctowl", "SCR", "115", "Rare", "Pokémon"),
                ("Bouffalant", "SCR", "119", "Rare", "Pokémon")
            ],
            "Double Rare": [
                ("Venusaur ex", "SCR", "001", "Double Rare", "Pokémon"), ("Hydrapple ex", "SCR", "014", "Double Rare", "Pokémon"),
                ("Cinderace ex", "SCR", "028", "Double Rare", "Pokémon"), ("Blastoise ex", "SCR", "030", "Double Rare", "Pokémon"),
                ("Lapras ex", "SCR", "032", "Double Rare", "Pokémon"), ("Greninja ex", "SCR", "041", "Double Rare", "Pokémon"),
                ("Galvantula ex", "SCR", "051", "Double Rare", "Pokémon"), ("Dachsbun ex", "SCR", "067", "Double Rare", "Pokémon"),
                ("Medicham ex", "SCR", "080", "Double Rare", "Pokémon"), ("Lucario ex", "SCR", "082", "Double Rare", "Pokémon"),
                ("Garganacl ex", "SCR", "089", "Double Rare", "Pokémon"), ("Melmetal ex", "SCR", "105", "Double Rare", "Pokémon"),
                ("Orthworm ex", "SCR", "110", "Double Rare", "Pokémon"), ("Terapagos ex", "SCR", "128", "Double Rare", "Pokémon")
            ],
            "ACE SPEC Rare": [
                ("Deluxe Bomb", "SCR", "134", "ACE SPEC Rare", "Trainer"), ("Grand Tree", "SCR", "136", "ACE SPEC Rare", "Trainer"),
                ("Sparkling Crystal", "SCR", "142", "ACE SPEC Rare", "Trainer")
            ],
            "Illustration Rare": [
                ("Bulbasaur", "SCR", "143", "Illustration Rare", "Pokémon"), ("Ledian", "SCR", "144", "Illustration Rare", "Pokémon"),
                ("Lileep", "SCR", "145", "Illustration Rare", "Pokémon"), ("Turtonator", "SCR", "146", "Illustration Rare", "Pokémon"),
                ("Raboot", "SCR", "147", "Illustration Rare", "Pokémon"), ("Squirtle", "SCR", "148", "Illustration Rare", "Pokémon"),
                ("Crabominable", "SCR", "149", "Illustration Rare", "Pokémon"), ("Joltik", "SCR", "150", "Illustration Rare", "Pokémon"),
                ("Zeraora", "SCR", "151", "Illustration Rare", "Pokémon"), ("Milcery", "SCR", "152", "Illustration Rare", "Pokémon"),
                ("Meditite", "SCR", "153", "Illustration Rare", "Pokémon"), ("Gulpin", "SCR", "154", "Illustration Rare", "Pokémon"),
                ("Archaludon", "SCR", "155", "Illustration Rare", "Pokémon")
            ],
            "Ultra Rare": [
                ("Hydrapple ex", "SCR", "156", "Ultra Rare", "Pokémon"), ("Cinderace ex", "SCR", "157", "Ultra Rare", "Pokémon"),
                ("Lapras ex", "SCR", "158", "Ultra Rare", "Pokémon"), ("Galvantula ex", "SCR", "159", "Ultra Rare", "Pokémon"),
                ("Dachsbun ex", "SCR", "160", "Ultra Rare", "Pokémon"), ("Medicham ex", "SCR", "161", "Ultra Rare", "Pokémon"),
                ("Orthworm ex", "SCR", "162", "Ultra Rare", "Pokémon"), ("Briar", "SCR", "163", "Ultra Rare", "Trainer"),
                ("Crispin", "SCR", "164", "Ultra Rare", "Trainer"), ("Kofu", "SCR", "165", "Ultra Rare", "Trainer"),
                ("Lacey", "SCR", "166", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Hydrapple ex", "SCR", "167", "Special Illustration Rare", "Pokémon"), ("Galvantula ex", "SCR", "168", "Special Illustration Rare", "Pokémon"),
                ("Dachsbun ex", "SCR", "169", "Special Illustration Rare", "Pokémon"), ("Terapagos ex", "SCR", "170", "Special Illustration Rare", "Pokémon"),
                ("Briar", "SCR", "171", "Special Illustration Rare", "Trainer"), ("Lacey", "SCR", "172", "Special Illustration Rare", "Trainer")
            ],
            "Hyper Rare": [
                ("Terapagos ex", "SCR", "173", "Hyper Rare", "Pokémon"), ("Area Zero Underdepths", "SCR", "174", "Hyper Rare", "Trainer"),
                ("Bravery Charm", "SCR", "175", "Hyper Rare", "Trainer")
            ]
        }
    },
        "Surging Sparks": {
        "pull_rates": {
            "P_DR": 1/6, "P_ASR": 1/20, "P_IR": 1/13, "P_UR": 1/15, "P_SIR": 1/87, "P_HR": 1/188
        },
        "card_database": {
            "Common": [
                ("Exeggcute", "SSP", "001", "Common", "Pokémon"), ("Exeggcute", "SSP", "002", "Common", "Pokémon"),
                ("Scatterbug", "SSP", "005", "Common", "Pokémon"), ("Spewpa", "SSP", "006", "Common", "Pokémon"),
                ("Morelull", "SSP", "008", "Common", "Pokémon"), ("Dhelmise", "SSP", "010", "Common", "Pokémon"),
                ("Capsakid", "SSP", "012", "Common", "Pokémon"), ("Rellor", "SSP", "013", "Common", "Pokémon"),
                ("Vulpix", "SSP", "016", "Common", "Pokémon"), ("Castform Sunny Form", "SSP", "020", "Common", "Pokémon"),
                ("Pansear", "SSP", "022", "Common", "Pokémon"), ("Simisear", "SSP", "023", "Common", "Pokémon"),
                ("Larvesta", "SSP", "024", "Common", "Pokémon"), ("Volcarona", "SSP", "025", "Common", "Pokémon"),
                ("Oricorio", "SSP", "026", "Common", "Pokémon"), ("Sizzlipede", "SSP", "027", "Common", "Pokémon"),
                ("Centiskorch", "SSP", "028", "Common", "Pokémon"), ("Fuecoco", "SSP", "029", "Common", "Pokémon"),
                ("Crocalor", "SSP", "030", "Common", "Pokémon"), ("Charcadet", "SSP", "032", "Common", "Pokémon"),
                ("Charcadet", "SSP", "033", "Common", "Pokémon"), ("Mantine", "SSP", "040", "Common", "Pokémon"),
                ("Feebas", "SSP", "041", "Common", "Pokémon"), ("Spheal", "SSP", "043", "Common", "Pokémon"),
                ("Sealeo", "SSP", "044", "Common", "Pokémon"), ("Shellos", "SSP", "046", "Common", "Pokémon"),
                ("Cryogonal", "SSP", "047", "Common", "Pokémon"), ("Quaxly", "SSP", "050", "Common", "Pokémon"),
                ("Quaxwell", "SSP", "051", "Common", "Pokémon"), ("Cetoddle", "SSP", "053", "Common", "Pokémon"),
                ("Cetitan", "SSP", "054", "Common", "Pokémon"), ("Magnemite", "SSP", "058", "Common", "Pokémon"),
                ("Rotom", "SSP", "061", "Common", "Pokémon"), ("Blitzle", "SSP", "062", "Common", "Pokémon"),
                ("Zebstrika", "SSP", "063", "Common", "Pokémon"), ("Stunfisk", "SSP", "064", "Common", "Pokémon"),
                ("Wattrel", "SSP", "066", "Common", "Pokémon"), ("Togepi", "SSP", "070", "Common", "Pokémon"),
                ("Togetic", "SSP", "071", "Common", "Pokémon"), ("Marill", "SSP", "073", "Common", "Pokémon"),
                ("Smoochum", "SSP", "075", "Common", "Pokémon"), ("Uxie", "SSP", "078", "Common", "Pokémon"),
                ("Mesprit", "SSP", "079", "Common", "Pokémon"), ("Azelf", "SSP", "080", "Common", "Pokémon"),
                ("Sigilyph", "SSP", "081", "Common", "Pokémon"), ("Yamask", "SSP", "082", "Common", "Pokémon"),
                ("Espurr", "SSP", "084", "Common", "Pokémon"), ("Dedenne", "SSP", "087", "Common", "Pokémon"),
                ("Oricorio", "SSP", "089", "Common", "Pokémon"), ("Sandygast", "SSP", "090", "Common", "Pokémon"),
                ("Flittle", "SSP", "094", "Common", "Pokémon"), ("Gimmighoul", "SSP", "097", "Common", "Pokémon"),
                ("Mankey", "SSP", "098", "Common", "Pokémon"), ("Primeape", "SSP", "099", "Common", "Pokémon"),
                ("Phanpy", "SSP", "102", "Common", "Pokémon"), ("Donphan", "SSP", "103", "Common", "Pokémon"),
                ("Trapinch", "SSP", "104", "Common", "Pokémon"), ("Vibrava", "SSP", "105", "Common", "Pokémon"),
                ("Drilbur", "SSP", "108", "Common", "Pokémon"), ("Excadrill", "SSP", "109", "Common", "Pokémon"),
                ("Clobbopus", "SSP", "112", "Common", "Pokémon"), ("Grapploct", "SSP", "113", "Common", "Pokémon"),
                ("Glimmet", "SSP", "114", "Common", "Pokémon"), ("Glimmora", "SSP", "115", "Common", "Pokémon"),
                ("Deino", "SSP", "117", "Common", "Pokémon"), ("Zweilous", "SSP", "118", "Common", "Pokémon"),
                ("Shroodle", "SSP", "120", "Common", "Pokémon"), ("Alolan Diglett", "SSP", "122", "Common", "Pokémon"),
                ("Skarmory", "SSP", "124", "Common", "Pokémon"), ("Bronzor", "SSP", "126", "Common", "Pokémon"),
                ("Bronzong", "SSP", "127", "Common", "Pokémon"), ("Klefki", "SSP", "128", "Common", "Pokémon"),
                ("Duraludon", "SSP", "129", "Common", "Pokémon"), ("Applin", "SSP", "138", "Common", "Pokémon"),
                ("Eevee", "SSP", "143", "Common", "Pokémon"), ("Snorlax", "SSP", "144", "Common", "Pokémon"),
                ("Slakoth", "SSP", "145", "Common", "Pokémon"), ("Vigoroth", "SSP", "146", "Common", "Pokémon"),
                ("Swablu", "SSP", "148", "Common", "Pokémon"), ("Zangoose", "SSP", "149", "Common", "Pokémon"),
                ("Kecleon", "SSP", "150", "Common", "Pokémon"), ("Bouffalant", "SSP", "151", "Common", "Pokémon"),
                ("Rufflet", "SSP", "152", "Common", "Pokémon"), ("Helioptile", "SSP", "154", "Common", "Pokémon"),
                ("Heliolisk", "SSP", "155", "Common", "Pokémon"), ("Oranguru", "SSP", "156", "Common", "Pokémon"),
                ("Tandemaus", "SSP", "157", "Common", "Pokémon"), ("Drasna", "SSP", "173", "Common", "Trainer")
            ],
            "Uncommon": [
                ("Exeggutor", "SSP", "003", "Uncommon", "Pokémon"), ("Vivillon", "SSP", "007", "Uncommon", "Pokémon"),
                ("Shiinotic", "SSP", "009", "Uncommon", "Pokémon"), ("Wo-Chien", "SSP", "015", "Uncommon", "Pokémon"),
                ("Ninetales", "SSP", "017", "Uncommon", "Pokémon"), ("Paldean Tauros", "SSP", "018", "Uncommon", "Pokémon"),
                ("Ho-Oh", "SSP", "019", "Uncommon", "Pokémon"), ("Victini", "SSP", "021", "Uncommon", "Pokémon"),
                ("Armarouge", "SSP", "034", "Uncommon", "Pokémon"), ("Ceruledge", "SSP", "035", "Uncommon", "Pokémon"),
                ("Paldean Tauros", "SSP", "039", "Uncommon", "Pokémon"), ("Walrein", "SSP", "045", "Uncommon", "Pokémon"),
                ("Bruxish", "SSP", "049", "Uncommon", "Pokémon"), ("Quaquaval", "SSP", "052", "Uncommon", "Pokémon"),
                ("Iron Bundle", "SSP", "055", "Uncommon", "Pokémon"), ("Magneton", "SSP", "059", "Uncommon", "Pokémon"),
                ("Magnezone", "SSP", "060", "Uncommon", "Pokémon"), ("Kilowattrel", "SSP", "067", "Uncommon", "Pokémon"),
                ("Miraidon", "SSP", "069", "Uncommon", "Pokémon"), ("Azumarill", "SSP", "074", "Uncommon", "Pokémon"),
                ("Latios", "SSP", "077", "Uncommon", "Pokémon"), ("Meowstic", "SSP", "085", "Uncommon", "Pokémon"),
                ("Xerneas", "SSP", "088", "Uncommon", "Pokémon"), ("Indeedee", "SSP", "093", "Uncommon", "Pokémon"),
                ("Espathra", "SSP", "095", "Uncommon", "Pokémon"), ("Flutter Mane", "SSP", "096", "Uncommon", "Pokémon"),
                ("Annihilape", "SSP", "100", "Uncommon", "Pokémon"), ("Paldean Tauros", "SSP", "101", "Uncommon", "Pokémon"),
                ("Passimian", "SSP", "111", "Uncommon", "Pokémon"), ("Koraidon", "SSP", "116", "Uncommon", "Pokémon"),
                ("Grafaiai", "SSP", "121", "Uncommon", "Pokémon"), ("Alolan Dugtrio", "SSP", "123", "Uncommon", "Pokémon"),
                ("Registeel", "SSP", "125", "Uncommon", "Pokémon"), ("Gholdengo", "SSP", "131", "Uncommon", "Pokémon"),
                ("Altaria", "SSP", "134", "Uncommon", "Pokémon"), ("Turtonator", "SSP", "137", "Uncommon", "Pokémon"),
                ("Flapple", "SSP", "139", "Uncommon", "Pokémon"), ("Appletun", "SSP", "140", "Uncommon", "Pokémon"),
                ("Braviary", "SSP", "153", "Uncommon", "Pokémon"), ("Maushold", "SSP", "158", "Uncommon", "Pokémon"),
                ("Babiri Berry", "SSP", "163", "Uncommon", "Trainer"), ("Call Bell", "SSP", "165", "Uncommon", "Trainer"),
                ("Chill Teaser Toy", "SSP", "166", "Uncommon", "Trainer"), ("Clemont’s Quick Wit", "SSP", "167", "Uncommon", "Trainer"),
                ("Colbur Berry", "SSP", "168", "Uncommon", "Trainer"), ("Counter Gain", "SSP", "169", "Uncommon", "Trainer"),
                ("Cyrano", "SSP", "170", "Uncommon", "Trainer"), ("Deduction Kit", "SSP", "171", "Uncommon", "Trainer"),
                ("Dragon Elixir", "SSP", "172", "Uncommon", "Trainer"), ("Drayton", "SSP", "174", "Uncommon", "Trainer"),
                ("Dusk Ball", "SSP", "175", "Uncommon", "Trainer"), ("Gravity Mountain", "SSP", "177", "Uncommon", "Trainer"),
                ("Jasmine’s Gaze", "SSP", "178", "Uncommon", "Trainer"), ("Lisia’s Appeal", "SSP", "179", "Uncommon", "Trainer"),
                ("Lively Stadium", "SSP", "180", "Uncommon", "Trainer"), ("Meddling Memo", "SSP", "181", "Uncommon", "Trainer"),
                ("Passho Berry", "SSP", "184", "Uncommon", "Trainer"), ("Surfer", "SSP", "187", "Uncommon", "Trainer"),
                ("Technical Machine: Fluorite", "SSP", "188", "Uncommon", "Trainer"), ("Tera Orb", "SSP", "189", "Uncommon", "Trainer"),
                ("Tyme", "SSP", "190", "Uncommon", "Trainer")
            ],
            "Rare": [
                ("Zarude", "SSP", "011", "Rare", "Pokémon"), ("Rabsca", "SSP", "014", "Rare", "Pokémon"),
                ("Skeledirge", "SSP", "031", "Rare", "Pokémon"), ("Gouging Fire", "SSP", "038", "Rare", "Pokémon"),
                ("Chien-Pao", "SSP", "056", "Rare", "Pokémon"), ("Tapu Koko", "SSP", "065", "Rare", "Pokémon"),
                ("Togekiss", "SSP", "072", "Rare", "Pokémon"), ("Cofagrigus", "SSP", "083", "Rare", "Pokémon"),
                ("Tapu Lele", "SSP", "092", "Rare", "Pokémon"), ("Gastrodon", "SSP", "107", "Rare", "Pokémon"),
                ("Landorus", "SSP", "110", "Rare", "Pokémon"), ("Iron Crown", "SSP", "132", "Rare", "Pokémon"),
                ("Dialga", "SSP", "135", "Rare", "Pokémon"), ("Palkia", "SSP", "136", "Rare", "Pokémon"),
                ("Eternatus", "SSP", "141", "Rare", "Pokémon"), ("Terapagos", "SSP", "161", "Rare", "Pokémon")
            ],
            "Double Rare": [
                ("Durant ex", "SSP", "004", "Double Rare", "Pokémon"), ("Ceruledge ex", "SSP", "036", "Double Rare", "Pokémon"),
                ("Scovillain ex", "SSP", "037", "Double Rare", "Pokémon"), ("Milotic ex", "SSP", "042", "Double Rare", "Pokémon"),
                ("Black Kyurem ex", "SSP", "048", "Double Rare", "Pokémon"), ("Pikachu ex", "SSP", "057", "Double Rare", "Pokémon"),
                ("Kilowattrel ex", "SSP", "068", "Double Rare", "Pokémon"), ("Latias ex", "SSP", "076", "Double Rare", "Pokémon"),
                ("Sylveon ex", "SSP", "086", "Double Rare", "Pokémon"), ("Palossand ex", "SSP", "091", "Double Rare", "Pokémon"),
                ("Medicham ex", "SSP", "080", "Double Rare", "Pokémon"), ("Lucario ex", "SSP", "082", "Double Rare", "Pokémon"),
                ("Flygon ex", "SSP", "106", "Double Rare", "Pokémon"), ("Hydreigon ex", "SSP", "119", "Double Rare", "Pokémon"),
                ("Archaludon ex", "SSP", "130", "Double Rare", "Pokémon"), ("Alolan Exeggutor ex", "SSP", "133", "Double Rare", "Pokémon"),
                ("Tatsugiri ex", "SSP", "142", "Double Rare", "Pokémon"), ("Slaking ex", "SSP", "147", "Double Rare", "Pokémon"),
                ("Cyclizar ex", "SSP", "159", "Double Rare", "Pokémon"), ("Flamigo ex", "SSP", "160", "Double Rare", "Pokémon")
            ],
            "ACE SPEC Rare": [
                ("Amulet of Hope", "SSP", "162", "ACE SPEC Rare", "Trainer"), ("Brilliant Blender", "SSP", "164", "ACE SPEC Rare", "Trainer"),
                ("Energy Search Pro", "SSP", "176", "ACE SPEC Rare", "Trainer"), ("Megaton Blower", "SSP", "182", "ACE SPEC Rare", "Trainer"),
                ("Miracle Headset", "SSP", "183", "ACE SPEC Rare", "Trainer"), ("Precious Trolley", "SSP", "185", "ACE SPEC Rare", "Trainer"),
                ("Scramble Switch", "SSP", "186", "ACE SPEC Rare", "Trainer"), ("Enriching Energy", "SSP", "191", "ACE SPEC Rare", "Energy")
            ],
            "Illustration Rare": [
                ("Exeggcute", "SSP", "192", "Illustration Rare", "Pokémon"), ("Vivillon", "SSP", "193", "Illustration Rare", "Pokémon"),
                ("Shiinotic", "SSP", "194", "Illustration Rare", "Pokémon"), ("Castform Sunny Form", "SSP", "195", "Illustration Rare", "Pokémon"),
                ("Larvesta", "SSP", "196", "Illustration Rare", "Pokémon"), ("Ceruledge", "SSP", "197", "Illustration Rare", "Pokémon"),
                ("Feebas", "SSP", "198", "Illustration Rare", "Pokémon"), ("Spheal", "SSP", "199", "Illustration Rare", "Pokémon"),
                ("Bruxish", "SSP", "200", "Illustration Rare", "Pokémon"), ("Cetitan", "SSP", "201", "Illustration Rare", "Pokémon"),
                ("Stunfisk", "SSP", "202", "Illustration Rare", "Pokémon"), ("Latios", "SSP", "203", "Illustration Rare", "Pokémon"),
                ("Mesprit", "SSP", "204", "Illustration Rare", "Pokémon"), ("Phanpy", "SSP", "205", "Illustration Rare", "Pokémon"),
                ("Vibrava", "SSP", "206", "Illustration Rare", "Pokémon"), ("Clobbopus", "SSP", "207", "Illustration Rare", "Pokémon"),
                ("Alolan Dugtrio", "SSP", "208", "Illustration Rare", "Pokémon"), ("Skarmory", "SSP", "209", "Illustration Rare", "Pokémon"),
                ("Flapple", "SSP", "210", "Illustration Rare", "Pokémon"), ("Appletun", "SSP", "211", "Illustration Rare", "Pokémon"),
                ("Slakoth", "SSP", "212", "Illustration Rare", "Pokémon"), ("Kecleon", "SSP", "213", "Illustration Rare", "Pokémon"),
                ("Braviary", "SSP", "214", "Illustration Rare", "Pokémon")
            ],
            "Ultra Rare": [
                ("Durant ex", "SSP", "215", "Ultra Rare", "Pokémon"), ("Scovillain ex", "SSP", "216", "Ultra Rare", "Pokémon"),
                ("Milotic ex", "SSP", "217", "Ultra Rare", "Pokémon"), ("Black Kyurem ex", "SSP", "218", "Ultra Rare", "Pokémon"),
                ("Pikachu ex", "SSP", "219", "Ultra Rare", "Pokémon"), ("Latias ex", "SSP", "220", "Ultra Rare", "Pokémon"),
                ("Palossand ex", "SSP", "221", "Ultra Rare", "Pokémon"), ("Flygon ex", "SSP", "222", "Ultra Rare", "Pokémon"),
                ("Hydreigon ex", "SSP", "223", "Ultra Rare", "Pokémon"), ("Archaludon ex", "SSP", "224", "Ultra Rare", "Pokémon"),
                ("Alolan Exeggutor ex", "SSP", "225", "Ultra Rare", "Pokémon"), ("Tatsugiri ex", "SSP", "226", "Ultra Rare", "Pokémon"),
                ("Slaking ex", "SSP", "227", "Ultra Rare", "Pokémon"), ("Cyclizar ex", "SSP", "228", "Ultra Rare", "Pokémon"),
                ("Clemont’s Quick Wit", "SSP", "229", "Ultra Rare", "Trainer"), ("Cyrano", "SSP", "230", "Ultra Rare", "Trainer"),
                ("Drasna", "SSP", "231", "Ultra Rare", "Trainer"), ("Drayton", "SSP", "232", "Ultra Rare", "Trainer"),
                ("Jasmine’s Gaze", "SSP", "233", "Ultra Rare", "Trainer"), ("Lisia’s Appeal", "SSP", "234", "Ultra Rare", "Trainer"),
                ("Surfer", "SSP", "235", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Durant ex", "SSP", "236", "Special Illustration Rare", "Pokémon"), ("Milotic ex", "SSP", "237", "Special Illustration Rare", "Pokémon"),
                ("Pikachu ex", "SSP", "238", "Special Illustration Rare", "Pokémon"), ("Latias ex", "SSP", "239", "Special Illustration Rare", "Pokémon"),
                ("Hydreigon ex", "SSP", "240", "Special Illustration Rare", "Pokémon"), ("Archaludon ex", "SSP", "241", "Special Illustration Rare", "Pokémon"),
                ("Alolan Exeggutor ex", "SSP", "242", "Special Illustration Rare", "Pokémon"), ("Clemont’s Quick Wit", "SSP", "243", "Special Illustration Rare", "Trainer"),
                ("Drayton", "SSP", "244", "Special Illustration Rare", "Trainer"), ("Jasmine’s Gaze", "SSP", "245", "Special Illustration Rare", "Trainer"),
                ("Lisia’s Appeal", "SSP", "246", "Special Illustration Rare", "Trainer")
            ],
            "Hyper Rare": [
                ("Pikachu ex", "SSP", "247", "Hyper Rare", "Pokémon"), ("Alolan Exeggutor ex", "SSP", "248", "Hyper Rare", "Pokémon"),
                ("Counter Gain", "SSP", "249", "Hyper Rare", "Trainer"), ("Gravity Mountain", "SSP", "250", "Hyper Rare", "Trainer"),
                ("Night Stretcher", "SSP", "251", "Hyper Rare", "Trainer"), ("Jet Energy", "SSP", "252", "Hyper Rare", "Energy")
            ]
        }
    },
        "Prismatic Evolutions": {
        "pull_rates": {
            "P_DR": 1/6, "P_ASR": 1/21, "P_UR": 1/13, "P_SIR": 1/45, "P_HR": 1/180
        },
        "card_database": {
            "Common": [
                ("Exeggcute", "PRE", "001", "Common", "Pokémon"), ("Pinsir", "PRE", "003", "Common", "Pokémon"),
                ("Budew", "PRE", "004", "Common", "Pokémon"), ("Cottonee", "PRE", "007", "Common", "Pokémon"),
                ("Applin", "PRE", "009", "Common", "Pokémon"), ("Litleo", "PRE", "015", "Common", "Pokémon"),
                ("Slowpoke", "PRE", "018", "Common", "Pokémon"), ("Goldeen", "PRE", "020", "Common", "Pokémon"),
                ("Larvitar", "PRE", "047", "Common", "Pokémon"), ("Pupitar", "PRE", "048", "Common", "Pokémon"),
                ("Riolu", "PRE", "050", "Common", "Pokémon"), ("Hippopotas", "PRE", "052", "Common", "Pokémon"),
                ("Hippowdon", "PRE", "053", "Common", "Pokémon"), ("Sneasel", "PRE", "061", "Common", "Pokémon"),
                ("Houndour", "PRE", "062", "Common", "Pokémon"), ("Houndoom", "PRE", "063", "Common", "Pokémon"),
                ("Bronzor", "PRE", "066", "Common", "Pokémon"), ("Duraludon", "PRE", "069", "Common", "Pokémon"),
                ("Dreepy", "PRE", "071", "Common", "Pokémon"), ("Drakloak", "PRE", "072", "Common", "Pokémon"),
                ("Eevee", "PRE", "074", "Common", "Pokémon"), ("Hoothoot", "PRE", "077", "Common", "Pokémon"),
                ("Dunsparce", "PRE", "079", "Common", "Pokémon"), ("Miltank", "PRE", "081", "Common", "Pokémon"),
                ("Buneary", "PRE", "083", "Common", "Pokémon"), ("Lopunny", "PRE", "084", "Common", "Pokémon"),
                ("Fan Rotom", "PRE", "085", "Common", "Pokémon"), ("Furfrou", "PRE", "088", "Common", "Pokémon"),
                ("Noibat", "PRE", "090", "Common", "Pokémon"), ("Amarys", "PRE", "093", "Common", "Trainer"),
                ("Black Belt’s Training", "PRE", "096", "Common", "Trainer"), ("Black Belt’s Training", "PRE", "097", "Common", "Trainer"),
                ("Black Belt’s Training", "PRE", "098", "Common", "Trainer"), ("Black Belt’s Training", "PRE", "099", "Common", "Trainer"),
                ("Friends in Paldea", "PRE", "109", "Common", "Trainer"), ("Haban Berry", "PRE", "111", "Common", "Trainer"),
                ("Larry’s Skill", "PRE", "115", "Common", "Trainer"), ("Professor’s Research", "PRE", "122", "Common", "Trainer"),
                ("Professor’s Research", "PRE", "123", "Common", "Trainer"), ("Professor’s Research", "PRE", "124", "Common", "Trainer"),
                ("Professor’s Research", "PRE", "125", "Common", "Trainer"), ("Roto-Stick", "PRE", "127", "Common", "Trainer")
            ],
            "Uncommon": [
                ("Exeggutor", "PRE", "002", "Uncommon", "Pokémon"), ("Dipplin", "PRE", "010", "Uncommon", "Pokémon"),
                ("Pyroar", "PRE", "016", "Uncommon", "Pokémon"), ("Slowking", "PRE", "019", "Uncommon", "Pokémon"),
                ("Seaking", "PRE", "021", "Uncommon", "Pokémon"), ("Suicune", "PRE", "024", "Uncommon", "Pokémon"),
                ("Scream Tail", "PRE", "042", "Uncommon", "Pokémon"), ("Great Tusk", "PRE", "055", "Uncommon", "Pokémon"),
                ("Bronzong", "PRE", "067", "Uncommon", "Pokémon"), ("Heatran", "PRE", "068", "Uncommon", "Pokémon"),
                ("Regigigas", "PRE", "086", "Uncommon", "Pokémon"), ("Shaymin", "PRE", "087", "Uncommon", "Pokémon"),
                ("Hawlucha", "PRE", "089", "Uncommon", "Pokémon"), ("Area Zero Underdepths", "PRE", "094", "Uncommon", "Trainer"),
                ("Binding Mochi", "PRE", "095", "Uncommon", "Trainer"), ("Briar", "PRE", "100", "Uncommon", "Trainer"),
                ("Buddy-Buddy Poffin", "PRE", "101", "Uncommon", "Trainer"), ("Bug Catching Set", "PRE", "102", "Uncommon", "Trainer"),
                ("Carmine", "PRE", "103", "Uncommon", "Trainer"), ("Ciphermaniac’s Codebreaking", "PRE", "104", "Uncommon", "Trainer"),
                ("Crispin", "PRE", "105", "Uncommon", "Trainer"), ("Earthen Vessel", "PRE", "106", "Uncommon", "Trainer"),
                ("Explorer’s Guidance", "PRE", "107", "Uncommon", "Trainer"), ("Festival Grounds", "PRE", "108", "Uncommon", "Trainer"),
                ("Glass Trumpet", "PRE", "110", "Uncommon", "Trainer"), ("Janine’s Secret Art", "PRE", "112", "Uncommon", "Trainer"),
                ("Kieran", "PRE", "113", "Uncommon", "Trainer"), ("Lacey", "PRE", "114", "Uncommon", "Trainer"),
                ("Ogre’s Mask", "PRE", "118", "Uncommon", "Trainer"), ("Professor Sada’s Vitality", "PRE", "120", "Uncommon", "Trainer"),
                ("Professor Turo’s Scenario", "PRE", "121", "Uncommon", "Trainer"), ("Rescue Board", "PRE", "126", "Uncommon", "Trainer"),
                ("Techno Radar", "PRE", "130", "Uncommon", "Trainer")
            ],
            "Rare": [
                ("Leafeon", "PRE", "005", "Rare", "Pokémon"), ("Whimsicott", "PRE", "008", "Rare", "Pokémon"),
                ("Flareon", "PRE", "013", "Rare", "Pokémon"), ("Vaporeon", "PRE", "022", "Rare", "Pokémon"),
                ("Glaceon", "PRE", "025", "Rare", "Pokémon"), ("Jolteon", "PRE", "029", "Rare", "Pokémon"),
                ("Espeon", "PRE", "033", "Rare", "Pokémon"), ("Dusknoir", "PRE", "037", "Rare", "Pokémon"),
                ("Sylveon", "PRE", "040", "Rare", "Pokémon"), ("Flutter Mane", "PRE", "043", "Rare", "Pokémon"),
                ("Munkidori", "PRE", "044", "Rare", "Pokémon"), ("Fezandipiti", "PRE", "045", "Rare", "Pokémon"),
                ("Iron Boulder", "PRE", "046", "Rare", "Pokémon"), ("Groudon", "PRE", "049", "Rare", "Pokémon"),
                ("Bloodmoon Ursaluna", "PRE", "054", "Rare", "Pokémon"), ("Okidogi", "PRE", "057", "Rare", "Pokémon"),
                ("Umbreon", "PRE", "059", "Rare", "Pokémon"), ("Roaring Moon", "PRE", "065", "Rare", "Pokémon"),
                ("Archaludon", "PRE", "070", "Rare", "Pokémon"), ("Noctowl", "PRE", "078", "Rare", "Pokémon"),
                ("Dudunsparce", "PRE", "080", "Rare", "Pokémon")
            ],
            "Double Rare": [
                ("Leafeon ex", "PRE", "006", "Double Rare", "Pokémon"), ("Hydrapple ex", "PRE", "011", "Double Rare", "Pokémon"),
                ("Teal Mask Ogerpon ex", "PRE", "012", "Double Rare", "Pokémon"), ("Flareon ex", "PRE", "014", "Double Rare", "Pokémon"),
                ("Hearthflame Mask Ogerpon ex", "PRE", "017", "Double Rare", "Pokémon"), ("Vaporeon ex", "PRE", "023", "Double Rare", "Pokémon"),
                ("Glaceon ex", "PRE", "026", "Double Rare", "Pokémon"), ("Wellspring Mask Ogerpon ex", "PRE", "027", "Double Rare", "Pokémon"),
                ("Pikachu ex", "PRE", "028", "Double Rare", "Pokémon"), ("Jolteon ex", "PRE", "030", "Double Rare", "Pokémon"),
                ("Iron Hands ex", "PRE", "031", "Double Rare", "Pokémon"), ("Iron Thorns ex", "PRE", "032", "Double Rare", "Pokémon"),
                ("Espeon ex", "PRE", "034", "Double Rare", "Pokémon"), ("Sylveon ex", "PRE", "041", "Double Rare", "Pokémon"),
                ("Lucario ex", "PRE", "051", "Double Rare", "Pokémon"), ("Sandy Shocks ex", "PRE", "056", "Double Rare", "Pokémon"),
                ("Cornerstone Mask Ogerpon ex", "PRE", "058", "Double Rare", "Pokémon"), ("Umbreon ex", "PRE", "060", "Double Rare", "Pokémon"),
                ("Tyranitar ex", "PRE", "064", "Double Rare", "Pokémon"), ("Dragapult ex", "PRE", "073", "Double Rare", "Pokémon"),
                ("Eevee ex", "PRE", "075", "Double Rare", "Pokémon"), ("Snorlax ex", "PRE", "076", "Double Rare", "Pokémon"),
                ("Lugia ex", "PRE", "082", "Double Rare", "Pokémon"), ("Noivern ex", "PRE", "091", "Double Rare", "Pokémon"),
                ("Terapagos ex", "PRE", "092", "Double Rare", "Pokémon")
            ],
            "ACE SPEC Rare": [
                ("Max Rod", "PRE", "116", "ACE SPEC Rare", "Trainer"), ("Maximum Belt", "PRE", "117", "ACE SPEC Rare", "Trainer"),
                ("Prime Catcher", "PRE", "119", "ACE SPEC Rare", "Trainer"), ("Scoop Up Cyclone", "PRE", "128", "ACE SPEC Rare", "Trainer"),
                ("Sparkling Crystal", "PRE", "129", "ACE SPEC Rare", "Trainer"), ("Treasure Tracker", "PRE", "131", "ACE SPEC Rare", "Trainer")
            ],
            "Ultra Rare": [
                ("Amarys", "PRE", "132", "Ultra Rare", "Trainer"), ("Atticus", "PRE", "133", "Ultra Rare", "Trainer"),
                ("Atticus", "PRE", "134", "Ultra Rare", "Trainer"), ("Brassius", "PRE", "135", "Ultra Rare", "Trainer"),
                ("Eri", "PRE", "136", "Ultra Rare", "Trainer"), ("Friends in Paldea", "PRE", "137", "Ultra Rare", "Trainer"),
                ("Giacomo", "PRE", "138", "Ultra Rare", "Trainer"), ("Larry’s Skill", "PRE", "139", "Ultra Rare", "Trainer"),
                ("Mela", "PRE", "140", "Ultra Rare", "Trainer"), ("Ortega", "PRE", "141", "Ultra Rare", "Trainer"),
                ("Raifort", "PRE", "142", "Ultra Rare", "Trainer"), ("Tyme", "PRE", "143", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Leafeon ex", "PRE", "144", "Special Illustration Rare", "Pokémon"), ("Teal Mask Ogerpon ex", "PRE", "145", "Special Illustration Rare", "Pokémon"),
                ("Flareon ex", "PRE", "146", "Special Illustration Rare", "Pokémon"), ("Ceruledge ex", "PRE", "147", "Special Illustration Rare", "Pokémon"),
                ("Hearthflame Mask Ogerpon ex", "PRE", "148", "Special Illustration Rare", "Pokémon"), ("Vaporeon ex", "PRE", "149", "Special Illustration Rare", "Pokémon"),
                ("Glaceon ex", "PRE", "150", "Special Illustration Rare", "Pokémon"), ("Palafin ex", "PRE", "151", "Special Illustration Rare", "Pokémon"),
                ("Wellspring Mask Ogerpon ex", "PRE", "152", "Special Illustration Rare", "Pokémon"), ("Jolteon ex", "PRE", "153", "Special Illustration Rare", "Pokémon"),
                ("Iron Hands ex", "PRE", "154", "Special Illustration Rare", "Pokémon"), ("Espeon ex", "PRE", "155", "Special Illustration Rare", "Pokémon"),
                ("Sylveon ex", "PRE", "156", "Special Illustration Rare", "Pokémon"), ("Iron Valiant ex", "PRE", "157", "Special Illustration Rare", "Pokémon"),
                ("Iron Crown ex", "PRE", "158", "Special Illustration Rare", "Pokémon"), ("Sandy Shocks ex", "PRE", "159", "Special Illustration Rare", "Pokémon"),
                ("Cornerstone Mask Ogerpon ex", "PRE", "160", "Special Illustration Rare", "Pokémon"), ("Umbreon ex", "PRE", "161", "Special Illustration Rare", "Pokémon"),
                ("Roaring Moon ex", "PRE", "162", "Special Illustration Rare", "Pokémon"), ("Pecharunt ex", "PRE", "163", "Special Illustration Rare", "Pokémon"),
                ("Gholdengo ex", "PRE", "164", "Special Illustration Rare", "Pokémon"), ("Dragapult ex", "PRE", "165", "Special Illustration Rare", "Pokémon"),
                ("Raging Bolt ex", "PRE", "166", "Special Illustration Rare", "Pokémon"), ("Eevee ex", "PRE", "167", "Special Illustration Rare", "Pokémon"),
                ("Bloodmoon Ursaluna ex", "PRE", "168", "Special Illustration Rare", "Pokémon"), ("Terapagos ex", "PRE", "169", "Special Illustration Rare", "Pokémon"),
                ("Amarys", "PRE", "170", "Special Illustration Rare", "Trainer"), ("Crispin", "PRE", "171", "Special Illustration Rare", "Trainer"),
                ("Drayton", "PRE", "172", "Special Illustration Rare", "Trainer"), ("Janine’s Secret Art", "PRE", "173", "Special Illustration Rare", "Trainer"),
                ("Kieran", "PRE", "174", "Special Illustration Rare", "Trainer"), ("Lacey", "PRE", "175", "Special Illustration Rare", "Trainer")
            ],
            "Hyper Rare": [
                ("Iron Leaves ex", "PRE", "176", "Hyper Rare", "Pokémon"), ("Teal Mask Ogerpon ex", "PRE", "177", "Hyper Rare", "Pokémon"),
                ("Walking Wake ex", "PRE", "178", "Hyper Rare", "Pokémon"), ("Pikachu ex", "PRE", "179", "Hyper Rare", "Pokémon"),
                ("Terapagos ex", "PRE", "180", "Hyper Rare", "Pokémon")
            ]
        }
    },
        "Journey Together": {
        "pull_rates": {
            "P_DR": 1/5, "P_IR": 1/12, "P_UR": 1/15, "P_SIR": 1/86, "P_HR": 1/137
        },
        "card_database": {
            "Common": [
                ("Caterpie", "JTG", "001", "Common", "Pokémon"), ("Metapod", "JTG", "002", "Common", "Pokémon"),
                ("Paras", "JTG", "004", "Common", "Pokémon"), ("Parasect", "JTG", "005", "Common", "Pokémon"),
                ("Petilil", "JTG", "006", "Common", "Pokémon"), ("Lilligant", "JTG", "007", "Common", "Pokémon"),
                ("Karrablast", "JTG", "009", "Common", "Pokémon"), ("Foongus", "JTG", "010", "Common", "Pokémon"),
                ("Shelmet", "JTG", "012", "Common", "Pokémon"), ("Durant", "JTG", "014", "Common", "Pokémon"),
                ("Sprigatito", "JTG", "016", "Common", "Pokémon"), ("Floragato", "JTG", "017", "Common", "Pokémon"),
                ("Nymble", "JTG", "019", "Common", "Pokémon"), ("Magmar", "JTG", "020", "Common", "Pokémon"),
                ("Torchic", "JTG", "022", "Common", "Pokémon"), ("Torkoal", "JTG", "025", "Common", "Pokémon"),
                ("N’s Darumaka", "JTG", "026", "Common", "Pokémon"), ("Larvesta", "JTG", "028", "Common", "Pokémon"),
                ("Remoraid", "JTG", "033", "Common", "Pokémon"), ("Lotad", "JTG", "035", "Common", "Pokémon"),
                ("Lombre", "JTG", "036", "Common", "Pokémon"), ("Wingull", "JTG", "038", "Common", "Pokémon"),
                ("Wailmer", "JTG", "040", "Common", "Pokémon"), ("Alolan Geodude", "JTG", "044", "Common", "Pokémon"),
                ("Alolan Graveler", "JTG", "045", "Common", "Pokémon"), ("Iono’s Voltorb", "JTG", "047", "Common", "Pokémon"),
                ("N’s Joltik", "JTG", "049", "Common", "Pokémon"), ("Togedemaru", "JTG", "050", "Common", "Pokémon"),
                ("Iono’s Tadbulb", "JTG", "052", "Common", "Pokémon"), ("Iono’s Wattrel", "JTG", "054", "Common", "Pokémon"),
                ("Mr. Mime", "JTG", "058", "Common", "Pokémon"), ("Shuppet", "JTG", "059", "Common", "Pokémon"),
                ("Beldum", "JTG", "061", "Common", "Pokémon"), ("Metang", "JTG", "062", "Common", "Pokémon"),
                ("N’s Sigilyph", "JTG", "064", "Common", "Pokémon"), ("Oricorio", "JTG", "065", "Common", "Pokémon"),
                ("Lillie’s Cutiefly", "JTG", "066", "Common", "Pokémon"), ("Lillie’s Comfey", "JTG", "068", "Common", "Pokémon"),
                ("Dhelmise", "JTG", "070", "Common", "Pokémon"), ("Impidimp", "JTG", "071", "Common", "Pokémon"),
                ("Morgrem", "JTG", "072", "Common", "Pokémon"), ("Milcery", "JTG", "074", "Common", "Pokémon"),
                ("Cubone", "JTG", "076", "Common", "Pokémon"), ("Swinub", "JTG", "077", "Common", "Pokémon"),
                ("Piloswine", "JTG", "078", "Common", "Pokémon"), ("Larvitar", "JTG", "080", "Common", "Pokémon"),
                ("Pupitar", "JTG", "081", "Common", "Pokémon"), ("Pancham", "JTG", "083", "Common", "Pokémon"),
                ("Rockruff", "JTG", "084", "Common", "Pokémon"), ("Hop’s Silicobra", "JTG", "086", "Common", "Pokémon"),
                ("Toedscool", "JTG", "088", "Common", "Pokémon"), ("Koffing", "JTG", "091", "Common", "Pokémon"),
                ("Paldean Wooper", "JTG", "093", "Common", "Pokémon"), ("N’s Purrloin", "JTG", "096", "Common", "Pokémon"),
                ("N’s Zorua", "JTG", "097", "Common", "Pokémon"), ("Bombirdier", "JTG", "101", "Common", "Pokémon"),
                ("N’s Klink", "JTG", "103", "Common", "Pokémon"), ("N’s Klang", "JTG", "104", "Common", "Pokémon"),
                ("Galarian Stunfisk", "JTG", "106", "Common", "Pokémon"), ("Cufant", "JTG", "109", "Common", "Pokémon"),
                ("Bagon", "JTG", "112", "Common", "Pokémon"), ("Shelgon", "JTG", "113", "Common", "Pokémon"),
                ("Druddigon", "JTG", "115", "Common", "Pokémon"), ("Hop’s Snorlax", "JTG", "117", "Common", "Pokémon"),
                ("Sentret", "JTG", "118", "Common", "Pokémon"), ("Furret", "JTG", "119", "Common", "Pokémon"),
                ("Dunsparce", "JTG", "120", "Common", "Pokémon"), ("Kecleon", "JTG", "122", "Common", "Pokémon"),
                ("Tropius", "JTG", "123", "Common", "Pokémon"), ("Audino", "JTG", "124", "Common", "Pokémon"),
                ("Minccino", "JTG", "125", "Common", "Pokémon"), ("Noibat", "JTG", "127", "Common", "Pokémon"),
                ("Komala", "JTG", "129", "Common", "Pokémon"), ("Drampa", "JTG", "130", "Common", "Pokémon"),
                ("Skwovet", "JTG", "131", "Common", "Pokémon"), ("Hop’s Rookidee", "JTG", "133", "Common", "Pokémon"),
                ("Hop’s Corvisquire", "JTG", "134", "Common", "Pokémon"), ("Hop’s Wooloo", "JTG", "135", "Common", "Pokémon"),
                ("Cramorant", "JTG", "137", "Common", "Pokémon"), ("Lechonk", "JTG", "139", "Common", "Pokémon"),
                ("Squawkabilly", "JTG", "141", "Common", "Pokémon"), ("Billy & O’Nare", "JTG", "142", "Common", "Trainer"),
                ("Black Belt’s Training", "JTG", "143", "Common", "Trainer"), ("Black Belt’s Training", "JTG", "144", "Common", "Trainer"),
                ("Black Belt’s Training", "JTG", "145", "Common", "Trainer"), ("Professor’s Research", "JTG", "155", "Common", "Trainer")
            ],
            "Uncommon": [
                ("Maractus", "JTG", "008", "Uncommon", "Pokémon"), ("Accelgor", "JTG", "013", "Uncommon", "Pokémon"),
                ("Virizion", "JTG", "015", "Uncommon", "Pokémon"), ("Combusken", "JTG", "023", "Uncommon", "Pokémon"),
                ("N’s Darmanitan", "JTG", "027", "Uncommon", "Pokémon"), ("Volcarona", "JTG", "029", "Uncommon", "Pokémon"),
                ("Articuno", "JTG", "032", "Uncommon", "Pokémon"), ("Octillery", "JTG", "034", "Uncommon", "Pokémon"),
                ("Pelipper", "JTG", "039", "Uncommon", "Pokémon"), ("Regice", "JTG", "042", "Uncommon", "Pokémon"),
                ("Alolan Golem", "JTG", "046", "Uncommon", "Pokémon"), ("Iono’s Electrode", "JTG", "048", "Uncommon", "Pokémon"),
                ("Alolan Marowak", "JTG", "057", "Uncommon", "Pokémon"), ("Banette", "JTG", "060", "Uncommon", "Pokémon"),
                ("Grimmsnarl", "JTG", "073", "Uncommon", "Pokémon"), ("Hop’s Sandaconda", "JTG", "087", "Uncommon", "Pokémon"),
                ("Toedscruel", "JTG", "089", "Uncommon", "Pokémon"), ("Klawf", "JTG", "090", "Uncommon", "Pokémon"),
                ("Weezing", "JTG", "092", "Uncommon", "Pokémon"), ("Pangoro", "JTG", "099", "Uncommon", "Pokémon"),
                ("Lokix", "JTG", "100", "Uncommon", "Pokémon"), ("Escavalier", "JTG", "102", "Uncommon", "Pokémon"),
                ("N’s Klinklang", "JTG", "105", "Uncommon", "Pokémon"), ("Hop’s Corviknight", "JTG", "108", "Uncommon", "Pokémon"),
                ("Copperajah", "JTG", "110", "Uncommon", "Pokémon"), ("Cinccino", "JTG", "126", "Uncommon", "Pokémon"),
                ("Greedent", "JTG", "132", "Uncommon", "Pokémon"), ("Hop’s Cramorant", "JTG", "138", "Uncommon", "Pokémon"),
                ("Oinkologne", "JTG", "140", "Uncommon", "Pokémon"), ("Brock’s Scouting", "JTG", "146", "Uncommon", "Trainer"),
                ("Hop’s Bag", "JTG", "147", "Uncommon", "Trainer"), ("Hop’s Choice Band", "JTG", "148", "Uncommon", "Trainer"),
                ("Iris’s Fighting Spirit", "JTG", "149", "Uncommon", "Trainer"), ("Levincia", "JTG", "150", "Uncommon", "Trainer"),
                ("Lillie’s Pearl", "JTG", "151", "Uncommon", "Trainer"), ("N’s Castle", "JTG", "152", "Uncommon", "Trainer"),
                ("N’s PP Up", "JTG", "153", "Uncommon", "Trainer"), ("Postwick", "JTG", "154", "Uncommon", "Trainer"),
                ("Redeemable Ticket", "JTG", "156", "Uncommon", "Trainer"), ("Ruffian", "JTG", "157", "Uncommon", "Trainer"),
                ("Super Potion", "JTG", "158", "Uncommon", "Trainer"), ("Spiky Energy", "JTG", "159", "Uncommon", "Energy")
            ],
            "Rare": [
                ("Butterfree", "JTG", "003", "Rare", "Pokémon"), ("Meowscarada", "JTG", "018", "Rare", "Pokémon"),
                ("Magmortar", "JTG", "021", "Rare", "Pokémon"), ("Ludicolo", "JTG", "037", "Rare", "Pokémon"),
                ("Wailord", "JTG", "041", "Rare", "Pokémon"), ("Iono’s Kilowattrel", "JTG", "055", "Rare", "Pokémon"),
                ("Metagross", "JTG", "063", "Rare", "Pokémon"), ("Lillie’s Ribombee", "JTG", "067", "Rare", "Pokémon"),
                ("Regirock", "JTG", "082", "Rare", "Pokémon"), ("Lycanroc", "JTG", "085", "Rare", "Pokémon"),
                ("Tyranitar", "JTG", "095", "Rare", "Pokémon"), ("Magearna", "JTG", "107", "Rare", "Pokémon"),
                ("N’s Reshiram", "JTG", "116", "Rare", "Pokémon"), ("Noivern", "JTG", "128", "Rare", "Pokémon"),
                ("Hop’s Dubwool", "JTG", "136", "Rare", "Pokémon")
            ],
            "Double Rare": [
                ("Amoonguss ex", "JTG", "011", "Double Rare", "Pokémon"), ("Blaziken ex", "JTG", "024", "Double Rare", "Pokémon"),
                ("Reshiram ex", "JTG", "030", "Double Rare", "Pokémon"), ("Volcanion ex", "JTG", "031", "Double Rare", "Pokémon"),
                ("Veluza ex", "JTG", "043", "Double Rare", "Pokémon"), ("Tapu Koko ex", "JTG", "051", "Double Rare", "Pokémon"),
                ("Iono’s Bellibolt ex", "JTG", "053", "Double Rare", "Pokémon"), ("Lillie’s Clefairy ex", "JTG", "056", "Double Rare", "Pokémon"),
                ("Mimikyu ex", "JTG", "069", "Double Rare", "Pokémon"), ("Alcremie ex", "JTG", "075", "Double Rare", "Pokémon"),
                ("Mamoswine ex", "JTG", "079", "Double Rare", "Pokémon"), ("Paldean Clodsire ex", "JTG", "094", "Double Rare", "Pokémon"),
                ("N’s Zoroark ex", "JTG", "098", "Double Rare", "Pokémon"), ("Hop’s Zacian ex", "JTG", "111", "Double Rare", "Pokémon"),
                ("Salamence ex", "JTG", "114", "Double Rare", "Pokémon"), ("Dudunsparce ex", "JTG", "121", "Double Rare", "Pokémon")
            ],
            "Illustration Rare": [
                ("Maractus", "JTG", "160", "Illustration Rare", "Pokémon"), ("Articuno", "JTG", "161", "Illustration Rare", "Pokémon"),
                ("Wailord", "JTG", "162", "Illustration Rare", "Pokémon"), ("Iono’s Kilowattrel", "JTG", "163", "Illustration Rare", "Pokémon"),
                ("Lillie’s Ribombee", "JTG", "164", "Illustration Rare", "Pokémon"), ("Swinub", "JTG", "165", "Illustration Rare", "Pokémon"),
                ("Lycanroc", "JTG", "166", "Illustration Rare", "Pokémon"), ("N’s Reshiram", "JTG", "167", "Illustration Rare", "Pokémon"),
                ("Furret", "JTG", "168", "Illustration Rare", "Pokémon"), ("Noibat", "JTG", "169", "Illustration Rare", "Pokémon"),
                ("Hop’s Wooloo", "JTG", "170", "Illustration Rare", "Pokémon")
            ],
            "Ultra Rare": [
                ("Volcanion ex", "JTG", "171", "Ultra Rare", "Pokémon"), ("Iono’s Bellibolt ex", "JTG", "172", "Ultra Rare", "Pokémon"),
                ("Lillie’s Clefairy ex", "JTG", "173", "Ultra Rare", "Pokémon"), ("Mamoswine ex", "JTG", "174", "Ultra Rare", "Pokémon"),
                ("N’s Zoroark ex", "JTG", "175", "Ultra Rare", "Pokémon"), ("Hop’s Zacian ex", "JTG", "176", "Ultra Rare", "Pokémon"),
                ("Salamence ex", "JTG", "177", "Ultra Rare", "Pokémon"), ("Dudunsparce ex", "JTG", "178", "Ultra Rare", "Pokémon"),
                ("Brock’s Scouting", "JTG", "179", "Ultra Rare", "Trainer"), ("Iris’s Fighting Spirit", "JTG", "180", "Ultra Rare", "Trainer"),
                ("Ruffian", "JTG", "181", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Volcanion ex", "JTG", "182", "Special Illustration Rare", "Pokémon"), ("Iono’s Bellibolt ex", "JTG", "183", "Special Illustration Rare", "Pokémon"),
                ("Lillie’s Clefairy ex", "JTG", "184", "Special Illustration Rare", "Pokémon"), ("N’s Zoroark ex", "JTG", "185", "Special Illustration Rare", "Pokémon"),
                ("Hop’s Zacian ex", "JTG", "186", "Special Illustration Rare", "Pokémon"), ("Salamence ex", "JTG", "187", "Special Illustration Rare", "Pokémon")
            ],
            "Hyper Rare": [
                ("Iono’s Bellibolt ex", "JTG", "188", "Hyper Rare", "Pokémon"), ("N’s Zoroark ex", "JTG", "189", "Hyper Rare", "Pokémon"),
                ("Spiky Energy", "JTG", "190", "Hyper Rare", "Energy")
            ]
        }
    },
    "Destined Rivals": {
        "pull_rates": {
            'P_DR': 1/5, 'P_UR': 1/16, 'P_SIR': 1/94, 'P_HR': 1/149, 'P_IR': 1/12,
        },
        "card_database": {
            "Common": [
                ("Yanma", "DRI", "002", "Common", "Pokémon"), ("Pineco", "DRI", "004", "Common", "Pokémon"),
                ("Shroomish", "DRI", "005", "Common", "Pokémon"), ("Breloom", "DRI", "006", "Common", "Pokémon"),
                ("Cynthia's Roselia", "DRI", "007", "Common", "Pokémon"), ("Mow Rotom", "DRI", "009", "Common", "Pokémon"),
                ("Dwebble", "DRI", "011", "Common", "Pokémon"), ("Fomantis", "DRI", "013", "Common", "Pokémon"),
                ("Team Rocket's Blipbug", "DRI", "015", "Common", "Pokémon"), ("Applin", "DRI", "016", "Common", "Pokémon"),
                ("Dipplin", "DRI", "017", "Common", "Pokémon"), ("Team Rocket's Tarountula", "DRI", "019", "Common", "Pokémon"),
                ("Smoliv", "DRI", "021", "Common", "Pokémon"), ("Dolliv", "DRI", "022", "Common", "Pokémon"),
                ("Rellor", "DRI", "024", "Common", "Pokémon"), ("Growlithe", "DRI", "027", "Common", "Pokémon"),
                ("Ponyta", "DRI", "029", "Common", "Pokémon"), ("Ethan's Cyndaquil", "DRI", "032", "Common", "Pokémon"),
                ("Ethan's Quilava", "DRI", "033", "Common", "Pokémon"), ("Ethan's Slugma", "DRI", "035", "Common", "Pokémon"),
                ("Team Rocket's Houndour", "DRI", "037", "Common", "Pokémon"), ("Torchic", "DRI", "040", "Common", "Pokémon"),
                ("Combusken", "DRI", "041", "Common", "Pokémon"), ("Heat Rotom", "DRI", "043", "Common", "Pokémon"),
                ("Misty's Staryu", "DRI", "046", "Common", "Pokémon"), ("Misty's Magikarp", "DRI", "048", "Common", "Pokémon"),
                ("Misty's Lapras", "DRI", "050", "Common", "Pokémon"), ("Cynthia's Feebas", "DRI", "052", "Common", "Pokémon"),
                ("Clamperl", "DRI", "054", "Common", "Pokémon"), ("Buizel", "DRI", "057", "Common", "Pokémon"),
                ("Snover", "DRI", "059", "Common", "Pokémon"), ("Wash Rotom", "DRI", "061", "Common", "Pokémon"),
                ("Arrokuda", "DRI", "062", "Common", "Pokémon"), ("Cetoddle", "DRI", "064", "Common", "Pokémon"),
                ("Electabuzz", "DRI", "068", "Common", "Pokémon"), ("Ethan's Pichu", "DRI", "071", "Common", "Pokémon"),
                ("Team Rocket's Mareep", "DRI", "072", "Common", "Pokémon"), ("Team Rocket's Flaaffy", "DRI", "073", "Common", "Pokémon"),
                ("Electrike", "DRI", "075", "Common", "Pokémon"), ("Rotom", "DRI", "077", "Common", "Pokémon"),
                ("Team Rocket's Drowzee", "DRI", "079", "Common", "Pokémon"), ("Steven's Baltoy", "DRI", "083", "Common", "Pokémon"),
                ("Team Rocket's Chingling", "DRI", "085", "Common", "Pokémon"), ("Steven's Carbink", "DRI", "086", "Common", "Pokémon"),
                ("Team Rocket's Dottler", "DRI", "088", "Common", "Pokémon"), ("Mankey", "DRI", "090", "Common", "Pokémon"),
                ("Primeape", "DRI", "091", "Common", "Pokémon"), ("Ethan's Sudowoodo", "DRI", "093", "Common", "Pokémon"),
                ("Team Rocket's Larvitar", "DRI", "094", "Common", "Pokémon"), ("Team Rocket's Pupitar", "DRI", "095", "Common", "Pokémon"),
                ("Nosepass", "DRI", "097", "Common", "Pokémon"), ("Meditite", "DRI", "099", "Common", "Pokémon"),
                ("Cynthia's Gible", "DRI", "102", "Common", "Pokémon"), ("Cynthia's Gabite", "DRI", "103", "Common", "Pokémon"),
                ("Hippopotas", "DRI", "105", "Common", "Pokémon"), ("Mudbray", "DRI", "107", "Common", "Pokémon"),
                ("Arven's Toedscool", "DRI", "109", "Common", "Pokémon"), ("Team Rocket's Ekans", "DRI", "112", "Common", "Pokémon"),
                ("Team Rocket's Nidoran♀", "DRI", "114", "Common", "Pokémon"), ("Team Rocket's Nidorina", "DRI", "115", "Common", "Pokémon"),
                ("Team Rocket's Nidoran♂", "DRI", "117", "Common", "Pokémon"), ("Team Rocket's Nidorino", "DRI", "118", "Common", "Pokémon"),
                ("Team Rocket's Zubat", "DRI", "120", "Common", "Pokémon"), ("Team Rocket's Grimer", "DRI", "123", "Common", "Pokémon"),
                ("Team Rocket's Koffing", "DRI", "125", "Common", "Pokémon"), ("Marnie's Purrloin", "DRI", "130", "Common", "Pokémon"),
                ("Marnie's Scraggy", "DRI", "132", "Common", "Pokémon"), ("Marnie's Impidimp", "DRI", "134", "Common", "Pokémon"),
                ("Marnie's Morpeko", "DRI", "137", "Common", "Pokémon"), ("Arven's Maschiff", "DRI", "138", "Common", "Pokémon"),
                ("Skarmory", "DRI", "141", "Common", "Pokémon"), ("Steven's Skarmory", "DRI", "142", "Common", "Pokémon"),
                ("Steven's Beldum", "DRI", "143", "Common", "Pokémon"), ("Team Rocket's Rattata", "DRI", "147", "Common", "Pokémon"),
                ("Team Rocket's Raticate", "DRI", "148", "Common", "Pokémon"), ("Team Rocket's Meowth", "DRI", "149", "Common", "Pokémon"),
                ("Kangaskhan", "DRI", "151", "Common", "Pokémon"), ("Tauros", "DRI", "152", "Common", "Pokémon"),
                ("Team Rocket's Porygon", "DRI", "153", "Common", "Pokémon"), ("Team Rocket's Porygon2", "DRI", "154", "Common", "Pokémon"),
                ("Taillow", "DRI", "156", "Common", "Pokémon"), ("Swellow", "DRI", "157", "Common", "Pokémon"),
                ("Arven's Skwovet", "DRI", "158", "Common", "Pokémon"), ("Squawkabilly", "DRI", "160", "Common", "Pokémon"),
                ("Emcee's Hype", "DRI", "163", "Common", "Trainer")
            ],
            "Uncommon": [
                ("Ethan's Pinsir", "DRI", "001", "Uncommon", "Pokémon"), ("Shaymin", "DRI", "010", "Uncommon", "Pokémon"),
                ("Lurantis", "DRI", "014", "Uncommon", "Pokémon"), ("Teal Mask Ogerpon", "DRI", "026", "Uncommon", "Pokémon"),
                ("Arcanine", "DRI", "028", "Uncommon", "Pokémon"), ("Rapidash", "DRI", "030", "Uncommon", "Pokémon"),
                ("Team Rocket's Houndoom", "DRI", "038", "Uncommon", "Pokémon"), ("Hearthflame Mask Ogerpon", "DRI", "044", "Uncommon", "Pokémon"),
                ("Misty's Psyduck", "DRI", "045", "Uncommon", "Pokémon"), ("Misty's Starmie", "DRI", "047", "Uncommon", "Pokémon"),
                ("Cynthia's Milotic", "DRI", "053", "Uncommon", "Pokémon"), ("Huntail", "DRI", "055", "Uncommon", "Pokémon"),
                ("Floatzel", "DRI", "058", "Uncommon", "Pokémon"), ("Abomasnow", "DRI", "059", "Uncommon", "Pokémon"),
                ("Barraskewda", "DRI", "063", "Uncommon", "Pokémon"), ("Wellspring Mask Ogerpon", "DRI", "067", "Uncommon", "Pokémon"),
                ("Team Rocket's Ampharos", "DRI", "074", "Uncommon", "Pokémon"), ("Manectric", "DRI", "076", "Uncommon", "Pokémon"),
                ("Team Rocket's Hypno", "DRI", "080", "Uncommon", "Pokémon"), ("Steven's Claydol", "DRI", "084", "Uncommon", "Pokémon"),
                ("Team Rocket's Mimikyu", "DRI", "087", "Uncommon", "Pokémon"), ("Team Rocket's Orbeetle", "DRI", "089", "Uncommon", "Pokémon"),
                ("Probopass", "DRI", "098", "Uncommon", "Pokémon"), ("Medicham", "DRI", "100", "Uncommon", "Pokémon"),
                ("Hippowdon", "DRI", "106", "Uncommon", "Pokémon"), ("Mudsdale", "DRI", "108", "Uncommon", "Pokémon"),
                ("Arven's Toedscruel", "DRI", "110", "Uncommon", "Pokémon"), ("Cornerstone Mask Ogerpon", "DRI", "111", "Uncommon", "Pokémon"),
                ("Team Rocket's Arbok", "DRI", "113", "Uncommon", "Pokémon"), ("Team Rocket's Nidoqueen", "DRI", "116", "Uncommon", "Pokémon"),
                ("Team Rocket's Golbat", "DRI", "121", "Uncommon", "Pokémon"), ("Team Rocket's Muk", "DRI", "124", "Uncommon", "Pokémon"),
                ("Team Rocket's Weezing", "DRI", "126", "Uncommon", "Pokémon"), ("Team Rocket's Murkrow", "DRI", "127", "Uncommon", "Pokémon"),
                ("Cynthia's Spiritomb", "DRI", "129", "Uncommon", "Pokémon"), ("Marnie's Liepard", "DRI", "131", "Uncommon", "Pokémon"),
                ("Marnie's Scrafty", "DRI", "133", "Uncommon", "Pokémon"), ("Marnie's Morgrem", "DRI", "135", "Uncommon", "Pokémon"),
                ("Forretress", "DRI", "140", "Uncommon", "Pokémon"), ("Steven's Metang", "DRI", "144", "Uncommon", "Pokémon"),
                ("Team Rocket's Porygon-Z", "DRI", "155", "Uncommon", "Pokémon"), ("Arven's Sandwich", "DRI", "161", "Uncommon", "Trainer"),
                ("Cynthia's Power Weight", "DRI", "162", "Uncommon", "Trainer"), ("Energy Recycler", "DRI", "164", "Uncommon", "Trainer"),
                ("Ethan's Adventure", "DRI", "165", "Uncommon", "Trainer"), ("Granite Cave", "DRI", "166", "Uncommon", "Trainer"),
                ("Judge", "DRI", "167", "Uncommon", "Trainer"), ("Sacred Ash", "DRI", "168", "Uncommon", "Trainer"),
                ("Spikemuth Gym", "DRI", "169", "Uncommon", "Trainer"), ("Team Rocket's Archer", "DRI", "170", "Uncommon", "Trainer"),
                ("Team Rocket's Ariana", "DRI", "171", "Uncommon", "Trainer"), ("Team Rocket's Bother-Bot", "DRI", "172", "Uncommon", "Trainer"),
                ("Team Rocket's Factory", "DRI", "173", "Uncommon", "Trainer"), ("Team Rocket's Giovanni", "DRI", "174", "Uncommon", "Trainer"),
                ("Team Rocket's Great Ball", "DRI", "175", "Uncommon", "Trainer"), ("Team Rocket's Petrel", "DRI", "176", "Uncommon", "Trainer"),
                ("Team Rocket's Proton", "DRI", "177", "Uncommon", "Trainer"), ("Team Rocket's Transceiver", "DRI", "178", "Uncommon", "Trainer"),
                ("Team Rocket's Venture Bomb", "DRI", "179", "Uncommon", "Trainer"), ("Team Rocket's Watchtower", "DRI", "180", "Uncommon", "Trainer"),
                ("TM Machine", "DRI", "181", "Uncommon", "Trainer"), ("Team Rocket's Energy", "DRI", "182", "Uncommon", "Energy")
            ],
            "Rare": [
                ("Cynthia's Roserade", "DRI", "008", "Rare", "Pokémon"), ("Crustle", "DRI", "012", "Rare", "Pokémon"),
                ("Hydrapple", "DRI", "018", "Rare", "Pokémon"), ("Team Rocket's Spidops", "DRI", "020", "Rare", "Pokémon"),
                ("Ethan's Typhlosion", "DRI", "034", "Rare", "Pokémon"), ("Ethan's Magcargo", "DRI", "036", "Rare", "Pokémon"),
                ("Blaziken", "DRI", "042", "Rare", "Pokémon"), ("Misty's Gyarados", "DRI", "049", "Rare", "Pokémon"),
                ("Team Rocket's Articuno", "DRI", "051", "Rare", "Pokémon"), ("Gorebyss", "DRI", "056", "Rare", "Pokémon"),
                ("Team Rocket's Zapdos", "DRI", "070", "Rare", "Pokémon"), ("Zeraora", "DRI", "078", "Rare", "Pokémon"),
                ("Team Rocket's Wobbuffet", "DRI", "082", "Rare", "Pokémon"), ("Annihilape", "DRI", "092", "Rare", "Pokémon"),
                ("Team Rocket's Tyranitar", "DRI", "096", "Rare", "Pokémon"), ("Team Rocket's Sneasel", "DRI", "128", "Rare", "Pokémon"),
                ("Zamazenta", "DRI", "146", "Rare", "Pokémon"), ("Arven's Greedent", "DRI", "159", "Rare", "Pokémon")
            ],
            "Holo Rare": [],
            "Double Rare": [
                ("Yanmega ex", "DRI", "003", "Double Rare", "Pokémon"), ("Arboliva ex", "DRI", "023", "Double Rare", "Pokémon"),
                ("Rabsca ex", "DRI", "025", "Double Rare", "Pokémon"), ("Team Rocket's Moltres ex", "DRI", "031", "Double Rare", "Pokémon"),
                ("Ethan's Ho-Oh ex", "DRI", "039", "Double Rare", "Pokémon"), ("Cetitan ex", "DRI", "065", "Double Rare", "Pokémon"),
                ("Dondozo ex", "DRI", "066", "Double Rare", "Pokémon"), ("Electivire ex", "DRI", "069", "Double Rare", "Pokémon"),
                ("Team Rocket's Mewtwo ex", "DRI", "081", "Double Rare", "Pokémon"), ("Regirock ex", "DRI", "101", "Double Rare", "Pokémon"),
                ("Cynthia's Garchomp ex", "DRI", "104", "Double Rare", "Pokémon"), ("Team Rocket's Nidoking ex", "DRI", "119", "Double Rare", "Pokémon"),
                ("Team Rocket's Crobat ex", "DRI", "122", "Double Rare", "Pokémon"), ("Marnie's Grimmsnarl ex", "DRI", "136", "Double Rare", "Pokémon"),
                ("Arven's Mabosstiff ex", "DRI", "139", "Double Rare", "Pokémon"), ("Steven's Metagross ex", "DRI", "145", "Double Rare", "Pokémon"),
                ("Team Rocket's Persian ex", "DRI", "150", "Double Rare", "Pokémon")
            ],
            "Illustration Rare": [
                ("Yanma", "DRI", "183", "Illustration Rare", "Pokémon"), ("Cynthia's Roserade", "DRI", "184", "Illustration Rare", "Pokémon"),
                ("Shaymin", "DRI", "185", "Illustration Rare", "Pokémon"), ("Crustle", "DRI", "186", "Illustration Rare", "Pokémon"),
                ("Team Rocket's Spidops", "DRI", "187", "Illustration Rare", "Pokémon"), ("Hydrapple", "DRI", "188", "Illustration Rare", "Pokémon"),
                ("Rapidash", "DRI", "189", "Illustration Rare", "Pokémon"), ("Ethan's Typhlosion", "DRI", "190", "Illustration Rare", "Pokémon"),
                ("Team Rocket's Houndoom", "DRI", "191", "Illustration Rare", "Pokémon"), ("Blaziken", "DRI", "192", "Illustration Rare", "Pokémon"),
                ("Misty's Psyduck", "DRI", "193", "Illustration Rare", "Pokémon"), ("Misty's Lapras", "DRI", "194", "Illustration Rare", "Pokémon"),
                ("Clamperl", "DRI", "195", "Illustration Rare", "Pokémon"), ("Electrike", "DRI", "196", "Illustration Rare", "Pokémon"),
                ("Rotom", "DRI", "197", "Illustration Rare", "Pokémon"), ("Team Rocket's Orbeetle", "DRI", "198", "Illustration Rare", "Pokémon"),
                ("Team Rocket's Weezing", "DRI", "199", "Illustration Rare", "Pokémon"), ("Team Rocket's Murkrow", "DRI", "200", "Illustration Rare", "Pokémon"),
                ("Zamazenta", "DRI", "201", "Illustration Rare", "Pokémon"), ("Team Rocket's Raticate", "DRI", "202", "Illustration Rare", "Pokémon"),
                ("Team Rocket's Meowth", "DRI", "203", "Illustration Rare", "Pokémon"), ("Kangaskhan", "DRI", "204", "Illustration Rare", "Pokémon"),
                ("Arven's Greedent", "DRI", "205", "Illustration Rare", "Pokémon")
            ],
            "Ultra Rare": [
                ("Yanmega ex", "DRI", "206", "Ultra Rare", "Pokémon"), ("Arboliva ex", "DRI", "207", "Ultra Rare", "Pokémon"),
                ("Team Rocket's Moltres ex", "DRI", "208", "Ultra Rare", "Pokémon"), ("Ethan's Ho-Oh ex", "DRI", "209", "Ultra Rare", "Pokémon"),
                ("Cetitan ex", "DRI", "210", "Ultra Rare", "Pokémon"), ("Dondozo ex", "DRI", "211", "Ultra Rare", "Pokémon"),
                ("Electivire ex", "DRI", "212", "Ultra Rare", "Pokémon"), ("Team Rocket's Mewtwo ex", "DRI", "213", "Ultra Rare", "Pokémon"),
                ("Regirock ex", "DRI", "214", "Ultra Rare", "Pokémon"), ("Cynthia's Garchomp ex", "DRI", "215", "Ultra Rare", "Pokémon"),
                ("Team Rocket's Nidoking ex", "DRI", "216", "Ultra Rare", "Pokémon"), ("Team Rocket's Crobat ex", "DRI", "217", "Ultra Rare", "Pokémon"),
                ("Arven's Mabosstiff ex", "DRI", "218", "Ultra Rare", "Pokémon"), ("Team Rocket's Persian ex", "DRI", "219", "Ultra Rare", "Pokémon"),
                ("Emcee's Hype", "DRI", "220", "Ultra Rare", "Trainer"), ("Ethan's Adventure", "DRI", "221", "Ultra Rare", "Trainer"),
                ("Judge", "DRI", "222", "Ultra Rare", "Trainer"), ("Team Rocket's Archer", "DRI", "223", "Ultra Rare", "Trainer"),
                ("Team Rocket's Ariana", "DRI", "224", "Ultra Rare", "Trainer"), ("Team Rocket's Giovanni", "DRI", "225", "Ultra Rare", "Trainer"),
                ("Team Rocket's Petrel", "DRI", "226", "Ultra Rare", "Trainer"), ("Team Rocket's Proton", "DRI", "227", "Ultra Rare", "Trainer")
            ],
            "Special Illustration Rare": [
                ("Yanmega ex", "DRI", "228", "Special Illustration Rare", "Pokémon"), ("Team Rocket's Moltres ex", "DRI", "229", "Special Illustration Rare", "Pokémon"),
                ("Ethan's Ho-Oh ex", "DRI", "230", "Special Illustration Rare", "Pokémon"), ("Team Rocket's Mewtwo ex", "DRI", "231", "Special Illustration Rare", "Pokémon"),
                ("Cynthia's Garchomp ex", "DRI", "232", "Special Illustration Rare", "Pokémon"), ("Team Rocket's Nidoking ex", "DRI", "233", "Special Illustration Rare", "Pokémon"),
                ("Team Rocket's Crobat ex", "DRI", "234", "Special Illustration Rare", "Pokémon"), ("Arven's Mabosstiff ex", "DRI", "235", "Special Illustration Rare", "Pokémon"),
                ("Ethan's Adventure", "DRI", "236", "Special Illustration Rare", "Trainer"), ("Team Rocket's Ariana", "DRI", "237", "Special Illustration Rare", "Trainer"),
                ("Team Rocket's Giovanni", "DRI", "238", "Special Illustration Rare", "Trainer")
            ],
            "Hyper Rare": [
                ("Ethan's Ho-Oh ex", "DRI", "239", "Hyper Rare", "Pokémon"), ("Team Rocket's Mewtwo ex", "DRI", "240", "Hyper Rare", "Pokémon"),
                ("Cynthia's Garchomp ex", "DRI", "241", "Hyper Rare", "Pokémon"), ("Team Rocket's Crobat ex", "DRI", "242", "Hyper Rare", "Pokémon"),
                ("Jamming Tower", "DRI", "243", "Hyper Rare", "Trainer"), ("Levincia", "DRI", "244", "Hyper Rare", "Trainer")
            ]
        }
    },
}

BASIC_ENERGIES = ["Fire", "Water", "Grass", "Metal", "Darkness", "Psychic", "Lightning", "Fighting"]

def get_random_card(rarity, card_db):
    if rarity in card_db and card_db[rarity]:
        return random.choice(card_db[rarity])
    return None

def open_one_pack(set_data, set_name):
    # ... (this entire function is copied here, unchanged) ...
    pack_contents = []
    card_db = set_data['card_database']
    rates = set_data['pull_rates']
    
    p_holo = 1 - (rates.get('P_DR', 0) + rates.get('P_UR', 0) + rates.get('P_SIR', 0) + rates.get('P_HR', 0))
    pull_rates_rare_slot = {
        'Holo Rare': p_holo, 'Double Rare': rates.get('P_DR', 0), 'Ultra Rare': rates.get('P_UR', 0),
        'Special Illustration Rare': rates.get('P_SIR', 0), 'Hyper Rare': rates.get('P_HR', 0),
    }

    pack_contents.extend([get_random_card('Common', card_db) for _ in range(3)])
    pack_contents.extend([get_random_card('Uncommon', card_db) for _ in range(3)])
    pack_contents.append((f"{random.choice(BASIC_ENERGIES)} Energy", "Energy", "1", "Energy", "Energy"))

    if set_name == "Paldean Fates":
        pack_contents.append(get_random_card('Shiny Rare', card_db))
        reverse_holo_rarity = random.choice(['Common', 'Uncommon', 'Rare'])
        pack_contents.append(get_random_card(reverse_holo_rarity, card_db))
    elif set_name == "Temporal Forces" and 'ACE SPEC' in card_db and random.random() < 1/20:
        pack_contents.append(get_random_card('ACE SPEC', card_db))
        reverse_holo_rarity = random.choice(['Common', 'Uncommon', 'Rare'])
        pack_contents.append(get_random_card(reverse_holo_rarity, card_db))
    else:
        if random.random() < rates.get('P_IR', 0):
            pack_contents.append(get_random_card('Illustration Rare', card_db))
        else:
            reverse_holo_rarity = random.choice(['Common', 'Uncommon', 'Rare'])
            pack_contents.append(get_random_card(reverse_holo_rarity, card_db))
        
        reverse_holo_rarity_2 = random.choice(['Common', 'Uncommon', 'Rare'])
        pack_contents.append(get_random_card(reverse_holo_rarity_2, card_db))

    rare_slot_rarity = random.choices(list(pull_rates_rare_slot.keys()), weights=list(pull_rates_rare_slot.values()), k=1)[0]
    card_rare = get_random_card(rare_slot_rarity, card_db)
    if card_rare is None:
        card_rare = get_random_card('Rare', card_db)
    if card_rare:
        pack_contents.append(card_rare)

    return [c for c in pack_contents if c is not None]


def format_collection_for_export(collection):
    # ... (this entire function is copied here, unchanged) ...
    if not collection:
        return "No cards collected yet."

    card_counts = collections.Counter(collection)
    pokemon_cards, trainer_cards, energy_cards = {}, {}, {}

    for card, count in card_counts.items():
        if not isinstance(card, tuple) or len(card) != 5:
            continue
        name, set_code, num, _, card_type = card
        if card_type == 'Energy' and set_code == 'Energy':
            formatted_line = f"{count} {name}"
        else:
            formatted_line = f"{count} {name} {set_code} {num}"

        if card_type == 'Pokémon': pokemon_cards[formatted_line] = count
        elif card_type == 'Trainer': trainer_cards[formatted_line] = count
        elif card_type == 'Energy': energy_cards[formatted_line] = count
    
    output_str = ""
    output_str += f"Pokémon: {sum(pokemon_cards.values())}\n"
    for line in sorted(pokemon_cards.keys()): output_str += f"{line}\n"
    output_str += "\n"
    output_str += f"Trainer: {sum(trainer_cards.values())}\n"
    for line in sorted(trainer_cards.keys()): output_str += f"{line}\n"
    output_str += "\n"
    output_str += f"Energy: {sum(energy_cards.values())}\n"
    for line in sorted(energy_cards.keys()): output_str += f"{line}\n"
    
    return output_str