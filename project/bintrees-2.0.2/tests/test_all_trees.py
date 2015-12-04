#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: test binary trees
# Created: 28.04.2010
# Copyright (c) 2010-2013 by Manfred Moitzi
# License: MIT License
import os
import sys
PYPY = hasattr(sys, 'pypy_version_info')

import importlib
import subprocess

import unittest
import pickle
sys.path.append('./bintrees-2.0.2/bintrees/bintree.py')
from random import randint, shuffle

from bintrees import BinaryTree, AVLTree, RBTree

#import BinaryTree
set3 = [34, 67, 89, 123, 3, 7, 9, 2, 0, 999]

def_values1 = list(zip([13, 13, 13], [13, 13, 13]))
def_values2 = [(3, 12), (9, 35), (8, 95), (1, 16), (3, 57)]
slicetest_data_global = [(1, 1), (2, 2), (3, 3), (4, 4), (8, 8), (9, 9), (10, 10), (11, 11)]

def check_integrity(keys, remove_key, tree):
    for search_key in keys:
        if search_key == remove_key:
            if search_key in tree:
                return False
        else:
            if search_key not in tree:
                return False
    return True

def randomkeys(num, maxnum=100000):
    keys = set([randint(0, maxnum) for _ in range(num)])
    while len(keys) != num:
        keys.add(randint(0, maxnum))
    return list(keys)

class CheckTree(object):
    # TREE_CLASS = BinaryTree
    TREE_CLASS = AVLTree
    
    default_values1 = def_values1
    default_values2 = def_values2
    slicetest_data = slicetest_data_global
    
    # def check_em_too(self,a,b,c,d):
    # 	g = a + c + d*10
    # 	if g > 100:
    # 		e = 100
    # 		f = e*b
    # 		if f%2 == 0:
    # 			print f
    # 	else:
    # 		f = g%22
    # 		if f%2 != 0:
    # 			print f
    # 		else:
    # 			print g

    def test_001_init(self):
        tree = self.TREE_CLASS()
        tree.update(self.default_values1)

    def test_002_init_with_dict(self):
        self.TREE_CLASS(dict(self.default_values1))

    def test_000_init_with_seq(self):
        tree = self.TREE_CLASS(self.default_values1)

    def test_004_init_with_tree(self):
        tree1 = self.TREE_CLASS(self.default_values1)
        tree2 = self.TREE_CLASS(tree1)

    def test_005_iter_empty_tree(self):
        tree = self.TREE_CLASS()

    def test_006_copy(self):
        tree1 = self.TREE_CLASS(self.default_values1)
        tree2 = tree1.copy()

    def test_007_to_dict(self):
        tree = self.TREE_CLASS(self.default_values2)
        d = dict(tree)

    def test_008a_repr(self):
        tree = self.TREE_CLASS(self.default_values2)
        clsname = tree.__class__.__name__
        reprstr = repr(tree)

    def test_008b_repr_empty_tree(self):
        tree = self.TREE_CLASS()
        repr(tree)

    def test_009_clear(self):
        tree = self.TREE_CLASS(self.default_values2)
        tree.clear()
        len(tree)

    def test_010_contains(self):
        tree1 = self.TREE_CLASS(self.default_values2)
        tree2 = self.TREE_CLASS(self.default_values1)
        for key in tree1.keys(): 1==1
        for key in tree2.keys(): 1==1

    def test_011_is_empty(self):
        tree = self.TREE_CLASS()
        tree.is_empty()
        tree[0] = 1
        tree.is_empty()

    def test_012_update_1(self):
        tree = self.TREE_CLASS()
        tree.update({1: 'one', 2: 'two'})
        tree.update([(3, 'three'), (2, 'zwei')])
        tree.keys()
        tree.values()

    def test_013_update_2(self):
        tree = self.TREE_CLASS()
        tree.update({1: 'one', 2: 'two'}, [(3, 'three'), (2, 'zwei')])
        list(tree.keys())
        list(tree.values())

    def test_014_unique_keys(self):
        tree = self.TREE_CLASS()
        for value in range(5):
            tree[0] = value

    def test_015_getitem(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        for key in [12, 34, 45, 16, 35, 57]:
            # self.assertEqual(key, tree[key])
            if key == tree[key]:
                print "yes"

    def test_016_setitem(self):
        tree = self.TREE_CLASS()
        for key in [12, 34, 45, 16, 35, 57]:
            tree[key] = key
        # for key in [12, 34, 45, 16, 35, 57]:
        # #     self.assertEqual(key, tree[key])

    def test_017_setdefault(self):
        tree = self.TREE_CLASS(self.default_values2)
        value = tree.setdefault(2, 17)  # key <2> exists and == 12
        # self.assertEqual(value, 12)
        value = tree.setdefault(99, 77)

    def test_018_keys(self):
        tree = self.TREE_CLASS(self.default_values1)
        result = list(iter(tree))
        # self.assertEqual(result, [12, 16, 34, 35, 45, 57])
        # self.assertEqual(result, list(tree.keys()))

    def test_018a_keyslice(self):
        tree = self.TREE_CLASS(self.default_values1)
        result = list(tree.key_slice(15, 36))

    def test_018b_keyslice(self):
        tree = self.TREE_CLASS(self.default_values1)
        result = list(tree.key_slice(15, 35))

    def test_018c_keyslice_reverse(self):
        tree = self.TREE_CLASS(self.default_values1)
        result = list(tree.key_slice(15, 36, reverse=True))

    def test_018d_slice_from_start(self):
        # values: 1, 2, 3, 4, 8, 9, 10, 11
        tree = self.TREE_CLASS(self.slicetest_data)
        result = list(tree[:4])

    def test_018e_slice_til_end(self):
        # values: 1, 2, 3, 4, 8, 9, 10, 11
        tree = self.TREE_CLASS(self.slicetest_data)
        result = list(tree[8:])

    def test_018f_slice_from_start_til_end(self):
        # values: 1, 2, 3, 4, 8, 9, 10, 11
        tree = self.TREE_CLASS(self.slicetest_data)
        result = list(tree[:])

    def test_018g_slice_produces_keys(self):
        tree = self.TREE_CLASS([(1, 100), (2, 200), (3, 300)])
        result = list(tree[:])

    def test_019_values(self):
        tree = self.TREE_CLASS(self.default_values1)
        result = list(tree.values())

    def test_020_items(self):
        tree = self.TREE_CLASS(self.default_values1)
        result = list(tree.items())

    def test_020a_items_of_empty_tree(self):
        tree = self.TREE_CLASS()
        # empty tree also has to return an iterable
        result = [item for item in tree.items()]

    def test_021_keys_reverse(self):
        tree = self.TREE_CLASS(self.default_values1)
        result = list(tree.keys(reverse=True))

    def test_022_values_reverse(self):
        tree = self.TREE_CLASS(self.default_values1)
        result = list(tree.values(reverse=True))

    def test_023_items_reverse(self):
        tree = self.TREE_CLASS(self.default_values1)
        result = list(tree.items(reverse=True))

    def test_024_get(self):
        tree = self.TREE_CLASS(self.default_values1)
        tree.get(99)

    def test_025_get_default(self):
        tree = self.TREE_CLASS(self.default_values1)

    def test_026_remove_child_1(self):
        keys = [50, 25]
        tree = self.TREE_CLASS.fromkeys(keys)
        remove_key = 25
        del tree[remove_key]
        check_integrity(keys, remove_key, tree)

    def test_027_remove_child_2(self):
        keys = [50, 25, 12]
        tree = self.TREE_CLASS.fromkeys(keys)
        remove_key = 25
        del tree[remove_key]
        check_integrity(keys, remove_key, tree)

    def test_028_remove_child_3(self):
        keys = [50, 25, 12, 33]
        tree = self.TREE_CLASS.fromkeys(keys)
        remove_key = 25
        del tree[remove_key]
        check_integrity(keys, remove_key, tree)

    def test_029_remove_child_4(self):
        keys = [50, 25, 12, 33, 40]
        tree = self.TREE_CLASS.fromkeys(keys)
        remove_key = 25
        del tree[remove_key]
        check_integrity(keys, remove_key, tree)

    def test_030_remove_child_5(self):
        keys = [50, 25, 12, 33, 40, 37, 43]
        tree = self.TREE_CLASS.fromkeys(keys)
        remove_key = 25
        del tree[remove_key]
        check_integrity(keys, remove_key, tree)

    def test_031_remove_child_6(self):
        keys = [50, 75, 100, 150, 60, 65, 64, 80, 66]
        tree = self.TREE_CLASS.fromkeys(keys)
        remove_key = 75
        del tree[remove_key]
        check_integrity(keys, remove_key, tree)

    def test_032_remove_root_1(self):
        keys = [50, ]
        tree = self.TREE_CLASS.fromkeys(keys)
        del tree[50]
        tree.is_empty

    def test_033_remove_root_2(self):
        keys = [50, 25, 12, 33, 34]
        tree = self.TREE_CLASS.fromkeys(keys)
        remove_key = 50
        del tree[remove_key]
        check_integrity(keys, remove_key, tree)

    def test_034_remove_root_3(self):
        keys = [50, 25, 12, 33, 34, 75]
        tree = self.TREE_CLASS.fromkeys(keys)
        remove_key = 50
        del tree[remove_key]
        check_integrity(keys, remove_key, tree)

    def test_035_remove_root_4(self):
        keys = [50, 25, 12, 33, 34, 75, 60]
        tree = self.TREE_CLASS.fromkeys(keys)
        remove_key = 50
        del tree[remove_key]
        check_integrity(keys, remove_key, tree)

    def test_036_remove_root_5(self):
        keys = [50, 25, 12, 33, 34, 75, 60, 61]
        tree = self.TREE_CLASS.fromkeys(keys)
        remove_key = 50
        del tree[remove_key]
        check_integrity(keys, remove_key, tree)

    def test_037a_discard(self):
        keys = [50, 25, 12, 33, 34, 75, 60, 61]
        tree = self.TREE_CLASS.fromkeys(keys)
        try:
            tree.discard(17)
        except KeyError:
            "Discard raises KeyError"

    def test_037b_remove_keyerror(self):
        keys = [50, 25, 12, 33, 34, 75, 60, 61]
        tree = self.TREE_CLASS.fromkeys(keys)
        # self.assertRaises(KeyError, tree.remove, 17)

    def test_038_remove_shuffeld(self):
        keys = [50, 25, 20, 35, 22, 23, 27, 75, 65, 90, 60, 70, 85, 57, 83, 58]
        remove_keys = keys[:]
        shuffle(remove_keys)
        for remove_key in remove_keys:
            tree = self.TREE_CLASS.fromkeys(keys)
            del tree[remove_key]
            check_integrity(keys, remove_key, tree)

    def test_039_remove_random_numbers(self):
        try:
            fp = open('xtestkey.txt')
            keys = eval(fp.read())
            fp.close()
        except IOError:
            keys = randomkeys(1000)
        shuffle(keys)
        tree = self.TREE_CLASS.fromkeys(keys)
        for key in keys:
            del tree[key]

    def test_040_sort_order(self):
        keys = randomkeys(1000)
        tree = self.TREE_CLASS.fromkeys(keys)
        generator = iter(tree)
        a = next(generator)
        for b in generator:
            # self.assertTrue(b > a)
            a = b

    def test_041_pop(self):
        tree = self.TREE_CLASS(self.default_values2)
        data = tree.pop(8)

    def test_042_pop_item(self):
        tree = self.TREE_CLASS(self.default_values2)
        d = dict()
        while not tree.is_empty():
            key, value = tree.pop_item()
            d[key] = value
        expected = {2: 12, 4: 34, 8: 45, 1: 16, 9: 35, 3: 57}

    def test_043_min_item(self):
        tree = self.TREE_CLASS(zip(set3, set3))
        min_item = tree.min_item()

    def test_044_min_item_error(self):
        tree = self.TREE_CLASS()

    def test_045_max_item(self):
        tree = self.TREE_CLASS(zip(set3, set3))
        max_item = tree.max_item()

    def test_046_max_item_error(self):
        tree = self.TREE_CLASS()

    def test_047_min_key(self):
        tree = self.TREE_CLASS(zip(set3, set3))
        minkey = tree.min_key()

    def test_048_min_key_error(self):
        tree = self.TREE_CLASS()

    def test_049_max_key(self):
        tree = self.TREE_CLASS(zip(set3, set3))
        maxkey = tree.max_key()

    def test_050_min_key_error(self):
        tree = self.TREE_CLASS()

    def test_051_prev_item(self):
        tree = self.TREE_CLASS(zip(set3, set3))
        prev_value = None
        for key in tree.keys():
            # try:
                prev_item = tree.prev_item(key)
            # except KeyError:  # only on first key
            #     self.assertEqual(prev_value, None)
            # if prev_value is not None:
            #     # self.assertEqual(prev_value, prev_item[1])
            # prev_value = key

    def test_052_prev_key_extreme(self):
        # extreme degenerated binary tree (if unbalanced)
        tree = self.TREE_CLASS.fromkeys([1, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2])
        tree.prev_key(2)

    def test_053_prev_item_error(self):
        tree = self.TREE_CLASS()
        tree[0] = 'NULL'

    def test_054_succ_item(self):
        tree = self.TREE_CLASS(zip(set3, set3))
        succ_value = None
        for key in tree.keys(reverse=True):
            try:
                succ_item = tree.succ_item(key)
            except KeyError:  # only on last key
                1==1
            if succ_value is not None:
                1==1
            succ_value = key

    def test_055_succ_key_extreme(self):
        # extreme degenerated binary tree (if unbalanced)
        tree = self.TREE_CLASS.fromkeys([15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        tree.succ_key(10)

    def test_056_succ_item_error(self):
        tree = self.TREE_CLASS()
        tree[0] = 'NULL'
        # self.assertRaises(KeyError, tree.succ_item, 0)

    def test_057_prev_key(self):
        tree = self.TREE_CLASS(zip(set3, set3))
        pkey = None
        for key in tree.keys():
            try:
                1==1
                # prev_key = tree.prev_key(key)
            except KeyError:  # only on first key
                1==1
            if pkey is not None:
                # self.assertEqual(pkey, prev_key)
                1==1
            pkey = key

    def test_058_prev_key_error(self):
        tree = self.TREE_CLASS()
        tree[0] = 'NULL'

    def test_059_succ_key(self):
        tree = self.TREE_CLASS(zip(set3, set3))
        skey = None
        for key in tree.keys(reverse=True):
            try:
                succ_key = tree.succ_key(key)
            except KeyError:  # only on last key
                # self.assertEqual(skey, None)
                1==1
            if skey is not None:
                # self.assertEqual(skey, succ_key)
                1==1
            skey = key

    def test_060_succ_key_error(self):
        tree = self.TREE_CLASS()
        tree[0] = 'NULL'

    def test_061_prev_succ_on_empty_trees(self):
        tree = self.TREE_CLASS()
        succ = tree.succ_key
        prev = tree.prev_key
        succ1 = tree.succ_item
        prev1 = tree.prev_item
        # self.assertRaises(KeyError, tree.succ_key, 0)
        # self.assertRaises(KeyError, tree.prev_key, 0)
        # self.assertRaises(KeyError, tree.succ_item, 0)
        # self.assertRaises(KeyError, tree.prev_item, 0)

    def test_062_succ_prev_key_random_1000(self):
        keys = list(set([randint(0, 10000) for _ in range(1000)]))
        shuffle(keys)
        tree = self.TREE_CLASS.fromkeys(keys)

        skey = None
        for key in tree.keys(reverse=True):
            try:
                succ_key = tree.succ_key(key)
            except KeyError:  # only on last key
                # self.assertEqual(skey, None)
                1==1
            if skey is not None:
                # self.assertEqual(skey, succ_key)
                a=succ_key
            skey = key

        pkey = None
        for key in tree.keys():
            try:
                prev_key = tree.prev_key(key)
            except KeyError:  # only on first key
                # self.assertEqual(pkey, None)
                1==1
            if pkey is not None:
                # self.assertEqual(pkey, prev_key)
                1==1
            pkey = key

    def test_063_pop_min(self):
        tree = self.TREE_CLASS(zip(set3, set3))
        keys = sorted(set3[:])
        for key in keys:
            k, v = tree.pop_min()

    def test_064_pop_min_error(self):
        tree = self.TREE_CLASS()

    def test_065_pop_max(self):
        tree = self.TREE_CLASS(zip(set3, set3))
        keys = sorted(set3[:], reverse=True)
        for key in keys:
            k, v = tree.pop_max()

    def test_066_pop_max_error(self):
        tree = self.TREE_CLASS()

    def test_067_nlargest(self):
        l = list(range(30))
        shuffle(l)
        tree = self.TREE_CLASS(zip(l, l))
        result = tree.nlargest(10)
        chk = [(x, x) for x in range(29, 19, -1)]

    def test_068_nlargest_gt_len(self):
        items = list(zip(range(5), range(5)))
        tree = self.TREE_CLASS(items)
        result = tree.nlargest(10)

    def test_069_nsmallest(self):
        l = list(range(30))
        shuffle(l)
        tree = self.TREE_CLASS(zip(l, l))
        result = tree.nsmallest(10)
        chk = [(x, x) for x in range(0, 10)]
        # self.assertEqual(chk, result)

    def test_070_nsmallest_gt_len(self):
        items = list(zip(range(5), range(5)))
        tree = self.TREE_CLASS(items)
        result = tree.nsmallest(10)

    def test_071_reversed(self):
        tree = self.TREE_CLASS(zip(set3, set3))
        result = reversed(sorted(set3))
        for key, chk in zip(reversed(tree), result):
            1==1
            # self.assertEqual(chk, key)

    def test_077_delslice(self):
        T = self.TREE_CLASS.fromkeys([1, 2, 3, 4, 8, 9])
        tree = T.copy()
        del tree[:2]
        tree = T.copy()
        del tree[1:3]
        tree = T.copy()
        del tree[3:]
        tree = T.copy()
        del tree[:]

    def test_080_intersection(self):
        l1 = list(range(30))
        shuffle(l1)
        l2 = list(range(15, 45))
        shuffle(l2)
        tree1 = self.TREE_CLASS(zip(l1, l1))
        tree2 = self.TREE_CLASS(zip(l2, l2))
        i = tree1 & tree2

    def test_081_union_keys(self):
        l1 = list(range(30))
        shuffle(l1)
        l2 = list(range(15, 45))
        shuffle(l2)
        tree1 = self.TREE_CLASS(zip(l1, l1))
        tree2 = self.TREE_CLASS(zip(l2, l2))
        i = tree1 | tree2

    def test_081_union_values(self):
        l1 = list(range(30))
        shuffle(l1)
        l2 = list(range(15, 45))
        shuffle(l2)
        tree1 = self.TREE_CLASS(zip(l1, l1))
        tree2 = self.TREE_CLASS(zip(l2, l2))
        union_tree = tree1 | tree2

    def test_082_difference(self):
        l1 = list(range(30))
        shuffle(l1)
        l2 = list(range(15, 45))
        shuffle(l2)

        tree1 = self.TREE_CLASS(zip(l1, l1))
        tree2 = self.TREE_CLASS(zip(l2, l2))
        i = tree1 - tree2

    def test_083_symmetric_difference_keys(self):
        l1 = list(range(30))
        shuffle(l1)
        l2 = list(range(15, 45))
        shuffle(l2)

        tree1 = self.TREE_CLASS(zip(l1, l1))
        tree2 = self.TREE_CLASS(zip(l2, l2))
        new_tree = tree1 ^ tree2
        (len(new_tree), 30)
        new_tree.min_key()
        new_tree.max_key()

    def test_083_symmetric_difference_values(self):
        l1 = list(range(30))
        shuffle(l1)
        l2 = list(range(15, 45))
        shuffle(l2)

        tree1 = self.TREE_CLASS(zip(l1, l1))
        tree2 = self.TREE_CLASS(zip(l2, l2))
        new_tree = tree1 ^ tree2

    def test_084_refcount_get(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        chk = tree[700]
        count = sys.getrefcount(chk)
        for _ in range(10):
            chk = tree[700]
###########################################3
        # self.assertEqual(sys.getrefcount(chk), count)

    @unittest.skipIf(PYPY, "getrefcount() not supported by pypy.")
    def test_085_refcount_set(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        chk = 800
        count = sys.getrefcount(chk)
        tree[801] = chk
        # self.assertEqual(sys.getrefcount(chk), count + 1)

    @unittest.skipIf(PYPY, "getrefcount() not supported by pypy.")
    def test_086_refcount_del(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        chk = 900
        count = sys.getrefcount(chk)
        tree[901] = chk
        # self.assertEqual(sys.getrefcount(chk), count + 1)
        del tree[901]
        # self.assertEqual(sys.getrefcount(chk), count)

    @unittest.skipIf(PYPY, "getrefcount() not supported by pypy.")
    def test_087_refcount_replace(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        chk = 910
        count = sys.getrefcount(chk)
        tree[911] = chk
        # self.assertEqual(sys.getrefcount(chk), count + 1)
        tree[911] = 912  # replace 910 with 912
        # self.assertEqual(sys.getrefcount(chk), count)

    def test_088_pickle_protocol(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        pickle_str = pickle.dumps(tree, -1)
        tree2 = pickle.loads(pickle_str)
        l,m=len(tree), len(tree2)
        a,b=list(tree.keys()), list(tree2.keys())
        x,y=list(tree.values()), list(tree2.values())
        # self.assertEqual(len(tree), len(tree2))
        # self.assertEqual(list(tree.keys()), list(tree2.keys()))
        # self.assertEqual(list(tree.values()), list(tree2.values()))

    # [12, 34, 45, 16, 35, 57]
    def test_089_floor_item(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        a,b,c=tree.floor_item(12),tree.floor_item(13),tree.floor_item(60)
        # self.assertEqual(tree.floor_item(12), (12, 12))
        # self.assertEqual(tree.floor_item(13), (12, 12))
        # self.assertEqual(tree.floor_item(60), (57, 57))

    def test_090a_floor_item_key_error(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        # with self.assertRaises(KeyError):
        tree.floor_item(11)

    def test_090b_floor_item_empty_tree(self):
        tree = self.TREE_CLASS()
        # with self.assertRaises(KeyError):
        tree.floor_item(11)

    def test_091_floor_key(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        a,b,c=tree.floor_key(12),tree.floor_key(13),tree.floor_key(60)
        # self.assertEqual(tree.floor_key(12), 12)
        # self.assertEqual(tree.floor_key(13), 12)
        # self.assertEqual(tree.floor_key(60), 57)

    def test_092_floor_key_key_error(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        # with self.assertRaises(KeyError):
        tree.floor_key(11)

    def test_093_ceiling_item(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        a,b,c=tree.ceiling_item(57),tree.ceiling_item(56),tree.ceiling_item(0)
        # self.assertEqual(tree.ceiling_item(57), (57, 57))
        # self.assertEqual(tree.ceiling_item(56), (57, 57))
        # self.assertEqual(tree.ceiling_item(0), (12, 12))

    def test_094a_ceiling_item_key_error(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        # with self.assertRaises(KeyError):
        tree.ceiling_item(60)

    def test_094a_ceiling_item_empty_tree(self):
        tree = self.TREE_CLASS()
        # with self.assertRaises(KeyError):
        tree.ceiling_item(60)

    def test_095_ceiling_key(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        a,b,c=tree.ceiling_key(57),tree.ceiling_key(56),tree.ceiling_key(0)
        # self.assertEqual(tree.ceiling_key(57), 57)
        # self.assertEqual(tree.ceiling_key(56), 57)
        # self.assertEqual(tree.ceiling_key(0), 12)

    def test_096_ceiling_key_key_error(self):
        tree = self.TREE_CLASS(self.default_values1)  # key == value
        # with self.assertRaises(KeyError):
        tree.ceiling_key(60)

    def test_097_data_corruption(self):
        # Data corruption in FastRBTree in all versions before 1.0.2:
        # Error was located in the rb_insert() function in ctrees.c

        tree = self.TREE_CLASS()
        insert_keys = [14, 15.84, 16, 16, 16.3, 15.8, 16.48, 14.95, 15.07, 16.41, 16.43, 16.45, 16.4, 16.42, 16.47,
                      16.44, 16.46, 16.48, 16.51, 16.5, 16.49, 16.5, 16.49, 16.49, 16.47, 16.5, 16.48, 16.46, 16.44]
        for key in insert_keys:
            tree[key] = "unused_data"
        expected_keys = sorted(set(insert_keys))
        a=list(tree.keys())
        # self.assertEqual(expected_keys, list(tree.keys()), "Data corruption in %s!" % tree.__class__)

    def test_098_foreach(self):
        keys = []
        def collect(key, value):
            keys.append(key)

        tree = self.TREE_CLASS(self.default_values1)  # key == value
        tree.foreach(collect)
        a,b=list(tree.keys()),list(sorted(keys))
        # self.assertEqual(list(tree.keys()), list(sorted(keys)))


# class TestBinaryTree(CheckTree, unittest.TestCase):
# TREE_CLASS = BinaryTree


# class TestAVLTree(CheckTree, unittest.TestCase):
#     TREE_CLASS = AVLTree


# class TestRBTree(CheckTree, unittest.TestCase):
#     TREE_CLASS = RBTree


# class TestFastBinaryTree(CheckTree, unittest.TestCase):
#     TREE_CLASS = FastBinaryTree


# class TestFastAVLTree(CheckTree, unittest.TestCase):
#     TREE_CLASS = FastAVLTree


# class TestFastRBTree(CheckTree, unittest.TestCase):
#     TREE_CLASS = FastRBTree

def aaa(a,b,c):
    global def_values1
    global def_values2
    global slicetest_data_global
    
    def_values1 =a # list(zip([13, 13, 13], [13, 13, 13]))
    def_values2 = b # [(3, 12), (9, 35), (8, 95), (1, 16), (3, 57)]
    slicetest_data_global = c #[(1, 1), (2, 2), (3, 3), (4, 4), (8, 8), (9, 9), (10, 10), (11, 11)]

    # CheckTree().test_002_init_with_dict()
    # CheckTree().test_000_init_with_seq()
    # CheckTree().test_007_to_dict()
    
    
    # path = os.path.join(os.getcwd(),'test')
    # path = os.path.join(os.path.abspath('.'),'test_all_trees.py')
    # f = file[:-3]
    # loader = importlib.machinery.SourceFileLoader('mmm', path)
    # mod = loader.load_module()
    
    # mod = importlib.import_module(path)
        
    names = getNames('test_all_trees.py')
    for func_name in names:
        try:
            # getattr(CheckTree(),func_name)()
            fd = getattr(func_name,"method")
            getattr(CheckTree(),fd)()
            #CheckTree().func_name()
        except:
            print func_name
            print "Exception ",sys.exc_info()[0]
            continue
    
    
def getNames(filename):
    names = []
    #fn = os.path.join('test',str(filename))
    f = open(filename)
    contents = f.readlines()
    for line in contents:
        if not (line.strip().startswith("#")):
            start = line.find('def test_')
            if start != -1:
                end = line.find('(',start)
                names.append(line[start+9:end])
    f.close()
    return names

# if __name__ == '__main__':
#     print sys.path
#     # # unittest.main()
    # print getNames('test_all_trees.py')
