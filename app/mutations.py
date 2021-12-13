import graphene
from graphql_relay import from_global_id

from .models import People_film, Planet, Film
from .types import PeopleFilmType, PlanetType, FilmType
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


# class CreatePeople(graphene.Mutation):
#     people = graphene.Field(PeopleFilmType)

#     class Arguments:

#         name = graphene.String()
#         height = graphene.String()
#         mass = graphene.String()
#         hair_color = graphene.String()
#         skin_color = graphene.String()
#         eye_color = graphene.String()
#         birth_year = graphene.String()
#         gender = graphene.String()
#         home_world_id = graphene.Int()
#         people_film_id = graphene.Int()

#     def mutate(self, info,  name, height, mass, hair_color, skin_color,
#         eye_color, birth_year, gender, home_world_id, people_film_id):
#         p = People(name=name, height=height, mass=mass,
#         hair_color=hair_color,
#         skin_color=skin_color, eye_color=eye_color,
#         birth_year=birth_year, gender=gender)
#         hw = Planet.objects.get(id=home_world_id)
#         pf = Film.objects.get(id=people_film_id)
#         p.home_world = hw
#         p.save()
#         p.films.set([pf])

#         return CreatePeople(people=p)


class FilmInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    episode_id = graphene.Int()


class PeopleFilmInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    height = graphene.String()
    mass = graphene.String()
    hair_color = graphene.String()
    skin_color = graphene.String()
    eye_color = graphene.String()
    birth_year = graphene.String()
    gender = graphene.String()
    home_world_id = graphene.Int()
    pp_film = graphene.List(FilmInput)


class CreateFilm(graphene.Mutation):
    class Arguments:
        input = FilmInput(required=True)
    film = graphene.Field(FilmType)

    @staticmethod
    def mutate(root, info, input=None):

        film_instance = Film(
            title=input.title,
            episode_id=input.episode_id
        )
        film_instance.save()
        return CreateFilm(film=film_instance)


class CreatePeopleFilm(graphene.Mutation):
    class Arguments:
        input = PeopleFilmInput(required=True)

    PeopleFilms = graphene.Field(PeopleFilmType)

    @staticmethod
    def mutate(root, info, input=None):

        filmss = []
        for f_input in input.pp_film:
            f = Film.objects.get(id=f_input.id)
            if f is None:
                return CreatePeopleFilm(movie=None)
            filmss.append(f)
        pf = People_film(
            name=input.name,
            height=input.height,
            home_world_id=input.home_world_id
        )
        pf.save()
        pf.films.set(filmss)
        return CreatePeopleFilm(PeopleFilms=pf)


class UpdatePeople(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = PeopleFilmInput(required=True)

    People = graphene.Field(PeopleFilmType)

    @staticmethod
    def mutate(root, info, id, input=None):

        p = People_film.objects.get(pk=id)
        if p:
            filmss = []
            for f_input in input.pp_film:
                f = Film.objects.get(pk=f_input.id)
                if f is None:
                    return UpdatePeople(movie=None)
                filmss.append(f)
            p.name = input.name
            p.height = input.height
            p.save()
            p.films.set(filmss)
            return UpdatePeople(People=p)
        return UpdatePeople(movie=None)
