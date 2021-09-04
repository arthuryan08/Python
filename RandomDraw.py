import random
donor = []

initProgram = int(input('Register donor? 0 - No  |  1 - Yes '))

def registerDonor(name:str, donation:float):
    donor.extend( ((name + ' ') * int(donation//10)).split())
    
while initProgram == 1:
    name = input('Donor name: ')
    donation = float(input('Donor value: '))
    registerDonor(name, donation)
    initProgram = int(input('Register donor? 0 - No  |  1 - Yes '))

def randomDraw():
    print(f'List of donors for the draw: {donor}')
    random.shuffle(donor)
    print(f'Lista of donor shuffled: {donor}')
    return random.choice(donor)
    
print(f'The winner was: {randomDraw()}')
