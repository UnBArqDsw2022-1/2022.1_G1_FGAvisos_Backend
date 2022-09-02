from fastapi.testclient import TestClient

from main import app


client = TestClient(app)

def test_get_professor():
    response = client.get("/professor/2")
    assert response.status_code == 200


def test_get_professor_invalid():
    response = client.get("/professor/5")
    assert response.status_code == 404


def test_get_professor_invalid():
    response = client.get("/professor/2")
    assert response.status_code == 200
    body = response.json()
    assert body["nome"] == 'Fellipe Pereira'
    assert body["id"] == 2
    assert body["email"] == 'fellipe@gmail.com'
    assert body["matricula"] == 200017772
    assert body["senha"] == 'fellps'


def test_post_professor_status():
    response = client.post(
        url="/professor/99"
    )
    assert response.status_code == 405


def test_post_professor_json():
    response = client.post(
        url="/professor/",
        json={  "id": 1000,
                "nome": "Joãozinho", 
                "email": "test_3@gmail.com", 
                "senha": "bekoajnsd", 
                "numero_telefone": "81556698899",
                "dt_nascumento": "1985-08-02 17:41:02.621282",
                "created_at": "2022-08-02 17:41:02.621282",
                "matricula": 150123654,
                "is_coordenador": False}
    )
    assert response.status_code == 201
    assert response.json() == {
	    "id": 1000,
	    "nome": "Joãozinho",
	    "email": "test_3@gmail.com",
	    "senha": "bekoajnsd",
	    "numero_telefone": "81556698899",
	    "dt_nascimento": None,
	    "created_at": "2022-08-02T17:41:02.621282",
	    "matricula": 150123654,
	    "is_coordenador": False
    }


def test_post_professor_json_url():
    response = client.post(
        url="/professor",
        json={  "nome": "Elaine", 
                "email": "test_34@gmail.com", 
                "senha": "bekoajnasdasd21312sd", 
                "numero_telefone": "815566988499",
                "dt_nascumento": "1985-08-02 17:41:02.621282",
                "created_at": "2022-08-02 17:41:02.621282",
                "matricula": 43120123654,
                "is_coordenador": False}
    )
    assert response.status_code == 307


    
