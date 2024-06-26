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

class OrderBookApp:
    def __init__(self):
        self.__orderbook = OrderBook()

    def instructions(self):
            print ('commands:')
            print ('0 exit')
            print ('1 add order')
            print ('2 list finished tasks')
            print ('3 list unfinished tasks')
            print ('4 mark task as finished')
            print ('5 programmers')
            print ('6 status of programmer')

    def execute(self):
        self.instructions()
        while True:
            try:
                command = int(input('command: '))
            except:
                print('erroneous input')
                continue
            if command == 0:
                break
            if command == 1:
                self.add_order()
            if command == 2:
                self.finished_tasks()
            if command == 3:
                self.unfinished_tasks()
            if command == 4:
                self.mark_finished()
            if command == 5:
                self.programmers()
            if command == 6:
                self.programmer_status()
            if command < 0 or command > 6:
                print('erroneous input')
                continue

    def add_order(self):
        try:    
            description = input('description: ')
            programmer_and_time = input('programmer and workload estimate: ')
            programmer_and_time = programmer_and_time.split(' ')
            programmer = programmer_and_time[0]
            workload = int(programmer_and_time[1])
            self.__orderbook.add_order(description, programmer, workload)
        except:
            print('erroneous input')
            return
        print('added!')

    def finished_tasks(self):
        finished = self.__orderbook.finished_orders()
        if finished == []:
            print('no finished tasks: ')
        else:
            for task in finished:
                print (task)

    def unfinished_tasks(self):
        unfinished = self.__orderbook.unfinished_orders()
        if unfinished == []:
            print('no unfinished tasks')
        else:
            for task in unfinished:
                print (task)

    def mark_finished(self):
        try:
            id = int(input('id: '))
            self.__orderbook.mark_finished(id)
        except:
            print('erroneous input')
            return
        print('marked as finished')

    def programmers(self):
        programmers_list = self.__orderbook.programmers()
        for programmer in programmers_list:
            print(programmer)
    
    def programmer_status(self):
        try:
            programmer = input('programmer: ')
            programmer_status = self.__orderbook.status_of_programmer(programmer)
        except ValueError:
            print('erroneous input')
            return
        print(f'tasks: finished {programmer_status[0]} not finished {programmer_status[1]}, hours: done {programmer_status[2]} scheduled {programmer_status[3]}')


order_app = OrderBookApp()
order_app.execute()
