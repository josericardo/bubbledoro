import json
from pprint import pprint

class Goal:

  def __init__(self, title):
    self.title = title

  def set_dedication(self, mins):
    self.mins = mins

  def __eq__(self, other):
    return self.title == other.title

class GoalsRepository:
  def __init__(self, repo_path='bubbledoro.json'):
    self.goals = []
    self.repo_path = repo_path

  def add(self, goal):
    self.goals.append(goal)

  def delete(self, goal):
    self.goals.remove(goal)

  def rename(self, old_goal, new_goal_title):
    for i, goal in enumerate(self.goals):
      if goal.title == old_goal:
        self.goals[i].title = new_goal_title

  def load(self):
    self.goals = json.loads(self.read_repo_file())

  def read_repo_file(self):
    f = open(self.repo_path, 'r')
    data = f.read()
    f.close()
    return '[]' if data == '' else data

  def persist(self):
    f = open(self.repo_path, 'w')
    f.write(json.dumps(self.goals))
    f.close()
