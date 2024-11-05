import data
import sender_stand_request


def positive_assert(kit_name):  #funcion para las pruebas positivas
    response1 = sender_stand_request.post_personal_kit(kit_name)
    assert response1.status_code == 201
    assert response1.json()["name"] == kit_name["name"]


def negative_assert(kit_name):
    response1 = sender_stand_request.post_personal_kit(kit_name)
    assert response1.status_code == 400



# prueba 1
def test_create_test_1_character():
    positive_assert(data.test_1_character)

# prueba 2
def test_create_test_511_characters():
    positive_assert(data.test_511_characters)

# prueba 3
def test_create_test_0_characters():
    negative_assert(data.test_0_characters)

# prueba 4
def test_create_test_512_characters():
    negative_assert(data.test_512_characters)

# prueba 5
def test_create_test_speacial_characters():
    positive_assert(data.test_special_characters)

# prueba 6
def test_create_test_space_characters():
    positive_assert(data.test_space_characters)

# prueba 7
def test_create_test_number_characters():
    positive_assert(data.test_number_characters)

# prueba 8
def test_create_test_empty():
    negative_assert(data.test_empty)

# prueba 9

def test_create_test_number2_characters():
    negative_assert(data.test_number2_characters)

