import unittest
from unittest import TestCase
from src.zoo import Zoo, ZooKeeper, Animal, Fence

class TestZoo(TestCase):
    
    def test_animal_dimension(self):
        """
        Questo test controlla che animali troppo grandi non vengano aggiunti alla fence
        """
        zookeeper_1: ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id=1)
        fence_1: Fence = Fence(area=100, temperature=25.0, habitat="Savana")
        animal_1: Animal = Animal(name="Pluto", species="Canide", age=5, height=300.0, width=1.0, preferred_habitat="Savana")
        zookeeper_1.add_animal(animal_1, fence_1)
        result: int = len(fence_1.animals)
        message: str = f"Error: the function add_animal should not add self.animal_1 into self.fence_1"
        
        self.assertEqual(result, 0, message)
        
    def test_animal_habitat(self):
        """
        
        """
        zookeeper_1: ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id=1)
        fence_1: Fence = Fence(area=100, temperature=25.0, habitat="Sea")
        animal_1: Animal = Animal(name="Pluto", species="Canide", age=5, height=5.0, width=1.0, preferred_habitat="Savana")
        zookeeper_1.add_animal(animal_1, fence_1)
        result: int = len(fence_1.animals)
        message: str = f"Error: the function add_animal should not add self.animal_1 into self.fence_1"
        
        self.assertEqual(result, 0, message)
        
    def test_animal_add(self):
        """
        
        """
        zookeeper_1: ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id=1)
        fence_1: Fence = Fence(area=100, temperature=25.0, habitat="Savana")
        animal_1: Animal = Animal(name="Pluto", species="Canide", age=5, height=5.0, width=1.0, preferred_habitat="Savana")
        zookeeper_1.add_animal(animal_1, fence_1)
        result: int = len(fence_1.animals)
        message: str = f"Error: the function add_animal should not add self.animal_1 into self.fence_1"
        
        self.assertEqual(result, 1, message)
        
    
    


if __name__ == "__main__":
    
    unittest.main()
    
