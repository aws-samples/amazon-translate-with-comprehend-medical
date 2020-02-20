#!/bin/bash

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

cd ./translate-cm
zip -r ../translate-cm.zip ./*
cd ../translate-cm-athena
zip -r ../translate-cm-athena.zip ./*
