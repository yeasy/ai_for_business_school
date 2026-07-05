## 延伸阅读

本书全部数据与案例的出处，见[参考文献](references.md)与[数据与案例证据索引](evidence_index.md)；本篇不求全量，只按全书四部分精选二十余种最值得整篇精读的论文、报告、经典著作与官方文档，每条配一句导读，说明它为什么值得读、与哪一章互补。经典著作以出版信息标注；在线文献均为正文引用过的原始链接，以链接指向的版本为准。

### 第一部分 认知篇（第一至三章）

- **Timothy Bresnahan & Manuel Trajtenberg, _General Purpose Technologies: “Engines of Growth?”_（NBER 工作论文第 4148 号，[原文](https://www.nber.org/papers/w4148)）**——“通用目的技术”概念的原始论文，[1.2](../01_essence/1.2_llm_base.md) 的理论底座；精读可理解三特征中“催生互补创新”为何最关键——它直接预言了第九章的落地困境。
- **Paul A. David, _The Dynamo and the Computer_（《发电机与计算机》，1990，[JSTOR](https://www.jstor.org/stable/2006600)）**——电气化“生产率悖论”的出处，只有十余页；与 1.2 和 [9.3](../09_landing/9.3_workflow_rebuild.md) 的电气化叙事互文，把今天“人手一个 AI 助手”的做法照进一百年前的镜子。
- **克莱顿·克里斯坦森，《创新者的窘境》（The Innovator's Dilemma，1997，中译本多次再版）**——[3.4](../03_why_now/3.4_first_mover.md) 组织惯性（“管理得太好”的理性陷阱）与 [10.3](../10_strategy/10.3_three_strategies.md) 颠覆战略的理论源头；读柯达与诺基亚的故事之前，值得先读这本原典。
- **Epoch AI, _LLM Inference Price Trends_（[数据洞察页](https://epoch.ai/data-insights/llm-inference-price-trends)）**——第三章两条成本曲线（等价成本下行、前沿成本上行）的数据来源，持续更新；是“所有划不划算的结论都自带保质期、账要每年重算”（3.2）的现成工具。
- **OpenAI, _How Agents Are Transforming Work_（2026 年 6 月，[原文](https://openai.com/index/how-agents-are-transforming-work/)）**——[2.1](../02_agent/2.1_definition.md)“99.8%”数据的原始出处；建议带着本书的三重限定口径（内部员工、编程为主、输出 token 计）重读一遍厂商叙事，本身就是一次口径训练。
- **斯坦福 HAI，《AI 指数报告 2026》（[报告页](https://hai.stanford.edu/ai-index/2026-ai-index-report)）**——年度全景基准，[4.4](../04_llm/4.4_model_choice.md) 开源与闭源能力差距的口径出处；每年更新，适合作为全书各类数字的年度校准器。

### 第二部分 原理篇（第四至六章）

- **Jason Wei 等, _Chain-of-Thought Prompting Elicits Reasoning in Large Language Models_（2022，[arXiv](https://arxiv.org/abs/2201.11903)）**——思维链的源头论文，[5.1](../05_agent_tech/5.1_cot.md) 的起点；配合 DeepSeek-R1 经同行评审的[《自然》论文](https://www.nature.com/articles/s41586-025-09422-z)（2025）对读，可见“先想后答”如何从提示技巧变成训练出来的内生能力。
- **Patrick Lewis 等, _Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks_（2020，[arXiv](https://arxiv.org/abs/2005.11401)）**——RAG 的原始论文，[5.3](../05_agent_tech/5.3_rag.md)“开卷考试”比喻的学术起点；管理者读引言与结论即可，重在理解“检索质量决定生成质量”的因果链。
- **Kalai 等, _Why Language Models Hallucinate_（OpenAI，2025，[原文](https://openai.com/index/why-language-models-hallucinate/)）**——[4.3](../04_llm/4.3_hallucination.md) 幻觉第三层成因（评测激励奖励猜测）的依据；读懂它就明白幻觉为何部分是评测文化的产物、因而可以通过改变激励而改善，但不可根除。
- **Anthropic 工程博客, _Effective Context Engineering for AI Agents_（[原文](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)）**——[5.4](../05_agent_tech/5.4_context_eng.md) 上下文工程的实操延伸；“给对上下文，往往比换更强模型更有效”的一手论证，也是“行业经验如何变成智能体战斗力”的工程注脚。
- **Simon Willison, _The Lethal Trifecta for AI Agents_（2025，[原文](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)）**——[5.6](../05_agent_tech/5.6_security.md)“致命三件套”的出处，评估智能体风险敞口最好用的经验法则；与 OWASP [《LLM 应用十大风险》2025 版](https://genai.owasp.org/llm-top-10/)互为表里——一个给直觉，一个给清单。
- **Anthropic 工程博客, _Demystifying Evals for AI Agents_（[原文](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)）**——[6.5](../06_ecosystem/6.5_evaluation.md) 评测产线的方法来源；讲清黄金评测集为什么要从真实失败中来，以及评测如何从一次动作变成一条产线。

### 第三部分 落地篇（第七至九章）

- **罗纳德·科斯, _The Nature of the Firm_（《企业的性质》，1937，[原文](https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x)）**——交易成本理论的原点，[7.1](../07_value/7.1_value_shift.md) 用它解释智能体压缩协调与执行成本后企业边界为何松动；也是 6.3 与 10.4 自建与外购之辨最深处的学理。
- **Erik Brynjolfsson, Daniel Rock & Chad Syverson, _The Productivity J-Curve_（AEJ: Macroeconomics, 2021，[原文](https://www.aeaweb.org/articles?id=10.1257/mac.20180386)）**——全书理论主线的原始论文，[9.1](../09_landing/9.1_why_fail.md)“回报去哪儿了”的答案；与 Bresnahan & Trajtenberg 前后呼应，构成“通用目的技术—互补性投资—回报滞后”的完整链条。
- **Fortune 对 MIT NANDA《State of AI in Business 2025》的报道（2025 年 8 月，[原文](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)）**——“95%”数字进入公共讨论的现场；建议与 9.1“这组数字的口径与局限”一段对照读，练习把二手引用追回一手语境。
- **Gartner 新闻稿, _Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027_（2025 年 6 月，[原文](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)）**——[7.4](../07_value/7.4_budget.md) 与 9.1 引用的预测原文；精读价值在于观察严谨机构如何为预测加限定，以及企业该把预测当风险提示而非统计事实来使用。
- **Menlo Ventures, _2025: The State of Generative AI in the Enterprise_（[报告页](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)）**——7.4 规模化预算与支出结构的宏观参照；“支出重心从模型转向应用与运营”的量化证据，可用来校验自家预算结构是否漏掉了大头。
- **英矽智能关于 rentosertib 的公司公告（[原文](https://insilico.com/news_sc/dt2e5ogh61-rentosertib)）**——[8.4](../08_cases/8.4_pharma.md) 案例的一手后续：IIa 期临床结果发表、推进 III 期；对照阅读可以体会“研发前端提速”与“新药上市”之间还隔着什么，正是第八章口径纪律的活教材。

### 第四部分 战略篇（第十至十二章）

- **国务院，《关于深入实施“人工智能+”行动的意见》（2025 年 8 月，[原文](https://www.gov.cn/zhengce/content/202508/content_7037861.htm)）**——中国 AI 政策总纲，[12.2](../12_governance/12.2_regulation.md) 与 [12.4](../12_governance/12.4_ai_native.md) 反复引用；“智能原生企业”的官方定义与 2027/2030 普及率目标的出处，篇幅不长，值得逐条通读。
- **欧盟，《人工智能法案》（Regulation (EU) 2024/1689，[EUR-Lex 文本](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)）**——出海合规的基准法律文本；重点读风险分级与高风险义务清单，并结合 12.2 所述 2026 年简化修正案的生效时间表理解“推迟不是取消”。
- **NIST《人工智能风险管理框架》（[框架页](https://www.nist.gov/itl/ai-risk-management-framework)）与 ISO/IEC 42001（[标准页](https://www.iso.org/standard/81230.html)）**——[12.3](../12_governance/12.3_governance_system.md) 治理体系的两副“对表骨架”；适合在自建六要件制度时作检查清单用，但血肉只能来自自家业务与被验证的实践。
- **国家网信办等，《生成式人工智能服务管理暂行办法》（2023，[原文](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm)）与《人工智能生成合成内容标识办法》（2025，[原文](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm)）**——中国监管“小切口、快迭代”路线的一手文本，12.2 境内合规底线的直接依据；条文不多，建议合规负责人全文精读而非只读解读稿。
- **美国证监会对 Presto Automation 的执法文件（2025 年 1 月，[原文](https://www.sec.gov/enforcement-litigation/administrative-proceedings/33-11352-s)）**——首例针对上市公司“AI 洗白”的执法行动，[10.5](../10_strategy/10.5_pacing_reporting.md)“对外别把话说满”的最佳反面教材；读原始文书能看清监管认定夸大的具体尺度。
