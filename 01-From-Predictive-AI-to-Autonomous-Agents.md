# From Predictive AI to Autonomous Agents | <mark>从预测性 AI 到自主智能体</mark>

---

## Introduction to Agents and Agent Architectures | <mark>智能体及其架构简介</mark>

**November 2025**

---

## From Predictive AI to Autonomous Agents | <mark>从预测性 AI 到自主智能体</mark>

Artificial intelligence is changing. For years, the focus has been on models that excel at passive, discrete tasks: answering a question, translating text, or generating an image from a prompt. This paradigm, while powerful, requires constant human direction for every step. We're now seeing a paradigm shift, moving from AI that just predicts or creates content to a new class of software capable of autonomous problem-solving and task execution.

<mark>人工智能正在发生变革。多年来，人们一直专注于擅长被动、离散任务的模型：回答问题、翻译文本或根据提示生成图像。这种范式虽然强大，但每一步都需要持续的人工指导。我们现在正在见证一次范式转变，从仅能预测或创建内容的 AI，转向能够自主解决问题和执行任务的新型软件。</mark>

This new frontier is built around AI agents. An agent is not simply an AI model in a static workflow; it's a complete application, making plans and taking actions to achieve goals. It combines a Language Model's (LM) ability to reason with the practical ability to act, allowing

<mark>这一新前沿围绕着 AI 智能体 (AI Agents) 构建。智能体 (Agent) 不仅仅是静态工作流中的 AI 模型；它是一个完整的应用程序，能够制定计划并采取行动来实现目标。它将语言模型 (Language Model, LM) 的推理能力与实际行动能力相结合，使得</mark>

> **Agents are the natural evolution of Language Models, made useful in software.**
>
> <mark>**智能体是语言模型的自然演进，在软件中发挥实用价值。**</mark>

it to handle complex, multi-step tasks that a model alone cannot. The critical capability is that agents can work on their own, figuring out the next steps needed to reach a goal without a person guiding them at every turn.

<mark>智能体能够处理单个模型无法完成的复杂、多步骤任务。关键能力在于，智能体可以自主工作，无需在每个步骤都由人指导，就能确定达成目标所需的后续步骤。</mark>

---

This document is the first in a five-part series, acting as a formal guide for the developers, architects, and product leaders transitioning from proofs-of-concept to robust, production-grade agentic systems. While building a simple prototype is straightforward, ensuring security, quality and reliability is a significant challenge. This paper provides a comprehensive foundation:

<mark>本文档是五部分系列的第一部分，作为开发者、架构师和产品负责人从概念验证过渡到稳健的生产级智能体系统 (Agentic Systems) 的正式指南。虽然构建简单原型很容易，但确保安全性、质量和可靠性是一个重大挑战。本文提供了全面的基础：</mark>

- **Core Anatomy**: Deconstructing an agent into its three essential components: the reasoning Model, actionable Tools, and the governing Orchestration Layer.

<mark>- **核心解剖**：将智能体分解为三个基本组件：推理模型 (Model)、可执行工具 (Tools) 和治理编排层 (Orchestration Layer)。</mark>

- **A Taxonomy of Capabilities**: Classifying agents from simple, connected problem-solvers to complex, collaborative multi-agent systems.

<mark>- **能力分类**：对智能体进行分类，从简单的连接式问题解决者到复杂的协作式多智能体系统 (Multi-Agent Systems)。</mark>

- **Architectural Design**: Diving into the practical design considerations for each component, from model selection to tool implementation.

<mark>- **架构设计**：深入探讨每个组件的实际设计考虑因素，从模型选择到工具实现。</mark>

- **Building for Production**: Establishing the Agent Ops discipline needed to evaluate, debug, secure, and scale agentic systems from a single instance to a fleet with enterprise governance.

<mark>- **面向生产的构建**：建立 Agent Ops 规范，用于评估、调试、保护和扩展智能体系统，从单个实例扩展到具有企业治理的集群。</mark>

---

Building on the previous Agents whitepaper¹ and Agent Companion²; this guide provides the foundational concepts and strategic frameworks you will need to successfully build, deploy, and manage this new generation of intelligent applications which can reason, act and observe to accomplish goals³.

<mark>基于之前的智能体白皮书¹ 和智能体伴侣²；本指南提供了基础概念和战略框架，您将需要这些来成功构建、部署和管理这一新一代智能应用程序，它们能够推理 (Reason)、行动 (Act) 和观察 (Observe) 来完成目标³。</mark>

---

**References | <mark>参考文献</mark>**

1. Previous Agents whitepaper
2. Agent Companion
3. Goals-based intelligent applications

---

**Page 6-7 | <mark>第 6-7 页</mark>**
