"""
def main():
    numIndex = 0
    numList = [
        3, #knightquest:bamboo_blue_helmet == armor
        1, #knightquest:bamboo_blue_helmet == toughness
        2, #knightquest:bamboo_blue_helmet == kb res
        8, #knightquest:bamboo_blue_chestplate == armor
        1, #knightquest:bamboo_blue_chestplate == toughness
        0, #knightquest:bamboo_blue_chestplate == kb res
        7, #knightquest:bamboo_blue_leggings == armor
        1, #knightquest:bamboo_blue_leggings == toughness
        0, #knightquest:bamboo_blue_leggings == kb res
        3, #knightquest:bamboo_blue_boots == armor
        1, #knightquest:bamboo_blue_boots == toughness
        0, #knightquest:bamboo_blue_boots == kb res
        3, #knightquest:bamboo_green_helmet == armor
        1, #knightquest:bamboo_green_helmet == toughness
        0, #knightquest:bamboo_green_helmet == kb res
        8, #knightquest:bamboo_green_chestplate == armor
        1, #knightquest:bamboo_green_chestplate == toughness
        0, #knightquest:bamboo_green_chestplate == kb res
        7, #knightquest:bamboo_green_leggings == armor
        1, #knightquest:bamboo_green_leggings == toughness
        0, #knightquest:bamboo_green_leggings == kb res
        3, #knightquest:bamboo_green_boots == armor
        1, #knightquest:bamboo_green_boots == toughness
        0, #knightquest:bamboo_green_boots == kb res
        2, #knightquest:bamboo_helmet == armor
        1, #knightquest:bamboo_helmet == toughness
        0, #knightquest:bamboo_helmet == kb res
        6, #knightquest:bamboo_chestplate == armor
        1, #knightquest:bamboo_chestplate == toughness
        0, #knightquest:bamboo_chestplate == kb res
        6, #knightquest:bamboo_leggings == armor
        1, #knightquest:bamboo_leggings == toughness
        0, #knightquest:bamboo_leggings == kb res
        5, #knightquest:bamboo_boots == armor
        6, #knightquest:bamboo_boots == toughness
        0.12, #knightquest:bamboo_boots == kb res
        3, #knightquest:bat_helmet == armor
        1, #knightquest:bat_helmet == toughness
        0.2, #knightquest:bat_helmet == kb res
        8, #knightquest:bat_chestplate == armor
        1, #knightquest:bat_chestplate == toughness
        0.2, #knightquest:bat_chestplate == kb res
        7, #knightquest:bat_leggings == armor
        1, #knightquest:bat_leggings == toughness
        0.2, #knightquest:bat_leggings == kb res
        2, #knightquest:bat_boots == armor
        1, #knightquest:bat_boots == toughness
        0.2, #knightquest:bat_boots == kb res
        3, #knightquest:blaze_helmet == armor
        2, #knightquest:blaze_helmet == toughness
        0.2, #knightquest:blaze_helmet == kb res
        8, #knightquest:blaze_chestplate == armor
        2, #knightquest:blaze_chestplate == toughness
        0.2, #knightquest:blaze_chestplate == kb res
        7, #knightquest:blaze_leggings == armor
        2, #knightquest:blaze_leggings == toughness
        0.2, #knightquest:blaze_leggings == kb res
        3, #knightquest:blaze_boots == armor
        2, #knightquest:blaze_boots == toughness
        0.2, #knightquest:blaze_boots == kb res
        2, #knightquest:bow_helmet == armor
        0, #knightquest:bow_helmet == toughness
        0, #knightquest:bow_helmet == kb res
        8, #knightquest:bow_chestplate == armor
        0, #knightquest:bow_chestplate == toughness
        0, #knightquest:bow_chestplate == kb res
        7, #knightquest:bow_leggings == armor
        0, #knightquest:bow_leggings == toughness
        0, #knightquest:bow_leggings == kb res
        2, #knightquest:bow_boots == armor
        0, #knightquest:bow_boots == toughness
        0, #knightquest:bow_boots == kb res
        2, #knightquest:horn_helmet == armor
        0, #knightquest:horn_helmet == toughness
        0, #knightquest:horn_helmet == kb res
        8, #knightquest:horn_chestplate == armor
        0, #knightquest:horn_chestplate == toughness
        0, #knightquest:horn_chestplate == kb res
        7, #knightquest:horn_leggings == armor
        0, #knightquest:horn_leggings == toughness
        0, #knightquest:horn_leggings == kb res
        2, #knightquest:horn_boots == armor
        0, #knightquest:horn_boots == toughness
        0, #knightquest:horn_boots == kb res
        2, #knightquest:creeper_helmet == armor
        0, #knightquest:creeper_helmet == toughness
        0, #knightquest:creeper_helmet == kb res
        8, #knightquest:creeper_chestplate == armor
        0, #knightquest:creeper_chestplate == toughness
        0, #knightquest:creeper_chestplate == kb res
        7, #knightquest:creeper_leggings == armor
        1, #knightquest:creeper_leggings == toughness
        0, #knightquest:creeper_leggings == kb res
        2, #knightquest:creeper_boots == armor
        1, #knightquest:creeper_boots == toughness
        0, #knightquest:creeper_boots == kb res
        3, #knightquest:deepslate_helmet == armor
        0.5, #knightquest:deepslate_helmet == toughness
        0.8, #knightquest:deepslate_helmet == kb res
        8, #knightquest:deepslate_chestplate == armor
        0.5, #knightquest:deepslate_chestplate == toughness
        0.8, #knightquest:deepslate_chestplate == kb res
        7, #knightquest:deepslate_leggings == armor
        0.5, #knightquest:deepslate_leggings == toughness
        0.8, #knightquest:deepslate_leggings == kb res
        3, #knightquest:deepslate_boots == armor
        0.5, #knightquest:deepslate_boots == toughness
        0.8, #knightquest:deepslate_boots == kb res
        2, #knightquest:evoker_helmet == armor
        0, #knightquest:evoker_helmet == toughness
        0, #knightquest:evoker_helmet == kb res
        4, #knightquest:evoker_chestplate == armor
        0, #knightquest:evoker_chestplate == toughness
        0, #knightquest:evoker_chestplate == kb res
        3, #knightquest:evoker_leggings == armor
        0, #knightquest:evoker_leggings == toughness
        0, #knightquest:evoker_leggings == kb res
        1, #knightquest:evoker_boots == armor
        0, #knightquest:evoker_boots == toughness
        0, #knightquest:evoker_boots == kb res
        2, #knightquest:forze_helmet == armor
        0.5, #knightquest:forze_helmet == toughness
        0, #knightquest:forze_helmet == kb res
        8, #knightquest:forze_chestplate == armor
        0.5, #knightquest:forze_chestplate == toughness
        0, #knightquest:forze_chestplate == kb res
        7, #knightquest:forze_leggings == armor
        0.5, #knightquest:forze_leggings == toughness
        0, #knightquest:forze_leggings == kb res
        3, #knightquest:forze_boots == armor
        0.5, #knightquest:forze_boots == toughness
        0, #knightquest:forze_boots == kb res
        2, #knightquest:hollow_helmet == armor
        0, #knightquest:hollow_helmet == toughness
        -0.2, #knightquest:hollow_helmet == kb res
        4, #knightquest:hollow_chestplate == armor
        0, #knightquest:hollow_chestplate == toughness
        0.2, #knightquest:hollow_chestplate == kb res
        4, #knightquest:hollow_leggings == armor
        0, #knightquest:hollow_leggings == toughness
        0.2, #knightquest:hollow_leggings == kb res
        2, #knightquest:hollow_boots == armor
        0, #knightquest:hollow_boots == toughness
        0.2, #knightquest:hollow_boots == kb res
        2, #knightquest:nether_helmet == armor
        0, #knightquest:nether_helmet == toughness
        0, #knightquest:nether_helmet == kb res
        8, #knightquest:nether_chestplate == armor
        0, #knightquest:nether_chestplate == toughness
        0, #knightquest:nether_chestplate == kb res
        6, #knightquest:nether_leggings == armor
        0, #knightquest:nether_leggings == toughness
        0, #knightquest:nether_leggings == kb res
        2, #knightquest:nether_boots == armor
        0, #knightquest:nether_boots == toughness
        0, #knightquest:nether_boots == kb res
        1, #knightquest:veteran_helmet == armor
        2, #knightquest:veteran_helmet == toughness
        0.5, #knightquest:veteran_helmet == kb res
        8, #knightquest:veteran_chestplate == armor
        2, #knightquest:veteran_chestplate == toughness
        0.5, #knightquest:veteran_chestplate == kb res
        7, #knightquest:veteran_leggings == armor
        2, #knightquest:veteran_leggings == toughness
        0.5, #knightquest:veteran_leggings == kb res
        3, #knightquest:veteran_boots == armor
        4, #knightquest:veteran_boots == toughness
        0.5, #knightquest:veteran_boots == kb res
        2, #knightquest:phantom_helmet == armor
        0, #knightquest:phantom_helmet == toughness
        0, #knightquest:phantom_helmet == kb res
        7, #knightquest:phantom_chestplate == armor
        0, #knightquest:phantom_chestplate == toughness
        0, #knightquest:phantom_chestplate == kb res
        7, #knightquest:phantom_leggings == armor
        0, #knightquest:phantom_leggings == toughness
        0, #knightquest:phantom_leggings == kb res
        2, #knightquest:phantom_boots == armor
        0, #knightquest:phantom_boots == toughness
        0, #knightquest:phantom_boots == kb res
        3, #knightquest:sea_helmet == armor
        3, #knightquest:sea_helmet == toughness
        0.15, #knightquest:sea_helmet == kb res
        8, #knightquest:sea_chestplate == armor
        3, #knightquest:sea_chestplate == toughness
        0.15, #knightquest:sea_chestplate == kb res
        7, #knightquest:sea_leggings == armor
        3, #knightquest:sea_leggings == toughness
        0.15, #knightquest:sea_leggings == kb res
        3, #knightquest:sea_boots == armor
        3, #knightquest:sea_boots == toughness
        0.15, #knightquest:sea_boots == kb res
        3, #knightquest:silver_helmet == armor
        1, #knightquest:silver_helmet == toughness
        0, #knightquest:silver_helmet == kb res
        8, #knightquest:silver_chestplate == armor
        1, #knightquest:silver_chestplate == toughness
        0, #knightquest:silver_chestplate == kb res
        6, #knightquest:silver_leggings == armor
        1, #knightquest:silver_leggings == toughness
        0, #knightquest:silver_leggings == kb res
        3, #knightquest:silver_boots == armor
        1, #knightquest:silver_boots == toughness
        3, #knightquest:silver_boots == kb res
        3, #knightquest:silverfish_helmet == armor
        2.5, #knightquest:silverfish_helmet == toughness
        0, #knightquest:silverfish_helmet == kb res
        8, #knightquest:silverfish_chestplate == armor
        2.5, #knightquest:silverfish_chestplate == toughness
        0, #knightquest:silverfish_chestplate == kb res
        7, #knightquest:silverfish_leggings == armor
        2.5, #knightquest:silverfish_leggings == toughness
        0, #knightquest:silverfish_leggings == kb res
        3, #knightquest:silverfish_boots == armor
        2.5, #knightquest:silverfish_boots == toughness
        0, #knightquest:silverfish_boots == kb res
        1, #knightquest:skeleton_helmet == armor
        0, #knightquest:skeleton_helmet == toughness
        0, #knightquest:skeleton_helmet == kb res
        7, #knightquest:skeleton_chestplate == armor
        0, #knightquest:skeleton_chestplate == toughness
        0, #knightquest:skeleton_chestplate == kb res
        5, #knightquest:skeleton_leggings == armor
        0, #knightquest:skeleton_leggings == toughness
        0, #knightquest:skeleton_leggings == kb res
        3, #knightquest:skeleton_boots == armor
        0, #knightquest:skeleton_boots == toughness
        0, #knightquest:skeleton_boots == kb res
        3, #knightquest:spider_helmet == armor
        3, #knightquest:spider_helmet == toughness
        0, #knightquest:spider_helmet == kb res
        8, #knightquest:spider_chestplate == armor
        3, #knightquest:spider_chestplate == toughness
        0, #knightquest:spider_chestplate == kb res
        7, #knightquest:spider_leggings == armor
        3, #knightquest:spider_leggings == toughness
        0, #knightquest:spider_leggings == kb res
        3, #knightquest:spider_boots == armor
        3, #knightquest:spider_boots == toughness
        0.16, #knightquest:spider_boots == kb res
        3, #knightquest:warlord_helmet == armor
        0, #knightquest:warlord_helmet == toughness
        0.2, #knightquest:warlord_helmet == kb res
        7, #knightquest:warlord_chestplate == armor
        0, #knightquest:warlord_chestplate == toughness
        0.2, #knightquest:warlord_chestplate == kb res
        6, #knightquest:warlord_leggings == armor
        0, #knightquest:warlord_leggings == toughness
        0.2, #knightquest:warlord_leggings == kb res
        2, #knightquest:warlord_boots == armor
        0, #knightquest:warlord_boots == toughness
        0.2, #knightquest:warlord_boots == kb res
        3, #knightquest:strawhat_helmet == armor
        0, #knightquest:strawhat_helmet == toughness
        0, #knightquest:strawhat_helmet == kb res
        8, #knightquest:strawhat_chestplate == armor
        0, #knightquest:strawhat_chestplate == toughness
        0, #knightquest:strawhat_chestplate == kb res
        7, #knightquest:strawhat_leggings == armor
        0, #knightquest:strawhat_leggings == toughness
        0, #knightquest:strawhat_leggings == kb res
        3, #knightquest:strawhat_boots == armor
        0, #knightquest:strawhat_boots == toughness
        0, #knightquest:strawhat_boots == kb res
        3, #knightquest:pirate_helmet == armor
        3, #knightquest:pirate_helmet == toughness
        0.4, #knightquest:pirate_helmet == kb res
        3, #knightquest:pirate2_helmet == armor
        3, #knightquest:pirate2_helmet == toughness
        0.4, #knightquest:pirate2_helmet == kb res
        3, #knightquest:pirate3_helmet == armor
        3, #knightquest:pirate3_helmet == toughness
        0.4, #knightquest:pirate3_helmet == kb res
        8, #knightquest:pirate_chestplate == armor
        3, #knightquest:pirate_chestplate == toughness
        0.4, #knightquest:pirate_chestplate == kb res
        7, #knightquest:pirate_leggings == armor
        3, #knightquest:pirate_leggings == toughness
        0.4, #knightquest:pirate_leggings == kb res
        3, #knightquest:pirate_boots == armor
        3, #knightquest:pirate_boots == toughness
        0.4, #knightquest:pirate_boots == kb res
        3, #knightquest:conquistador_helmet == armor
        0, #knightquest:conquistador_helmet == toughness
        0, #knightquest:conquistador_helmet == kb res
        3, #knightquest:conquistador2_helmet == armor
        0, #knightquest:conquistador2_helmet == toughness
        0, #knightquest:conquistador2_helmet == kb res
        3, #knightquest:conquistador3_helmet == armor
        0, #knightquest:conquistador3_helmet == toughness
        0, #knightquest:conquistador3_helmet == kb res
        7, #knightquest:conquistador_chestplate == armor
        0, #knightquest:conquistador_chestplate == toughness
        0, #knightquest:conquistador_chestplate == kb res
        6, #knightquest:conquistador_leggings == armor
        0, #knightquest:conquistador_leggings == toughness
        0, #knightquest:conquistador_leggings == kb res
        3, #knightquest:conquistador_boots == armor
        0, #knightquest:conquistador_boots == toughness
        0, #knightquest:conquistador_boots == kb res
        2, #knightquest:zombie_helmet == armor
        0, #knightquest:zombie_helmet == toughness
        0, #knightquest:zombie_helmet == kb res
        2, #knightquest:zombie2_helmet == armor
        0, #knightquest:zombie2_helmet == toughness
        0, #knightquest:zombie2_helmet == kb res
        0, #knightquest:zombie_chestplate == armor
        7, #knightquest:zombie_chestplate == toughness
        0, #knightquest:zombie_chestplate == kb res
        6, #knightquest:zombie_leggings == armor
        0, #knightquest:zombie_leggings == toughness
        0, #knightquest:zombie_leggings == kb res
        3, #knightquest:zombie_boots == armor
        0, #knightquest:zombie_boots == toughness
        0, #knightquest:zombie_boots == kb res
        3, #knightquest:husk_helmet == armor
        0, #knightquest:husk_helmet == toughness
        0, #knightquest:husk_helmet == kb res
        3, #knightquest:husk_helmet2 == armor
        0, #knightquest:husk_helmet2 == toughness
        0, #knightquest:husk_helmet2 == kb res
        3, #knightquest:husk_helmet3 == armor
        0, #knightquest:husk_helmet3 == toughness
        0, #knightquest:husk_helmet3 == kb res
        8, #knightquest:husk_chestplate == armor
        0, #knightquest:husk_chestplate == toughness
        0, #knightquest:husk_chestplate == kb res
        6, #knightquest:husk_leggings == armor
        0, #knightquest:husk_leggings == toughness
        0, #knightquest:husk_leggings == kb res
        2, #knightquest:husk_boots == armor
        0, #knightquest:husk_boots == toughness
        0, #knightquest:husk_boots == kb res
        2, #knightquest:squire_helmet == armor
        0, #knightquest:squire_helmet == toughness
        0, #knightquest:squire_helmet == kb res
        0, #knightquest:squire_chestplate == armor
        8, #knightquest:squire_chestplate == toughness
        0, #knightquest:squire_chestplate == kb res
        6, #knightquest:squire_leggings == armor
        0, #knightquest:squire_leggings == toughness
        0, #knightquest:squire_leggings == kb res
        2, #knightquest:squire_boots == armor
        0, #knightquest:squire_boots == toughness
        0, #knightquest:squire_boots == kb res
        3, #knightquest:witch_helmet == armor
        0, #knightquest:witch_helmet == toughness
        0, #knightquest:witch_helmet == kb res
        8, #knightquest:witch_chestplate == armor
        0, #knightquest:witch_chestplate == toughness
        0, #knightquest:witch_chestplate == kb res
        6, #knightquest:witch_leggings == armor
        0, #knightquest:witch_leggings == toughness
        0, #knightquest:witch_leggings == kb res
        3, #knightquest:witch_boots == armor
        0, #knightquest:witch_boots == toughness
        0, #knightquest:witch_boots == kb res
        3, #knightquest:shinobi_helmet == armor
        3, #knightquest:shinobi_helmet == toughness
        0.2, #knightquest:shinobi_helmet == kb res
        8, #knightquest:shinobi_chestplate == armor
        3, #knightquest:shinobi_chestplate == toughness
        0.2, #knightquest:shinobi_chestplate == kb res
        6, #knightquest:shinobi_leggings == armor
        3, #knightquest:shinobi_leggings == toughness
        0.2, #knightquest:shinobi_leggings == kb res
        3, #knightquest:shinobi_boots == armor
        3, #knightquest:shinobi_boots == toughness
        0.2, #knightquest:shinobi_boots == kb res
        3, #knightquest:skulk_helmet == armor
        0, #knightquest:skulk_helmet == toughness
        0, #knightquest:skulk_helmet == kb res
        3, #knightquest:skulk2_helmet == armor
        0, #knightquest:skulk2_helmet == toughness
        0, #knightquest:skulk2_helmet == kb res
        3, #knightquest:skulk3_helmet == armor
        0, #knightquest:skulk3_helmet == toughness
        0, #knightquest:skulk3_helmet == kb res
        3, #knightquest:skulk4_helmet == armor
        0, #knightquest:skulk4_helmet == toughness
        0, #knightquest:skulk4_helmet == kb res
        8, #knightquest:skulk_chestplate == kb res
        0, #knightquest:skulk_chestplate == kb res
        0, #knightquest:skulk_chestplate == kb res
        6, #knightquest:skulk_leggings == kb res
        0, #knightquest:skulk_leggings == kb res
        0, #knightquest:skulk_leggings == kb res
        3, #knightquest:skulk_boots == kb res
        0, #knightquest:skulk_boots == kb res
        0, #knightquest:skulk_boots == kb res
        2, #archers:archer_armor_head == armor
        0, #archers:archer_armor_head == toughness
        0, #archers:archer_armor_head == kb res
        3, #archers:archer_armor_chest == armor
        0, #archers:archer_armor_chest == toughness
        0, #archers:archer_armor_chest == kb res
        3, #archers:archer_armor_legs == armor
        0, #archers:archer_armor_legs == toughness
        0, #archers:archer_armor_legs == kb res
        2, #archers:archer_armor_feet == armor
        0, #archers:archer_armor_feet == toughness
        0, #archers:archer_armor_feet == kb res
        1, #rogues:rogue_armor_head == armor
        0, #rogues:rogue_armor_head == toughness
        0, #rogues:rogue_armor_head == kb res
        4, #rogues:rogue_armor_chest == armor
        0, #rogues:rogue_armor_chest == toughness
        0, #rogues:rogue_armor_chest == kb res
        3, #rogues:rogue_armor_legs == armor
        0, #rogues:rogue_armor_legs == toughness
        0, #rogues:rogue_armor_legs == kb res
        2, #rogues:rogue_armor_feet == armor
        0, #rogues:rogue_armor_feet == toughness
        0, #rogues:rogue_armor_feet == kb res
        1, #paladins:priest_robe_head == armor
        0, #paladins:priest_robe_head == toughness
        0, #paladins:priest_robe_head == kb res
        2, #paladins:priest_robe_chest == armor
        0, #paladins:priest_robe_chest == toughness
        0, #paladins:priest_robe_chest == kb res
        1, #paladins:priest_robe_legs == armor
        0, #paladins:priest_robe_legs == toughness
        0, #paladins:priest_robe_legs == kb res
        1, #paladins:priest_robe_feet == armor
        0, #paladins:priest_robe_feet == toughness
        0, #paladins:priest_robe_feet == kb res
        1, #paladins:prior_robe_head == armor
        0, #paladins:prior_robe_head == toughness
        0, #paladins:prior_robe_head == kb res
        3, #paladins:prior_robe_chest == armor
        0, #paladins:prior_robe_chest == toughness
        0, #paladins:prior_robe_chest == kb res
        2, #paladins:prior_robe_legs == armor
        0, #paladins:prior_robe_legs == toughness
        0, #paladins:prior_robe_legs == kb res
        1, #paladins:prior_robe_feet == armor
        0, #paladins:prior_robe_feet == toughness
        0, #paladins:prior_robe_feet == kb res
        2, #paladins:paladin_armor_head == armor
        0, #paladins:paladin_armor_head == toughness
        0, #paladins:paladin_armor_head == kb res
        6, #paladins:paladin_armor_chest == armor
        0, #paladins:paladin_armor_chest == toughness
        0, #paladins:paladin_armor_chest == kb res
        5, #paladins:paladin_armor_legs == armor
        0, #paladins:paladin_armor_legs == toughness
        0, #paladins:paladin_armor_legs == kb res
        2, #paladins:paladin_armor_feet == armor
        0, #paladins:paladin_armor_feet == toughness
        0, #paladins:paladin_armor_feet == kb res
        3, #paladins:crusader_armor_head == armor
        0, #paladins:crusader_armor_head == toughness
        0, #paladins:crusader_armor_head == kb res
        8, #paladins:crusader_armor_chest == armor
        0, #paladins:crusader_armor_chest == toughness
        0, #paladins:crusader_armor_chest == kb res
        6, #paladins:crusader_armor_legs == armor
        0, #paladins:crusader_armor_legs == toughness
        0, #paladins:crusader_armor_legs == kb res
        3, #paladins:crusader_armor_feet == armor
        0, #paladins:crusader_armor_feet == toughness
        0, #paladins:crusader_armor_feet == kb res
        2, #rogues:assassin_armor_head == armor
        0, #rogues:assassin_armor_head == toughness
        0, #rogues:assassin_armor_head == kb res
        6, #rogues:assassin_armor_chest == armor
        0, #rogues:assassin_armor_chest == toughness
        0, #rogues:assassin_armor_chest == kb res
        5, #rogues:assassin_armor_legs == armor
        0, #rogues:assassin_armor_legs == toughness
        0, #rogues:assassin_armor_legs == kb res
        2, #rogues:assassin_armor_feet == armor
        0, #rogues:assassin_armor_feet == toughness
        0, #rogues:assassin_armor_feet == kb res
        2, #archers:ranger_armor_head == armor
        0, #archers:ranger_armor_head == toughness
        0, #archers:ranger_armor_head == kb res
        5, #archers:ranger_armor_chest == armor
        0, #archers:ranger_armor_chest == toughness
        0, #archers:ranger_armor_chest == kb res
        4, #archers:ranger_armor_legs == armor
        0, #archers:ranger_armor_legs == toughness
        0, #archers:ranger_armor_legs == kb res
        2, #archers:ranger_armor_feet == armor
        0, #archers:ranger_armor_feet == toughness
        0, #archers:ranger_armor_feet == kb res
        2, #rogues:warrior_armor_head == armor
        1, #rogues:warrior_armor_head == toughness
        0.1, #rogues:warrior_armor_head == kb res
        6, #rogues:warrior_armor_chest == armor
        1, #rogues:warrior_armor_chest == toughness
        0.1, #rogues:warrior_armor_chest == kb res
        5, #rogues:warrior_armor_legs == armor
        1, #rogues:warrior_armor_legs == toughness
        0.1, #rogues:warrior_armor_legs == kb res
        2, #rogues:warrior_armor_feet == armor
        1, #rogues:warrior_armor_feet == toughness
        0.1, #rogues:warrior_armor_feet == kb res
        3, #rogues:berserker_armor_head == armor
        1, #rogues:berserker_armor_head == toughness
        0.4, #rogues:berserker_armor_head == kb res
        8, #rogues:berserker_armor_chest == armor
        1, #rogues:berserker_armor_chest == toughness
        0.4, #rogues:berserker_armor_chest == kb res
        6, #rogues:berserker_armor_legs == armor
        1, #rogues:berserker_armor_legs == toughness
        0.4, #rogues:berserker_armor_legs == kb res
        3, #rogues:berserker_armor_feet == armor
        1, #rogues:berserker_armor_feet == toughness
        0.4, #rogues:berserker_armor_feet == kb res
	    4, #minecraft:netherite_helmet == armor
        4, #minecraft:netherite_helmet == toughness
        0.2, #minecraft:netherite_helmet == kb res
        9, #minecraft:netherite_chestplate == armor
        4, #minecraft:netherite_chestplate == toughness
        0.2, #minecraft:netherite_chestplate == kb res
        7, #minecraft:netherite_leggings == armor
        4, #minecraft:netherite_leggings == toughness
        0.2, #minecraft:netherite_leggings == kb res
        3, #minecraft:netherite_boots == armor
        4, #minecraft:netherite_boots == toughness
        0.2, #minecraft:netherite_boots == kb res
        3, #minecraft:diamond_helmet == armor
        3, #minecraft:diamond_helmet == toughness
        0, #minecraft:diamond_helmet == kb res
        9, #minecraft:diamond_chestplate == armor
        3, #minecraft:diamond_chestplate == toughness
        0, #minecraft:diamond_chestplate == kb res
        7, #minecraft:diamond_leggings == armor
        3, #minecraft:diamond_leggings == toughness
        0, #minecraft:diamond_leggings == kb res
        3, #minecraft:diamond_boots == armor
        3, #minecraft:diamond_boots == toughness
        0, #minecraft:diamond_boots == kb res
        2, #minecraft:iron_helmet == armor
        0, #minecraft:iron_helmet == toughness
        0, #minecraft:iron_helmet == kb res
        8, #minecraft:iron_chestplate == armor
        0, #minecraft:iron_chestplate == toughness
        0, #minecraft:iron_chestplate == kb res
        6, #minecraft:iron_leggings == armor
        0, #minecraft:iron_leggings == toughness
        0, #minecraft:iron_leggings == kb res
        2, #minecraft:iron_boots == armor
        0, #minecraft:iron_boots == toughness
        0, #minecraft:iron_boots == kb res
    ]

    itemList = [
        "knightquest:bamboo_blue_helmet",
        "knightquest:bamboo_blue_chestplate",
        "knightquest:bamboo_blue_leggings",
        "knightquest:bamboo_blue_boots",
        "knightquest:bamboo_green_helmet",
        "knightquest:bamboo_green_chestplate",
        "knightquest:bamboo_green_leggings",
        "knightquest:bamboo_green_boots",
        "knightquest:bamboo_helmet",
        "knightquest:bamboo_chestplate",
        "knightquest:bamboo_leggings",
        "knightquest:bamboo_boots",
        "knightquest:bat_helmet",
        "knightquest:bat_chestplate",
        "knightquest:bat_leggings",
        "knightquest:bat_boots",
	    "knightquest:blaze_helmet",
        "knightquest:blaze_chestplate",
        "knightquest:blaze_leggings",
        "knightquest:blaze_boots",
        "knightquest:bow_helmet",
        "knightquest:bow_chestplate",
        "knightquest:bow_leggings",
        "knightquest:bow_boots",
        "knightquest:horn_helmet",
        "knightquest:horn_chestplate",
        "knightquest:horn_leggings",
        "knightquest:horn_boots",
        "knightquest:creeper_helmet",
        "knightquest:creeper_chestplate",
        "knightquest:creeper_leggings",
        "knightquest:creeper_boots",
        "knightquest:deepslate_helmet",
        "knightquest:deepslate_chestplate",
        "knightquest:deepslate_leggings",
        "knightquest:deepslate_boots",
        "knightquest:evoker_helmet",
        "knightquest:evoker_chestplate",
        "knightquest:evoker_leggings",
        "knightquest:evoker_boots",
        "knightquest:forze_helmet",
        "knightquest:forze_chestplate",
        "knightquest:forze_leggings",
        "knightquest:forze_boots",
        "knightquest:hollow_helmet",
        "knightquest:hollow_chestplate",
        "knightquest:hollow_leggings",
        "knightquest:hollow_boots",
        "knightquest:nether_helmet",
        "knightquest:nether_chestplate",
        "knightquest:nether_leggings",
        "knightquest:nether_boots",
        "knightquest:veteran_helmet",
        "knightquest:veteran_chestplate",
        "knightquest:veteran_leggings",
        "knightquest:veteran_boots",
        "knightquest:phantom_helmet",
        "knightquest:phantom_chestplate",
        "knightquest:phantom_leggings",
        "knightquest:phantom_boots",
        "knightquest:sea_helmet",
        "knightquest:sea_chestplate",
        "knightquest:sea_leggings",
        "knightquest:sea_boots",
        "knightquest:silver_helmet",
        "knightquest:silver_chestplate",
        "knightquest:silver_leggings",
        "knightquest:silver_boots",
        "knightquest:silverfish_helmet",
        "knightquest:silverfish_chestplate",
        "knightquest:silverfish_leggings",
        "knightquest:silverfish_boots",
        "knightquest:skeleton_helmet",
        "knightquest:skeleton_chestplate",
        "knightquest:skeleton_leggings",
        "knightquest:skeleton_boots",
        "knightquest:spider_helmet",
        "knightquest:spider_chestplate",
        "knightquest:spider_leggings",
        "knightquest:spider_boots",
        "knightquest:warlord_helmet",
        "knightquest:warlord_chestplate",
        "knightquest:warlord_leggings",
        "knightquest:warlord_boots",
        "knightquest:strawhat_helmet",
        "knightquest:strawhat_chestplate",
        "knightquest:strawhat_leggings",
        "knightquest:strawhat_boots",
        "knightquest:pirate_helmet",
        "knightquest:pirate2_helmet",
        "knightquest:pirate3_helmet",
        "knightquest:pirate_chestplate",
        "knightquest:pirate_leggings",
        "knightquest:pirate_boots",
        "knightquest:conquistador_helmet",
        "knightquest:conquistador2_helmet",
        "knightquest:conquistador3_helmet",
        "knightquest:conquistador_chestplate",
        "knightquest:conquistador_leggings",
        "knightquest:conquistador_boots",
        "knightquest:zombie_helmet",
        "knightquest:zombie2_helmet",
        "knightquest:zombie_chestplate",
        "knightquest:zombie_leggings",
        "knightquest:zombie_boots",
        "knightquest:husk_helmet",
        "knightquest:husk_helmet2",
        "knightquest:husk_helmet3",
        "knightquest:husk_chestplate",
        "knightquest:husk_leggings",
        "knightquest:husk_boots",
        "knightquest:squire_helmet",
        "knightquest:squire_chestplate",
        "knightquest:squire_leggings",
        "knightquest:squire_boots",
        "knightquest:witch_helmet",
        "knightquest:witch_chestplate",
        "knightquest:witch_leggings",
        "knightquest:witch_boots",
        "knightquest:shinobi_helmet",
        "knightquest:shinobi_chestplate",
        "knightquest:shinobi_leggings",
        "knightquest:shinobi_boots",
        "knightquest:skulk_helmet",
        "knightquest:skulk2_helmet",
        "knightquest:skulk3_helmet",
        "knightquest:skulk4_helmet",
        "archers:archer_armor_head",
        "archers:archer_armor_chest",
        "archers:archer_armor_legs",
        "archers:archer_armor_feet",
        "rogues:rogue_armor_head",
        "rogues:rogue_armor_chest",
        "rogues:rogue_armor_legs",
        "rogues:rogue_armor_feet",
        "paladins:priest_robe_head",
        "paladins:priest_robe_chest",
        "paladins:priest_robe_legs",
        "paladins:priest_robe_feet",
        "paladins:prior_robe_head",
        "paladins:prior_robe_chest",
        "paladins:prior_robe_legs",
        "paladins:prior_robe_feet",
        "paladins:paladin_armor_head",
        "paladins:paladin_armor_chest",
        "paladins:paladin_armor_legs",
        "paladins:paladin_armor_feet",
        "paladins:crusader_armor_head",
        "paladins:crusader_armor_chest",
        "paladins:crusader_armor_legs",
        "paladins:crusader_armor_feet",
        "rogues:assassin_armor_head",
        "rogues:assassin_armor_chest",
        "rogues:assassin_armor_legs",
        "rogues:assassin_armor_feet",
        "archers:ranger_armor_head",
        "archers:ranger_armor_chest",
        "archers:ranger_armor_legs",
        "archers:ranger_armor_feet",
        "rogues:warrior_armor_head",
        "rogues:warrior_armor_chest",
        "rogues:warrior_armor_legs",
        "rogues:warrior_armor_feet",
        "rogues:berserker_armor_head",
        "rogues:berserker_armor_chest",
        "rogues:berserker_armor_legs",
        "rogues:berserker_armor_feet",
	    "minecraft:netherite_helmet",
	    "minecraft:netherite_chestplate",
	    "minecraft:netherite_leggings",
	    "minecraft:netherite_boots",
	    "minecraft:diamond_helmet",
	    "minecraft:diamond_chestplate",
	    "minecraft:diamond_leggings",
	    "minecraft:diamond_boots",
        "minecraft:iron_helmet",
	    "minecraft:iron_chestplate",
	    "minecraft:iron_leggings",
	    "minecraft:iron_boots"
    ]


    changeArmorFunction = []

    #if len(itemList) > len(numList)/3: raise ValueError('You dont have enough numbers in your list')
    #elif len(itemList) < len(numList)/3: raise ValueError('You have too many numbers in your list')

    for i in range(len(itemList)):


        #armorValue, kbResValue, armorToughnessValue = '', '', ''
        #armorValue = input(f'Set a generic armor value for {itemList[i]}: ')
        #kbResValue = input(f'Set a generic kb resistance value for {itemList[i]}: ')
        #armorToughnessValue = input(f'Set a generic toughness value for {itemList[i]}: ')
        #print('\n')


        armorValue = numList[numIndex]
        numIndex += 1
        armorToughnessValue = numList[numIndex]
        numIndex += 1
        kbResValue = numList[numIndex]
        numIndex += 1

        print(f'armor of {itemList[i]} = {armorValue}')
        print(f'Toughness of {itemList[i]} = {armorToughnessValue}')
        print(f'Kb Res of {itemList[i]} = {kbResValue}\n')



        if 'helmet' in itemList[i]: function = 'changeArmorHead'
        elif 'chestplate' in itemList[i]: function = 'changeArmorChest'
        elif 'leggings' in itemList[i]: function = 'changeArmorLegs'
        elif 'boots' in itemList[i]: function = 'changeArmorFeet'


        changeArmorFunction.append(f'{function}(<item:{itemList[i]}>, {armorValue}, {armorToughnessValue}, {kbResValue});')


    print('function changeArmorHead(item as IItemStack, armor as double, toughness as double, resistance as double) as void {\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor>, AttributeModifier.create(<resource:minecraft:armor.helmet>, armor, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:head>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.knockback_resistance>, AttributeModifier.create(<resource:minecraft:armor.helmet>, resistance, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:head>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor_toughness>, AttributeModifier.create(<resource:minecraft:armor.helmet>, toughness, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:head>);\n}')
    print('function changeArmorChest(item as IItemStack, armor as double, toughness as double, resistance as double) as void {\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor>, AttributeModifier.create(<resource:minecraft:armor.helmet>, armor, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:chest>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.knockback_resistance>, AttributeModifier.create(<resource:minecraft:armor.helmet>, resistance, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:chest>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor_toughness>, AttributeModifier.create(<resource:minecraft:armor.helmet>, toughness, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:chest>);\n}')
    print('function changeArmorLegs(item as IItemStack, armor as double, toughness as double, resistance as double) as void {\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor>, AttributeModifier.create(<resource:minecraft:armor.helmet>, armor, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:legs>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.knockback_resistance>, AttributeModifier.create(<resource:minecraft:armor.helmet>, resistance, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:legs>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor_toughness>, AttributeModifier.create(<resource:minecraft:armor.helmet>, toughness, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:legs>);\n}')
    print('function changeArmorFeet(item as IItemStack, armor as double, toughness as double, resistance as double) as void {\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor>, AttributeModifier.create(<resource:minecraft:armor.helmet>, armor, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:feet>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.knockback_resistance>, AttributeModifier.create(<resource:minecraft:armor.helmet>, resistance, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:feet>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor_toughness>, AttributeModifier.create(<resource:minecraft:armor.helmet>, toughness, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:feet>);\n}\n')
    for i in range(len(changeArmorFunction)): print(changeArmorFunction[i])

    count = 0
    for i in range(len(itemList)):
        print(f"{count}, #{itemList[i]} == armor")
        count += 1
        print(f"{count}, #{itemList[i]} == toughness")
        count += 1
        print(f"{count}, #{itemList[i]} == kb res")
        count += 1


if __name__ == '__main__':
    main()
"""

