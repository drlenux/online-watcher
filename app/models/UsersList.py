import time
import threading
from typing import Dict

from app.models.User import User


class UsersList:
    def __init__(self, save_time: int = 5):
        self.cleanup_thread = None
        self.list: Dict[str, User] = {}
        self.save_time = save_time
        self.running = True
        self.lock = threading.Lock()

    def add(self, uuid: str):
        now = time.time()
        with self.lock:
            if uuid not in self.list:
                self.list[uuid] = User(id=uuid, last_visit=int(now), hit=1)
            else:
                self.list[uuid].last_visit = int(now)
                self.list[uuid].hit += 1

    def cleanup(self):
        while self.running:
            with self.lock:
                now = time.time()
                to_remove = [user for user, details in self.list.items() if details.last_visit + self.save_time < now]
                for user in to_remove:
                    del self.list[user]

            time.sleep(self.save_time)

    def count(self) -> int:
        with self.lock:
            return len(self.list)

    def count_hits(self) -> int:
        res = 0
        with self.lock:
            for _, user in self.list.items():
                res += user.hit

        return res

    def start_cleanup(self):
        self.cleanup_thread = threading.Thread(target=self.cleanup)
        self.cleanup_thread.start()

    def stop_cleanup(self):
        self.running = False
        self.cleanup_thread.join()
