import csv

viewports = {}
screens = {}
total = 0

with open('data.csv', 'rb') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        total += 1
        viewport = (int(row[1]), int(row[2]))
        screen = row[0].split('x')
        if len(screen) != 2:
            # Malformed screen size - ignore.
            continue
        screen = (int(screen[0]), int(screen[1]))
        count = screens.get(screen, 0)
        count += 1
        screens[screen] = count
        count = viewports.get(viewport, 0)
        count += 1
        viewports[viewport] = count
