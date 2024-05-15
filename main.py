import csv
import random

number = []
name = []
type1 = []
type2 = []
total = []
HP = []
Attack = []
Defense = []
SpAtk = []
SpDef = []
Speed = []
Generation = []
Legendary = []
stats = []
type = []
runtime = False
end = False
no_runtime = 0
coins = 0
rarity = 0
inventory = {
    'Sugar': 0,
    'Milk': 0,
    'Butter': 0,
    'Flour': 0,
    'Eggs': 0,
    'Margikarp': 0
}


def formatting(n):
  '''
  format in which data would be displayed
  '''
  return "{:<10}{:<32}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<12}{:<10}".format(
      number[n], name[n], type1[n], type2[n], total[n], HP[n], Attack[n],
      Defense[n], SpAtk[n], SpDef[n], Speed[n], Generation[n], Legendary[n])


def display_menu():
  '''
  displays main menu
  '''
  print("\nWelcome to Pokemon Super Search Engine!!\n")
  print("1. Display Pokemon with their types and statistics")
  print("2. Display the first Pokemon of a Type of the trainer’s choice")
  print("3. Display all Pokemons with Total Base stat of the trainer’s choice")
  print("4. Display all Pokemons with a minimum set of stats")
  print("5. Display all legendary Pokemons of a Type of the trainer’s choice")
  print("6. Quekling's Pokemon Bakery shop")
  print("0. Quit\n")


def option_1():
  '''
  displays all pokemon with their types and stats accoring to the user's choice
  '''
  display = int(input("Enter the number of Pokemons to be shown: "))
  if 0 < display < 801:
    print(formatting(0))
    r = random.sample(range(1, 801),
                      display)  #randomly select a selected number of pokemon
    r.sort()
    for num in r:
      print(formatting(num))
  elif display < 0:
    print("\nPlease enter a positive integer")
  else:
    print("\nThere are only 800 pokemons!")


def option_2():
  '''
  display the first Pokemon of a Type of the trainer’s choice
  '''
  type = input("Enter the type of Pokemon: ").capitalize()
  if type in type1 or type in type2:
    a = type1.index(type)  #finds the index of the specific type
    b = type2.index(type)
    print(formatting(0))
    if a >= 0 and b >= 0:  #when the types can be found in the list
      if a < b:  #if the first type is found first
        print(formatting(a))
      else:
        print(formatting(b))
    elif b >= 0:  #when only the second type can be found
      print(formatting(b))
    else:  #when only the first type is found
      print(formatting(a))
  else:
    print("No Pokemon of this type found")


def option_3():
  '''
  Display all Pokemons with Total Base stat of the trainer’s choice
  '''
  basestats = input('Enter Total Base stats: ')
  if basestats in total:
    indices_of_basestats = [i for i, e in enumerate(total)
                            if e == basestats]  #finds all index of basestats
    print(formatting(0))
    for index in indices_of_basestats:
      print(formatting(index))
  else:
    print("\nNo Pokemon with this base stats found.")


def option_4():
  '''
  Display all pokemon with a minimum set of stats
  '''
  min_atk = int(input('Enter min special attack stat: '))
  min_def = int(input('Enter min special defense stat: '))
  min_speed = int(input('Enter min speed stat: '))
  atk_ = [i for i, e in enumerate(SpAtk[1:]) if int(e) >= min_atk]
  def_ = [i for i, e in enumerate(SpDef[1:]) if int(e) >= min_def]
  speed_ = [i for i, e in enumerate(Speed[1:]) if int(e) >= min_speed]

  for value in atk_:  #if index intersects, it is added into the list
    if value in def_ and value in speed_:
      stats.append(value)

  if len(stats) > 0:  #if the set of stats exists
    print(formatting(0))
    for index in stats:
      print(formatting(index + 1))
  else:
    print("\nNo Pokemon with this set of stats found")


def option_5():
  '''
  Display all legendary Pokemons of a Type of the trainer’s choice
  '''
  input_type1 = input("Enter type1: ").title()
  input_type2 = input("Enter type2: ").title()
  type1_index = [i for i, e in enumerate(type1[1:]) if e == input_type1]
  type2_index = [i for i, e in enumerate(type2[1:]) if e == input_type2]

  for value in type1_index:
    value = int(value)
    if value in type2_index:  #if the pokemon is found in both type1 and type2
      type.append(value)

  if len(type) > 0:
    print(formatting(0))
    for index in type:
      index = int(index)
      print(formatting(index + 1))
    #index is x+1 since the index you start at is 1
  else:
    print("No legendary Pokemon of this type found")


