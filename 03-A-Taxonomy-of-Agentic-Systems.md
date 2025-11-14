# A Taxonomy of Agentic Systems | <mark>智能体系统分类</mark>

---

## Introduction to Agents and Agent Architectures | <mark>智能体及其架构简介</mark>

**November 2025**

---

## A Taxonomy of Agentic Systems | <mark>智能体系统分类</mark>

Understanding the 5-step operational loop is the first part of the puzzle. The second is recognizing that this loop can be scaled in complexity to create different classes of agents. For an architect or product leader, a key initial decision is scoping what kind of agent to build.

<mark>理解 5 步操作循环是拼图的第一部分。第二部分是认识到这个循环可以在复杂性上扩展，以创建不同类别的智能体。对于架构师或产品负责人来说，一个关键的初始决策是确定要构建什么样的智能体。</mark>

We can classify agentic systems into a few broad levels, each building on the capabilities of the last.

<mark>我们可以将智能体系统分为几个大的层次，每个层次都建立在前一个的能力之上。</mark>

---

[IMAGE_2: image_002_page_14_1.png - 位于第 14 页]

![Agentic system in 5 steps](images/image_002_page_14_1.png)

**Figure 2: Agentic system in 5 steps**

<mark>**图 2：5 步智能体系统**</mark>

---

## Level 0: The Core Reasoning System | <mark>Level 0：核心推理系统</mark>

Before we can have an agent, we must start with the "Brain" in its most basic form: the reasoning engine itself. In this configuration, a Language Model (LM) operates in isolation, responding solely based on its vast pre-trained knowledge without any tools, memory, or interaction with the live environment.

<mark>在拥有智能体之前，我们必须从最基本形式的"大脑"开始：推理引擎本身。在这种配置中，语言模型 (LM) 在隔离状态下运行，仅基于其庞大的预训练知识进行响应，没有任何工具、记忆或与实时环境的交互。</mark>

Its strength lies in this extensive training, allowing it to explain established concepts and plan how to approach solving a problem with great depth. The trade-off is a complete lack of real-time awareness; it is functionally "blind" to any event or fact outside its training data.

<mark>它的优势在于这种广泛的训练，使其能够解释既定概念，并以很大的深度规划如何解决问题。权衡是完全缺乏实时意识；它在功能上对训练数据之外的任何事件或事实都是"盲目的"。</mark>

For instance, it can explain the rules of professional baseball and the complete history of the New York Yankees. But if you ask, "What was the final score of the Yankees game last night?", it would be unable to answer. That game is a specific, real-world event that happened after its training data was collected, so the information simply doesn't exist in its knowledge.

<mark>例如，它可以解释职业棒球的规则和纽约洋基队的完整历史。但如果你问，"昨晚洋基队比赛的最终比分是多少？"，它将无法回答。那场比赛是在其训练数据收集之后发生的特定真实世界事件，因此该信息根本不存在于其知识中。</mark>

---

## Level 1: The Connected Problem-Solver | <mark>Level 1：连接式问题解决者</mark>

At this level, the reasoning engine becomes a functional agent by connecting to and utilizing external tools - the "Hands" component of our architecture. Its problem-solving is no longer confined to its static, pre-trained knowledge.

<mark>在这个层次，推理引擎通过连接和利用外部工具——我们架构中的"双手"组件——成为功能性智能体。它的问题解决不再局限于其静态的预训练知识。</mark>

Using the 5-step loop, the agent can now answer our previous question. Given the "Mission": "What was the final score of the Yankees game last night?", its "Think" step recognizes this as a real-time data need. Its "Act" step then invokes a tool, like a Google Search API with the proper date and search terms. It "Observes" the search result (e.g., "Yankees won 5-3"), and synthesizes that fact into a final answer.

<mark>使用 5 步循环，智能体现在可以回答我们之前的问题。给定"任务"："昨晚洋基队比赛的最终比分是多少？"，它的"思考"步骤识别这是一个实时数据需求。然后它的"行动"步骤调用一个工具，比如带有正确日期和搜索词的 Google 搜索 API。它"观察"搜索结果（例如，"洋基队以 5-3 获胜"），并将该事实综合成最终答案。</mark>

