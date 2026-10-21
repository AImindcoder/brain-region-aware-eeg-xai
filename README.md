# Brain-Region-Aware Explainable AI for EEG-Based Neurological Disorder Detection

**Research focus:** EEG classification, explainable AI (XAI), and exploratory brain-region occlusion analysis.

## Overview

This project investigates whether perturbing groups of scalp EEG channels changes the predictions of a deep-learning model trained to distinguish normal from abnormal EEG recordings.

The initial study uses the NMT-Scalp-EEG dataset and a hybrid Convolutional Neural Network–Long Short-Term Memory (CNN–LSTM) classifier. Regional occlusion is used to examine the model's dependence on selected channel groups.

**Important:** Occlusion measures model sensitivity to an input perturbation. It does not establish the anatomical origin of an EEG signal, prove a neurological mechanism, or provide a disease-specific diagnosis.

## Research objectives

- Establish a baseline for normal-versus-abnormal EEG classification.
- Evaluate prediction changes when selected scalp-channel groups are masked.
- Compare regional occlusion effects against matched-size random channel groups.
- Report uncertainty, class imbalance, and statistical limitations transparently.
- Develop a reproducible framework for future, dataset-specific EEG experiments.

## Current experimental stage: NMT-Scalp-EEG

### Model and input

- **Architecture:** Hybrid CNN–LSTM.
- **Input:** 21 channels × 6,000 samples per window.
- **Window duration:** 30 seconds at 200 Hz.
- **Task:** Normal-versus-abnormal EEG classification.
- **Evaluation split:** 442 validation windows/records as defined by the existing experiment manifest; 378 normal and 64 abnormal.
- **Official evaluation set:** The separate set of 185 recordings was not used in this experiment.

The input includes 19 scalp channels and two auxiliary channels, A1 and A2. The regional comparisons use the 19 scalp channels; A1 and A2 are excluded from the five regional groups.

### Regional channel groups

| Region | Channels | Number |
|---|---|---:|
| Frontal | FP1, FP2, F3, F4, F7, F8, FZ | 7 |
| Central | C3, C4, CZ | 3 |
| Parietal | P3, P4, PZ | 3 |
| Temporal | T3, T4, T5, T6 | 4 |
| Occipital | O1, O2 | 2 |

For regional occlusion, the selected channels are replaced with their temporal mean. This is a perturbation-based model analysis, not physiological source localization.

## Baseline validation results

| Metric | Result |
|---|---:|
| Accuracy | 0.8100 |
| Balanced accuracy | 0.6423 |
| Macro F1 | 0.6350 |
| AUROC | 0.7600 |
| Abnormal-class precision | 0.3611 |
| Abnormal-class sensitivity | 0.4063 |
| Specificity | 0.8783 |

Confusion matrix, with rows representing true classes and columns representing predicted classes:

| | Predicted normal | Predicted abnormal |
|---|---:|---:|
| True normal | 332 | 46 |
| True abnormal | 38 | 26 |

The validation set is imbalanced, with 64 abnormal examples out of 442. Accuracy alone therefore does not adequately describe model performance. Abnormal-class sensitivity is limited, and these results should not be interpreted as evidence of clinical readiness.

## Regional occlusion results

| Region masked | AUROC after masking | AUROC decrease |
|---|---:|---:|
| Frontal | 0.6996 | 0.0604 |
| Central | 0.7374 | 0.0226 |
| Parietal | 0.7238 | 0.0362 |
| Temporal | 0.7483 | 0.0117 |
| Occipital | 0.7532 | 0.0068 |

An AUROC decrease indicates that the model's discrimination changed after the selected input channels were perturbed. It does not, by itself, establish that a region is biologically responsible for an abnormality.

## Matched-size random-channel comparison

The regional groups were compared with 200 random channel groups for each corresponding group size (2, 3, 4, and 7 channels), using the same 19 scalp channels.

| Region | Observed AUROC decrease | Empirical p-value | FDR-adjusted p-value |
|---|---:|---:|---:|
| Frontal | 0.0604 | 0.3881 | 0.6468 |
| Central | 0.0226 | 0.3367 | 0.6468 |
| Parietal | 0.0362 | 0.0948 | 0.4738 |
| Temporal | 0.0117 | 0.8358 | 0.8358 |
| Occipital | 0.0068 | 0.6169 | 0.7711 |

No regional AUROC effect was statistically significant after false-discovery-rate (FDR) correction in this comparison. The results therefore do **not** establish regional specificity beyond the matched random-channel control.

Some changes in abnormal-class sensitivity were observed under masking, but they should be interpreted cautiously alongside the class imbalance, uncertainty, and lack of significant adjusted AUROC effects.

## Interpretation and limitations

1. This is an exploratory normal-versus-abnormal EEG screening experiment, not a disease-specific diagnostic system.
2. Regional masking tests model dependence on selected inputs; it does not localize the physiological source of abnormal activity.
3. The validation set contains relatively few abnormal examples, limiting the precision of sensitivity estimates.
4. The regional AUROC comparisons did not survive FDR correction.
5. EEG amplitude calibration and physical-unit interpretation require confirmation from the dataset documentation.
6. The separate official evaluation set remains untouched and must not be used for model selection or exploratory tuning.
7. Results from other datasets must be analyzed separately when their labels, recording protocols, or clinical tasks differ.

## Planned research stages

### Stage 1 — NMT-Scalp-EEG

Document and verify the existing baseline and regional occlusion experiments, including their statistical limitations.

### Stage 2 — CHB-MIT

Investigate seizure-versus-non-seizure classification and, where supported by the annotations, seizure onset and offset analysis. CHB-MIT is a seizure-focused dataset; its labels must not be treated as equivalent to the NMT normal-versus-abnormal labels.

### Stage 3 — Artifact analysis

Consider a separate artifact-detection experiment only if suitable data and reliable artifact labels are available. Artifact detection should not be conflated with neurological disorder classification.

Future results will be added only after the relevant data, evaluation protocol, and outputs have been independently checked.

## Reproducibility and data protection

This repository is intended for research documentation and code that can legally be shared.

- Do not commit raw EEG recordings, cached EEG arrays, patient identifiers, private manifests, model checkpoints, credentials, or restricted dataset files.
- Follow the original dataset's access terms, citation requirements, and redistribution restrictions.
- Keep local data paths, machine-specific settings, and private research files outside the public repository.
- The `.gitignore` file reduces the risk of accidental additions but does not remove files that have already been committed.
- Scripts and reported outputs should be checked for consistency before publication.

## Dataset citation

Add the verified official citation and access information for the NMT-Scalp-EEG dataset before formal publication. Dataset attribution and permitted redistribution must be confirmed from its official documentation.

## Project status

**Status:** Exploratory validation and regional-occlusion analysis completed; further reproducibility review and independent validation are needed.

These results are preliminary research findings, not clinical evidence or medical advice.
