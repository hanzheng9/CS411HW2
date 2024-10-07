from typing import Any, Optional
from wildlife_tracker.animal_managment.animal import Animal # type: ignore

class Animal:
    # methods: get_animal_by_id, register_animal, get_animal_details, update_animal_details, assign_animals_to_habitat
    # properties: animal_id, animal
    def get_animal_by_id(animal_id: int) -> Optional[Animal]:
        pass

    def register_animal(animal: Animal) -> None:
        pass

    def get_animal_details(animal_id) -> dict[str, Any]:
        pass

    def remove_animal(animal_id: int) -> None:
        pass

    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass

