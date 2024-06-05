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
    
    def test_the_vilgax(self):
        """
        Questo test evoca Vilgax se fallisci.
        """
        zoo_keeper_test:ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id="1")
        fence_test:Fence = Fence(area=100, temperature=25.0, habitat="Steppa")
        animal_test:Animal = Animal(name="Pluto", species="Canide", age=5,
                                    height=5.5, width=2.0, 
                                    preferred_habitat="Steppa")
        zoo_keeper_test.add_animal(animal_test, fence_test)
        result:int = len(fence_test.animals)
        message:str = f"Error, the function didn't add the animal to the fence."

        counter = 0
        if result != 1:
            while counter < 100000:
                counter += 1
                print("V I L G A X")

        self.assertEqual(result, 1, message)

    def test_gar(self):
        zoo_keeper_test:ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id="1")
        fence_test:Fence = Fence(area=100, temperature=25.0, habitat="Steppa")
        animal_test:Animal = Animal(name="Pluto", species="Canide", age=5,
                                    height=5.5, width=2.0, 
                                    preferred_habitat="Steppa")
        zoo_keeper_test.add_animal(animal_test, fence_test)
        zoo_keeper_test.remove_animal(animal_test, fence_test)
        message:str = f"Error, the function didn't remove the animal from the fence."
        result:int = len(fence_test.animals)

        self.assertEqual(result, 0, message)

    def test_eatle(self):
        zoo_keeper_test:ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id="1")
        fence_test:Fence = Fence(area=100, temperature=25.0, habitat="Steppa")
        animal_test:Animal = Animal(name="Pluto", species="Canide", age=5,
                                    height=5.5, width=2.0, 
                                    preferred_habitat="Steppa")
        zoo_keeper_test.add_animal(animal_test, fence_test)
        zoo_keeper_test.feed(animal_test)
        result:int = round(animal_test.area, 3)
        message:str = f"Error, the function didn't feed the animal correctly {result}."

        self.assertEqual(result, 11.444, message)

    def test_sudato(self):
        zoo_keeper_test:ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id="1")
        fence_test:Fence = Fence(area=100, temperature=25.0, habitat="Steppa")
        animal_test:Animal = Animal(name="Pluto", species="Canide", age=5,
                                    height=5.5, width=2.0, 
                                    preferred_habitat="Steppa")
        zoo_keeper_test.add_animal(animal_test, fence_test)
        result = round(zoo_keeper_test.clean(fence_test), 3)
        message:str = f"Error, the function didn't clean the fence correctly."

        self.assertEqual(result, 0.124, message)

    def test_golgoroth(self):
        try:
            zoo_keeper_test:ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id="1")
            fence_test:Fence = Fence(area=100, temperature=25.0, habitat="Steppa")
            animal_test:Animal = Animal(name="Pluto", species="Canide", age=5,
                                        height=5.5, width=2.0, 
                                        preferred_habitat="Steppa")
            zoo_keeper_test.feed(animal_test)
            result:int = round(animal_test.area, 3)
            message:str = f"Error, the function feed the animal even if the animal wasn't in a fence."

            self.assertEqual(result, 11, message)
        except Exception:
            raise RuntimeError("The code crashed.")
        
    def test_vilgax1(self):
        """
        Questo test evoca Vilgax se fallisci (1).
        """
        try:
            zoo_keeper_test:ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id="1")
            fence_test:Fence = Fence(area=0, temperature=25.0, habitat="Steppa")
            animal_test:Animal = Animal(name="Pluto", species="Canide", age=5,
                                        height=0, width=0, 
                                        preferred_habitat="Steppa")
            zoo_keeper_test.add_animal(animal_test, fence_test)
            zoo_keeper_test.feed(animal_test)
            result:int = round(animal_test.area, 3)
            message:str = f"Error, the result has to be zero since the test result is evil."

            self.assertEqual(result, 0, message)
        except Exception:
            raise RuntimeError("VILGAX CONQUERED YOUR PC MORTAL, SURREDER OR YOU'LL BE ENDED.")
        
    def test_vilgax2(self):
        """
        Questo test evoca Vilgax se fallisci (2).
        """
        try:
            zoo_keeper_test:ZooKeeper = ZooKeeper(name=None, surname=None, id=None)
            fence_test:Fence = Fence(area=None, temperature=None, habitat="Alfonso")
            animal_test:Animal = Animal(name=None, species=None, age=None,
                                        height=None, width=None, 
                                        preferred_habitat="Alfonso")
            zoo_keeper_test.add_animal(animal_test, fence_test)
            counter:int = animal_test.area
            zoo_keeper_test.feed(animal_test)
            result:int = animal_test.area
            message:str = f"Error, the result has to be zero since the test result is evil."

            self.assertEqual(result, counter, message)
        except Exception:
            raise RuntimeError("VILGAX CONQUERED YOUR PC MORTAL, SURREDER OR YOU'LL BE ENDED.")
        
    def test_vilgax3(self):
        """
        Questo test evoca Vilgax se fallisci (3).
        """
        try:
            zoo_keeper_test:ZooKeeper = ZooKeeper(name=None, surname=None, id=None)
            fence_test:Fence = Fence(area=None, temperature=None, habitat="Alfonso")
            animal_test:Animal = Animal(name=None, species=None, age=None,
                                        height=None, width=None, 
                                        preferred_habitat="Alfonso")
            zoo_keeper_test.add_animal(animal_test, fence_test)
            result:int = round(zoo_keeper_test.clean(fence_test), 3)
            message:str = f"Error, the result has to be zero or None since the test result is evil."
            if result != 0 or result != None:
                counter:bool = False
            else:
                counter:bool = True

            self.assertEqual(counter, 0, message)
        except Exception:
            raise RuntimeError("VILGAX CONQUERED YOUR PC MORTAL, SURREDER OR YOU'LL BE ENDED.")
        
    def test_vilgax4(self):
        """
        Questo test evoca Vilgax se fallisci (4).
        """
        try:
            zoo_keeper_test:ZooKeeper = ZooKeeper(name=None, surname=None, id=None)
            fence_test:Fence = Fence(area=None, temperature=None, habitat=None)
            animal_test:Animal = Animal(name=None, species=None, age=None,
                                        height=None, width=None, 
                                        preferred_habitat="Alfonso")
            zoo_keeper_test.add_animal(animal_test, fence_test)
            result:int = round(zoo_keeper_test.clean(fence_test), 3)
            message:str = f"Error, the result has to be zero since the test result is evil."
            if result != 0 or result != None:
                counter:bool = False
            else:
                counter:bool = True

            self.assertEqual(counter, 0, message)
        except Exception:
            raise RuntimeError("VILGAX CONQUERED YOUR PC MORTAL, SURREDER OR YOU'LL BE ENDED.")
    
    def test_vilgax5(self):
        """
        Questo test evoca Vilgax se fallisci (5).
        """
        try:
            zoo_keeper_test:ZooKeeper = ZooKeeper(name=None, surname=None, id=None)
            fence_test:Fence = Fence(area=None, temperature=None, habitat=None)
            animal_test:Animal = Animal(name=None, species=None, age=None,
                                        height=None, width=None, 
                                        preferred_habitat="Alfonso")
            zoo_keeper_test.add_animal(animal_test, fence_test)
            result:int = round(zoo_keeper_test.clean(fence_test), 3)
            message:str = f"Error, the result has to be zero since the test result is evil."
            if result != 0 or result != None:
                counter:bool = False
            else:
                counter:bool = True

            self.assertEqual(counter, 0, message)
        except Exception:
            raise RuntimeError("VILGAX CONQUERED YOUR PC MORTAL, SURREDER OR YOU'LL BE ENDED.")

    


if __name__ == "__main__":
    
    unittest.main()
    
