class EventSourcer():

    '''
        ApplyBoard Co-op Challenge
        --------------------------
        Time Complexities:
        Add, Subtract, Undo, Redo: O(1)
        Bulk Undo(steps), Bulk Redo(steps): O(steps)

        value -> Current Value 
        current_events -> List of current events, implemented like a stack
        discarded_events -> List of discarded events(via undo), implemented like a stack
    '''

    def __init__(self):
        self.value = 0
        self.current_events = []    
        self.discarded_events = []  

    def add(self, num: int):
        self.current_events.append(num)
        self.value += num

    def subtract(self, num: int):
        self.current_events.append(-num)
        self.value -= num

    def undo(self):
        if len(self.current_events) > 0:
            event = self.current_events.pop()
            self.value -= event
            self.discarded_events.append(event)

    def redo(self):
        if len(self.discarded_events) > 0:
            event = self.discarded_events.pop()
            self.value += event

    def bulk_undo(self, steps: int):
        while steps:
            self.undo()
            steps -= 1

    def bulk_redo(self, steps: int):
        while steps:
            self.redo()
            steps -= 1
