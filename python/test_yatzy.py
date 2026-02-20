from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


import pytest

class TestYatzy:
        def test_chance(self):
                assert Yatzy.chance(1,2,3,4,5) == 15

        def test_yatzy(self):
                assert Yatzy.yatzy([2,2,2,2,2]) == 50
                assert Yatzy.yatzy([1,2,3,4,5]) == 0

        def test_ones(self):
                assert Yatzy.ones(1,1,1,1,1) == 5
                assert Yatzy.ones(2,3,4,5,6) == 0

        def test_twos(self):
                assert Yatzy.twos(2,2,2,2,2) == 10
                assert Yatzy.twos(1,3,4,5,6) == 0

        def test_threes(self):
                assert Yatzy.threes(3,3,3,3,3) == 15
                assert Yatzy.threes(1,2,4,5,6) == 0


        # Métodos únicos, sin duplicados
        def test_fours(self):
                y = Yatzy(4,4,4,4,4)
                assert y.fours() == 20
                y = Yatzy(1,2,3,5,6)
                assert y.fours() == 0

        def test_fives(self):
                y = Yatzy(5,5,5,5,5)
                assert y.fives() == 25
                y = Yatzy(1,2,3,4,6)
                assert y.fives() == 0

        def test_sixes(self):
                y = Yatzy(6,6,6,6,6)
                assert y.sixes() == 30
                y = Yatzy(1,2,3,4,5)
                assert y.sixes() == 0

        def test_score_pair(self):
                assert Yatzy.score_pair(3,3,2,4,5) == 6
                assert Yatzy.score_pair(1,2,3,4,5) == 0

        def test_two_pair(self):
                assert Yatzy.two_pair(3,3,5,5,2) == 16
                assert Yatzy.two_pair(1,2,3,4,5) == 0

        def test_three_of_a_kind(self):
                assert Yatzy.three_of_a_kind(2,2,2,4,5) == 6
                assert Yatzy.three_of_a_kind(1,2,3,4,5) == 0

        def test_four_of_a_kind(self):
                assert Yatzy.four_of_a_kind(4,4,4,4,2) == 16
                assert Yatzy.four_of_a_kind(1,2,3,4,5) == 0

        def test_smallStraight(self):
                assert Yatzy.smallStraight(1,2,3,4,5) == 15
                assert Yatzy.smallStraight(2,3,4,5,6) == 0

        def test_largeStraight(self):
                assert Yatzy.largeStraight(2,3,4,5,6) == 20
                assert Yatzy.largeStraight(1,2,3,4,5) == 0

        def test_fullHouse(self):
                assert Yatzy.fullHouse(2,2,3,3,3) == 13
                assert Yatzy.fullHouse(1,2,3,4,5) == 0
