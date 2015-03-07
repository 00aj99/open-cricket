from elasticsearch import Elasticsearch

index_settings='{  "settings": {    "index": {      "analysis": {        "filter": {          "stemmer": {            "type": "stemmer",            "language": "english"          },          "autocompleteFilter": {            "max_shingle_size": "5",            "min_shingle_size": "2",            "type": "shingle"          },          "stopwords": {            "type": "stop",            "stopwords": [              "_english_"            ]          }        },        "analyzer": {          "didYouMean": {            "filter": [              "lowercase"            ],            "char_filter": [              "html_strip"            ],            "type": "custom",            "tokenizer": "standard"          },          "autocomplete": {            "filter": [              "lowercase",              "autocompleteFilter"            ],            "char_filter": [              "html_strip"            ],            "type": "custom",            "tokenizer": "standard"          },          "default": {            "filter": [              "lowercase",              "stopwords",              "stemmer"            ],            "char_filter": [              "html_strip"            ],            "type": "custom",            "tokenizer": "standard"          }        }      }    }  }  }'
mapping='{  "player_stats": {    "properties": {      "autocomplete": {        "type": "string",        "analyzer": "autocomplete"      },      "did_you_mean": {        "type": "string",        "analyzer": "didYouMean"      },      "question": {        "type": "string",        "copy_to": [          "autocomplete",          "did_you_mean"        ]      }    }  }  }'

def es_suggestion(search_string):
    return '{"suggest":{"didYouMean":{"text":"%s","phrase":{"field":"did_you_mean"}}},"query":{"match":{"question":"%s"}}}' % (search_string, search_string)

def es_fuzzy_match(search_string):
    return '{"query":{"match":{"question":{"query":"%s","fuzziness":3,"prefix_length":2}}}}' % search_string


def es_builder(hosts=None):
    if (hosts == None): hosts = '127.0.0.1'
    return Elasticsearch(hosts=hosts)
