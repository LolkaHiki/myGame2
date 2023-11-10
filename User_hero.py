class Character:
    def __init__(self, name, race, profession, stats, skills, abilities):
        self.name = name
        self.race = race
        self.profession = profession
        self.stats = stats
        self.skills = skills
        self.abilities = abilities

    def attack(self, target):
        pass

    def defend(self, damage):
        pass


class Swordsman(Character):
    def __init__(self, name, race, stats, skills, abilities):
        super().__init__(name, race, "Warrior", stats, skills, abilities)

        self.stats["Strength"] += 2
        self.stats["Constitution"] += 1
        self.skills["Fighting"] += 3
        self.abilities["Battle Spirit"] = True
        self.abilities["Two-Handed Attack"] = True
        self.abilities["Turning Strike"] = True


class Archer(Character):
    def __init__(self, name, race, stats, skills, abilities):
        super().__init__(name, race, "Ranger", stats, skills, abilities)

        self.stats["Dexterity"] += 2
        self.stats["Constitution"] += 1
        self.skills["Archery"] += 3
        self.abilities["Arrow of Destiny"] = True
        self.abilities["Arrow of Speed"] = True
        self.abilities["Arrow of Invisibility"] = True


class Mage(Character):
    def __init__(self, name, race, stats, skills, abilities):
        super().__init__(name, race, "Sorcerer", stats, skills, abilities)

        self.stats["Intelligence"] += 2
        self.stats["Constitution"] += 1
        self.skills["Magic"] += 3
        self.abilities["Summoning Spell"] = True
        self.abilities["Teleportation Spell"] = True
        self.abilities["Healing Spell"] = True


class Catdog(Character):
    def __init__(self, name, race, stats, skills, abilities):
        super().__init__(name, race, "Wild Beast", stats, skills, abilities)

        self.stats["Strength"] += 1
        self.stats["Dexterity"] += 2
        self.stats["Constitution"] += 1
        self.skills["Acrobatics"] += 3
        self.abilities["Bite"] = True
        self.abilities["Claw Strike"] = True
        self.abilities["Super Jump"] = True
