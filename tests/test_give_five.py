from unittest import TestCase
from dummy.Dummy import give_five


class TestGive_five(TestCase):
    def test_give_five(self):
        self.assertEquals(give_five(), 5)
