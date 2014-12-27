import unittest
import json

from opencricket.chart.sentence_parser import SentenceParser


class TestMostX(unittest.TestCase):

    def setUp(self):
        self.input_sixes = 'who has the most sixes'
        self.expected_sixes = '{"most_x": {"most": "most", "who_player": {"who": "who"}, "metric": "sixes", "filler": {"filler": "the"}}}'

        self.input_match_type = 'who has the most fours in odi'
        self.expected_match_type = '{"most_x": {"filler": "in", "match_type": "odi", "who_player": {"who": "who"}, "metric": "fours", "most": "most"}}'

        self.input_which_player = 'which player has the most sixes'
        self.expected_which_player = '{"most_x": {"filler": {"filler": "the"}, "who_player": {"which_player": {"which": "which", "player": "player"}}, "most": "most", "metric": "sixes"}}'

        self.input_ground = 'which player has the most sixes in Chennai'
        self.expected_ground = '{"most_x": {"filler": "in", "who_player": {"which_player": {"which": "which", "player": "player"}}, "most": "most", "metric": "sixes", "ground": {"ground1": "chennai"}}}'

        self.input_series_year = 'which player has the most sixes in world cup 2011'
        self.expected_series_year = '{"most_x": {"metric": "sixes", "filler": "in", "series": {"series2": "cup", "series1": "world"}, "most": "most", "year": "2011", "who_player": {"which_player": {"which": "which", "player": "player"}}}}'

        self.input_match_type_year = 'which player has the most runs in 2011 in test'
        self.expected_match_type_year = '{"most_x": {"year": "2011", "metric": "runs", "match_type": "test", "most": "most", "filler": "in", "who_player": {"which_player": {"which": "which", "player": "player"}}}}'

    def test_search_sixes(self):
        parser = SentenceParser(self.input_sixes)
        self.assertEqual(json.loads(self.expected_sixes), json.loads(parser.parse_sentence()))

    def test_search_match_type(self):
        parser = SentenceParser(self.input_match_type)
        self.assertEqual(json.loads(self.expected_match_type), json.loads(parser.parse_sentence()))

    def test_search_which_player(self):
        parser = SentenceParser(self.input_which_player)
        self.assertEqual(json.loads(self.expected_which_player), json.loads(parser.parse_sentence()))

    def test_search_ground(self):
        parser = SentenceParser(self.input_ground)
        self.assertEqual(json.loads(self.expected_ground), json.loads(parser.parse_sentence()))

    def test_search_series_year(self):
        parser = SentenceParser(self.input_series_year)
        self.assertEqual(json.loads(self.expected_series_year), json.loads(parser.parse_sentence()))

    def test_search_match_type_year(self):
        parser = SentenceParser(self.input_match_type_year)
        self.assertEqual(json.loads(self.expected_match_type_year), json.loads(parser.parse_sentence()))

if __name__ == '__main__':
    unittest.main()

