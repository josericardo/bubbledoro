from bubbledoro.goals import *
from pprint import pprint
import unittest

TEST_REPO_PATH = 'bubbledoro/tests/bubbledoro_test_repo'

class IntegrationTest(unittest.TestCase):

  def persistence_works_test(self):
    goals = [Goal('Goal 1', 120), Goal('Goal 2')]
    repo = GoalsRepository(TEST_REPO_PATH)

    for g in goals:
      repo.add(g)

    repo.persist()

    repo2 = GoalsRepository(TEST_REPO_PATH)
    repo2.load()

    self.assertEqual(goals, repo2.goals)

  def tearDown(self):
    from subprocess import call
    call(["rm", "-rf", TEST_REPO_PATH])
