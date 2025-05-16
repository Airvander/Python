import random
import logging
import logging.handlers
import datetime

# Create a logger object
logger = logging.getLogger('game')
logger.setLevel(logging.DEBUG)

# Define the log format
log_format = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# Create a file handler to write logs to file
log_file = 'game.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(log_format)

# Add the handlers to the logger
logger.addHandler(file_handler)


class Unit:
    def __init__(self, name):
        # The init character, doAttack, doDefence are None as the child class will super init the stats
        # Healthy = True as all units are healthy by default
        self.name = name
        self.character = None
        self.fullHp = 100
        self.doAttack = None
        self.doDefence = None
        self.expPoint = 0
        self.level = 1
        self.healthy = True
        self.coins = 0
        logger.debug('Created unit %s', name)

    def usePotion(self):
        # each potion cost 20 coins
        if self.coins >= 20:
            # each health potion heals for 20hp
            self.fullHp += 20
            self.coins -= 20
            print(f"{self.name}  consumed a potion and feels much better. HP+20 ")
        else:
            print(f"{self.name} 20 coins is needed to consume a potion.")

    def attack(self, unit):

        dead = False

        # Randint for the negative 5 to 10 based on game requirements
        damage = self.doAttack - unit.doDefence + (random.randint(-5, 10))
        damage = max(0, damage)
        unit.fullHp -= damage
        print(f'{self.name} damaged {unit.name} for {damage} ')

        if unit.fullHp <= 0:
            # The game to state if any 1 of the unit are dead due to 0 or lesser HP
            unit.healthy = False
            unit.fullHhp = 0
            print(f'{unit.name} is dead! ')
            return True
        # The game to reward EXP based on the damage dealt and damage taken
        attackerExp = damage
        defenderExp = unit.doDefence
        # Extra EXP if damage more than 10 or equal or less than 0
        if damage > 10:
            attackerExp = damage * 1.2
        elif damage <= 0:
            defenderExp = unit.doDefence * 1.5
        # The game to reward EXP based on the damage dealt and damage taken
        self.expPoint += attackerExp
        unit.expPoint += defenderExp
        # Game to update on the EXP receieved by both player and pc unit each round
        logger.info('%s received %d exp points', unit.name, defenderExp)
        logger.debug('%s received %d exp points, total exp %d', unit.name, defenderExp, unit.expPoint)
        print(f"At this round, {self.name} received {int(attackerExp)} EXP!")
        print(f"While {unit.name} received {int(defenderExp)} EXP!")
        print("")

        # Point system where attacker gains coins equal to half of damage dealt
        self.coins += (damage // 2)
        print(f"{self.name} gained {damage // 2}coins!\n")

        # if unit hits 100 EXP
        # Unit to level up by 1 and reduced their current EXP by 100
        if self.expPoint >= 100:
            self.level += 1
            self.expPoint -= 100
            logger.debug('Congrats, %s gained a new level!', self.name)
            print(f"Congrats, {self.name} gained a new level! ")

        if self.expPoint >= 100:
            unit.level += 1
            unit.expPoint -= 100
            logger.debug('Congrats, %s gained a new level!', unit.name)
            print(f"Congrats, {unit.name} gained a new level! ")
        return False

        logger.info('%s attacked %s and caused %d damage', self.name, unit.name, damage)
        if unit.fullHp <= 0:
            logger.info('%s died', unit.name)
        else:
            logger.info('%s received %d exp points', unit.name, defenderExp)
        return False


class Warrior(Unit):
    def __init__(self, name):
        super().__init__(name)
        # As mentioned, the child class to super init parent stats while changing the None values to each unique class
        self.character = "Warrior"
        self.doAttack = random.randint(5, 20)
        self.doDefence = random.randint(1, 10)
        logger.debug('Created warrior %s', name)

    def __str__(self):
        return f""" 
     {self.character} {self.name}
     HP: {self.fullHp}/100
     ATK: {self.doAttack}
     DEF: {self.doDefence}
     EXP: {int(self.expPoint)}
     LVL: {self.level}
     Coins: {self.coins}
        """

    def __repr__(self):
        return self.__str__()


class Tanker(Unit):
    def __init__(self, name):
        # As mentioned, the child class to super init parent stats while changing the None values to each unique class
        super().__init__(name)
        self.character = "Tanker"
        self.doAttack = random.randint(1, 10)
        self.doDefence = random.randint(5, 15)

    def __str__(self):

        return f""" 
     {self.character}  {self.name}
     HP: {self.fullHp}/100
     ATK: {self.doAttack}
     DEF: {self.doDefence}
     EXP: {int(self.expPoint)}
     LVL: {self.level}   
     Coins: {self.coins}
         """

    def __repr__(self):
        return self.__str__()


def playerUnits(player, units):
    # Allow player to choose their unit between Warrior and Tanker, then ask player to input a name for each unit
    while len(player) < 3:
        print(f"Please select your Unit {len(player) + 1}!\n")
        for i, unit in enumerate(units):
            print(f"{i + 1}: {unit}")

        player_choice = input("Please make a choice: ")
        if not player_choice.isnumeric():
            print(f"Please choose a number between 1 and {len(units)}")
            print("===============================================")
            continue

        elif int(player_choice) == 1:
            # player choosing 1 will append Warrior class
            unit_name = input("Enter a desired name of choice for your warrior! : ")
            print(f'{unit_name} is ready for battle')
            player.append(Warrior(unit_name))
            print("===============================================")

        elif int(player_choice) == 2:
            # player choosing 2 will append Tanker class
            unit_name = input("Enter a desired name of choice for your Tanker! : ")
            print(f'{unit_name} is ready for battle')
            player.append(Tanker(unit_name))
            print("===============================================")

        else:
            # If player choose other numbers, system will detect and pop an error
            print(f"Please choose a number between 1 and {len(units)}")
            print("===============================================")
            continue

    return player


def opponentUnits(opponent, units):
    # PC choose 3 random units with randon generated name
    while len(opponent) < 3:
        randomChoice = random.randint(1, len(units))
        randomName = str(random.randint(10, 99))

        if randomChoice == 1:
            opponent.append(Warrior(f"AI{randomName}"))
        elif randomChoice == 2:
            opponent.append(Tanker(f"AI{randomName}"))

    return opponent


def table(player, opponent):
    numberCol = 25
    # we are choosing 25 colums for our table

    for player_, opponent_ in zip(player, opponent):
        opponentRows = str(opponent_).split("\n")
        playerRows = str(player_).split("\n")

        playerRowsAdj = list(map(lambda x: x + (numberCol - len(x)) * " ", playerRows))

        for pRow, oRow in zip(playerRowsAdj, opponentRows):
            # adding player row and pc row together
            print(pRow + oRow)


def chooseUnit(team, action=0):
    messages = [
        "Please choose your attacking unit!: ",
        "Please choose a AI unit to attack!: ",
    ]
    choice_message = messages[action]

    while True:
        for i, unit in enumerate(team):
            if unit.healthy:
                print(f"{i + 1}: {unit.character} {unit.name}")

        choice = input(choice_message)
        print("===============================================")
        if not choice.isnumeric():
            print(f" Please choose a number from 1 to {len(team)}")
            continue

        elif 1 <= int(choice) <= len(team):
            unitChoice = team[int(choice) - 1]
            if unitChoice.healthy:
                return unitChoice
            else:
                print(f"{unitChoice.name} died!")
                continue

        else:
            print(f"Please choose a number from 1 to {len(team)}")
            continue


def opponentAttack(opponent, player):
    # PC will choose a random player unit to attack
    while True:
        attackerChoice = random.randint(0, len(opponent) - 1)
        if opponent[attackerChoice].healthy:
            attacker = opponent[attackerChoice]
            break

    while True:
        defenderChoice = random.randint(0, len(player) - 1)
        if player[defenderChoice].healthy:
            defender = player[defenderChoice]
            break

    return attacker, defender


def playerAction(actions):
    while True:
        for i, action in enumerate(actions):
            print(f"{i + 1}. {action}")
        choice = input("Please choose between Attack or Quit?: ")
        print("")

        if not choice.isnumeric():
            print(f"Please choose a number between 1 and {len(actions)}")
            print("===============================================")

        elif 1 <= int(choice) <= len(actions):
            playerAction = actions[int(choice) - 1]
            return playerAction

        else:
            print(f"Please choose a number between 1 and {len(actions)}")
            print("===============================================")


def main_menu():
    print("Are you ready for PSB Battle Game?")

    options = [
        "Start Game",
        "Quit"
    ]

    while True:
        for i, action in enumerate(options):
            print(f"{i + 1}. {action}")
        choice = input("Input 1 if you are ready to start the game: ")
        print("")

        if not choice.isnumeric():
            print("Please choose a valid option")
            continue

        elif 1 <= int(choice) <= len(options):
            return choice

        else:
            print("Please choose a valid option")
            continue


def init_game():
    units = ["Warrior", "Tanker"]

    player = []
    opponent = []

    playerUnits(player, units)
    opponentUnits(opponent, units)

    playerHealthy = len(player)
    opponentHealthy = len(opponent)

    return player, opponent


def main():
    action = int(main_menu())
    if action == 1:
        logger.info('Game started')
        player, opponent = init_game()
        playerHealthy = len(player)
        opponentHealthy = len(opponent)

    else:
        print("Bye!")
        return

    actions = ["Attack", "Quit"]

    while True:
        table(player, opponent)

        userAction = playerAction(actions)
        if userAction == "Attack":
            attacker = chooseUnit(player, action=0)
            defender = chooseUnit(opponent, action=1)
            dead = attacker.attack(defender)

            if dead:
                opponentHealthy -= 1

            if opponentHealthy == 0:
                print("You are the winner!")

        elif userAction == "Quit":
            print("Game ended, we hope to see you soon!")
            return

        attacker, defender = opponentAttack(opponent, player)
        dead = attacker.attack(defender)
        if dead:
            playerHealthy -= 1

        if playerHealthy == 0:
            print("Oh no, you lost the game!")
            print("========GAME ENDS===============")
            logger.info('Game ended')
            break


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error encountered", e)






