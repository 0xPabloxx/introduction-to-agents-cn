# Introduction to AI Agents | <mark>AI 智能体简介</mark>

---

## Introduction to Agents and Agent Architectures | <mark>智能体及其架构简介</mark>

**November 2025**

---

Words are insufficient to describe how humans interact with AI. We tend to anthropomorphize and use human terms like "think" and "reason" and "know." We don't yet have words for "know with semantic meaning" vs "know with high probability of maximizing a reward function." Those are two different types of knowing, but the results are the same 99.X% of the time.

<mark>语言不足以描述人类如何与 AI 交互。我们倾向于拟人化，使用诸如"思考"、"推理"和"知道"等人类术语。我们还没有词汇来区分"以语义意义知道"与"以最大化奖励函数的高概率知道"。这是两种不同类型的知道，但在 99.X% 的情况下，结果是相同的。</mark>

---

## Introduction to AI Agents | <mark>AI 智能体简介</mark>

In the simplest terms, an AI Agent can be defined as the combination of models, tools, an orchestration layer, and runtime services which uses the LM in a loop to accomplish a goal. These four elements form the essential architecture of any autonomous system.

<mark>简而言之，AI 智能体 (AI Agent) 可以定义为模型 (Models)、工具 (Tools)、编排层 (Orchestration Layer) 和运行时服务 (Runtime Services) 的组合，在循环中使用大语言模型 (LM) 来完成目标。这四个要素构成了任何自主系统的基本架构。</mark>

- **The Model (The "Brain")**: The core language model (LM) or foundation model that serves as the agent's central reasoning engine to process information, evaluate options, and make decisions. The type of model (general-purpose, fine-tuned, or multimodal) dictates the agent's cognitive capabilities. An agentic system is the ultimate curator of the input context window the LM.

<mark>- **模型（"大脑"）**：核心语言模型 (LM) 或基础模型，作为智能体的中央推理引擎，用于处理信息、评估选项和做出决策。模型的类型（通用型、微调型或多模态）决定了智能体的认知能力。智能体系统 (Agentic System) 是 LM 输入上下文窗口的最终策展者。</mark>

- **Tools (The "Hands")**: These mechanisms connect the agent's reasoning to the outside world, enabling actions beyond text generation. They include API extensions, code functions, and data stores (like databases or vector stores) for accessing real-time, factual information. An agentic system allows a LM to plan which tools to use, executes the tool, and puts the tool results into the input context window of the next LM call.

<mark>- **工具（"双手"）**：这些机制将智能体的推理与外部世界连接起来，实现超越文本生成的行动。它们包括 API 扩展、代码函数和数据存储（如数据库或向量存储），用于访问实时、事实性信息。智能体系统允许 LM 规划使用哪些工具，执行工具，并将工具结果放入下一次 LM 调用的输入上下文窗口中。</mark>

- **The Orchestration Layer (The "Nervous System")**: The governing process that manages the agent's operational loop. It handles planning, memory (state), and reasoning strategy execution. This layer uses prompting frameworks and reasoning techniques (like Chain-of-Thought⁴ or ReAct⁵) to break down complex goals into steps and decide when to think versus use a tool. This layer is also responsible for giving agents the memory to "remember."

<mark>- **编排层（"神经系统"）**：管理智能体操作循环的治理过程。它处理规划 (Planning)、记忆 (Memory)（状态）和推理策略执行。该层使用提示框架和推理技术（如思维链 Chain-of-Thought⁴ 或 ReAct⁵）将复杂目标分解为步骤，并决定何时思考与何时使用工具。该层还负责赋予智能体"记忆"能力。</mark>

- **Deployment (The "Body and Legs")**: While building an agent on a laptop is effective for prototyping, production deployment is what makes it a reliable and accessible service. This involves hosting the agent on a secure, scalable server and integrating it with essential production services for monitoring, logging, and management. Once deployed, the agent can be accessed by users through a graphical interface or programmatically by other agents via an Agent-to-Agent (A2A) API.

