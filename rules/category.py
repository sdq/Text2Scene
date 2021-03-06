#!./env python

### pre-defined categories

# from collections import defaultdict
surrouding_dict = dict()
# surrouding_dict['indoor'] = {'concrete': ['furniture', 'appliance', 'wall', 'ornament'], 'abstract': ['chart', 'art']}
# surrouding_dict['outdoor'] = {'city': ['street', 'building', 'vehicle'], 'field':['park', 'nature']}

## should we use explicit meaning of the words or use the max to let it more flexible?
# Counterexample:
#   wn.lch_similarity(wn.synset('stand.v.01'), wn.synset('stand.n.02'))
#       returns 0
#       because POS is different
#       But they are actually similar
#
surrouding_dict['room.n.01'] = {'object.n.01': ['furniture.n.01',
                                                  'appliance.n.02',
                                                  'wall.n.01',
                                                  'sundries.n.01'],
                                  'abstraction.n.01': ['chart.n.01', 'art.n.01']}

# why don't we use nested list?
# nested list has subordination ambiguity between strings and lists at each level

surrouding_dict['landscape.n.01'] = {'city.n.01': ['street.n.01',
                                                 'building.n.01',
                                                 'vehicle.n.01'],
                                   'nature.n.03':['park.n.02', 'wild.n.02']}
# print(surrouding_dict)

person_dict = dict()
# person_dict['interaction'] = ['business',
# 							  'concept',
# 							  'emotion',
# 							  'social',
# 							  'travel',
# 							  'enjoyment']
# person_dict['person'] = [{'stand': ['lean', 'back', 'front']},
# 						  'sit', 'sport', 'show', 'gesture']

person_dict['interaction.n.01'] = ['occupation.n.01',
                                   'abstraction.n.01', # is it okay to include exactly the same keyword?
                                   'emotion.n.01',
                                   'sociable.n.01',
                                   'travel.n.01',
                                   'enjoyment.n.02']

person_dict['person.n.02'] = [{'stand.v.01': ['lean.v.01', 'back.n.01', 'front.n.01']},
                               'sit.v.01', 'sport.n.01', 'show.v.01', 'gesture.n.01']
# print(person_dict)