This fundamental ability to interact with the world - whether using a search tool for a score, a financial API for a live stock price, or a database via Retrieval-Augmented Generation (RAG) is the core capability of a Level 1 agent.

<mark>这种与世界交互的基本能力——无论是使用搜索工具查询比分、使用金融 API 获取实时股票价格，还是通过检索增强生成 (Retrieval-Augmented Generation, RAG) 查询数据库——都是 Level 1 智能体的核心能力。</mark>

---

## Level 2: The Strategic Problem-Solver | <mark>Level 2：战略性问题解决者</mark>

Level 2 marks a significant expansion in capability, moving from executing simple tasks to strategically planning complex, multi-part goals. The key skill that emerges here is context engineering: the agent's ability to actively select, package, and manage the most relevant information for each step of its plan.

<mark>Level 2 标志着能力的显著扩展，从执行简单任务转向战略性规划复杂的多部分目标。这里出现的关键技能是上下文工程 (Context Engineering)：智能体主动选择、打包和管理其计划每个步骤最相关信息的能力。</mark>

An agent's accuracy depends on a focused, high-quality context. Context engineering curates the model's limited attention to prevent overload and ensure efficient performance.

<mark>智能体的准确性取决于专注的高质量上下文。上下文工程策展模型的有限注意力，以防止过载并确保高效性能。</mark>

For instance, consider the "Mission": "Find a good coffee shop halfway between my office at 1600 Amphitheatre Parkway, Mountain View, and my client's office at 1 Market St, San Francisco."

<mark>例如，考虑这个"任务"："在我位于 Mountain View 1600 Amphitheatre Parkway 的办公室和客户位于 San Francisco 1 Market St 的办公室之间找一家好的咖啡店。"</mark>

A Level 2 agent will start creating a plan:

<mark>Level 2 智能体将开始制定计划：</mark>

1. **Think**: "I must first find the halfway point."
   - **Act**: Call the Maps tool with both addresses.
   - **Observe**: "The halfway point is Millbrae, CA."

<mark>1. **思考**："我必须首先找到中点。"
   - **行动**：使用两个地址调用地图工具。
   - **观察**："中点是加州 Millbrae。"</mark>

