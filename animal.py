class Animal:
    # weight/age ratio - how much does the species grow for a month
    # till average weight (when the species gets to average weight,
    #it stops growing)
    def __init__(
            self, species, age, name, gender,
            weight, life_expectancy, food_type, weight_age_ratio,
            food_weight_ratio,
            gestation_period=None):

        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.life_expectancy = life_expectancy
        self.food_type = food_type
        if self.gender == 'female':
            self.gestation_period = gestation_period
        self.weight_age_ratio = weight_age_ratio
        self.food_weight_ratio = food_weight_ratio
        #self.daily_food_consumption = food_weight_ratio * weight
