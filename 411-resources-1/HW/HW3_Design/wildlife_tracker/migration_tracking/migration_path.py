from typing import Optional
from typing import Any
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    # methods: get_migration_path_details, create_migration_path, get_migrations_by_migration_path, remove_migration_path, update_migration_path_details
    # properties: path_id, species, migration_path_id
    def get_migration_path_details(path_id) -> dict:
        pass

    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
        pass

    def remove_migration_path(path_id: int) -> None:
        pass

    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass