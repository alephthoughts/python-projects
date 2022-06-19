import pyinputplus as pyip

items = []
breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'],
                      prompt='Which type of bread do you want?: ',
                     numbered=True)
items.append(breadType)
proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
                        prompt='Choose your protein: ',
                        numbered=True)
items.append(proteinType)
cheese = pyip.inputYesNo('Do you want cheese? ')

if cheese == 'yes':
    cheeseType =pyip.inputMenu(['cheddar', 'Swiss', 'mozarella'],
                           prompt='which cheese? ',
                           numbered=True)
    items.append(cheeseType)
sauce = pyip.inputYesNo('Do you want Mayo, Mustard, Lettuce or Tomato? ')
if sauce == 'yes':
    sauceType = pyip.inputMenu(['Mayo', 'Mustard', 'Lettuce', 'Tomato'],
                         prompt='Choose ',
                         numbered=True)
    items.append(sauceType)
numOfSandwiches = pyip.inputInt('How many sandwiches you want? ', min=1)

totalCost = 0
itemCost = {'wheat': 2, 'white': 1, 'sourdough':3,
            'chicken': 4, 'turkey': 8, 'ham': 2, 'tofu': 1,
            'cheddar': 2, 'Swiss': 6, 'mozzarella': 4,
            'Mayo': 2, 'Mustard' : 4, 'Lettuce': 6, 'Tomato': 1}

for item in items:
        totalCost += itemCost.get(item)
print(f'Your bill: ${numOfSandwiches * totalCost}')
