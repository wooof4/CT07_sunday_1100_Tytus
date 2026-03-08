# print("Hello from lesson 5")
# food=['food','fodo','fdoo','doof','goog']
# food.pop(2)
# food.append('gogo')
# print(food)
# for i in food:
#     print(i)
##task 1##
# import random
# for i in range(101):
#     number=random.randint(1,1000)
#     print(str(number))
##task 2##
# import random
# numbers=[]
# lgbtq=0
# while True:
#     number=random.randint(1,1000)
#     print(str(number))
#     if number not in numbers:
#         numbers.append(number)
#         lgbtq=lgbtq+1
#     if lgbtq==100:
#         break
##task 3##
# print(max(numbers))
# print(min(numbers))





##task 4##
# namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
#             "Sophia", "Lucas", "Mia", "Aiden"]
# heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]
# print(max(heightlist))
# print(min(heightlist))
# tallest=max(heightlist)
# shortest=min(heightlist)
# IndexTall=heightlist.index(tallest)
# IndexShort=heightlist.index(shortest)
# print(namelist(IndexTall))
# print(namelist(IndexShort))
##task 5##
import random
pokemons = ["Pikachu", "Charizard", "Bulbasaur", "Squirtle",
"Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
"Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
"Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
"Electabuzz"]
powers = [55, 84, 49, 48, 45,
45, 52, 55, 110, 110,
85, 65, 134, 130, 110,
50, 125, 65, 110, 83]
pokemon1=random.choice(pokemons)
pokemon2=random.choice(pokemons)
print(pokemon1)
if pokemon2==pokemon1:
    pokemon2=random.choice(pokemon2)
print(pokemon2)
indexpokemon1=pokemons.index(pokemon1)
indexpokemon2=pokemons.index(pokemon2)
pokemon2power=powers[indexpokemon2]
pokemon1power=powers[indexpokemon1]
if pokemon1power<pokemon2power:
    print(pokemon2+' won')
elif pokemon1power>pokemon2power:
    print(pokemon1+' won')
elif pokemon1power==pokemon2power:
    print('draw')