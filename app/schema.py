import graphene
from django.db.models import Q
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from graphql_relay.node.node import from_global_id
from graphql import GraphQLError
from .models import Planet, People, Film, Director, Producer
from .mutations import *
from .types import PlanetType, PeopleType, FilmType, DirectorType, ProducerType,PeopleFilter


class Query(graphene.ObjectType):
    planet = graphene.relay.Node.Field(PlanetType)
    all_planets = DjangoFilterConnectionField(PlanetType)

    people = graphene.relay.Node.Field(PeopleType)
    all_people = DjangoFilterConnectionField(PeopleType, filterset_class=PeopleFilter)

    def resolve_all_people(parent, info, gender):
        # returns an object that represents a Person
        if not gender:
            raise GraphQLError('Valid options are: male, female, hermaphrodite, and n / a.')
        else:
            return People.objects.filter(gender__icontains=gender)

    # def resolve_all_people(self, info, **kwargs):
    #     id = kwargs.get("id")
    #     return People.objects.get(id)
    #     # if gender:
    #     #     return People.objects.get(gender)
    #     # else:
    #     #     raise GraphQLError('Valid options are: male, female, hermaphrodite, and n / a.')




    film = graphene.relay.Node.Field(FilmType)
    all_films = DjangoFilterConnectionField(FilmType)

    director = graphene.relay.Node.Field(DirectorType)
    all_directors = DjangoFilterConnectionField(DirectorType)

    producer = graphene.relay.Node.Field(ProducerType)
    all_producers = DjangoFilterConnectionField(ProducerType)

    people_films = graphene.relay.Node.Field(PeopleFilmType)
    all_people_films = DjangoFilterConnectionField(PeopleFilmType)


class Mutation(graphene.ObjectType):
    create_planet = CreatePlanet.Field()
    # create_people = CreatePeople.Field()
    create_film = CreateFilm.Field()
    Create_peopleFilm = CreatePeopleFilm.Field()
    update_peopleFilm = UpdatePeople.Field()
