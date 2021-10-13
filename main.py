from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

from MoneyModel import MoneyModel

def agent_portrayal(agent):
    portrayal = {
      "Shape": "circle",
      "Filled": "true",
      "r": agent.wealth + 0.5}
    if agent.wealth > 2:
      portrayal["Color"] = "red"
      portrayal["Layer"] = 0
    elif agent.wealth > 1:
      portrayal["Color"] = "orange"
      portrayal["Layer"] = 2
    elif agent.wealth > 0:
      portrayal["Color"] = "yellow"
      portrayal["Layer"] = 3
    else:
      portrayal["Color"] = "lightgrey"
      portrayal["Layer"] = 4
    return portrayal

grid = CanvasGrid(
  agent_portrayal,
  30,
  30,
  800,
  800)

chart = ChartModule([{
  'Label': 'Gini',
  'Color': 'Black'}],
  data_collector_name='datacollector')

server = ModularServer(
  MoneyModel,
  [grid, chart],
  "Money Model",
  {"N":50, "width":30, "height":30}
  )
server.port = 8521 # Any non-80 port to appease replit
server.launch()