[![Travis Build Status](https://travis-ci.org/douglaskastle/lwo_strut.svg?branch=master)](https://travis-ci.org/douglaskastle/lwo_strut)
[![Github Build Status](https://github.com/douglaskastle/lwo_strut/workflows/lwo_struct/badge.svg)](https://github.com/douglaskastle/lwo_strut/actions)
[![CircleCI](https://circleci.com/gh/douglaskastle/lwo_strut.svg?style=svg)](https://circleci.com/gh/douglaskastle/lwo_strut)

# lwo_strut

This is a python only parser of the Lightwave format LWO.  This code was originally lifted from the blender project, however this is only the part that reads the lwo file and loads it into a python object.  

The subsequent conversion into a blender format has been excised so there is no requirement on the bpy module. 

This code can be run on a standard python install, starting from 3.6. Please refer to the CI session to see it in operation.

    from lwo_strut.lwoObject import lwoObject
    
    infile = "tests/basic/src/LWO2/box/box0.lwo"
    x = lwoObject(infile)
    x.read()
    
    x.pprint()
    
    OrderedDict([('layers',
              ([OrderedDict([('name', 'Layer 1'),
                             ('index', 0),
                             ('parent_index', -1),
                             ('pivot', [0.0, 0.0, 0.0]),
                             ('pols',
                              [[3, 2, 1, 0],
                               [1, 5, 4, 0],
                               [2, 6, 5, 1],
                               [7, 6, 2, 3],
                               [4, 7, 3, 0],
                               [5, 6, 7, 4]]),
                             ('bones', []),
                             ('bone_names', {}),
                             ('bone_rolls', {}),
                             ('pnts',
                              [[-0.5, -0.5, -0.5],
                               [0.5, -0.5, -0.5],
                               [0.5, 0.5, -0.5],
                               [-0.5, 0.5, -0.5],
                               [-0.5, -0.5, 0.5],
                               [0.5, -0.5, 0.5],
                               [0.5, 0.5, 0.5],
                               [-0.5, 0.5, 0.5]]),
                             ('vnorms', {}),
                             ('lnorms', {}),
                             ('wmaps', {}),
                             ('colmaps', {}),
                             ('uvmaps_vmad', {}),
                             ('uvmaps_vmap', {}),
                             ('morphs', {}),
                             ('edge_weights', {}),
                             ('surf_tags', {1: [0, 1, 2, 3, 4, 5]}),
                             ('has_subds', False)])],)),
             ('surfs',
              ({'Default': OrderedDict([('bl_mat', None),
                                        ('name', 'Default'),
                                        ('source_name', ''),
                                        ('colr',
                                         (0.7843137383460999,
                                          0.7843137383460999,
                                          0.7843137383460999)),
                                        ('diff', 1.0),
                                        ('lumi', 0.0),
                                        ('spec', 0.0),
                                        ('refl', 0.0),
                                        ('rblr', 0.0),
                                        ('tran', 0.0),
                                        ('rind', 1.0),
                                        ('tblr', 0.0),
                                        ('trnl', 0.0),
                                        ('glos', 0.4),
                                        ('shrp', 0.0),
                                        ('bump', 1.0),
                                        ('strs', 0.0),
                                        ('smooth', False),
                                        ('textures', {}),
                                        ('textures_5', [])])},)),
             ('tags', (['DkBlu', 'Default'],)),
             ('clips', ({},)),
             ('images', ([],))])

To run pytest:

    export PYTHONPATH=`pwd`
    pytest
    
    
    ============================= test session starts ==============================
    platform cygwin -- Python 3.6.4, pytest-5.3.1, py-1.8.0, pluggy-0.13.1
    rootdir: /home/dave/projects/lwo_strut
    collected 2 items

    tests/basic/test_load_lwo.py ..                                          [100%]

    ============================== 2 passed in 0.09s ===============================