<mark>- **部署（"身体和腿"）**：虽然在笔记本电脑上构建智能体对原型设计很有效，但生产部署才能使其成为可靠且可访问的服务。这涉及在安全、可扩展的服务器上托管智能体，并将其与监控、日志记录和管理的关键生产服务集成。部署后，用户可以通过图形界面访问智能体，或其他智能体可以通过智能体对智能体 (Agent-to-Agent, A2A) API 以编程方式访问。</mark>

---

At the end of the day, building a generative AI agent is a new way to develop solutions to solve tasks. The traditional developer acts as a "bricklayer," precisely defining every logical step. The agent developer, in contrast, is more like a director. Instead of writing explicit code for every action, you set the scene (the guiding instructions and prompts), select the cast (the tools and APIs), and provide the necessary context (the data). The primary task becomes guiding this autonomous "actor" to deliver the intended performance.

<mark>归根结底，构建生成式 AI 智能体是开发解决任务的新方式。传统开发者就像"砌砖工"，精确定义每一个逻辑步骤。相比之下，智能体开发者更像是导演。你不是为每个动作编写明确的代码，而是布置场景（指导说明和提示），选择演员（工具和 API），并提供必要的上下文（数据）。主要任务变成了引导这个自主"演员"提供预期的表现。</mark>

You'll quickly find that an LM's greatest strength—its incredible flexibility—is also your biggest headache. A large language model's capacity to do anything makes it difficult to compel it to do one specific thing reliably and perfectly. What we used to call "prompt engineering" and now call "context engineering" guides LMs to generate the desired output. For any single call to a LM, we input our instructions, facts, available tools to call, examples, session history, user profile, etc – filling the context window with just the right information to get the outputs we need. Agents are software which manage the inputs of LMs to get work done.

<mark>你很快会发现，LM 最大的优势——其令人难以置信的灵活性——也是你最大的头痛问题。大语言模型什么都能做的能力，使得很难让它可靠且完美地做一件特定的事情。我们曾称之为"提示工程 (Prompt Engineering)"，现在称为"上下文工程 (Context Engineering)"，用于引导 LM 生成所需的输出。对于对 LM 的任何单次调用，我们都会输入指令、事实、可调用的工具、示例、会话历史、用户配置等——用恰到好处的信息填充上下文窗口，以获得我们需要的输出。智能体是管理 LM 输入以完成工作的软件。</mark>

Debugging becomes essential when issues arise. "Agent Ops" essentially redefines the familiar cycle of measurement, analysis, and system optimization. Through traces and logs, you can monitor the agent's "thought process" to identify deviations from the intended execution path. As models evolve and frameworks improve, the developer's role is to furnish critical components: domain expertise, a defined personality, and seamless integration with the tools necessary for practical task completion. It's crucial to remember that comprehensive evaluations and assessments often outweigh the initial prompt's influence.

<mark>当问题出现时，调试变得至关重要。"Agent Ops"本质上重新定义了熟悉的测量、分析和系统优化循环。通过跟踪和日志，你可以监控智能体的"思维过程"，识别与预期执行路径的偏差。随着模型的发展和框架的改进，开发者的角色是提供关键组件：领域专业知识、明确的个性，以及与实际任务完成所需工具的无缝集成。重要的是要记住，全面的评估和评价往往超过初始提示的影响。</mark>

When an agent is precisely configured with clear instructions, reliable tools, and an integrated context serving as memory, a great user interface, the ability to plan and problem solve, and general world knowledge, it transcends the notion of mere "workflow automation." It begins to function as a collaborative entity: a highly efficient, uniquely adaptable, and remarkably capable new member of your team.

<mark>当智能体被精确配置，具备清晰的指令、可靠的工具、作为记忆的集成上下文、出色的用户界面、规划和解决问题的能力以及通用世界知识时，它超越了单纯"工作流自动化"的概念。它开始作为协作实体发挥作用：一个高效、独特适应性强且能力卓越的团队新成员。</mark>

---

In essence, an agent is a system dedicated to the art of context window curation. It is a relentless loop of assembling context, prompting the model, observing the result, and then re-assembling a context for the next step. The context may include system instructions, user input, session history, long term memories, grounding knowledge from authoritative sources, what tools could be used, and the results of tools already invoked. This sophisticated management of the model's attention allows its reasoning capabilities to problem solve for novel circumstances and accomplish objectives.

