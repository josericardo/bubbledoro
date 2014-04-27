import unittest
from bubbledoro.goals import *

class GoalsRepositoryTest(unittest.TestCase):

  def setUp(self):
    self.repo = GoalsRepository()

  def goals_can_be_saved_test(self):
    self.repo.add(Goal('New Goal'))
    self.assertEqual(1, len(self.repo.goals))

  def goals_can_be_deleted_test(self):
    self.repo.add(Goal('A goal'))
    self.repo.delete(Goal('A goal'))
    self.assertEqual(0, len(self.repo.goals))

  def a_goal_can_be_renamed_test(self):
    self.repo.add(Goal('A goal'))
    self.repo.rename('A goal', 'Another goal')
    self.assertEqual(Goal('Another goal'), self.repo.goals[0])
