from sklearn.model_selection import KFold
import numpy as np
x = np.array(['B', 'H', 'L', 'O', 'K', 'P', 'W', 'G'])
kf = KFold(n_splits=2)
d = kf.split(x)
for train_idx, test_idx in d:
    train_data = x[train_idx]
    test_data = x[test_idx]
    print('train_idx:{}, train_data:{}'.format(train_idx, train_data))
    print('test_idx:{}, test_data:{}'.format(test_idx, test_data))

# train_idx:[4 5 6 7], train_data:['K' 'P' 'W' 'G']
# test_idx:[0 1 2 3], test_data:['B' 'H' 'L' 'O']
# train_idx:[0 1 2 3], train_data:['B' 'H' 'L' 'O']
# test_idx:[4 5 6 7], test_data:['K' 'P' 'W' 'G']