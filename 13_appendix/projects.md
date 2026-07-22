## 开源项目与平台清单

本清单汇总正文提及的开源项目、商业平台与标准协议，供选型时快速索引。**需要特别提示：智能体生态迭代极快，本表为 2026 年年中口径——星标数、版本号、产品线乃至项目本身，半年后都可能变化，使用前请以各项目官方页面的当时状态为准。**表中链接均取自正文；未列链接的条目，正文未附官方链接，请自行检索核实。

### 开源框架与开发工具

正文详见[第 6.1 节 开源框架图谱](../06_ecosystem/6.1_opensource.md)与[第 5.3 节 RAG](../05_agent_tech/5.3_rag.md)。开源框架承担“脚手架”角色：把工具调用、状态管理、多智能体协作等通用工程问题预先解决好。选定一个框架，往往同时选定了人才画像、生态依赖与后续维护成本。

| 名称 | 类型 | 一句话定位 | 适用场景 | 链接 |
|---|---|---|---|---|
| LangChain / LangGraph | 开源框架 | 企业侧采用最广的组合：LangChain 提供大模型应用通用组件，LangGraph 专注智能体编排，长于持久化状态管理与人在回路 | 有专职研发、要上生产环境的团队 | [GitHub](https://github.com/langchain-ai/langgraph)｜[官网](https://www.langchain.com) |
| CrewAI | 开源框架 | 以“角色班组”为范式的多智能体协作框架，隐喻贴近管理直觉、上手快 | 快速验证多角色分工的场景 | [GitHub](https://github.com/crewAIInc/crewAI)｜[官网](https://www.crewai.com) |
| Microsoft Agent Framework | 开源框架 | AutoGen 与 Semantic Kernel 合流后的微软系智能体框架，2026 年 4 月发布 1.0 | .NET / Azure 技术栈的企业 | [GitHub](https://github.com/microsoft/agent-framework)｜[文档](https://learn.microsoft.com/en-us/agent-framework/overview/) |
| OpenAI Agents SDK | 开源框架 | 轻量智能体框架，内建交接、护栏与追踪，与 OpenAI 模型及工具链衔接最顺 | 已锁定 OpenAI 系模型的团队 | [GitHub](https://github.com/openai/openai-agents-python)｜[文档](https://openai.github.io/openai-agents-python/) |
| Dify | 开源框架（低代码） | 国产开源可视化低代码平台：模型接入、RAG、工作流做成拖拽画布，GitHub 星标超 10 万 | 业务部门做原型与轻量应用 | [GitHub](https://github.com/langgenius/dify)｜[官网](https://dify.ai) |
| Coze Studio | 开源框架（低代码） | 字节扣子平台核心引擎，2025 年 7 月以 Apache 2.0 协议开源 | 零代码搭建与插件生态（商业侧见下表“扣子”） | [GitHub](https://github.com/coze-dev/coze-studio) |
| LlamaIndex | 开源框架 | 专注数据接入与检索 | RAG 的数据侧工程 | [GitHub](https://github.com/run-llama/llama_index) |
| Google ADK | 开源框架 | Google 的智能体开发套件，贴 Google 模型生态 | Google 云生态团队 | [GitHub](https://github.com/google/adk-python) |
| Claude Agent SDK | 开源框架 | Anthropic 的智能体开发套件，贴 Claude 模型生态 | Anthropic 系模型团队 | [GitHub](https://github.com/anthropics/claude-agent-sdk-python) |
| GraphRAG | 开源框架（检索） | 微软 2024 年开源，把文档抽取成知识图谱，能回答跨文档关联与全局概览类问题 | 知识关联复杂的场景；构建与维护成本明显更高 | [文档](https://microsoft.github.io/graphrag/) |

### 商业智能体平台

正文详见[第 6.2 节 商业平台格局](../06_ecosystem/6.2_platforms.md)。选择逻辑一句话：**跟着现有系统栈走**——先问“我的数据和员工在哪里”，再问“哪家平台演示效果好”；同时把计费口径与放量后的价格阶梯在试点前问清。

| 名称 | 类型 | 一句话定位 | 适用场景 | 链接 |
|---|---|---|---|---|
| Salesforce Agentforce | 商业平台 | CRM 原生智能体，直接长在客户数据与销售、服务流程之上 | 客户数据沉在 Salesforce 的企业；销售、客服流程自动化 | [官网](https://www.salesforce.com/agentforce/) |
| Microsoft Copilot Studio | 商业平台 | 依托 M365 生态的低代码智能体构建，直接部署进 Teams、Outlook；专业开发走 Azure AI Foundry | 办公在微软系的企业；员工助手、办公协同 | [官网](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio) |
| Google Gemini Enterprise | 商业平台 | 统一入口加智能体编排，2026 年与 Vertex AI 整合为统一企业智能体平台，力推 A2A 协议 | Google Cloud / Workspace 生态；跨系统编排 | [官网](https://cloud.google.com/gemini-enterprise) |
| AWS Bedrock AgentCore | 商业平台 | 基础设施中立的托管运行时：“自带框架、自带模型、自带协议”，配安全、记忆与可观测能力 | 技术自主性强、多云多模型并存的组织 | [官网](https://aws.amazon.com/bedrock/agentcore/) |
| 阿里云百炼 | 商业平台 | 一站式模型服务与智能体开发平台，依托通义系模型，企业级集成能力较全 | 国内企业级应用开发 | [官网](https://www.aliyun.com/product/bailian) |
| 字节扣子（Coze） | 商业平台 | 零代码搭建与插件生态见长，核心引擎已开源，走“商业平台＋开源”双线 | 轻量应用、面客分发 | [官网](https://www.coze.cn) |
| 百度千帆 | 商业平台 | 覆盖模型开发到应用搭建的全流程平台，依托文心系模型 | 国内企业级应用开发 | [官网](https://cloud.baidu.com/product/qianfan) |
| 腾讯元器 | 商业平台 | 轻量智能体创作与微信生态分发；企业级场景由腾讯云智能体开发平台承接（产品线多次调整，以官方页面为准） | 轻量应用、微信生态触达 | [官网](https://yuanqi.tencent.com) |
| SAP Joule / ServiceNow AI Agents 等 | 商业平台（SaaS 内嵌） | SaaS 产品原地长出的智能体能力，国内用友、金蝶等 ERP 与财务软件同样在版本升级中内嵌 | 采购独立 AI 产品前，先盘点现有软件供应商的智能体路线图，避免重复付费 | —（见各自产品页） |

### 协议与标准

正文详见[第 5.5 节 MCP 与 A2A](../05_agent_tech/5.5_mcp_a2a.md)与[第 5.6 节 安全边界](../05_agent_tech/5.6_security.md)。选型清单应加一问：是否原生支持 MCP（以及 A2A）？不支持开放协议的平台，要按更高的退出成本折价评估。

| 名称 | 类型 | 一句话定位 | 适用场景 | 链接 |
|---|---|---|---|---|
| MCP（Model Context Protocol） | 协议标准 | 智能体连接工具与数据源的标准接口（“AI 应用的 USB-C”），Anthropic 2024 年 11 月开源，2025 年 12 月捐赠给 Linux 基金会旗下智能体 AI 基金会；截至 2026 年年中已是业界事实标准 | 纵向“接能力”：智能体接入企业系统与数据 | [发布公告](https://www.anthropic.com/news/model-context-protocol)｜[捐赠公告](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) |
| A2A（Agent2Agent） | 协议标准 | 智能体间发现、委托任务与跟踪进度的协作协议，Google 2025 年 4 月发布、同年 6 月捐赠 Linux 基金会；已超 150 家组织参与；规范已发布 v1.0（2026-03）并更新至 v1.0.1（2026-05），但跨企业协作的实际案例仍少于 MCP | 横向“做协作”：跨厂商、跨框架的多智能体协作 | [发布公告](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)｜[基金会公告](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents)｜[一周年进展](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year) |
| OWASP《LLM 应用十大风险》 | 安全标准 | LLM 应用安全风险权威清单，提示注入连续两版居首位（LLM01） | 智能体安全评审的对照清单 | [官方页面](https://genai.owasp.org/llm-top-10/) |

一条对价关系须记住：每接入一个第三方 MCP 服务器，都等于引入一个供应链依赖——2025 年已有安全团队公开演示“工具投毒”攻击（见 [5.6](../05_agent_tech/5.6_security.md)），接入前要审查，接入后要盯更新。

### 评测与运维工具

正文详见[第 6.5 节 评估与运维](../06_ecosystem/6.5_evaluation.md)。智能体的质检是贯穿全生命周期的一条产线（AgentOps），黄金评测集是企业资产，也是验收谈判中“评估权”的物质载体。

| 名称 | 类型 | 一句话定位 | 适用场景 | 链接 |
|---|---|---|---|---|
| LangSmith | 评测工具（商业） | LangChain 公司的商业化调试与评估平台，以执行链路追踪为核心能力 | 智能体的调试、评测与追踪 | [官网](https://www.langchain.com) |
| Langfuse | 评测工具 | 与 LangSmith 并列提及的追踪（tracing）工具，完整记录每一步推理与工具调用链路 | 排障定位与审计留证 | — |

方法论层面，正文引用了两份官方指南可作评测体系建设参考：Anthropic《[Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)》（从 20—50 条源自真实失败的任务起步）与 OpenAI《[评估最佳实践](https://developers.openai.com/api/docs/guides/evaluation-best-practices)》（LLM 评审员先与人工标注对齐）。

### 开放权重模型

正文详见[第 4.4 节 模型选择的商业考量](../04_llm/4.4_model_choice.md)、[第 5.1 节 思维链与推理模型](../05_agent_tech/5.1_cot.md)与[第 6.4 节 部署与数据安全](../06_ecosystem/6.4_deployment.md)。2026 年格局最显著的事实：开放权重的主力供给来自中国厂商；私有化部署已从“能力上的妥协”变为“能力够用”的正常选项。各家基准测试口径不一，以自身任务实测为准。

| 名称 | 类型 | 一句话定位 | 适用场景 | 链接 |
|---|---|---|---|---|
| DeepSeek V3 / R1 | 开放权重 | MIT 许可开放权重与训练方法，R1 论文经《自然》同行评审并登上封面，大幅下修行业训练成本预期 | 私有化部署、低成本推理 | [R1 论文](https://arxiv.org/abs/2501.12948)｜[《自然》论文](https://www.nature.com/articles/s41586-025-09422-z) |
| 通义千问（Qwen） | 开放权重 | Apache 2.0 许可、覆盖大小尺寸的完整家族，全球衍生模型最多的开源模型系之一（Hugging Face 统计口径） | 私有化部署、按任务混搭不同尺寸 | — |
| 智谱 GLM、月之暗面 Kimi | 开放权重 | 持续开放旗舰级权重的国产模型系 | 私有化部署备选 | — |
| Meta Llama | 开放权重 | 海外开放权重代表，2025 年以来迭代声势较前明显放缓（正文口径） | 海外生态兼容场景 | — |
| OpenAI gpt-oss | 开放权重 | OpenAI 2025 年 8 月以该系列重返开放权重 | 开源部署备选 | — |

### 使用本清单的三条提醒

第一，框架选择本质是人才与生态的绑定：选微软系要有 .NET/Azure 储备，选 LangGraph 就进入 Python 工程师市场竞争——技术团队“顺手”的选择隐含着企业的招聘与留人成本。第二，低代码与代码框架不是二选一：常见打法是业务团队先用 Dify 一类工具验证场景价值，跑通后再由工程团队用 LangGraph 一类框架重写为可监控、可回滚的生产系统。第三，本领域从明星项目到并入新框架可能只需两年半（AutoGen 即是先例）——分层框架与判断逻辑比任何一个具体项目名字都更耐用，做选型决策时请回到[第六章](../06_ecosystem/README.md)的方法，并以官方文档的当时状态为准。
