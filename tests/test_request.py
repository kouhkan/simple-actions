from app import app
import json

def test_factorial_endpoint():
    with app.test_client() as c:
        response = c.get('/5')
        data = json.loads(response.get_data(as_text=True))
        assert response.status_code == 200
        assert data == {'result': 120}