<mark>本质上，智能体是一个致力于上下文窗口策展艺术的系统。它是一个不懈的循环：组装上下文、提示模型、观察结果，然后为下一步重新组装上下文。上下文可能包括系统指令、用户输入、会话历史、长期记忆、来自权威来源的基础知识、可以使用的工具以及已调用工具的结果。对模型注意力的这种复杂管理，使其推理能力能够解决新情况并完成目标。</mark>

---

## The Agentic Problem-Solving Process | <mark>智能体问题解决过程</mark>

We have defined an AI agent as a complete, goal-oriented application that integrates a reasoning model, actionable tools, and a governing orchestration layer. A short version is "LMs in a loop with tools to accomplish an objective."

<mark>我们将 AI 智能体定义为一个完整的、目标导向的应用程序，它集成了推理模型、可执行工具和治理编排层。简短版本是"在循环中使用工具的 LM，以完成目标"。</mark>

But how does this system actually work? What does an agent do from the moment it receives a request to the moment it delivers a result?

<mark>但这个系统实际上是如何工作的？智能体从接收请求到交付结果的整个过程中做了什么？</mark>

At its core, an agent operates on a continuous, cyclical process to achieve its objectives. While this loop can become highly complex, it can be broken down into five fundamental steps as discussed in detail in the book Agentic System Design:⁶

<mark>从核心来看，智能体通过持续的循环过程来实现其目标。虽然这个循环可能变得非常复杂，但可以分解为五个基本步骤，详见《智能体系统设计》一书⁶：</mark>

1. **Get the Mission**: The process is initiated by a specific, high-level goal. This mission is provided by a user (e.g., "Organize my team's travel for the upcoming conference") or an automated trigger (e.g., "A new high-priority customer ticket has arrived").

<mark>1. **获取任务**：该过程由特定的高级目标启动。此任务由用户提供（例如，"为即将到来的会议组织我团队的旅行"）或由自动触发器提供（例如，"有新的高优先级客户工单到达"）。</mark>

2. **Scan the Scene**: The agent perceives its environment to gather context. This involves the orchestration layer accessing its available resources: "What does the user's request say?", "What information is in my term memory? Did I already try to do this task? Did the user give me guidance last week?", "What can I access from my tools, like calendars, databases, or APIs?"

<mark>2. **扫描场景**：智能体感知其环境以收集上下文。这涉及编排层访问其可用资源："用户的请求说了什么？"、"我的短期记忆中有什么信息？我已经尝试过这个任务了吗？用户上周给了我指导吗？"、"我可以从工具（如日历、数据库或 API）中访问什么？"</mark>

3. **Think It Through**: This is the agent's core "think" loop, driven by the reasoning model. The agent analyzes the Mission (Step 1) against the Scene (Step 2) and devises a plan. This isn't a single thought, but often a chain of reasoning: "To book travel, I first need to know who is on the team. I will use the get_team_roster tool. Then I will need to check their availability via the calendar_api."

<mark>3. **深思熟虑**：这是智能体的核心"思考"循环，由推理模型驱动。智能体根据场景（步骤 2）分析任务（步骤 1）并制定计划。这不是单一的思考，而是通常是一连串的推理："要预订旅行，我首先需要知道团队中有谁。我将使用 get_team_roster 工具。然后我需要通过 calendar_api 检查他们的可用性。"</mark>

4. **Take Action**: The orchestration layer executes the first concrete step of the plan. It selects and invokes the appropriate tool—calling an API, running a code function, or querying a database. This is the agent acting on the world beyond its own internal reasoning.

<mark>4. **采取行动**：编排层执行计划的第一个具体步骤。它选择并调用适当的工具——调用 API、运行代码函数或查询数据库。这是智能体对其内部推理之外的世界采取行动。</mark>