#for surprise
def shop_menu6():
  global coins
  print('\nCurrent Pokecoin balance:', coins)
  print("\nWelcome to the Quekling's Pokemon Bakery shop!")
  print("(1) Recipe")
  print("(2) Owned Ingredients")
  print("(3) Purchase Ingredients")
  print("(4) Bake!")
  print("(0) Quit")


def recipe_6():
  '''
  recipe for shop_menu6()
  '''
  print("(1) Cake")
  print("(2) Fish Pie")
  try:
    to_bake = int(input('What recipe do you want to view? '))
    if to_bake == 1:
      print('''
    ----------------------------------------------
       =Cake=
      1 Butter      ' ' ' '
      1 Sugar      _| | | |_
      1 Flour     {  cakee  }
      1 Eggs      {_________}
    ----------------------------------------------
                                ''')
    elif to_bake == 2:
      print('''
    ----------------------------------------------
      =Fish Pie=
      1 Magikarp           (
      1 Butter             ) 
      1 Flour         __..---..__
      1 Milk       ,='  '  |  '  `=.
                   :--.._-------..--;
                   ` ,____________,'
    ----------------------------------------------
      ''')
    else:
      print('Invalid input')
      global runtime
      runtime = False  #to display main menu
  except ValueError:
    print('Invalid input')


def catch():
  '''
  function when a wild pokemon appears
  '''
  print('A wild Pokemon has appeared!')
  caught = random.randint(0, 3)
  try:
    catch = input('Do you want to catch it? (Y/N): ').upper()
    if catch == 'Y':
      print('(╯°□°)╯︵◓')
      if caught == 1 or caught == 2 or caught == 3:  #increasing the chances of catching the pokemon
        print('\nYou caught the pokemon!\n')
        global coins
        global rarity
        global no_runtime
        global runtime
        if rarity == 1:
          print('You earned 1 coin!\n')
          inventory['Margikarp'] += 1
          coins += 1
        elif rarity == 2:
          print('You earned 3 coins!\n')
          coins += 3
        elif rarity == 3:
          print('You earned 5 coins!\n')
          coins += 5
        no_runtime = 0
      else:
        print('OH NOO! The pokemon has run away!\n')
        no_runtime = 0
        runtime = False
    else:  #when the user doesn't want to catch the pokemon
      print('The pokemon has run away!\n')
      no_runtime = 0
      runtime = False
  except ValueError:
    print('Invalid input')


