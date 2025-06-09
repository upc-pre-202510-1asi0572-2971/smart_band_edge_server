from health.domain.services import HealthRecordService
from health.infrastructure.repositories import HealthRecordRepository
from iam.application.services import AuthApplicationService


class HealthApplicationService:
    def __init__(self):
        self.health_record_repository = HealthRecordRepository()
        self.health_record_service = HealthRecordService()
        self.iam_service = AuthApplicationService()

    def create_health_record(self, device_id: str,bpm: float, created_at: str, api_key: str):
        # Validate API key
        if not self.iam_service.get_device_by_id_and_api_key(device_id, api_key):
            raise ValueError("Device not found or Invalid API key")

        # Create health record
        record = self.health_record_service.create_record(device_id, bpm, created_at)
        return self.health_record_repository.save(record)

