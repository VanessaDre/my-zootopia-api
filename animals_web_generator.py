"""
Module responsible for generating the website based on animal data.
"""

import data_fetcher


def serialize_animal(animal):
    """
    Converts a single animal dictionary into an HTML list item.

    Parameters:
        animal (dict): The animal data to display.

    Returns:
        str: HTML representation of the animal card.
    """
    if not isinstance(animal, dict):
        return ""

    name = animal.get("name")
    diet = animal.get("diet")

    if diet is None and isinstance(animal.get("characteristics"), dict):
        diet = animal["characteristics"].get("diet")

    locations = animal.get("locations")
    first_location = None
    if isinstance(locations, list) and locations:
        first_location = locations[0]

    animal_type = animal.get("type")
    if animal_type is None and isinstance(animal.get("characteristics"), dict):
        animal_type = animal["characteristics"].get("type")

    output = '<li class="cards__item">\n'

    if name:
        output += f'<div class="card__title">{name}</div>\n'

    output += '<p class="card__text">\n'

    if diet:
        output += f'<strong>Diet:</strong> {diet}<br/>\n'
    if first_location:
        output += f'<strong>Location:</strong> {first_location}<br/>\n'
    if animal_type:
        output += f'<strong>Type:</strong> {animal_type}<br/>\n'

    output += '</p>\n'
    output += '</li>\n'

    return output


def main():
    """
    Main function that prompts the user for an animal name,
    fetches data using the data_fetcher module,
    and generates an HTML page.
    """
    animal_name = input("Enter a name of an animal: ").strip()
    animals_data = data_fetcher.fetch_data(animal_name)

    if animals_data:
        output = ""
        for animal in animals_data:
            output += serialize_animal(animal)
    else:
        output = (
            f'<li class="cards__item">'
            f'<div class="card__title">No results</div>'
            f'<p class="card__text">The animal "{animal_name}" doesn\'t exist.</p>'
            f'</li>'
        )

    with open("animals_template.html", "r", encoding="utf-8") as handle:
        template = handle.read()

    new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(new_html)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()

