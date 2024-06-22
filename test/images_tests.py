import pytest
from server import app
from fastapi.testclient import TestClient

client = TestClient(app)

image_url1 = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/200.svg"

@pytest.mark.parametrize("poke_name", ["pikatchu","bulbasaur","bulbasaur"])
def test_get_pokemon_image_by_poke_name(poke_name):
    response = client.get(f'?poke_name={poke_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Get pokemon details by id works successfully\n{response.text}\n')


@pytest.mark.parametrize("poke_name", ['hoothoot'])
def test_add_new_pokemon_image(poke_name):
    response = client.post(f'/?poke_name={poke_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Add pokemon works successfully\n{response.text}\n')


@pytest.mark.parametrize("poke_name, new_image_url", [('hoothoot', image_url1)])
def test_update_pokemon_image(poke_name, new_image_url):
    response = client.put(f'?poke_name={poke_name}&new_image_url={new_image_url}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Delete pokemon by name works successfully\n{response.text}\n')


@pytest.mark.parametrize("poke_name", ['hoothoot'])
def test_delete_pokemon_image(poke_name):
    response = client.delete(f'/?poke_name={poke_name}')
    assert response.status_code == 200, f'Expected status_code 200 but got {response.status_code} - {response.text}'
    print(f'Delete pokemon by name works successfully\n{response.text}\n')


def main():
    test_get_pokemon_image_by_poke_name()
    test_add_new_pokemon_image()
    test_update_pokemon_image()
    test_delete_pokemon_image()


if __name__ == '__main__':
    main()