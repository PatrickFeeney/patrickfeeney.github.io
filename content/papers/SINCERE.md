---
Title: SINCERE: Supervised Information Noise-Contrastive Estimation REvisited
Authors: Patrick Feeney
Date: 2024-03-11 10:00
Tags: news
---

Under review for ICML 2024.
[arXiv version](https://arxiv.org/abs/2309.14277).

The information noise-contrastive estimation (InfoNCE) loss function provides the basis of many self-supervised deep learning methods due to its strong empirical results and theoretic motivation.
Previous work suggests a supervised contrastive (SupCon) loss to extend InfoNCE to learn from available class labels.
However, in this work we find that the prior SupCon loss formulation has questionable justification because it can encourage some images from the same class to repel one another in the learned embedding space.
We propose the Supervised InfoNCE REvisited (SINCERE) loss as a theoretically-justified supervised extension of InfoNCE that never causes images from the same class to repel one another.
Experiments show that SINCERE leads to better separation of embeddings from different classes while delivering competitive classification accuracy for supervised and transfer learning.
We further show an information-theoretic bound that relates SINCERE loss to the symmeterized KL divergence between data-generating distributions for a target class and all other classes. 
