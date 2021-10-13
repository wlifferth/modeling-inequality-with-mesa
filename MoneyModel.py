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
        self.wealth = 1

    def step(self):
      self.move()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
          self.pos,
          moore=False,
          include_center=True)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)


class MoneyModel(Model):
    """Our model--a home for our agents :)"""
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        # A physical world to place our agents in 
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        # Some metrics we'll measure about our model
        self.datacollector = DataCollector(
            model_reporters={"Gini": compute_gini},
            agent_reporters={"Wealth": "wealth"},
        )

    def step(self):
        """Runs a single tick of the clock in our simulation."""
        self.datacollector.collect(self)
        self.schedule.step()