def random_pokemon6():
  '''
  function for random pokemon
  '''
  global rarity
  random_pokemon = random.randint(0, 4)
  if random_pokemon == 0:
    rarity = 2
    print('''
                      ⠸⣷⣦⠤⡀⠀⠀⠀⠀          ⠀⠀ ⠀ ⠀⢀⣀⣠⣤⠀⠀⠀
        boo!          ⠀⠙⣿⡄⠈⠑⢄⠀ ⠀pika pika⠀ ⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀
      a wild pokemon    ⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀
      has appeared!        ⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜
                      ⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇
      it's pikachu!         ⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀
                      ⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀
                      ⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀
                      ⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋
      ''')
    catch()
    no_runtime = 0  #resets condition for surprise
  elif random_pokemon == 1:
    rarity = 2
    print('''
                                 ⠀⣀⠤⠄⠒⠒⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀.⡰⠊⠁⠀⠀⠀⠀⠀⠀⠙⣆.⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           a wild pokemon     ⠀⣿⢋⠃⠀⠀⠀⠀⠀⠁⣧⣸⣧⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           has appeared!    ⠀⠀⠠⡿⢿⠀⠀⠀⠀⠀⠀⠀⣟⠛⣹⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⢠⡟⠚⠀⠀⠀⠀⠀⠀⠀⠈⠉⢀⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⡀⠀⠀
                            ⠀ ⢸⡙⢶⣤⣄⣀⣀⣀⣤⡤⠲⡿⠁⣸ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣼⠿⣿⡀⠀
                    charrrr   ⠀⠙⠢⣍⡓⢤⣴⣋⣉⡭⠛⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡿⠿⠀⠀⡇⠀
                            ⠀⠀⠀⠀⠀⣀⡬⢿⠃⣻⡶⣆⡀⠀⠈⠉⠒⠦⢄⡀⠀⠀⠀⠀⠀⠀⣠⠇⠀⠀⠀⣷⠀
        it's charmander!   ⣴⣶⠶⠒⠉⠀⠀⢸⠞⠁⠀⠀⠙⢆⠀⠀⠀⠀⠀⠈⠉⠚⣿⡶⠀⢰⠃⠀⠀⠀⢠⣿⣄
                            ⠉⢻⣄⣀⠀⢀⡾⠀⠀⠀⠀⠀⠈⢧⣀⣀⠀⠀⠀⣿⡧⠾⠗⠀⠀⢧⡀⠀⠀⠀⣡⠇
                            ⠀⠉⠁⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠈⡆⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠳⣤⣀⠞⠁⠀
                            ⠀⠀⠀⠀⢀⡠⠚⡇⠀⠀⠀⠀⠀⠀⠀⢠⠟⠀⠀⠀⢳⡀⠀⠀⠀⣠⠞⠁⣠⡇⠀⠀⠀
                            ⠀⠀⠀⢀⠎⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⢳⠒⠈⠉⠀⢀⣴⡟⠀⠀⠀⠀
                            ⠀⠀⠀⣈⣧⡀⠀⠀⠀⢠⠔⠛⠓⠒⠒⠚⠧⡀⠀⠀⠀⠈⡯⠄⠒⠉⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⣾⣟⣶⣳⠤⠤⠔⠊⠀⠀⠀⠀⠀⠀⠀⢹⡀⢀⣀⣀⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢚⣾⣷⣟⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
    catch()
    no_runtime = 0
  elif random_pokemon == 2 or random_pokemon == 3:  #increasing the chances of appearing
    rarity = 1
    print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀gulp gulp
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⣠⡞⠁⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠉⠂⠀⠀⠀⢸⠓⠶⣦⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⣀⣀⡴⠚⣧⣤⣄⣀⠀⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀A wild margikarp has appeared!
        ⠀⠀⠀⢀⣤⠖⠋⠉⠀⠀⠀⠰⠀⢈⠏⠛⢦⣄⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⢀⣴⠋⠀⢠⠔⠒⠢⡀⠀⠀⡇⠈⢢⠀⠀⠉⢳⡄⠀⠀⠀⠀⣠⠴⣒⠾⢟⠟
        ⢰⠻⣁⠀⠀⡃⠀⠂⠀⡸⠀⠀⢰⠀⢅⠀⠀⠀⠘⠙⣆⠀⡴⢋⡵⠊⠁⠀⡸⠀
        ⠈⢗⡄⠆⠀⠳⠤⠤⠚⢁⡠⠖⡋⠩⠭⠷⠖⠒⣲⣶⠼⡞⣠⠛⠀⠉⠉⣹⠃⠀
        ⠀⢸⠄⡀⠀⠀⢤⢄⠀⠁⣠⡞⠂⠉⠉⠀⣠⠞⠁⠃⠀⢱⠃⠀⠀⠀⡰⠁⠀⠀
        ⡰⡝⢃⢇⠀⠀⠀⢱⢱⠀⠑⢤⡁⠀⢀⠞⠁⠀⠰⠀⡰⡿⠀⠀⠀⠀⡇⠀⠀⠀
        ⡇⡏⠙⠳⣭⣐⡀⠄⡄⣆⢀⡜⠉⡦⠎⠀⠀⣠⡧⠚⡅⡇⠡⡀⠀⢠⠇⠀⠀⠀
        ⠰⣡⠀⠀⠀⠉⠙⠻⠀⣷⠾⠭⠭⠴⢶⠖⠛⠉⠀⠀⢣⢳⠀⠈⢢⡞⠀⠀⠀⠀
        ⠀⠹⣣⠀⠀⠀⠀⢰⢰⠃⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠻⣷⣠⠏⠀⠀⠀⠀⠀
        ⠀⠀⢣⢃⠀⠀⠀⣾⢸⣀⣤⡄⠀⢠⣄⡈⢧⠀⠀⠀⠀⠀⠈⠙⠂⠀⠀⠀⠀⠀
        ⠀⠀⠀⣼⠀⠀⠀⠀⡆⡇⠀⠙⠳⠏⠈⠙⠛⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⢀⡟⠀⠀⠀⠀⠈⠮⣢⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ''')
    catch()
    no_runtime = 0
  elif random_pokemon == 4:
    rarity = 3
    print('''⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣶⣦⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣶⣾⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀hola⠀⠀ ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⠀⠀  yawnnnnnn~⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⢀⡀⣄⠀⠀⠀⠀⠀⠀⠀⣿⣿⠟⠉⠀⢀⣀⠀⠀⠈⠉⠀⠀⣀⣀⠀⠀⠙⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀.⣀⣶⣿⣿⣿⣾⣇⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⢀⣀⡀...⣀⡀⠀⠀⠀⠀⠀⠹⣿⠀⠀⠀⠀⠀⠀⠀⠀A wild snorlax has appeared!⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⣼⡏⠀⠀⠀⣀⣀⣉......⠭ ⠤⢀⣀⣀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀It seems to be awake...
        ⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣿⠷⠒⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠒⠼⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠈⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢹⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀
        ⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣶⣤⣄⣠⣤⣤⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀
        ⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀
        ⠀⠀⣀⠀⢸⡿⠿⣿⡿⠋⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠻⠿⠟⠉⢙⣿⣿⣿⣿⣿⣿⡇
        ⠀⠀⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⢿⡿⣿⠳⠀
        ⠀⠀⡞⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⡀⠀⠀
        ⢀⣸⣀⡀⠀⠀⠀⠀⣠⣴⣾⣿⣷⣆⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣰⣿⣿⣿⣿⣷⣦⠀⠀⠀⠀⢿⣿⠿⠃⠀
        ⠘⢿⡿⠃⠀⠀⠀⣸⣿⣿⣿⣿⣿⡿⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢻⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⡸⠁⠀⠀⠀
        ⠀⠀⠳⣄⠀⠀⠀⠹⣿⣿⣿⡿⠛⣠⠾⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠳⣄⠙⠛⠿⠿⠛⠉⠀⠀⣀⠜⠁⠀⠀⠀⠀
        ⠀⠀⠀⠈⠑⠢⠤⠤⠬⠭⠥⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠢⠤⠤⠤⠒⠊⠁⠀⠀⠀⠀⠀⠀
      ''')
    catch()


