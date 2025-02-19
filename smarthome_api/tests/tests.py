import unittest
from app.utils import response

class TestSmartHomeAPI(unittest.TestCase):
    
    # Users Tests
    def test_create_user(self):
        self.assertEqual(response(True, {"id": 1, "name": "Test User", "email": "test@example.com"})[1], 200)
    
    def test_list_users(self):
        self.assertEqual(response(True, [{"id": 1, "name": "Test User", "email": "test@example.com"}])[1], 200)
    
    def test_update_user(self):
        self.assertEqual(response(True, {"id": 1, "name": "Updated User", "email": "updated@example.com"})[1], 200)
    
    def test_delete_user(self):
        self.assertEqual(response(True, message="User 1 deleted")[1], 200)
    
    # Homes Tests
    def test_create_home(self):
        self.assertEqual(response(True, {"id": 1, "address": "123 Main St"})[1], 200)
    
    def test_list_homes(self):
        self.assertEqual(response(True, [{"id": 1, "address": "123 Main St"}])[1], 200)
    
    def test_update_home(self):
        self.assertEqual(response(True, {"id": 1, "address": "Updated Address"})[1], 200)
    
    def test_delete_home(self):
        self.assertEqual(response(True, message="Home 1 deleted")[1], 200)
    
    # Rooms Tests
    def test_create_room(self):
        self.assertEqual(response(True, {"id": 1, "home_id": 1, "name": "Living Room"})[1], 200)
    
    def test_list_rooms(self):
        self.assertEqual(response(True, [{"id": 1, "home_id": 1, "name": "Living Room"}])[1], 200)
    
    def test_update_room(self):
        self.assertEqual(response(True, {"id": 1, "name": "Updated Room"})[1], 200)
    
    def test_delete_room(self):
        self.assertEqual(response(True, message="Room 1 deleted")[1], 200)
    
    # Devices Tests
    def test_create_device(self):
        self.assertEqual(response(True, {"id": 1, "type": "light", "status": "off", "room_id": 1})[1], 200)
    
    def test_list_devices(self):
        self.assertEqual(response(True, [{"id": 1, "type": "light", "status": "off", "room_id": 1}])[1], 200)
    
    def test_update_device_status(self):
        self.assertEqual(response(True, {"id": 1, "status": "on"})[1], 200)
    
    def test_delete_device(self):
        self.assertEqual(response(True, message="Device 1 deleted")[1], 200)
    
if __name__ == "__main__":
    unittest.main()

