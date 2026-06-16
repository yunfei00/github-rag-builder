---
source: autogen
owner: microsoft
repo: autogen
path: python/packages/autogen-magentic-one/README.md
url: https://github.com/microsoft/autogen/blob/main/python/packages/autogen-magentic-one/README.md
---
# Magentic-One

> Magentic-One is now available as part of the `autogen-agentchat` library.
> Please see the user guide for information.

> Looking for the original implementation of Magentic-One? It is available here.

Magentic-One is a generalist multi-agent system for solving open-ended web and file-based tasks across a variety of domains. It represents a significant step forward for multi-agent systems, achieving competitive performance on a number of agentic benchmarks (see the technical report for full details).

When originally released in November 2024 Magentic-One was implemented directly on the `autogen-core` library. We have now ported Magentic-One to use `autogen-agentchat`, providing a more modular and easier to use interface. To this end, the older implementation is deprecated, but can be accessed at https://github.com/microsoft/autogen/tree/v0.4.4/python/packages/autogen-magentic-one.

Moving forward, the Magentic-One orchestrator MagenticOneGroupChat is now simply an AgentChat team, supporting all standard AgentChat agents and features. Likewise, Magentic-One's MultimodalWebSurfer, FileSurfer, and MagenticOneCoderAgent agents are now broadly available as AgentChat agents, to be used in any AgentChat workflows.

Lastly, there is a helper class, MagenticOne, which bundles all of this together as it was in the paper with minimal configuration

## Citation

```
@misc{fourney2024magenticonegeneralistmultiagentsolving,
      title={Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks},
      author={Adam Fourney and Gagan Bansal and Hussein Mozannar and Cheng Tan and Eduardo Salinas and Erkang and Zhu and Friederike Niedtner and Grace Proebsting and Griffin Bassman and Jack Gerrits and Jacob Alber and Peter Chang and Ricky Loynd and Robert West and Victor Dibia and Ahmed Awadallah and Ece Kamar and Rafah Hosn and Saleema Amershi},
      year={2024},
      eprint={2411.04468},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2411.04468},
}
```
