def generic_model_mutation_process(model, data, id=None, commit=True):
    """[esta función recibe un diccionario con la data de los input y 
    el modelo con el que se va trabajar en este caso Planet
    
    El id es el importante acá ya que va definir la opcion de crear el Plannet.

    1° va obtener el id y hacer le proceso de la consulta 
    2° .....
    3° .....
    4° .....


    ]

    Args:
        model ([Planet]): Modelo que envia en el diccionario desde la mutacion CreatePlanet
        data (input): los input(valores/data ) que envia en el diccionario desde la mutacion CreatePlanet
        id ([input]id): el valor de id
        commit (bool, optional): [description]. Defaults to True.

    Returns:
        [type]: [description]
    """
    if id:
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        item = model(**data)

    if commit:
        item.save()

    return item
