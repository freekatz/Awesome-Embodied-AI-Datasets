# EmbodiedMemory-Bench


## Introduction

[EmbodiedMemory-Bench](https://arxiv.org/abs/2609.28236) evaluates whether agents retain and update information from earlier observations and interactions, then use it to perform later embodied actions. It contains 2,554 episodes across four families: passive observation, dynamic tracking, interaction failure, and experience generalization.

This is a simulated interactive evaluation dataset for AI2-THOR, with scene assets derived from AI2-THOR and ProcTHOR. It is not a real-robot teleoperation dataset. Public metadata and episode artifacts are available on [Hugging Face](https://huggingface.co/datasets/lzLiang/EmbodiedMemoryBench); preparation and evaluation instructions are in the [official code](https://github.com/ZJU-OmniAI/Embodied-Omni/tree/main/embodied_memory). The evaluator reports success rate and memory-augmented efficiency (MAE).

Dataset license: CC BY-NC 4.0, as declared in the dataset card. Code in the benchmark subdirectory uses Apache-2.0; simulator assets retain their own terms.


## Homepage

[Visit the dataset homepage](https://zju-omniai.github.io/Embodied-Omni/EmbodiedMemoryBench/)


## Task Description

Build and update memory from observation and interaction histories, then execute later tasks testing visual recall, dynamic state tracking, interaction outcomes, and experience generalization.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| License                     | CC BY-NC 4.0           |
| Action Space                     | Discrete AI2-THOR navigation and object-interaction actions           |
| Episodes                     | 2554           |
| Language Annotations                     | English task instructions           |
| Robot                     | AI2-THOR simulated agent           |
| Scene Type                     | Indoor household scenes           |
| Paper                     | https://arxiv.org/abs/2609.28236           |
| Code                     | https://github.com/ZJU-OmniAI/Embodied-Omni/tree/main/embodied_memory           |
| Dataset                     | https://huggingface.co/datasets/lzLiang/EmbodiedMemoryBench           |
| Simulator                     | AI2-THOR / ProcTHOR scenes           |
| Task Families                     | 4           |


