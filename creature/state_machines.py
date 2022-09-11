from timer import Timer
from settings import settings

class State_machines():
    def __init__(self, behaviours):

        self.vs1 = Vspeed(init_position=behaviours.output_1_INTITIAL, result="int")
        self.vs1.set_bounds(lower_bound=behaviours.output_1_MIN, upper_bound=behaviours.output_1_MAX)

        self.vs2 = Vspeed(init_position=behaviours.output_2_INTITIAL, result="int")
        self.vs2.set_bounds(lower_bound=behaviours.output_2_MIN, upper_bound=behaviours.output_2_MAX)

        self.last_energy = 0
        self.energy = 0
        self.timer = Timer()
        self.timer.set_duration(1)
        self.last_state = 0
        self.state = 0 # Our state starts at 0, it can go up to 3. We use this number to keep track of 2 on or off variables
    # One variable is whether we have company. Here we use either 0 or 1 for this.
    # The second variable is whether it is day or night, for this we use 0 or 2.
    # When we combine these numbers we get either 0, 1, 2 or 3. Every combination of variables leads to a different number, thus we don't need to remember 2 numbers. Only this one.
    def setTime(self, time):
        self.last_state = self.state
        tempState = self.state%2 # State%2 means keep removing 2 from the number until we can't anymore. Meaning our number will end up being either 1 or 0. Thus we will know whether we have company or not.
        self.state = tempState + time * 2 # Then we add either 2 or 0, saving whether it is day or night.

    def setCompany(self, company):
        self.last_state = self.state
        if company != self.state%2:
            self.timer.start()
            self.timer.set_duration(1 + 9*(1-company))
        tempState = (self.state - self.state%2) # Here we remove either 0 or 1 from state. Thus making our state either 0 or 2. Thus we will know whether it is day or night.
        self.state = tempState + company # Then we add either 0 or 1, saving whether we have company or not.

    def incrementEnergy(self):
        self.energy = min(self.energy+1, 10)
        print("Energy level increased to ", self.energy)

    def checkEnergy(self, mqtt_client):
        if self.timer.expired():
            self.timer.start()
            self.last_energy = self.energy
            if self.state%2 == 1:
                self.energy = min(self.energy+1, 10)
            else:
                self.energy = max(self.energy-1, 0)
            mqtt_client.publish("energy-level", settings["clientid"]+", "+str(self.energy))
            if not self.last_energy == self.energy:
                print("Energy level: "+str(self.energy))

#     def behave(self, behaviours, mqtt_client):
    def behave(self, behaviours):
        # update energy
#         self.checkEnergy(mqtt_client)
        behaviours.energy = self.energy

        # get values
        if self.state == 0:
            output_1_value, running_1, changed_1 = self.vs1.sequence(behaviours.output_1_night_no_company_behaviour, loop_max=0)
            output_2_value, running_2, changed_2 = self.vs2.sequence(sequence=behaviours.output_2_night_no_company_behaviour,
                                                                     loop_max=0)
            if changed_1 or changed_2:
                behaviours.behave_night_no_company(output_1_value, output_2_value)
        elif self.state == 1:
            output_1_value, running_1, changed_1 = self.vs1.sequence(sequence=behaviours.output_1_night_company_behaviour,
                                                                     loop_max=0)
            output_2_value, running_2, changed_2 = self.vs2.sequence(sequence=behaviours.output_2_night_company_behaviour,
                                                                     loop_max=0)

            if changed_1 or changed_2:
                behaviours.behave_night_company(output_1_value, output_2_value)
        elif self.state == 2:
            output_1_value, running_1, changed_1 = self.vs1.sequence(sequence=behaviours.output_1_day_no_company_behaviour,
                                                                     loop_max=0)
            output_2_value, running_2, changed_2 = self.vs2.sequence(sequence=behaviours.output_2_day_no_company_behaviour,
                                                                     loop_max=0)

            if changed_1 or changed_2:
                behaviours.behave_day_no_company(output_1_value, output_2_value)
        else:
            output_1_value, running_1, changed_1 = self.vs1.sequence(sequence=behaviours.output_1_day_company_behaviour,
                                                                     loop_max=0)
            output_2_value, running_2, changed_2 = self.vs2.sequence(sequence=behaviours.output_2_day_company_behaviour,
                                                                     loop_max=0)

            if changed_1 or changed_2:
                behaviours.behave_day_company(output_1_value, output_2_value)
