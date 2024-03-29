---
Title: Evaluating the Use of Reconstruction Error for Novelty Localization
Authors: Patrick Feeney
Date: 2021-07-28 10:00
Tags: news
---

Published in [ICML 2021 Workshop on Uncertainty and Robustness in Deep Learning](https://icml.cc/virtual/2021/workshop/8374).
[arXiv version](https://arxiv.org/abs/2107.13379).

The pixelwise reconstruction error of deep autoencoders is often utilized for image novelty detection and localization under the assumption that pixels with high error indicate which parts of the input image are unfamiliar and therefore likely to be novel. This assumed correlation between pixels with high reconstruction error and novel regions of input images has not been verified and may limit the accuracy of these methods. In this paper we utilize saliency maps to evaluate whether this correlation exists. Saliency maps reveal directly how much a change in each input pixel would affect reconstruction loss, while each pixel's reconstruction error may be attributed to many input pixels when layers are fully connected. We compare saliency maps to reconstruction error maps via qualitative visualizations as well as quantitative correspondence between the top K elements of the maps for both novel and normal images. Our results indicate that reconstruction error maps do not closely correlate with the importance of pixels in the input images, making them insufficient for novelty localization.
