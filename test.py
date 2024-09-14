def main():
    itemList = [
        "knightquest:apple_helmet",
        "knightquest:apple_chestplate",
        "knightquest:apple_leggings",
        "knightquest:apple_boots"]
    """
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
        "knightquest:shield_helmet",
        "knightquest:shield_chestplate",
        "knightquest:shield_leggings",
        "knightquest:shield_boots",
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
        "knightquest:polar_helmet",
        "knightquest:polar_chestplate",
        "knightquest:polar_leggings",
        "knightquest:polar_boots",
        "knightquest:shinobi_helmet",
        "knightquest:shinobi_chestplate",
        "knightquest:shinobi_leggings",
        "knightquest:shinobi_boots",
        "knightquest:skulk_helmet",
        "knightquest:skulk2_helmet",
        "knightquest:skulk3_helmet",
        "knightquest:skulk4_helmet"
    """

    finalOutput, changeArmorFunction = [],[]


    for i in range(len(itemList)):

        armorValue, kbResValue, armorToughnessValue = '', '', ''
        armorValue = input(f'Set a generic armor value for {itemList[i]}: ')
        kbResValue = input(f'Set a generic kb resistance value for {itemList[i]}: ')
        armorToughnessValue = input(f'Set a generic toughness value for {itemList[i]}: ')
        print('\n')

        if 'helmet' in itemList[i]: armorSlot, uuid = 'head', '2ad3f246-fee1-4e67-b886-69fd380bb150'
        elif 'chestplate' in itemList[i]: armorSlot, uuid = 'chest', '9f3d476d-c118-4544-8365-64846904b48e'
        elif 'leggings' in itemList[i]: armorSlot, uuid = 'legs', 'd8499b04-0e66-4726-ab29-64469d734e0d'
        elif 'boots' in itemList[i]: armorSlot, uuid = 'feet', '845db27c-c624-495f-8c9f-6020a9a58b6b'

        finalOutput.append(f'item.definition.addAttributeModifier(<attribute:minecraft:generic.armor>, AttributeModifier.create(<resource:{itemList[i]}>, {armorValue}, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:{armorSlot}>);\nitem.definition.addAttributeModifier(<attribute:minecraft:generic.knockback_resistance>, AttributeModifier.create(<resource:{itemList[i]}>, {kbResValue}, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:{armorSlot}>);\nitem.definition.addAttributeModifier(<attribute:minecraft:generic.armor_toughness>, AttributeModifier.create(<resource:{itemList[i]}>, {armorToughnessValue}, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:{armorSlot}>);')
        changeArmorFunction.append(f'changeArmor(<item:{itemList[i]}>, {armorValue}, {armorToughnessValue}, {kbResValue});')

    finalOutput.append('}')
    for i in range(len(finalOutput)): print(finalOutput[i])
    for i in range(len(finalOutput)): print(changeArmorFunction[i])




if __name__ == '__main__':
    main()

"""
function changeArmor(item as IItemStack, armor as double, toughness as double, resistance as double) as void {
    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor>, AttributeModifier.create(<resource:minecraft:armor.helmet>, armor, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:head>);
    item.definition.addAttributeModifier(<attribute:minecraft:generic.knockback_resistance>, AttributeModifier.create(<resource:minecraft:armor.helmet>, resistance, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:head>);
    item.definition.addAttributeModifier(<attribute:minecraft:generic.armor_toughness>, AttributeModifier.create(<resource:minecraft:armor.helmet>, toughness, <constant:minecraft:attribute/operation:add_value>), <constant:minecraft:equipmentslot/group:head>);
}