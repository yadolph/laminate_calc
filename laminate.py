

class bcolors:
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'


def check_line(line):
    for element in line:
        if element <= 50:
            return 1
        if element <= 100:
            return 2
        else:
            continue
    return 0


room_xy = input('Размер комнаты (5590x3060): ') or '5590x3060'
room_xy_list = room_xy.split('x')
room_x, room_y = int(room_xy_list[0]), int(room_xy_list[1])

plank_xy = input('Размер доски (1380х193): ') or '1380x193'
plank_xy_list = plank_xy.split('x')
plank_x, plank_y = int(plank_xy_list[0]), int(plank_xy_list[1])

trim = int(input('Подрезка первой доски (100 мм): ') or 100)
step = int(input(f'Шаг смещения ряда (630 мм) (Для половины введите {int(plank_x / 2)}): ') or 630)

first_line = [plank_x - trim, ]
while sum(first_line) < room_x:
    if room_x - sum(first_line) >= plank_x:
        first_line.append(plank_x)
    else:
        first_line.append(room_x-sum(first_line))

lines = []
lines.append(first_line)

while len(lines)*plank_y < room_y:
    new_line = []
    new_line.append(lines[-1][0] + step)
    if new_line[0] > plank_x:
        new_line[0] -= plank_x
    while sum(new_line) < room_x:
        if room_x - sum(new_line) >= plank_x:
            new_line.append(plank_x)
        else:
            new_line.append(room_x-sum(new_line))
    lines.append(new_line)

for line in lines:
    if len(line) > 5:
        print(f'{bcolors.red}{line}{bcolors.end}')
    else:
        if check_line(line) == 1:
            print(f'{bcolors.red}{line}{bcolors.end}')
        elif check_line(line) == 2:
            print(f'{bcolors.yellow}{line}{bcolors.end}')
        else:
            print(line)
