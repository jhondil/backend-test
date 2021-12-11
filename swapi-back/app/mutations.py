import graphene
from graphql_relay import from_global_id

from .models import Planet, People
from .types import PlanetType,PeopleType
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
    people = graphene.Field(PeopleType)

    class Arguments:
        name= graphene.String()
        height = graphene.String()
        mass = graphene.String()
        hair_color = graphene.String()
        skin_color = graphene.String()
        eye_color = graphene.String()
        birth_year = graphene.String()
        gender = graphene.String()
        home_world_id = graphene.Int()


    def mutate(self, info, name, height,mass,hair_color,skin_color,eye_color,birth_year,gender,home_world_id):
        p = People(name=name, height=height,mass=mass,hair_color=hair_color,skin_color=skin_color,eye_color=eye_color,birth_year=birth_year,gender=gender)
        hw = Planet.objects.get(id=home_world_id)
        p.home_world = hw
        p.save()
        return CreatePeople(people=p)