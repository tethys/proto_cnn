# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 00:19:05 2014

@author: vivianapetrescu
"""

"""This tutorial introduces the LeNet5 neural network architecture
using Theano.  LeNet5 is a convolutional neural network, good for
classifying images. This tutorial shows how to build the architecture,
and comes with all the hyper-parameters you need to reproduce the
paper's MNIST results.


This implementation simplifies the model in the following ways:

 - LeNetConvPool doesn't implement location-specific gain and bias parameters
 - LeNetConvPool doesn't implement pooling by average, it implements pooling
   by max.
 - Digit classification is implemented with a logistic regression rather than
   an RBF network
 - LeNet5 was not fully-connected convolutions at second layer

References:
 - Y. LeCun, L. Bottou, Y. Bengio and P. Haffner:
   Gradient-Based Learning Applied to Document
   Recognition, Proceedings of the IEEE, 86(11):2278-2324, November 1998.
   http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf

"""
import scipy.io
import numpy as np
import time

import theano
import theano.tensor as T
from theano.tensor.signal import downsample
from theano.tensor.nnet import conv


class LeNetSeparableConvPoolLayer(object):
    """Pool Layer of a convolutional network """

    def __init__(self, rng, input_images, filter_shape, image_shape, poolsize=(2, 2),  
                 Pstruct = None, b= None):
        """
        Allocate a LeNetConvPoolLayer with shared variable internal parameters.

        :type rng: numpy.random.RandomState
        :param rng: a random number generator used to initialize weights

        :type input: theano.tensor.dtensor4
        :param input: symbolic image tensor, of shape image_shape

        :type filter_shape: tuple or list of length 4
        :param filter_shape: (number of filters, num input feature maps,
                              filter height,filter width)

        :type image_shape: tuple or list of length 4
        :param image_shape: (batch size, num input feature/channels maps,
                             image height, image width)
                             For a gray image, this is 1 for the first layer.
                             For the following layers it is equal with the 
                             number of output  channels/feature maps

        :type poolsize: tuple or list of length 2
        :param poolsize: the downsampling (pooling) factor (#rows,#cols)
        """

        assert image_shape[1] == filter_shape[1]
        # the bias is a 1D tensor -- one bias per output feature map
        # convolve input feature maps with filters

#(number of filters, num input feature maps,  filter height,filter width)
#   10filters, 1, 20, h 1,
#   10filtrs, 1,20 , 1 ,w
        
        ## P is of size  U0, U1, U2
        ## rank*nbr_filters, rank*w_filter,rank*w_filter
        
        ## Pstruct is contains an array of PU,lambda for every channel!
        ## We look at the composition for the first channel in the beginning  
        print Pstruct[0]['U1'].shape
        print Pstruct[0]['U2'].shape
        print Pstruct[0]['U3'].shape
        rank = Pstruct[0]['U1'].shape[1]
        fwidth = Pstruct[0]['U1'].shape[0]
        fheight = Pstruct[0]['U2'].shape[0]
        nbr_filters = Pstruct[0]['U3'].shape[0]
        
        print 'width, height, rank ', fwidth, fheight, rank
     #   rank 4, w,h 3x3, nbr filter 7
        print 'num input feaure maps ', filter_shape[1]
        num_input_feature_maps = filter_shape[1]
        horizontal_filter_shape = (rank, num_input_feature_maps, 1, fwidth)
        horizontal_filters = np.ndarray(horizontal_filter_shape)
        for chanel in range(num_input_feature_maps):
            horizontal_filters[:, chanel, 0, :] = np.transpose(Pstruct[chanel]['U1']);
            print Pstruct[chanel]['U1']
            print np.transpose(Pstruct[chanel]['U1'])

        horizontal_filters = theano.shared(horizontal_filters)
        horizontal_conv_out = conv.conv2d(input = input_images, filters = horizontal_filters,
                               filter_shape = horizontal_filter_shape, image_shape = image_shape)
                
        
        vertical_filter_shape = (rank, num_input_feature_maps, fheight, 1)
        vertical_filters = np.ndarray(vertical_filter_shape)        
        for chanel in range(num_input_feature_maps):
            vertical_filters[:, chanel, :, 0] = np.transpose(Pstruct[chanel]['U2']);
    #    number of filters, num input feature maps,
        vertical_filters = theano.shared(vertical_filters)
        new_image_shape = (image_shape[0], image_shape[1], image_shape[2], image_shape[3] -fwidth + 1)
        conv_out = conv.conv2d(input = horizontal_conv_out, filters = vertical_filters,
                               filter_shape = vertical_filter_shape, image_shape = new_image_shape)

        ## numberof images, number of filters, image width, image height
        batch_size = image_shape[0]
        n_rows = image_shape[2]- fwidth + 1
        n_cols = image_shape[3] - fheight + 1
        input4D = theano.shared(np.zeros((batch_size, nbr_filters, 
                                          n_rows, n_cols)))
        for f in range(nbr_filters):            
            temp = np.zeros((batch_size, n_rows, n_cols))
            for chanel in range(num_input_feature_maps):
                 alphas = Pstruct[chanel]['U3']
                 for r in range(rank):
                     out = conv_out[r,r, :,:]* alphas[f, r] * Pstruct[chanel]['lmbda'][r];   
                     temp = temp + out
            if f == 0:
                print'first map'
                print temp
            T.set_subtensor(input4D[:,f,:,:], temp)
             
        print 'Image shape ', input4D.shape.eval()
        # downsample each feature map individually, using maxpooling
        start = time.time()
        pooled_out = downsample.max_pool_2d(input=input4D,
                                            ds=poolsize, 
                                            ignore_border=True)
        end = time.time()
        self.downsample_time = (end - start)*1000/ image_shape[0]
        
        print 'Image shape ', pooled_out.shape.eval()
                
        # add the bias term. Since the bias is a vector (1D array), we first
        # reshape it to a tensor of shape (1,n_filters,1,1). Each bias will
        # thus be broadcasted across mini-batches and feature map
        # width & height
        self.output = T.tanh(pooled_out + b.dimshuffle('x', 0, 'x', 'x'))