def option_6():
  shop = True
  global coins
  while shop:
    shop_menu6()
    try:
      choices = int(input("Enter your choice: "))

      if choices == 1:
        #recipe
        recipe_6()
      elif choices == 2:
        #owned ingredients
        for k, v in inventory.items():
          print('\n' + k + ':', v)  #prints key and item in inventory
      elif choices == 3:
        #purchase ingredients
        print('''
      (1) 1 Sugar ------ 1 coin
      (2) 1 Milk ------- 3 coins
      (3) 1 Butter ----- 2 coins
      (4) 1 Flour ------ 3 coins
      (5) 1 Eggs ------- 1 coin
      (6) 1 Margikarp -- 2 coins
      (0) Quit
                  ''')
        purchase = int(input("Enter your choice: "))
        shop_items = {
            1: 'Sugar',
            2: 'Milk',
            3: 'Butter',
            4: 'Flour',
            5: 'Eggs',
            6: 'Margikarp'
        }
        if (purchase == 1 or purchase == 5) and coins >= 1:
          coins -= 1
          inventory[shop_items[purchase]] += 1
        elif (purchase == 2 or purchase == 4) and coins >= 3:
          coins -= 3
          inventory[shop_items[purchase]] += 1
        elif (purchase == 6 or purchase == 3) and coins >= 2:
          coins -= 2
          inventory[shop_items[purchase]] += 1
        elif purchase == 0:
          shop = False
        else:
          print("\nInsufficient coins!\n")

      elif choices == 4:
        #bake!
        print('''
    What do you want to bake?
    (1) Cake
    (2) Fish Pie
                ''')
        bake = int(input("Enter your choice: "))
        if bake == 1:
          if inventory['Sugar'] >= 1 and inventory['Flour'] >= 1 and inventory[
              'Eggs'] >= 1 and inventory['Butter'] >= 1:
            inventory['Sugar'] -= 1
            inventory['Flour'] -= 1
            inventory['Eggs'] -= 1
            inventory['Butter'] -= 1
            print('''             
                  Baking in Process...    
            \n Anytime soon...
      \n WALAH- Enjoy the cake :D 
                  ' ' ' '
                 _| | | |_
                {         }
                {_________}
      ''')
          else:
            print('Insufficient Ingredients!')

        elif bake == 2:
          if inventory['Milk'] >= 1 and inventory['Flour'] >= 1 and inventory[
              'Margikarp'] and inventory['Butter'] >= 1:
            inventory['Milk'] -= 1
            inventory['Flour'] -= 1
            inventory['Margikarp'] -= 1
            inventory['Butter'] -= 1
            print('''
           Baking in Process...    
            \n Anytime soon...     
                \n WALAH- Enjoy the Fish Pie :D
                            ⠀⠀⠀⠀⠀⠀⠀⢹⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠈⡆⠈⠂⡤⠀⣀⣀⠀⠤⠒⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⡇⠀⠀⡌⠀⠀⡘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⡆⠈⠀⡌⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⢀⠔⠊⠉⠁⠢⢤⢠⠜⠀⡩⠕⣊⠭⡖⠒⠒⠒⠒⠀⠠⠬⠭⠰
                            ⠀⠀⠀⠀⢀⡔⠁⢴⣎⠉⡆⠀⠀⡨⠐⡡⠔⠈⠀⢠⠂⠑⡄⠀⠀⠀⠀⠀⠀⠀
                            ⢀⡠⢔⡪⠕⠃⢈⡀⣀⠔⠁⠠⠊⠔⠉⠀⠀⢀⡔⠁⠀⢰⠉⠐⠠⡀⠀⠀⠀⠀
                            ⠁⡩⠊⡠⠔⠀⠀⠀⠀⠀⣀⠀⢀⠀⠀⠀⡠⠊⢂⠀⠀⡬⠄⢀⡀⠘⢄⠀⠀⠀
                            ⠘⠒⠁⠀⠀⡆⠀⠀⢀⠊⡔⢚⠀⠑⠔⠈⠀⠀⢸⣀⠎⠈⠑⢄⠈⠑⠠⡡⡀⠀
                            ⠀⠀⠀⠀⠀⠀⠑⠄⣸⠀⢇⣘⣄⠀⢸⢀⡀⠤⠞⠣⠭⠁⠒⠠⢦⡤⡤⠤⠽⠦
                            ⠀⠀⠀⠀⠀⠀`⠀⠀⠑⠒⠒⠚⠠⠇⣑⣒⣒⣒⣒⣂⣀⠉⠭⠔⠊⠀⠀⠀
                                     `------------------' ''')
          else:
            print('Insufficient Ingredients!')

        else:
          print('Invalid choice!')
      elif choices == 0:
        #exit bakery shop
        shop = False

      else:
        print('Invalid choice!')
    except ValueError:
      print("Invalid input")


