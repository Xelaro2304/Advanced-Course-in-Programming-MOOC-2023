# Write your solution here:
class Task:
    id = 0
    def __init__(self, description, programmer, workload):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        Task.id += 1
        self.id = Task.id
        self.status = 'NOT FINISHED'

    def is_finished(self):
        if self.status == 'FINISHED':
            return True
        else:
            return False
        
    def mark_finished (self):
        self.status = 'FINISHED'
    
    def __str__(self):
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.status}'
    
class OrderBook():
    def __init__(self):
        self.orders = []
    
    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders
    
    def programmers(self):
        programmers_list = [programmer.programmer for programmer in self.orders]
        programmers_list = list(set(programmers_list))
        return programmers_list

    def mark_finished(self, id):
        for task in self.orders:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError(f'Order with {id} does not exist')

    def finished_orders (self):
        return [order for order in self.orders if order.status == 'FINISHED']
    
    def unfinished_orders (self):
        return [order for order in self.orders if order.status == 'NOT FINISHED']

    def status_of_programmer(self, programmer: str):
        finished = self.finished_orders()
        unfinished = self.unfinished_orders()
        programmer_finished = [order.workload for order in finished if order.programmer == programmer]
        programmer_unfinished = [order.workload for order in unfinished if order.programmer == programmer]
        if programmer_finished == [] and programmer_unfinished == []:
            raise ValueError("Programmer does not exist")
        return (len(programmer_finished), len(programmer_unfinished), sum(programmer_finished), sum(programmer_unfinished))
