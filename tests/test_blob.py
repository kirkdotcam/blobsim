import pytest
from src import Blob

pop = Blob.gen_population(100)

def test_generation_len():
    assert len(pop) == 100

def test_report():
    report = pop[0].report()
    assert report["hunger"] == False
    assert report["diet"] == "carnivore" or report["diet"] == "herbivore"
    assert report["alive"] == True
    assert 0 <report["size"] < 120


def test_survive():
    blob = pop[0]
    assert blob.resources["food"]==1000
    blob.hunger = True
    blob.survive(pop)
    assert blob.resources["food"] < 1000

