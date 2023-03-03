import requests
import config

def recipe_search(ingredient, mealType):  # function to call recipe search API
    app_id = config.app_id
    app_key = config.app_key
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}&mealType={}'.format(ingredient, app_id, app_key, mealType))
    data = result.json()
    return data['hits']


def recipe_search2(ingredient, excluded, mealType):  # function to call recipe search API with an excluded ingredient added
    app_id = config.app_id
    app_key = config.app_key
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}&excluded={}&mealType={}'.format(ingredient, app_id, app_key, excluded, mealType))
    data = result.json()
    return data['hits']


def run():  # function being run
    ingredient = input('Enter an ingredient: ')
    mealType = input('Breakfast, Lunch, Dinner or Snack?  ')
    excluded = input("Any ingredients we shouldn't include? Type N if none-  ")

    # if statement to determine if we're using the first or the second recipe function (are ingredients being excluded or not)
    if excluded == "N" or excluded == 'n':
        results = recipe_search(ingredient, mealType)
    else:
        results = recipe_search2(ingredient, excluded, mealType)

    # if stattement determining if the ingredient entered can be found in the results. It's the only way I have found to create a redundancy for now
    if ingredient in results:
     print("Here are your recipes:")
    else:
     print("Sorry, no results found!")


    for result in results:
        recipe = result['recipe']

        with open('recipes.txt',
                  'w') as recipe_file:
            print("--------------------")
            recipe_file.write("Which yummy meal will you cook today?  " + "\r\n")
            print(recipe['label'])
            recipe_file.write(recipe['label'] + "\r\n")
            print(recipe['url'])
            recipe_file.write(recipe['url'] + "\r\n")
            ingredList = recipe['ingredientLines']
            for item in ingredList:
                print(item)
                recipe_file.write(f"You will need {ingredList}")
    #converter
    convertAsk = input('Do you need a unit converter? Type y or n-  ')
    convertList = {"Cups to ml": 1, "Pounds to g": 2, "Ounces to g": 3, "Quit": "Q"}
    if convertAsk == 'y':
        for item, number in convertList.items():
            print(f"{item} - {number}")
        convertSpecify = ""
        while convertSpecify != "Q":

            convertSpecify = input("Enter the corresponding number for the converter you need.-  ")

            #cups to ml
            if convertSpecify == "1":
                cupsAmt = float(input("Enter the amount in cups-  "))
                cupsToMl = cupsAmt * 236.6
                print(f"That's {cupsToMl}ml")

            #pounds to g
            elif convertSpecify == "2":
                poundsAmt = float(input("Enter the amount in pounds-  "))
                poundsToG = poundsAmt * 453.6
                print(f"That's {poundsToG}g")
            
            #ounces to g
            elif convertSpecify == "3":
                ozAmt = float(input("Enter the amount in ounces-  "))
                ozToG = ozAmt * 28.35
                print(f"That's {ozToG}g")
            
            #quit
            elif convertSpecify == "Q" or convertSpecify == "q":
                print("Happy cooking!")

            #wrong user input
            else:
                print("Sorry, input not recognised!")
    else:
        print("Happy cooking!")


run()