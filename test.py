def main():
    numIndex = 0
    numList = [
        1,
        2,
        3,
        4,
        5,
        6
    ]

    itemList = [
        "knightquest:bamboo_blue_helmet",
        "knightquest:bamboo_blue_chestplate"]
    """
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
        "knightquest:path_helmet",
        "knightquest:path_chestplate",
        "knightquest:path_leggings",
        "knightquest:path_boots",
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
    """


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
        kbResValue = numList[numIndex]
        numIndex += 1
        armorToughnessValue = numList[numIndex]
        numIndex += 1
        print(f'armor of {itemList[i]} = {armorValue}')
        print(f'Kb Res of {itemList[i]} = {kbResValue}')
        print(f'Toughness of {itemList[i]} = {armorToughnessValue}')



        if 'helmet' in itemList[i]: function = 'changeArmorHead'
        elif 'chestplate' in itemList[i]: function = 'changeArmorChest'
        elif 'leggings' in itemList[i]: function = 'changeArmorLegs'
        elif 'boots' in itemList[i]: function = 'changeArmorFeet'


        changeArmorFunction.append(f'{function}(<item:{itemList[i]}>, {armorValue}, {armorToughnessValue}, {kbResValue});')


    print('function changeArmorHead(item as IItemStack, armor as double, toughness as double, resistance as double) as void {\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor>, AttributeModifier.create(<resource:minecraft:armor.helmet>, armor, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:head>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.knockback_resistance>, AttributeModifier.create(<resource:minecraft:armor.helmet>, resistance, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:head>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor_toughness>, AttributeModifier.create(<resource:minecraft:armor.helmet>, toughness, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:head>);\n}')
    print('function changeArmorChest(item as IItemStack, armor as double, toughness as double, resistance as double) as void {\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor>, AttributeModifier.create(<resource:minecraft:armor.helmet>, armor, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:chest>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.knockback_resistance>, AttributeModifier.create(<resource:minecraft:armor.helmet>, resistance, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:chest>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor_toughness>, AttributeModifier.create(<resource:minecraft:armor.helmet>, toughness, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:chest>);\n}')
    print('function changeArmorLegs(item as IItemStack, armor as double, toughness as double, resistance as double) as void {\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor>, AttributeModifier.create(<resource:minecraft:armor.helmet>, armor, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:legs>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.knockback_resistance>, AttributeModifier.create(<resource:minecraft:armor.helmet>, resistance, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:legs>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor_toughness>, AttributeModifier.create(<resource:minecraft:armor.helmet>, toughness, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:legs>);\n}')
    print('function changeArmorFeet(item as IItemStack, armor as double, toughness as double, resistance as double) as void {\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor>, AttributeModifier.create(<resource:minecraft:armor.helmet>, armor, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:feet>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.knockback_resistance>, AttributeModifier.create(<resource:minecraft:armor.helmet>, resistance, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:feet>);\n    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor_toughness>, AttributeModifier.create(<resource:minecraft:armor.helmet>, toughness, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:feet>);\n}')
    for i in range(len(changeArmorFunction)): print(changeArmorFunction[i])




if __name__ == '__main__':
    main()
