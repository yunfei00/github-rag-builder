---
source: autogen
owner: microsoft
repo: autogen
path: docs/dotnet/index.md
url: https://github.com/microsoft/autogen/blob/main/docs/dotnet/index.md
---
---
_disableAffix: true
---

    AutoGen .NET
    
    A .NET framework for building AI agents and applications
    

  
    
      
        Core

        An event-driven programming framework for building scalable multi-agent AI systems.

- Deterministic and dynamic agentic workflows for business processes
- Research on multi-agent collaboration
- Distributed agents for multi-language applications
- integration with event-driven, cloud native applications

*Start here if you are building workflows or distributed agent systems*

```bash
dotnet add package Microsoft.AutoGen.Contracts
dotnet add package Microsoft.AutoGen.Core

# optionally - for distributed agent systems:
dotnet add package Microsoft.AutoGen.RuntimeGateway.Grpc
dotnet add package Microsoft.AutoGen.AgentHost

# other optional packages
dotnet add package Microsoft.AutoGen.Agents
dotnet add package Microsoft.AutoGen.Extensions.Aspire
dotnet add package Microsoft.AutoGen.Extensions.MEAI
dotnet add package Microsoft.AutoGen.Extensions.SemanticKernel
```

        Get started
      
    
  
  
    
      
        AgentChat
        A programming framework for building conversational single and multi-agent applications. Built on Core.
        Coming soon
