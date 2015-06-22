from opencricket.config import word_config
from opencricket.chart import syntax_expansions


def syntax():
    base_syntax_most_x = """most_x -> who_player word_has word_the word_most metric"""
    return """
        %s
        %s
        %s
        %s
        %s
        %s
        %s
        %s
        who_player -> word_who
        who_player -> word_which word_player
        who_player -> word_which teamplayer word_player
        who_player -> word_which word_captain
        who_player -> word_which teamplayer word_captain
        who_player -> word_which words_wicket_keeper
        who_player -> word_which teamplayer words_wicket_keeper
        word_who -> 'who'
        word_which -> 'which'
        word_player -> 'player'
        word_most -> 'highest' | 'most' | 'best'
        word_the -> 'the'
        %s
        %s
        %s
        %s
        %s
        %s
        %s
        %s
        %s
        %s
        %s
        """ % (base_syntax_most_x,
               syntax_expansions.expand_with_filters(base_syntax_most_x,
                                                     ['word_against team',
                                                      'word_batting word_wkt_order',
                                                      'word_in word_a words_single_innings',
                                                      'word_in word_a words_single_match',
                                                      'word_in word_a words_single_series',
                                                      'word_in word_a words_single_year',
                                                      'word_in word_a words_single_ground']),
               syntax_expansions.definition_for_expansion_filters('nlp_number'),
               word_config.cfg_helpers['metric'],
               word_config.cfg_helpers['team'],
               word_config.cfg_helpers['word_against'],
               word_config.cfg_helpers['word_has'],
               word_config.cfg_helpers['word_captain'],
               word_config.cfg_helpers['word_in'],
               word_config.cfg_helpers['word_a'],
               word_config.cfg_helpers['word_batting'],
               word_config.cfg_helpers['word_wkt_order'],
               word_config.cfg_helpers['words_single_innings'],
               word_config.cfg_helpers['words_single_match'],
               word_config.cfg_helpers['words_single_series'],
               word_config.cfg_helpers['words_single_year'],
               word_config.cfg_helpers['words_single_ground'],
               word_config.cfg_helpers['words_wicket_keeper'],
               word_config.cfg_helpers['teamplayer'])