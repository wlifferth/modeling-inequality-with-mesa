from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.batchrunner import BatchRunner


def compute_gini(model):
    # Do math here!
    return 0


class MoneyAgent(Agent):
    """An agent with hopes, dreams, and a mysterious past."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
      pass


class MoneyModel(Model):
    """Our model--a home for our agents :)"""
    def __init__(self, N, width, height):
        # A physical world to place our agents in 
        self.grid = MultiGrid(width, height, True)

        # Some metrics we'll measure about our model
        self.datacollector = DataCollector(
            model_reporters={"Gini": compute_gini},
            agent_reporters={"Wealth": "wealth"},
        )

    def step(self):
        """Runs a single tick of the clock in our simulation."""
        self.datacollector.collect(self)
        self.schedule.step()
