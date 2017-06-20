#!/usr/bin/env python
# -*- encoding:UTF-8 -*-
# Author: Sengsu Iun
# Copyright 2017 Sengsu <Iun cieltero(at)gmail(dot)com>
# License: GPL v3
# GIMP plugin to merge layers to background
from gimpfu import *

gettext.install("gimp20-python", gimp.locale_directory, unicode=True)

def python_fu_vertical_layout(image,layer,move_by_upper_layer_size,merge_layers,resize_canvas,run_mode=RUN_NONINTERACTIVE):
    pdb.gimp_image_undo_group_start(image)
    image_height = pdb.gimp_image_height(image)
    layers=image.layers
    if move_by_upper_layer_size==0:
        offx=0
        offy=0
        for layer in layers:
            pdb.gimp_image_set_active_layer(image, layer)
            offy +=image_height;
            pdb.gimp_layer_set_offsets(layer, offx, offy)
    else:
        offy=0
        offx=0
        for layer in layers:
            pdb.gimp_image_set_active_layer(image, layer)
            pdb.gimp_layer_set_offsets(layer, offx, offy) 
            layer_height = pdb.gimp_drawable_height(layer)
            offy += layer_height
    if(merge_layers):
        layer = pdb.gimp_image_merge_visible_layers(image, EXPAND_AS_NECESSARY)
    if(resize_canvas):
        pdb.gimp_image_resize_to_layers(image)
    pdb.gimp_undo_push_group_end(image)
    pdb.gimp_displays_flush()

register(
    "python-fu-vertical-layout",
    _("layout layers vertically"),
    _("layout layers vertically"),
    "Sengsu Iun<cieltero(at)gmail(dot)com>",
    "(c) Sengsu Iun, Published under GPL version 3",
    "June 20, 2017",
    _("<Image>/Layer/Vertical Layout"),
    "*",
    [
    (PF_OPTION, "move_by_upper_layer_size", "각 레이어 이동: ",0,["이미지 크기만큼씩 이동","위쪽 레이어 크기만큼 이동"]),
    (PF_BOOL, "merge_layers",   "레이어 합치기", False),
    (PF_BOOL, "resize_image",   "캔버스 크기 변경", True),
    ],
    [],
    python_fu_vertical_layout,
    domain=("gimp20-python", gimp.locale_directory)
    )

main()