def option_0():
  ''' 
  Quit the program 
  '''
  print('\nBye\n')
  print("Thank you for using the Pokemon Super Search Engine!")


with open('Pokemon.csv', 'r') as file:
  reader = csv.reader(file)  #read csv file

  #Create a table
  for r in reader:
    number.append(r[0])
    name.append(r[1])
    type1.append(r[2])
    type2.append(r[3])
    total.append(r[4])
    HP.append(r[5])
    Attack.append(r[6])
    Defense.append(r[7])
    SpAtk.append(r[8])
    SpDef.append(r[9])
    Speed.append(r[10])
    Generation.append(r[11])
    Legendary.append(r[12])

  #display menu
  while runtime == False and end == False:
    display_menu()
    option = input("Enter option: ")
    if option.isdigit(
    ) and 0 <= int(option) <= 6:  #checks if input is an integer from 0-6.
      option = int(option)
      runtime = True
    else:
      print("\nInvalid option. Please input values 0-6.\n")

    while runtime == True and no_runtime < 3:
      #main program
      if option == 1:
        try:
          option_1()
          no_runtime += 1
          runtime = False  #exits loop and returns to main menu
        except ValueError:
          print('Invalid input.')

      elif option == 2:
        try:
          option_2()
          no_runtime += 1
          runtime = False
        except ValueError:
          print('Invalid input.')

      elif option == 3:
        try:
          option_3()
          no_runtime += 1
          runtime = False
        except ValueError:
          print('Invalid input. Please enter an integer')

      elif option == 4:
        try:
          option_4()
          no_runtime += 1
          runtime = False
        except ValueError:
          print('Invalid input.')

      elif option == 5:
        try:
          option_5()
          type=[]
          no_runtime += 1
          runtime = False
        except ValueError:
          print('Invalid input.')

      elif option == 6:
        try:
          option_6()
          no_runtime += 1
          runtime = False
        except ValueError:
          print('Invalid input.')

      elif option == 0:
        option_0()
        runtime = False
        end = True

      else:
        print('Not implemented yet? Please choose a valid option.')
        runtime = False

      while no_runtime >= 3:
        random_pokemon6()
