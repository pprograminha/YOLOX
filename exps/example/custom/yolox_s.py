#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.
import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "datasets/coco128"
        self.train_ann = "instances_train2017.json"
        self.val_ann = "instances_val2017.json"
        # self.data_dir = "datasets/COCO"
        # self.train_ann = "annotations/instances_train2017.json"
        # self.val_ann = "annotations/instances_val2017.json"

        self.num_classes = 1

        self.max_epoch = 300
        self.data_num_workers = 4
        self.eval_interval = 1

        #         self.num_classes = 5  # Cracking, Layer_shifting, Off_platform, Stringing, Warping
        # self.data_dir = "datasets"  # Directory containing COCO format data
        # self.train_ann = "COCO/annotations/instances_train2017.json"
        # self.val_ann = "COCO/annotations/instances_val2017.json"
        # self.test_ann = "COCO/annotations/instances_test2017.json"  # Use validation for testing
        
        # # Training configuration
        # self.max_epoch = 100  # Reduced for faster training
        # self.basic_lr_per_img = 0.01 / 64.0
        # self.warmup_epochs = 3
        # self.no_aug_epochs = 10
        
        # # Data augmentation
        # self.mosaic_prob = 1.0
        # self.mixup_prob = 1.0
        # self.hsv_prob = 1.0
        # self.flip_prob = 0.5
        # self.degrees = 10.0
        # self.translate = 0.1
        # self.mosaic_scale = (0.1, 2)
        # self.enable_mixup = True
        # self.mixup_scale = (0.5, 1.5)
        # self.shear = 2.0
        
        # # Input size
        # self.input_size = (640, 640)
        # self.multiscale_range = 5
