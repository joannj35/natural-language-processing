test = {   'name': 'causal_attention_mask',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> T = 5;\n>>> mask = causal_mask(T);\n>>> mask.size() == torch.Size([T, T])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> T = 5;\n>>> mask = causal_mask(T);\n>>> mask[0, 0].item() == True # y_1 can attend to y_0\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> T = 5;\n>>> mask = causal_mask(T);\n>>> (mask[0, 1:] == False).all().item() # y_1 cannot attend to y_1, y_2, ...\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> T = 5;\n>>> mask = causal_mask(T);\n>>> mask[1, 0:2].all().item() == True # y_2 can attend to y_1, y_0\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> T = 5;\n>>> mask = causal_mask(T);\n>>> (mask[1, 2:] == False).all().item() # y_2 cannot attend to y_2, ...\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