2. **Think**: "Now I must find coffee shops in Millbrae. The user asked for 'good' ones, so I will search for places with a 4-star rating or higher."
   - **Act**: Call the google_places tool with query="coffee shop in Millbrae, CA", min_rating=4.0. (This is context engineering - it automatically created a new, focused search query from the previous step's output).
   - **Observe**: "The search returns 'Millbrae Coffee' and 'The Daily Grind'."

<mark>2. **思考**："现在我必须在 Millbrae 找咖啡店。用户要求'好的'咖啡店，所以我将搜索 4 星或更高评级的地方。"
   - **行动**：使用 query="coffee shop in Millbrae, CA"、min_rating=4.0 调用 google_places 工具。（这就是上下文工程——它自动从上一步的输出创建了一个新的、专注的搜索查询）。
   - **观察**："搜索返回'Millbrae Coffee'和'The Daily Grind'。"</mark>

3. **Think**: "I will synthesize these results and present them to the user."

<mark>3. **思考**："我将综合这些结果并呈现给用户。"</mark>

This strategic planning also enables proactive assistance, like an agent that reads a long flight confirmation email, engineers the key context (flight number, date), and acts by adding it to your calendar.

<mark>这种战略规划还支持主动协助，例如智能体读取长篇航班确认电子邮件，提取关键上下文（航班号、日期），并通过将其添加到日历中来行动。</mark>

---

## Level 3: The Collaborative Multi-Agent System | <mark>Level 3：协作式多智能体系统</mark>

At the highest level, the paradigm shifts entirely. We move away from building a single, all-powerful "super-agent" and toward a "team of specialists" working in concert, a model that directly mirrors a human organization. The system's collective strength lies in this division of labor.

<mark>在最高层次，范式完全转变。我们从构建单一的、全能的"超级智能体"转向协同工作的"专家团队"，这种模式直接反映了人类组织。系统的集体力量在于这种分工。</mark>

Here, agents treat other agents as tools. Imagine a "Project Manager" agent receiving a "Mission": "Launch our new 'Solaris' headphones."

<mark>在这里，智能体将其他智能体视为工具。想象一个"项目经理"智能体收到"任务"："推出我们的新'Solaris'耳机。"</mark>

The Project Manager agent doesn't do the entire work itself. It Acts by creating new Missions for its team of specialized agents much like how it works in the real life:

<mark>项目经理智能体不会自己完成全部工作。它通过为其专业智能体团队创建新任务来行动，就像在现实生活中一样：</mark>

1. **Delegates to MarketResearchAgent**: "Analyze competitor pricing for noise-canceling headphones. Return a summary document by tomorrow."

<mark>1. **委派给市场研究智能体 (MarketResearchAgent)**："分析降噪耳机的竞争对手定价。明天之前返回摘要文档。"</mark>

2. **Delegates to MarketingAgent**: "Draft three versions of a press release using the 'Solaris' product spec sheet as context."

<mark>2. **委派给营销智能体 (MarketingAgent)**："使用'Solaris'产品规格表作为上下文，起草三个版本的新闻稿。"</mark>

3. **Delegates to WebDevAgent**: "Generate the new product page HTML based on the attached design mockups."

<mark>3. **委派给网页开发智能体 (WebDevAgent)**："根据附加的设计样机生成新产品页面 HTML。"</mark>

This collaborative model, while currently constrained by the reasoning limitations of today's LMs, represents the frontier of automating entire, complex business workflows from start to finish.

<mark>这种协作模型，虽然目前受到当今 LM 推理能力限制的约束，但代表了从头到尾自动化整个复杂业务工作流的前沿。</mark>

---

## Level 4: The Self-Evolving System | <mark>Level 4：自我进化系统</mark>

Level 4 represents a profound leap from delegation to autonomous creation and adaptation. At this level, an agentic system can identify gaps in its own capabilities and dynamically create new tools or even new agents to fill them. It moves from using a fixed set of resources to actively expanding them.

<mark>Level 4 代表了从委派到自主创建和适应的深刻飞跃。在这个层次，智能体系统可以识别自身能力的差距，并动态创建新工具甚至新智能体来填补它们。它从使用固定的资源集转向主动扩展资源。</mark>

Following our example, the "Project Manager" agent, tasked with the 'Solaris' launch, might realize it needs to monitor social media sentiment, but no such tool or agent exists on its team.

<mark>延续我们的例子，负责'Solaris'发布的"项目经理"智能体可能意识到需要监控社交媒体情绪，但其团队中不存在这样的工具或智能体。</mark>

1. **Think (Meta-Reasoning)**: "I must track social media buzz for 'Solaris,' but I lack the capability."

<mark>1. **思考（元推理）**："我必须追踪'Solaris'的社交媒体热度，但我缺乏这种能力。"</mark>

2. **Act (Autonomous Creation)**: Instead of failing, it invokes a high-level AgentCreator tool with a new mission: "Build a new agent that monitors social media for keywords 'Solaris headphones', performs sentiment analysis, and reports a daily summary."

<mark>2. **行动（自主创建）**：它不是失败，而是调用高级 AgentCreator 工具并提出新任务："构建一个新智能体，监控社交媒体中的关键词'Solaris 耳机'，执行情绪分析，并报告每日摘要。"</mark>

3. **Observe**: A new, specialized SentimentAnalysisAgent is created, tested, and added to the team on the fly, ready to contribute to the original mission.

<mark>3. **观察**：一个新的专业情绪分析智能体 (SentimentAnalysisAgent) 被即时创建、测试并添加到团队中，准备为原始任务做出贡献。</mark>

This level of autonomy, where a system can dynamically expand its own capabilities, turns a team of agents into a truly learning and evolving organization.

<mark>这种自主性水平，即系统可以动态扩展自身能力，将智能体团队转变为真正的学习和进化组织。</mark>

---

**Page 14-18 | <mark>第 14-18 页</mark>**
