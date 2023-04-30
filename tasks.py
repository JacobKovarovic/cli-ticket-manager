from queues import Queue

class _AbstractTask():
    def __init__(self, title, description, leadTime, stages):
        self.category = type(self)
        self.title = title
        self.description = description
        self.leadTime = leadTime
        self.stages = Queue(stages)