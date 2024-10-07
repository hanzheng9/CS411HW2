from typing import Any
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath
from wildlife_tracker.habitat_management.habitat import Habitat

class Migration:
    # methods: cancel_migration, get_migration_by_id, get_migration_details, get_migrations, get_migrations_by_current_location, get_migrations_by_start_date, get_migrations_by_status, get_migration_paths_by_species, get_migration_paths_by_start_location, schedule_migration, update_migration_details
    # properties: migration_id, current_location, start_date, status, species, start_location, migration_path
    def cancel_migration(migration_id: int) -> None:
        pass

    def get_migration_by_id(migration_id: int) -> Migration:
        pass

    def get_migration_details(migration_id: int) -> dict[str, Any]: 
        pass

    def get_migrations() -> list[Migration]:
        pass

    def get_migrations_by_current_location(current_location: str) -> list[Migration]:
        pass

    def get_migrations_by_start_date(start_date: str) -> list[Migration]:
        pass

    def get_migrations_by_status(status: str) -> list[Migration]:
        pass

    def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
        pass

    def schedule_migration(migration_path: MigrationPath) -> None:
        pass

    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass