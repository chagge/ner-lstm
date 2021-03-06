import random
import numpy as np
import pickle


def get_dummy_data(num):
    emb = [[[random.random() for _ in range(300)] for i in range(113)] for j in range(num)]
    tag = [np.array([ [0 for i in range(5)] for j in range(113)]) for i in range(num)]
    for t in tag:
        t[random.randint(0,len(t)-1)] = 1
    return emb,tag

def get_train_data():
    emb = pickle.load(open('strain','rb'))
    tag = pickle.load(open('straintag','rb'))
    return emb,tag

def get_test_data():
    emb = pickle.load(open('s50test','rb'))
    tag = pickle.load(open('s50testtag','rb'))
    return emb,tag


def get_indi_data():
    emb = pickle.load(open('t','rb'))
    tag = pickle.load(open('tag','rb'))
    return emb,tag