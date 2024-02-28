from queue import Queue
import time
import random

class QueueHandler:
    def __init__(self):
        self.q = Queue()
        self.request_id = 0

    def generate_request(self, request_body):
        request_data = f"Заявка #{self.request_id} - {request_body}"
        if random.random() > 0.5:
            self.request_id += 1
            self.q.put(request_data)
            print(f"Згенеровано нову заявку: {request_data}")

    def process_request(self):
        if random.random() > 0.5:
            if not self.q.empty():
                request_data = self.q.get()
                print(f"Обробили заявку: {request_data}")
            else:
                print("Черга пуста. Заявок немає")    

def main():
    possible_requests = ["Technical issue", "Sale", "Question"]
    handler = QueueHandler()
    try:
        while True:
            handler.generate_request(random.choice(possible_requests))
            time.sleep(0.5)
            handler.process_request()
            time.sleep(0.5)
    except:
        print("Stopped")        
 
main()       