5. **Observe and Iterate**: The agent observes the outcome of its action. The get_team_roster tool returns a list of five names. This new information is added to the agent's context or "memory." The loop then repeats, returning to Step 3: "Now that I have the roster, my next step is to check the calendar for these five people. I will use the calendar_api."

<mark>5. **观察与迭代**：智能体观察其行动的结果。get_team_roster 工具返回五个名字的列表。这个新信息被添加到智能体的上下文或"记忆"中。然后循环重复，返回步骤 3："现在我有了名册，我的下一步是检查这五个人的日历。我将使用 calendar_api。"</mark>

---

This "Think, Act, Observe" cycle continues - managed by the Orchestration Layer, reasoned by the Model, and executed by the Tools until the agent's internal plan is complete and the initial Mission is achieved.

<mark>这个"思考、行动、观察"循环持续进行——由编排层管理、由模型推理、由工具执行，直到智能体的内部计划完成并实现初始任务。</mark>

---

[IMAGE_1: image_001_page_12_1.png - 位于第 12 页]

![Agentic AI problem-solving process](images/image_001_page_12_1.png)

**Figure 1: Agentic AI problem-solving process**

<mark>**图 1：智能体 AI 问题解决过程**</mark>

---

Let's take a real-world example of how a Customer Support Agent would operate in this 5-step cycle:

<mark>让我们看一个客户支持智能体如何在这个 5 步循环中运作的实际例子：</mark>

Imagine a user asks, "Where is my order #12345?"

<mark>假设用户问："我的订单 #12345 在哪里？"</mark>

Instead of immediately acting, the agent first enters its "Think It Through" phase to devise a complete strategy. It reasons:

<mark>智能体不是立即行动，而是首先进入"深思熟虑"阶段，制定完整的策略。它推理如下：</mark>

"The user wants a delivery status. To provide a complete answer, I need a multi-step plan:

<mark>"用户想要配送状态。为了提供完整的答案，我需要一个多步骤计划：</mark>

1. **Identify**: I must first find the order in our internal database to confirm it exists and get its details.

<mark>1. **识别**：我必须首先在内部数据库中找到订单，以确认它存在并获取其详细信息。</mark>

2. **Track**: From those details, I'll need to extract the shipping carrier's tracking number. Then, I'll query the external carrier's API for the live status.

<mark>2. **追踪**：从这些详细信息中，我需要提取运输承运商的追踪号。然后，我将查询外部承运商的 API 以获取实时状态。</mark>

3. **Report**: Finally, I must synthesize the information I've gathered into a clear, helpful response for the user."

<mark>3. **报告**：最后，我必须将收集的信息综合成清晰、有用的回复给用户。"</mark>

With this multi-step plan in mind, the agent begins execution.

<mark>有了这个多步骤计划，智能体开始执行。</mark>

In its first "Act" phase, it executes step one of its plan, calling the find_order("12345") tool. It observes the result—a full order record, including the tracking number "ZYX987."

<mark>在第一个"行动"阶段，它执行计划的第一步，调用 find_order("12345") 工具。它观察结果——完整的订单记录，包括追踪号"ZYX987"。</mark>

The agent's orchestration layer recognizes that the first part of its plan is complete and immediately proceeds to the second. It acts by calling the get_shipping_status("ZYX987") tool. It observes the new result: "Out for Delivery."

<mark>智能体的编排层识别到其计划的第一部分已完成，并立即进行第二部分。它通过调用 get_shipping_status("ZYX987") 工具来行动。它观察到新结果："正在配送中"。</mark>

Finally, having successfully executed the data-gathering stages of its plan, the agent moves to the "Report" step. It perceives it has all the necessary components, plans the final message, and acts by generating the response: "Your order #12345 is 'Out for Delivery'!"

<mark>最后，成功执行了计划的数据收集阶段后，智能体进入"报告"步骤。它感知到拥有所有必要的组件，计划最终消息，并通过生成回复来行动："您的订单 #12345 正在配送中！"</mark>

---

**References | <mark>参考文献</mark>**

4. Chain-of-Thought reasoning
5. ReAct (Reasoning and Acting)
6. Agentic System Design

---

**Page 8-13 | <mark>第 8-13 页</mark>**
