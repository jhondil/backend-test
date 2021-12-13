from collections import defaultdict


def order_pokemon(pokemons):
    first_pokemon = defaultdict(set)
    for pokemon in pokemons:
        first_pokemon[pokemon[0]].add(pokemon)

    return first_pokemon


def List_pokemon(first_pokemon, pokemon):

    assert pokemon
    word_pokemon = pokemon[-1][-1]
    list_pokem = first_pokemon[word_pokemon] - set(pokemon)

    # if  list_pokem =! word_pokemon:
    # return pokemon

    if not list_pokem:
        return pokemon
    else:
        option_pokemon = (List_pokemon(first_pokemon, list(pokemon) + [poke])
                        for poke in list_pokem)
        maxx_pokemon = max(option_pokemon, key=len)
        # print('listta de pokemones: %r' % maxx_pokemon)
        return maxx_pokemon


def pokemons(list_pokemon):

    first_pokemon = order_pokemon(list_pokemon)
    return max(
        (List_pokemon(first_pokemon, [word]) for word in list_pokemon), key=len)


if __name__ == '__main__':

    pokemon_li = '''audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon
                        cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig
                        gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune
                        landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
                        nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz
                        registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon
                        simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix
                        wailord wartortle whismur wingull yamask'''

    pokemon = pokemon_li.strip().lower().split()

    pokemonn = sorted(set(pokemon))

    pok = pokemons(pokemonn)
    for i in range(0, len(pok), 10):
        print(' '.join(pok[i:i+10]))
    # print(len(pok))
