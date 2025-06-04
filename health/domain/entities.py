class HealthRecord:
    def __init__(self, device_id, bpm, created_at, id=None):
        self.id = id
        self.device_id = device_id
        self.bpm = bpm
        self.created_at = created_at