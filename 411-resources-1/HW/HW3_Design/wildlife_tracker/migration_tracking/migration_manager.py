from typing import Optional
from typing import Any
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationManager:
    # methods: get_migration_details, schedule_migration, update_migration_details, get_migrations_by_migration_path, remove_migration_path,update_migration_path_details
    # properties: migration_id, migration_path, migration_path_id, path_id
    def get_migration_details(migration_id: int) -> dict[str, Any]: 
        pass

    def schedule_migration(migration_path: MigrationPath) -> None:
        pass

    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass

    def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
        pass

    def remove_migration_path(path_id: int) -> None:
        pass

    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass
