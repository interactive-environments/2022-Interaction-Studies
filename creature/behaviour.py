class Behaviour:
    def __init__(self, behaviour_id, sequence_1=[], sequence_2=[], run_function=None):
        self.behaviour_id = behaviour_id
        self.sequence_1 = sequence_1
        self.sequence_2 = sequence_2
        self.run_function = run_function