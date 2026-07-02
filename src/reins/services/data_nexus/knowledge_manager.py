import os

# 100 GB limit in bytes
STORAGE_LIMIT_BYTES = 100 * 1024 * 1024 * 1024
KB_DIR = os.path.expanduser("~/data_rein/DATA/data_nexus_kb")

class KnowledgeManager:
    def __init__(self) -> None:
        if not os.path.exists(KB_DIR):
            os.makedirs(KB_DIR)

    def get_directory_size(self, path: str) -> int:
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return total_size

    def enforce_storage_limit(self) -> None:
        """
        Prunes the oldest files if the storage limit is exceeded.
        """
        current_size = self.get_directory_size(KB_DIR)
        if current_size <= STORAGE_LIMIT_BYTES:
            return

        # Gather all files with their modification times
        files_with_mtime = []
        for dirpath, _, filenames in os.walk(KB_DIR):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    files_with_mtime.append((fp, os.path.getmtime(fp), os.path.getsize(fp)))

        # Sort by oldest first
        files_with_mtime.sort(key=lambda x: x[1])

        # Delete until we are under 95% of the limit (9.5GB)
        target_size = int(STORAGE_LIMIT_BYTES * 0.95)
        
        for fp, _, size in files_with_mtime:
            if current_size <= target_size:
                break
            try:
                os.remove(fp)
                current_size -= size
            except OSError:
                pass

    def save_insight(self, filename: str, content: str) -> None:
        """
        Saves a new insight to the knowledge base and enforces storage limits.
        """
        filepath = os.path.join(KB_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        self.enforce_storage_limit()
