import scipy.io
import h5py


CACD_DIR = '../dataset/CACD/'
CACD_TRAIN_DIR = 'data/CACD2000/'
CACD_VALID_DIR = 'data/CACD_VS/'


def load_celebrity2000_meta(filename):
    '''
    :param filename:
    :return:

    celebrityData - contains information of the 2,000 celebrities
        name - celebrity name
        identity - celebrity id
        birth - celebrity brith year
        rank - rank of the celebrity with same birth year in IMDB.com when the dataset was constructed
        lfw - whether the celebrity is in LFW dataset
    celebrityImageData - contains information of the face images
        age - estimated age of the celebrity
        identity - celebrity id
        year - estimated year of which the photo was taken
        feature - 75,520 dimension LBP feature extracted from 16 facial landmarks
        rank - rank of the celebrity with same birth year in IMDB.com when the dataset was constructed
        lfw - whether the celebrity is in LFW dataset
        birth - celebrity brith year
        name - file name of the image
    '''
    try:
        meta = scipy.io.loadmat(filename, mdict=None, appendmat=True)
        # scipy.io.savemat(filename, mdict, appendmat=True, format='5', long_field_names=False, do_compression=False, oned_as='row')
        print('celebrityImageData:', meta['celebrityImageData'][0][0][7].shape)  # meta['celebrityImageData'][0][0][7]
        print(meta['celebrityImageData'][0][0][7])
        print('celebrityData:', meta['celebrityData'][0][0][4].shape)  # meta['celebrityData'][0][0][4]
        print(meta['celebrityData'][0][0][4])
    except:
        meta = h5py.File(filename, 'r')
        print('keys:', meta.keys())
        print('items:', meta.items())
        print('values:', meta.values())
        print('celebrityImageData:', meta['celebrityImageData'].keys())
        print(meta['celebrityImageData']['feature'])
        print('celebrityData:', meta['celebrityData'].keys())
        print(meta['celebrityData'])

    print(meta)


if __name__ == '__main__':
    # load_celebrity2000_meta(CACD_DIR+'celebrity2000_meta.mat')
    load_celebrity2000_meta(CACD_DIR+'celebrity2000.mat')
