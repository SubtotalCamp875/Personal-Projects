def main():
    numIndex = 0
    numList = [
        0, #knightquest:bamboo_blue_helmet == armor
        1, #knightquest:bamboo_blue_helmet == toughness
        2, #knightquest:bamboo_blue_helmet == kb res
        3, #knightquest:bamboo_blue_chestplate == armor
        4, #knightquest:bamboo_blue_chestplate == toughness
        5, #knightquest:bamboo_blue_chestplate == kb res
        6, #knightquest:bamboo_blue_leggings == armor
        7, #knightquest:bamboo_blue_leggings == toughness
        8, #knightquest:bamboo_blue_leggings == kb res
        9, #knightquest:bamboo_blue_boots == armor
        10, #knightquest:bamboo_blue_boots == toughness
        11, #knightquest:bamboo_blue_boots == kb res
        12, #knightquest:bamboo_green_helmet == armor
        13, #knightquest:bamboo_green_helmet == toughness
        14, #knightquest:bamboo_green_helmet == kb res
        15, #knightquest:bamboo_green_chestplate == armor
        16, #knightquest:bamboo_green_chestplate == toughness
        17, #knightquest:bamboo_green_chestplate == kb res
        18, #knightquest:bamboo_green_leggings == armor
        19, #knightquest:bamboo_green_leggings == toughness
        20, #knightquest:bamboo_green_leggings == kb res
        21, #knightquest:bamboo_green_boots == armor
        22, #knightquest:bamboo_green_boots == toughness
        23, #knightquest:bamboo_green_boots == kb res
        24, #knightquest:bamboo_helmet == armor
        25, #knightquest:bamboo_helmet == toughness
        26, #knightquest:bamboo_helmet == kb res
        27, #knightquest:bamboo_chestplate == armor
        28, #knightquest:bamboo_chestplate == toughness
        29, #knightquest:bamboo_chestplate == kb res
        30, #knightquest:bamboo_leggings == armor
        31, #knightquest:bamboo_leggings == toughness
        32, #knightquest:bamboo_leggings == kb res
        33, #knightquest:bamboo_boots == armor
        34, #knightquest:bamboo_boots == toughness
        35, #knightquest:bamboo_boots == kb res
        36, #knightquest:bat_helmet == armor
        37, #knightquest:bat_helmet == toughness
        38, #knightquest:bat_helmet == kb res
        39, #knightquest:bat_chestplate == armor
        40, #knightquest:bat_chestplate == toughness
        41, #knightquest:bat_chestplate == kb res
        42, #knightquest:bat_leggings == armor
        43, #knightquest:bat_leggings == toughness
        44, #knightquest:bat_leggings == kb res
        45, #knightquest:bat_boots == armor
        46, #knightquest:bat_boots == toughness
        47, #knightquest:bat_boots == kb res
        48, #knightquest:blaze_chestplate == armor
        49, #knightquest:blaze_chestplate == toughness
        50, #knightquest:blaze_chestplate == kb res
        51, #knightquest:blaze_leggings == armor
        52, #knightquest:blaze_leggings == toughness
        53, #knightquest:blaze_leggings == kb res
        54, #knightquest:blaze_boots == armor
        55, #knightquest:blaze_boots == toughness
        56, #knightquest:blaze_boots == kb res
        57, #knightquest:bow_helmet == armor
        58, #knightquest:bow_helmet == toughness
        59, #knightquest:bow_helmet == kb res
        60, #knightquest:bow_chestplate == armor
        61, #knightquest:bow_chestplate == toughness
        62, #knightquest:bow_chestplate == kb res
        63, #knightquest:bow_leggings == armor
        64, #knightquest:bow_leggings == toughness
        65, #knightquest:bow_leggings == kb res
        66, #knightquest:bow_boots == armor
        67, #knightquest:bow_boots == toughness
        68, #knightquest:bow_boots == kb res
        69, #knightquest:horn_helmet == armor
        70, #knightquest:horn_helmet == toughness
        71, #knightquest:horn_helmet == kb res
        72, #knightquest:horn_chestplate == armor
        73, #knightquest:horn_chestplate == toughness
        74, #knightquest:horn_chestplate == kb res
        75, #knightquest:horn_leggings == armor
        76, #knightquest:horn_leggings == toughness
        77, #knightquest:horn_leggings == kb res
        78, #knightquest:horn_boots == armor
        79, #knightquest:horn_boots == toughness
        80, #knightquest:horn_boots == kb res
        81, #knightquest:creeper_helmet == armor
        82, #knightquest:creeper_helmet == toughness
        83, #knightquest:creeper_helmet == kb res
        84, #knightquest:creeper_chestplate == armor
        85, #knightquest:creeper_chestplate == toughness
        86, #knightquest:creeper_chestplate == kb res
        87, #knightquest:creeper_leggings == armor
        88, #knightquest:creeper_leggings == toughness
        89, #knightquest:creeper_leggings == kb res
        90, #knightquest:creeper_boots == armor
        91, #knightquest:creeper_boots == toughness
        92, #knightquest:creeper_boots == kb res
        93, #knightquest:deepslate_helmet == armor
        94, #knightquest:deepslate_helmet == toughness
        95, #knightquest:deepslate_helmet == kb res
        96, #knightquest:deepslate_chestplate == armor
        97, #knightquest:deepslate_chestplate == toughness
        98, #knightquest:deepslate_chestplate == kb res
        99, #knightquest:deepslate_leggings == armor
        100, #knightquest:deepslate_leggings == toughness
        101, #knightquest:deepslate_leggings == kb res
        102, #knightquest:deepslate_boots == armor
        103, #knightquest:deepslate_boots == toughness
        104, #knightquest:deepslate_boots == kb res
        105, #knightquest:evoker_helmet == armor
        106, #knightquest:evoker_helmet == toughness
        107, #knightquest:evoker_helmet == kb res
        108, #knightquest:evoker_chestplate == armor
        109, #knightquest:evoker_chestplate == toughness
        110, #knightquest:evoker_chestplate == kb res
        111, #knightquest:evoker_leggings == armor
        112, #knightquest:evoker_leggings == toughness
        113, #knightquest:evoker_leggings == kb res
        114, #knightquest:evoker_boots == armor
        115, #knightquest:evoker_boots == toughness
        116, #knightquest:evoker_boots == kb res
        117, #knightquest:forze_helmet == armor
        118, #knightquest:forze_helmet == toughness
        119, #knightquest:forze_helmet == kb res
        120, #knightquest:forze_chestplate == armor
        121, #knightquest:forze_chestplate == toughness
        122, #knightquest:forze_chestplate == kb res
        123, #knightquest:forze_leggings == armor
        124, #knightquest:forze_leggings == toughness
        125, #knightquest:forze_leggings == kb res
        126, #knightquest:forze_boots == armor
        127, #knightquest:forze_boots == toughness
        128, #knightquest:forze_boots == kb res
        129, #knightquest:hollow_helmet == armor
        130, #knightquest:hollow_helmet == toughness
        131, #knightquest:hollow_helmet == kb res
        132, #knightquest:hollow_chestplate == armor
        133, #knightquest:hollow_chestplate == toughness
        134, #knightquest:hollow_chestplate == kb res
        135, #knightquest:hollow_leggings == armor
        136, #knightquest:hollow_leggings == toughness
        137, #knightquest:hollow_leggings == kb res
        138, #knightquest:hollow_boots == armor
        139, #knightquest:hollow_boots == toughness
        140, #knightquest:hollow_boots == kb res
        141, #knightquest:nether_helmet == armor
        142, #knightquest:nether_helmet == toughness
        143, #knightquest:nether_helmet == kb res
        144, #knightquest:nether_chestplate == armor
        145, #knightquest:nether_chestplate == toughness
        146, #knightquest:nether_chestplate == kb res
        147, #knightquest:nether_leggings == armor
        148, #knightquest:nether_leggings == toughness
        149, #knightquest:nether_leggings == kb res
        150, #knightquest:nether_boots == armor
        151, #knightquest:nether_boots == toughness
        152, #knightquest:nether_boots == kb res
        153, #knightquest:veteran_helmet == armor
        154, #knightquest:veteran_helmet == toughness
        155, #knightquest:veteran_helmet == kb res
        156, #knightquest:veteran_chestplate == armor
        157, #knightquest:veteran_chestplate == toughness
        158, #knightquest:veteran_chestplate == kb res
        159, #knightquest:veteran_leggings == armor
        160, #knightquest:veteran_leggings == toughness
        161, #knightquest:veteran_leggings == kb res
        162, #knightquest:veteran_boots == armor
        163, #knightquest:veteran_boots == toughness
        164, #knightquest:veteran_boots == kb res
        165, #knightquest:phantom_helmet == armor
        166, #knightquest:phantom_helmet == toughness
        167, #knightquest:phantom_helmet == kb res
        168, #knightquest:phantom_chestplate == armor
        169, #knightquest:phantom_chestplate == toughness
        170, #knightquest:phantom_chestplate == kb res
        171, #knightquest:phantom_leggings == armor
        172, #knightquest:phantom_leggings == toughness
        173, #knightquest:phantom_leggings == kb res
        174, #knightquest:phantom_boots == armor
        175, #knightquest:phantom_boots == toughness
        176, #knightquest:phantom_boots == kb res
        177, #knightquest:sea_helmet == armor
        178, #knightquest:sea_helmet == toughness
        179, #knightquest:sea_helmet == kb res
        180, #knightquest:sea_chestplate == armor
        181, #knightquest:sea_chestplate == toughness
        182, #knightquest:sea_chestplate == kb res
        183, #knightquest:sea_leggings == armor
        184, #knightquest:sea_leggings == toughness
        185, #knightquest:sea_leggings == kb res
        186, #knightquest:sea_boots == armor
        187, #knightquest:sea_boots == toughness
        188, #knightquest:sea_boots == kb res
        189, #knightquest:silver_helmet == armor
        190, #knightquest:silver_helmet == toughness
        191, #knightquest:silver_helmet == kb res
        192, #knightquest:silver_chestplate == armor
        193, #knightquest:silver_chestplate == toughness
        194, #knightquest:silver_chestplate == kb res
        195, #knightquest:silver_leggings == armor
        196, #knightquest:silver_leggings == toughness
        197, #knightquest:silver_leggings == kb res
        198, #knightquest:silver_boots == armor
        199, #knightquest:silver_boots == toughness
        200, #knightquest:silver_boots == kb res
        201, #knightquest:silverfish_helmet == armor
        202, #knightquest:silverfish_helmet == toughness
        203, #knightquest:silverfish_helmet == kb res
        204, #knightquest:silverfish_chestplate == armor
        205, #knightquest:silverfish_chestplate == toughness
        206, #knightquest:silverfish_chestplate == kb res
        207, #knightquest:silverfish_leggings == armor
        208, #knightquest:silverfish_leggings == toughness
        209, #knightquest:silverfish_leggings == kb res
        210, #knightquest:silverfish_boots == armor
        211, #knightquest:silverfish_boots == toughness
        212, #knightquest:silverfish_boots == kb res
        213, #knightquest:skeleton_helmet == armor
        214, #knightquest:skeleton_helmet == toughness
        215, #knightquest:skeleton_helmet == kb res
        216, #knightquest:skeleton_chestplate == armor
        217, #knightquest:skeleton_chestplate == toughness
        218, #knightquest:skeleton_chestplate == kb res
        219, #knightquest:skeleton_leggings == armor
        220, #knightquest:skeleton_leggings == toughness
        221, #knightquest:skeleton_leggings == kb res
        222, #knightquest:skeleton_boots == armor
        223, #knightquest:skeleton_boots == toughness
        224, #knightquest:skeleton_boots == kb res
        225, #knightquest:spider_helmet == armor
        226, #knightquest:spider_helmet == toughness
        227, #knightquest:spider_helmet == kb res
        228, #knightquest:spider_chestplate == armor
        229, #knightquest:spider_chestplate == toughness
        230, #knightquest:spider_chestplate == kb res
        231, #knightquest:spider_leggings == armor
        232, #knightquest:spider_leggings == toughness
        233, #knightquest:spider_leggings == kb res
        234, #knightquest:spider_boots == armor
        235, #knightquest:spider_boots == toughness
        236, #knightquest:spider_boots == kb res
        237, #knightquest:warlord_helmet == armor
        238, #knightquest:warlord_helmet == toughness
        239, #knightquest:warlord_helmet == kb res
        240, #knightquest:warlord_chestplate == armor
        241, #knightquest:warlord_chestplate == toughness
        242, #knightquest:warlord_chestplate == kb res
        243, #knightquest:warlord_leggings == armor
        244, #knightquest:warlord_leggings == toughness
        245, #knightquest:warlord_leggings == kb res
        246, #knightquest:warlord_helmet == armor
        247, #knightquest:warlord_helmet == toughness
        248, #knightquest:warlord_helmet == kb res
        249, #knightquest:strawhat_helmet == armor
        250, #knightquest:strawhat_helmet == toughness
        251, #knightquest:strawhat_helmet == kb res
        252, #knightquest:strawhat_chestplate == armor
        253, #knightquest:strawhat_chestplate == toughness
        254, #knightquest:strawhat_chestplate == kb res
        255, #knightquest:strawhat_leggings == armor
        256, #knightquest:strawhat_leggings == toughness
        257, #knightquest:strawhat_leggings == kb res
        258, #knightquest:strawhat_boots == armor
        259, #knightquest:strawhat_boots == toughness
        260, #knightquest:strawhat_boots == kb res
        261, #knightquest:pirate_helmet == armor
        262, #knightquest:pirate_helmet == toughness
        263, #knightquest:pirate_helmet == kb res
        264, #knightquest:pirate2_helmet == armor
        265, #knightquest:pirate2_helmet == toughness
        266, #knightquest:pirate2_helmet == kb res
        267, #knightquest:pirate3_helmet == armor
        268, #knightquest:pirate3_helmet == toughness
        269, #knightquest:pirate3_helmet == kb res
        270, #knightquest:pirate_chestplate == armor
        271, #knightquest:pirate_chestplate == toughness
        272, #knightquest:pirate_chestplate == kb res
        273, #knightquest:pirate_leggings == armor
        274, #knightquest:pirate_leggings == toughness
        275, #knightquest:pirate_leggings == kb res
        276, #knightquest:pirate_boots == armor
        277, #knightquest:pirate_boots == toughness
        278, #knightquest:pirate_boots == kb res
        279, #knightquest:conquistador_helmet == armor
        280, #knightquest:conquistador_helmet == toughness
        281, #knightquest:conquistador_helmet == kb res
        282, #knightquest:conquistador2_helmet == armor
        283, #knightquest:conquistador2_helmet == toughness
        284, #knightquest:conquistador2_helmet == kb res
        285, #knightquest:conquistador3_helmet == armor
        286, #knightquest:conquistador3_helmet == toughness
        287, #knightquest:conquistador3_helmet == kb res
        288, #knightquest:conquistador_chestplate == armor
        289, #knightquest:conquistador_chestplate == toughness
        290, #knightquest:conquistador_chestplate == kb res
        291, #knightquest:conquistador_leggings == armor
        292, #knightquest:conquistador_leggings == toughness
        293, #knightquest:conquistador_leggings == kb res
        294, #knightquest:conquistador_boots == armor
        295, #knightquest:conquistador_boots == toughness
        296, #knightquest:conquistador_boots == kb res
        297, #knightquest:zombie_helmet == armor
        298, #knightquest:zombie_helmet == toughness
        299, #knightquest:zombie_helmet == kb res
        300, #knightquest:zombie2_helmet == armor
        301, #knightquest:zombie2_helmet == toughness
        302, #knightquest:zombie2_helmet == kb res
        303, #knightquest:zombie_chestplate == armor
        304, #knightquest:zombie_chestplate == toughness
        305, #knightquest:zombie_chestplate == kb res
        306, #knightquest:zombie_leggings == armor
        307, #knightquest:zombie_leggings == toughness
        308, #knightquest:zombie_leggings == kb res
        309, #knightquest:zombie_boots == armor
        310, #knightquest:zombie_boots == toughness
        311, #knightquest:zombie_boots == kb res
        312, #knightquest:husk_helmet == armor
        313, #knightquest:husk_helmet == toughness
        314, #knightquest:husk_helmet == kb res
        315, #knightquest:husk_helmet2 == armor
        316, #knightquest:husk_helmet2 == toughness
        317, #knightquest:husk_helmet2 == kb res
        318, #knightquest:husk_helmet3 == armor
        319, #knightquest:husk_helmet3 == toughness
        320, #knightquest:husk_helmet3 == kb res
        321, #knightquest:husk_chestplate == armor
        322, #knightquest:husk_chestplate == toughness
        323, #knightquest:husk_chestplate == kb res
        324, #knightquest:husk_leggings == armor
        325, #knightquest:husk_leggings == toughness
        326, #knightquest:husk_leggings == kb res
        327, #knightquest:husk_boots == armor
        328, #knightquest:husk_boots == toughness
        329, #knightquest:husk_boots == kb res
        330, #knightquest:squire_helmet == armor
        331, #knightquest:squire_helmet == toughness
        332, #knightquest:squire_helmet == kb res
        333, #knightquest:squire_chestplate == armor
        334, #knightquest:squire_chestplate == toughness
        335, #knightquest:squire_chestplate == kb res
        336, #knightquest:squire_leggings == armor
        337, #knightquest:squire_leggings == toughness
        338, #knightquest:squire_leggings == kb res
        339, #knightquest:squire_boots == armor
        340, #knightquest:squire_boots == toughness
        341, #knightquest:squire_boots == kb res
        342, #knightquest:witch_helmet == armor
        343, #knightquest:witch_helmet == toughness
        344, #knightquest:witch_helmet == kb res
        345, #knightquest:witch_chestplate == armor
        346, #knightquest:witch_chestplate == toughness
        347, #knightquest:witch_chestplate == kb res
        348, #knightquest:witch_leggings == armor
        349, #knightquest:witch_leggings == toughness
        350, #knightquest:witch_leggings == kb res
        351, #knightquest:witch_boots == armor
        352, #knightquest:witch_boots == toughness
        353, #knightquest:witch_boots == kb res
        354, #knightquest:shinobi_helmet == armor
        355, #knightquest:shinobi_helmet == toughness
        356, #knightquest:shinobi_helmet == kb res
        357, #knightquest:shinobi_chestplate == armor
        358, #knightquest:shinobi_chestplate == toughness
        359, #knightquest:shinobi_chestplate == kb res
        360, #knightquest:shinobi_leggings == armor
        361, #knightquest:shinobi_leggings == toughness
        362, #knightquest:shinobi_leggings == kb res
        363, #knightquest:shinobi_boots == armor
        364, #knightquest:shinobi_boots == toughness
        365, #knightquest:shinobi_boots == kb res
        366, #knightquest:skulk_helmet == armor
        367, #knightquest:skulk_helmet == toughness
        368, #knightquest:skulk_helmet == kb res
        369, #knightquest:skulk2_helmet == armor
        370, #knightquest:skulk2_helmet == toughness
        371, #knightquest:skulk2_helmet == kb res
        372, #knightquest:skulk3_helmet == armor
        373, #knightquest:skulk3_helmet == toughness
        374, #knightquest:skulk3_helmet == kb res
        375, #knightquest:skulk4_helmet == armor
        376, #knightquest:skulk4_helmet == toughness
        377, #knightquest:skulk4_helmet == kb res
        378, #archers:archer_armor_head == armor
        379, #archers:archer_armor_head == toughness
        380, #archers:archer_armor_head == kb res
        381, #archers:archer_armor_chest == armor
        382, #archers:archer_armor_chest == toughness
        383, #archers:archer_armor_chest == kb res
        384, #archers:archer_armor_legs == armor
        385, #archers:archer_armor_legs == toughness
        386, #archers:archer_armor_legs == kb res
        387, #archers:archer_armor_feet == armor
        388, #archers:archer_armor_feet == toughness
        389, #archers:archer_armor_feet == kb res
        390, #rogues:rogue_armor_head == armor
        391, #rogues:rogue_armor_head == toughness
        392, #rogues:rogue_armor_head == kb res
        393, #rogues:rogue_armor_chest == armor
        394, #rogues:rogue_armor_chest == toughness
        395, #rogues:rogue_armor_chest == kb res
        396, #rogues:rogue_armor_legs == armor
        397, #rogues:rogue_armor_legs == toughness
        398, #rogues:rogue_armor_legs == kb res
        399, #rogues:rogue_armor_feet == armor
        400, #rogues:rogue_armor_feet == toughness
        401, #rogues:rogue_armor_feet == kb res
        402, #paladins:priest_robe_head == armor
        403, #paladins:priest_robe_head == toughness
        404, #paladins:priest_robe_head == kb res
        405, #paladins:priest_robe_chest == armor
        406, #paladins:priest_robe_chest == toughness
        407, #paladins:priest_robe_chest == kb res
        408, #paladins:priest_robe_legs == armor
        409, #paladins:priest_robe_legs == toughness
        410, #paladins:priest_robe_legs == kb res
        411, #paladins:priest_robe_feet == armor
        412, #paladins:priest_robe_feet == toughness
        413, #paladins:priest_robe_feet == kb res
        414, #paladins:prior_robe_head == armor
        415, #paladins:prior_robe_head == toughness
        416, #paladins:prior_robe_head == kb res
        417, #paladins:prior_robe_chest == armor
        418, #paladins:prior_robe_chest == toughness
        419, #paladins:prior_robe_chest == kb res
        420, #paladins:prior_robe_legs == armor
        421, #paladins:prior_robe_legs == toughness
        422, #paladins:prior_robe_legs == kb res
        423, #paladins:prior_robe_feet == armor
        424, #paladins:prior_robe_feet == toughness
        425, #paladins:prior_robe_feet == kb res
        426, #paladins:paladin_armor_head == armor
        427, #paladins:paladin_armor_head == toughness
        428, #paladins:paladin_armor_head == kb res
        429, #paladins:paladin_armor_chest == armor
        430, #paladins:paladin_armor_chest == toughness
        431, #paladins:paladin_armor_chest == kb res
        432, #paladins:paladin_armor_legs == armor
        433, #paladins:paladin_armor_legs == toughness
        434, #paladins:paladin_armor_legs == kb res
        435, #paladins:paladin_armor_feet == armor
        436, #paladins:paladin_armor_feet == toughness
        437, #paladins:paladin_armor_feet == kb res
        438, #paladins:crusader_armor_head == armor
        439, #paladins:crusader_armor_head == toughness
        440, #paladins:crusader_armor_head == kb res
        441, #paladins:crusader_armor_chest == armor
        442, #paladins:crusader_armor_chest == toughness
        443, #paladins:crusader_armor_chest == kb res
        444, #paladins:crusader_armor_legs == armor
        445, #paladins:crusader_armor_legs == toughness
        446, #paladins:crusader_armor_legs == kb res
        447, #paladins:crusader_armor_feet == armor
        448, #paladins:crusader_armor_feet == toughness
        449, #paladins:crusader_armor_feet == kb res
        450, #rogues:assassin_armor_head == armor
        451, #rogues:assassin_armor_head == toughness
        452, #rogues:assassin_armor_head == kb res
        453, #rogues:assassin_armor_chest == armor
        454, #rogues:assassin_armor_chest == toughness
        455, #rogues:assassin_armor_chest == kb res
        456, #rogues:assassin_armor_legs == armor
        457, #rogues:assassin_armor_legs == toughness
        458, #rogues:assassin_armor_legs == kb res
        459, #rogues:assassin_armor_feet == armor
        460, #rogues:assassin_armor_feet == toughness
        461, #rogues:assassin_armor_feet == kb res
        462, #archers:ranger_armor_head == armor
        463, #archers:ranger_armor_head == toughness
        464, #archers:ranger_armor_head == kb res
        465, #archers:ranger_armor_chest == armor
        466, #archers:ranger_armor_chest == toughness
        467, #archers:ranger_armor_chest == kb res
        468, #archers:ranger_armor_legs == armor
        469, #archers:ranger_armor_legs == toughness
        470, #archers:ranger_armor_legs == kb res
        471, #archers:ranger_armor_feet == armor
        472, #archers:ranger_armor_feet == toughness
        473, #archers:ranger_armor_feet == kb res
        474, #rogues:warrior_armor_head == armor
        475, #rogues:warrior_armor_head == toughness
        476, #rogues:warrior_armor_head == kb res
        477, #rogues:warrior_armor_chest == armor
        478, #rogues:warrior_armor_chest == toughness
        479, #rogues:warrior_armor_chest == kb res
        480, #rogues:warrior_armor_legs == armor
        481, #rogues:warrior_armor_legs == toughness
        482, #rogues:warrior_armor_legs == kb res
        483, #rogues:warrior_armor_feet == armor
        484, #rogues:warrior_armor_feet == toughness
        485, #rogues:warrior_armor_feet == kb res
        486, #rogues:berserker_armor_head == armor
        487, #rogues:berserker_armor_head == toughness
        488, #rogues:berserker_armor_head == kb res
        489, #rogues:berserker_armor_chest == armor
        490, #rogues:berserker_armor_chest == toughness
        491, #rogues:berserker_armor_chest == kb res
        492, #rogues:berserker_armor_legs == armor
        493, #rogues:berserker_armor_legs == toughness
        494, #rogues:berserker_armor_legs == kb res
        495, #rogues:berserker_armor_feet == armor
        496, #rogues:berserker_armor_feet == toughness
        497, #rogues:berserker_armor_feet == kb res
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
        "knightquest:warlord_helmet",
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
        "rogues:berserker_armor_feet"
    ]


    changeArmorFunction = []

    if len(itemList) > len(numList)/3: raise ValueError('You dont have enough numbers in your list')
    elif len(itemList) < len(numList)/3: raise ValueError('You have too many numbers in your list')

    for i in range(len(itemList)):

        """
        armorValue, kbResValue, armorToughnessValue = '', '', ''
        armorValue = input(f'Set a generic armor value for {itemList[i]}: ')
        kbResValue = input(f'Set a generic kb resistance value for {itemList[i]}: ')
        armorToughnessValue = input(f'Set a generic toughness value for {itemList[i]}: ')
        print('\n')
        """

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
    
    '''
    count = 0
    for i in range(len(itemList)):
        print(f"{count}, #{itemList[i]} == armor")
        count += 1
        print(f"{count}, #{itemList[i]} == toughness")
        count += 1
        print(f"{count}, #{itemList[i]} == kb res")
        count += 1
    '''


if __name__ == '__main__':
    main()
