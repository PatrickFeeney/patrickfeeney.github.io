---
Title: NovelCraft: A Dataset for Novelty Detection and Discovery in Open Worlds
Authors: Patrick Feeney
Date: 2022-06-23 10:00
Tags: news
---

Published in [TMLR](https://openreview.net/forum?id=4eL6z9ziw7).
[arXiv version](https://arxiv.org/abs/2206.11736).

In order for artificial agents to successfully perform tasks in changing environments, they must be able to both detect and adapt to novelty. However, visual novelty detection research often only evaluates on repurposed datasets such as CIFAR-10 originally intended for object classification, where images focus on one distinct, well-centered object. New benchmarks are needed to represent the challenges of navigating the complex scenes of an open world. Our new NovelCraft dataset contains multimodal episodic data of the images and symbolic world-states seen by an agent completing a pogo stick assembly task within a modified Minecraft environment. In some episodes, we insert novel objects of varying size within the complex 3D scene that may impact gameplay. Our visual novelty detection benchmark finds that methods that rank best on popular area-under-the-curve metrics may be outperformed by simpler alternatives when controlling false positives matters most. Further multimodal novelty detection experiments suggest that methods that fuse both visual and symbolic information can improve time until detection as well as overall discrimination. Finally, our evaluation of recent generalized category discovery methods suggests that adapting to new imbalanced categories in complex scenes remains an exciting open problem.
