def main():
    itemList = [
        'netherite_helmet',
        'netherite_chestplate',
        'netherite_leggings',
        'netherite_boots',
    ]
    finalOutput = []


    for i in range(len(itemList)):

        armorValue = input(f'Set a armor value for {itemList[i]}: ')
        if 'helmet' in itemList[i]: armorSlot, uuid = 'head', '2ad3f246-fee1-4e67-b886-69fd380bb150'
        elif 'chestplate' in itemList[i]: armorSlot, uuid = 'chest', '9f3d476d-c118-4544-8365-64846904b48e'
        elif 'leggings' in itemList[i]: armorSlot, uuid = 'legs', 'd8499b04-0e66-4726-ab29-64469d734e0d'
        elif 'boots' in itemList[i]: armorSlot, uuid = 'feet', '845db27c-c624-495f-8c9f-6020a9a58b6b'

        finalOutput.append(f'<item:minecraft:{itemList[i]}>.anyDamage().addGlobalAttributeModifier(<attribute:minecraft:generic.armor>, "{uuid}", "New Armor", {armorValue}, AttributeOperation.ADDITION, [<constant:minecraft:equipmentslot:{armorSlot}>]);')

    for i in range(len(finalOutput)): print(finalOutput[i])



if __name__ == '__main__':
    main()