# pour éviter d'ouvrir fermer le fichier on met le tout en mémoire. Est-ce un gain de temps ?

class data():

    def __init__(self):

        self.immoweb_file = 'immoweb.csv'

        self.immoweb_list = []

    def load_db(self):
        pass

    def save_db(self):
        pass


class house():

    def __init__(self):
        """Constructor our class"""

        """ Données de base """
        self.state_of_the_building = "No Value found"
        self.house_area = "No Value found"  # living area
        self.price = "No Value found"

        self.kitchen_type = "No Value found"
        self.nbr_bedrooms = "No Value found"
        self.surface_of_the_land = "No Value found"
        self.terrace_area = "No Value found"


        """ Données de Localisation """



        """ Description du bien """
        self.construction_year = "No Value found"
        self.floor = "No Value found"  # a quel étage se trouve le bien
        self.nbr_floor = "No Value found"
        self.street_facade_width = "No Value found"
        self.nbr_facades = "No Value found"
        self.covered_parking_spaces = "No Value found"
        self.outdoor_parking_spaces = "No Value found"
        self.living_room_surface = "No Value found"
        self.bedroom_1_surface = "No Value found"
        self.bedroom_2_surface = "No Value found"
        self.bedroom_3_surface = "No Value found"
        self.bedroom_4_surface = "No Value found"
        self.bedroom_5_surface = "No Value found"
        self.nbr_bathrooms = "No Value found"
        self.nbr_shower = "No Value found"
        self.nbr_toilet = "No Value found"
        self.cellar = "No Value found"  # la cave
        self.office_surface = "No Value found"
        self.office = "No Value found"
        self.work_space_surface = "No Value found"
        self.attic = "No Value found"  # le grenier
        self.sewer_network = "No Value found"  # connection aux égouts

        """ Energie """
        self.energy_consumption = "No Value found" # kwh/m²
        self.energy_class = "No Value found"
        self.co2_emission = "No Value found"
        self.heating_type = "No Value found"
        self.solar_panels = "No Value found"
        self.double_glazing = "No Value found"

        """ Divers """

        self.property_name = "No Value found"
        self.neighbourhood = "No Value found"
        self.flood_zone = "No Value found"
        self.cadastral_income = "No Value found"
        self.agent = "No Value found"   # personne qui gére la vente sur immoweb


        """ Suivit et actualisation des données """

        self.available_date = "No Value found"
        self.removed_from_immoweb = False
        self.immoweb_id = "No Value found"

        """ a classer et trouver """

        self.postal_code = "No Value found"

        self.type_of_property = "No Value found"
        self.subtype_of_property = "No Value found"
        self.type_of_sale = "No Value found"
        self.furnished = str(None)
        self.open_fire = "No Value found"
        self.terrace = "No Value found"
        self.garden = "No Value found"
        self.garden_area = "No Value found"
        self.surface_of_the_plot_of_land = str(None)
        self.number_of_facades = "No Value found"
        self.swimming_pool = "No Value found"


    def __str__(self):
        return " " +self.open_fire + " " + self.terrace

    def nbr_donne_trouvee(self):
        pass
        for i in vars(self):
            print(i)