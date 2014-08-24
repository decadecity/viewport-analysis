import data

unique_screens = 0
unique_viewports = 0

for count in data.screens.values():
    if count == 1:
        unique_screens += 1
for count in data.viewports.values():
    if count == 1:
        unique_viewports += 1

print('Number of visits: %s' % (data.total))
print('Number of discrete screens: %s' % (len(data.screens)))
percentage = unique_screens / float(data.total) * 100
print('Percentage with unique screen: %s' % (percentage))
percentage = unique_viewports / float(data.total) * 100
print('Number of discrete viewports: %s' % (len(data.viewports)))
print('Percentage with unique viewport: %s' % (percentage))
