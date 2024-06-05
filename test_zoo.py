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
        ciao
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
        
    def test_animal_dimension_andbar27(self):
        self.zk = ZooKeeper("gino","paoli","gp001")
        fence_1 = Fence(0, 0, "Savana")
        animal_1 = Animal("pino", "Cane", 1, 1, 1, "Savana")
        zookeeper_1 = ZooKeeper("gino", "paoli", "gp001")
        zookeeper_1.add_animal(animal_1, fence_1)
        result = len(fence_1.animals)
        message = f"Error: area is 0 so the animal should not add in the fence"
        self.assertEqual(result, 0, message) # Se result = 0 scrivi message

    def test_animal_habitat_andbar27(self):
        self.zk = ZooKeeper("gino","paoli","gp001")
        a2 = Animal("luna", "gatto", 7, 2, 2, "Casa")
        f2 = Fence(10, 10, "Savana")
        self.zk.add_animal(a2, f2)
        result = len(f2.animals)
        message = "Error: habitat is different, so the animal should not add in the fence"
        self.assertEqual(result, 0, message)
        
    def test_clean_andbar27(self):
        self.zk = ZooKeeper("gino","paoli","gp001")
        a2 = Animal("luna", "gatto", 7, 2, 2, "Savana")
        f2 = Fence(10, 10, "Savana")
        self.zk.add_animal(a2, f2)
        result = self.zk.clean(f2)
        message = "Error: result of clean is not right, Expected 0.667"
        self.assertEqual(result, 0.667, message)

        a2 = Animal("luna", "gatto", 7, 2, 2, "Savana")
        f2 = Fence(4, 10, "Savana")
        self.zk.add_animal(a2, f2)
        result = self.zk.clean(f2)
        message = "Error: result of clean is not right, Expected: 4"
        self.assertEqual(result, 4, message)

    def test_feed_andbar27(self):
        self.zk = ZooKeeper("gino","paoli","gp001")
        a1 = Animal("a1", "coniglio", 1, 2, 2, "gabbia")
        f1 = Fence(4, 1, "gabbia")
        self.zk.add_animal(a1, f1)
        self.zk.feed(a1)
        result = a1.height
        message = "Error: height must be already 2, because there isn't space in fence, Expected: 2"
        self.assertEqual(result, 2, message)

        a1 = Animal("a1", "coniglio", 1, 2, 2, "gabbia")
        f1 = Fence(5, 1, "gabbia")
        self.zk.add_animal(a1, f1)
        self.zk.feed(a1)
        result = a1.height
        message = "Error: height must be height + 2%, Expected: 2.04"
        self.assertEqual(result, 2*1.02, message)
    
    def test_remove_andbar27(self):
        self.zk = ZooKeeper("gino","paoli","gp001")
        a1 = Animal("a1", "coniglio", 1, 2, 2, "gabbia")
        f1 = Fence(4, 1, "gabbia")
        a2 = Animal("a2", "uccello", 1, 1, 1, "gabbia")
        self.zk.add_animal(a1, f1)
        result = False
        try:
            self.zk.remove_animal(a2, f1)
        except Exception:
            result = True
        message = "Runtime error, try to remove animal not present"
        self.assertEqual(result, False, message)
    
    


if __name__ == "__main__":
    
    unittest.main()
    
