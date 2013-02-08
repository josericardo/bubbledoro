import json

class Goal:

  def __init__(self, title):
    self.title = title

  def set_dedication(self, mins):
    self.mins = mins

  def __eq__(self, other):
    return self.title == other.title

class GoalsRepository:
  def __init__(self, repo_file='~/.bubbledoro'):
    self.goals = []
    self.repo_file = repo_file 

  def add(self, goal):
    self.goals.append(goal)

  def delete(self, goal):
    self.goals.remove(goal)

  def rename(self, old_goal, new_goal_title):
    for i, goal in enumerate(self.goals):
      if goal.title == old_goal:
        self.goals[i].title = new_goal_title

  def goals(self):
    return self.goals

  def repo(self):
    return open(self.repo_file, 'w+b')

  def load(self):
    goals = json.load(self.repo().read())
    self.repo().close()

  def persist(self):
    self.repo().write(json.dumps(self.goals))
    self.repo().close()