nameList = [
    'Exploration Mods',
    'Antique Atlas 4',
    'Distant Horizons',
    'Bobby',
    'Chunky',
    'Hold That Chunk',
    'Concurrent Chunk Management Engine',
    'Nvidium',
    'Ambient Environment',

    'Optimization Mods',
    'Sodium',
    'Indium',
    'Iris Shaders (please note: shaders will prevent ship cannons from appearing!)',
    'Ferrite Core',
    'Lithium',
    'Entity Culling',
    'Modern Fix',
    'Dynamic FPS',
    'Memory Leak Fix',
    'More Culling',
    'Krypton',
    'Enhanced Block Entities (please note: this breaks Decorated Pots shaking animation!)',
    'Very Many Players',
    'BadOptimizations',
    "Reese's Sodium Options",
    'CullLeaves',
    'AuthMe',
    'FPS Reducer',

    'Customization Mods',
    'Entity Model Features [EMF]',
    'Entity Texture Features [ETF]',
    'Not Enough Animations',
    'Continuity',
    '3D Skin Layers',
    'Sound Physics Remastered',
    'Presence Footsteps',
    'Falling Leaves',
    'FabricSkyboxes',
    'AmbientSounds',
    'Visuality',
    'Essentials Mod',
    'Capes',
    'Wavey Capes',
    'Eating Animation',
    'Dynamic Crosshair',
    'Cherished Worlds',
    'Item Highlighter',
    'Physics Mod',
    'Make Bubbles Pop',
    'Cave Dust',
    'Blur+',
    'Advancement Plaques',
    'Show Me Your Skin!',
    'Legendary Tooltips',
    'First-person Model',
    'Wakes',
    'Resourcify',
    'Detail Armor Bar (please note: this has not been tested yet and may break some of the new armor!)',
    "YDM's Weapon Master",
    'Explosive Enhancement',
    'Status Effect Bars',
    'Item Borders',
    'Better Clouds',
    'Chunks fade in',
    'ToolTipFix',
    'TalkBubbles',
    'Voice Chat Soundboard',
    'WaterPlayer',
    'JEI',
    'REI',
    'EMI (most recommended)',

    'Helpful Mods',
    'Enchantment Descriptions',
    'Controlling',
    'Inventory Profiles Next',
    'Mouse Tweaks',
    'Chat Heads',
    'More Chat History',
    'Better Mount HUD',
    'Controlify',
    'Better Third Person',
    'Better Ping Display [Fabric]',
    'InvMove',
    'Jade (recommended over WTHIT)',
    'WTHIT',
    'Craftify',
    'Highlight',
    'Cubes Without Borders',
    'MidnightControls',
    'Enhanced Attack Indicator',
    'Pick Up Notifier',
    'Shoulder Surfing Reloaded',
    'Accurate Block Placement Reborn',

]

linkList = [
    '',
    https://modrinth.com/mod/antique-atlas-4/versions
    https://modrinth.com/mod/distanthorizons/versions
    https://modrinth.com/mod/bobby/versions?c=release
    https://modrinth.com/plugin/chunky/versions
    https://modrinth.com/mod/hold-that-chunk/versions
    https://modrinth.com/mod/c2me-fabric/versions
    https://modrinth.com/mod/nvidium/versions
    https://modrinth.com/mod/ambient-environment/versions
    '',
    https://modrinth.com/mod/sodium/versions
    https://modrinth.com/mod/indium/versions
    https://modrinth.com/mod/iris/versions
    https://modrinth.com/mod/ferrite-core/versions
    https://modrinth.com/mod/lithium/versions
    https://modrinth.com/mod/entityculling/versions
    
]