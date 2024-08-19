size1 = '톨'
size2 = '그란데'
size3 = '벤티'

sizes = ['톨', '그란데', '벤티']
volumes = [354, 473, 591]
shots = [2, 3, 4]

data = [sizes, volumes, shots]

#    사이즈, 용량, 샷
톨 = ['톨', 354, 2]
그란데 = ['그란데', 473, 3]
벤티 = ['벤티', 591, 4]

tall = {
    'size' : '톨',
    'volume' : 354,
    'shot' : 2
}
grande = {
    'size' : '그란데',
    'volume' : 473,
    'shot' : 3
}
venti = {
    'size' : '벤티',
    'volume' : 591,
    'shot' : 3
}

# 당도
# volume / shot
# shot / volume

# # tall
# volume = tall['volume']
# shot = tall['shot']

# volume_per_shot = volume / shot

# shot_per_volume = shot / volume
# print('volume_per_shot', volume_per_shot)
# print('shot_per_volume', shot_per_volume)

# # grande
# volume = grande['volume']
# shot = grande['shot']

# volume_per_shot = volume / shot

# shot_per_volume = shot / volume
# print('volume_per_shot', volume_per_shot)
# print('shot_per_volume', shot_per_volume)

# grande
for drink in [tall, grande, venti]:
    size = drink['size']
    volume = drink['volume']
    shot = drink['shot']

    volume_per_shot = volume / shot

    shot_per_volume = shot / volume * 1000
    print(size)
    print('volume_per_shot', volume_per_shot)
    print('shot_per_volume', shot_per_volume)
    print()

    drink['volume_per_shot'] = volume_per_shot
    drink['shot_per_volume'] = shot_per_volume

print(tall)


print(tall['shot_per_volume'] < venti['shot_per_volume'])

