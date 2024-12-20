import unittest
from app import app, db, Material

class MaterialManagementTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_material(self):
        response = self.client.post('/add', data={
            'name': 'Test Material',
            'type': 'Type A',
            'quantity': 10,
            'min_quantity': 2,
            'price': 5.99
        })
        self.assertEqual(response.status_code, 302)
        with self.app.app_context():
            material = Material.query.filter_by(name='Test Material').first()
            self.assertIsNotNone(material)

    def test_edit_material(self):
        with self.app.app_context():
            material = Material(name='Old Material', type='Type B', quantity=5, min_quantity=1, price=3.50)
            db.session.add(material)
            db.session.commit()
            material_id = material.id
        response = self.client.post(f'/edit/{material_id}', data={
            'name': 'Updated Material',
            'type': 'Type B',
            'quantity': 15,
            'min_quantity': 3,
            'price': 4.99
        })
        self.assertEqual(response.status_code, 302)
        with self.app.app_context():
            updated_material = db.session.get(Material, material_id)
            self.assertEqual(updated_material.name, 'Updated Material')

    def test_delete_material(self):
        with self.app.app_context():
            material = Material(name='Material to Delete', type='Type C', quantity=8, min_quantity=2, price=2.50)
            db.session.add(material)
            db.session.commit()
            material_id = material.id
        response = self.client.post(f'/delete/{material_id}')
        self.assertEqual(response.status_code, 302)
        with self.app.app_context():
            deleted_material = db.session.get(Material, material_id)
            self.assertIsNone(deleted_material)

if __name__ == '__main__':
    unittest.main()