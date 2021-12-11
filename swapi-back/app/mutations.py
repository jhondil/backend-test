import graphene
from graphql_relay import from_global_id

from .models import People_film, Planet, People, Film
from .types import PeopleFilmType, PlanetType, PeopleType, FilmType
from .utils import generic_model_mutation_process


class CreatePlanet(graphene.relay.ClientIDMutation):
    class Input:

        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        rotation_period = graphene.String(required=False)
        orbital_period = graphene.String(required=False)
        diameter = graphene.String(required=False)
        climate = graphene.String(required=False)
        gravity = graphene.String(required=False)
        terrain = graphene.String(required=False)
        surface_water = graphene.String(required=False)
        population = graphene.String(required=False)

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        data = {'model': Planet, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        planet = generic_model_mutation_process(**data)
        return CreatePlanet(planet=planet)


class CreatePeople(graphene.Mutation):
    people = graphene.Field(PeopleFilmType)

    class Arguments:

        name = graphene.String()
        height = graphene.String()
        mass = graphene.String()
        hair_color = graphene.String()
        skin_color = graphene.String()
        eye_color = graphene.String()
        birth_year = graphene.String()
        gender = graphene.String()
        home_world_id = graphene.Int()
        people_film_id = graphene.Int()

    def mutate(self, info,  name, height, mass, hair_color, skin_color, eye_color, birth_year, gender, home_world_id, people_film_id):
        p = People(name=name, height=height, mass=mass, hair_color=hair_color,
                   skin_color=skin_color, eye_color=eye_color, birth_year=birth_year, gender=gender)
        hw = Planet.objects.get(id=home_world_id)
        pf = Film.objects.get(id=people_film_id)
        p.home_world = hw
        p.save()
        p.films.set([pf])

        return CreatePeople(people=p)


# class PeopleFilmInput(graphene.InputObjectType):

#         name= graphene.String()
#         height = graphene.String()
#         mass = graphene.String()
#         hair_color = graphene.String()
#         skin_color = graphene.String()
#         eye_color = graphene.String()
#         birth_year = graphene.String()
#         gender = graphene.String()
#         home_world_id = graphene.Int()
#         people_film = graphene.List(FilmType)

# class CreatePeopleFilm(graphene.Mutation):
#     class Arguments:
#         input = PeopleFilmInput(required=True)


#     film = graphene.Field(FilmType)

#     @staticmethod
#     def mutate(root, info, input=None):

#         fielms = []
#         for f in input.fielms:
#           fi = Film.objects.get(id=f.id)
#           if fi is None:
#             return CreatePeopleFilm(ok=False, movie=None)
#           fielms.append(fi)
#         people_instance = People_film(
#             name= input.name,
#             height = input.height,
#             mass = input.mass,
#             hair_color = input.hair_color,
#             skin_color = input.skin_color,
#             eye_color = input.eye_color,
#             birth_year = input.birth_year,
#             gender = input.gender,
#             home_world_id = input.home_world_id

#           )
#         people_instance.save()
#         people_instance.fielms.set(fielms)
#         return CreatePeopleFilm(film=people_instance)



