# Review: WordPress 7.0 Roadmap and AI Integration Goals

## Executive Summary

WordPress 7.0 is positioned as a date-driven release with a planned ship date of **April 9, 2026** on the public roadmap, alongside tentative dates for 7.1 and 7.2. The roadmap also reiterates a **feature freeze one month before release**, which reinforces timeline-first planning and scope flexibility. AI work is being coordinated through the WordPress AI Team and delivered via **canonical plugins and building blocks** (Abilities API, MCP Adapter, AI Experiments), keeping core flexible while the ecosystem converges on standards and patterns.

## Roadmap Snapshot (7.0)

- The WordPress public roadmap lists planned dates of **7.0 on April 9, 2026**, **7.1 on August 19, 2026**, and **7.2 on December 10, 2026**, and reiterates that **new features are frozen a month before a release** to focus on quality and performance. (Source: WordPress Roadmap)
- The January 2026 call for volunteers proposes a detailed 7.0 schedule: **Beta 1 on February 19, 2026**, **RC1 on March 19, 2026**, **RC3 on April 2, 2026**, **Dry Run on April 8, 2026**, and **final release on April 9, 2026**. The post notes the timeline is flexible and depends on the release squad. (Source: WordPress 7.0 Call for Volunteers)
- The 2026 major release schedule proposal reiterates a target of **three major releases in 2026** on a roughly four‑month cadence, aligning with the roadmap’s planned dates. (Source: 2026 Major Release Schedule)

**Implication:** the 7.0 planning signal is “timeline-first, scope-flexible.” Teams and plugin developers should expect scope to shift based on readiness rather than a locked feature list.

## AI Integration Goals

- The WordPress AI Team is tasked with **coordinating cross‑team AI work**, publishing a public roadmap for AI initiatives and canonical plugins, and collaborating with Core, Design, Accessibility, and other teams on shared standards. (Source: AI Team Announcement)
- The AI Building Blocks initiative defines the near‑term foundation: **Abilities API** for capability registration and an **MCP Adapter** that translates WordPress abilities into MCP tools/resources for AI assistants. (Source: AI Building Blocks)
- The AI Experiments plugin is positioned as a **reference implementation** and experimentation space, bringing **AI writing/editing tools** into WordPress while keeping features opt‑in and manually triggered. The plugin supports **OpenAI, Google AI (Gemini), and Anthropic (Claude)** providers. (Source: AI Experiments Plugin)
- The AI team’s six‑month recap emphasizes a **bidirectional MCP strategy**: WordPress will expose its own tools to MCP clients and also act as an MCP client to consume external MCP tools inside WordPress. (Source: Six Months of Core AI)

**Implication:** AI is being advanced as an ecosystem layer rather than a monolithic core feature. The canonical plugin strategy means the fastest progress will likely happen in plugins first, with core adoption contingent on stability and community alignment.

## What to Watch (Next 3–6 Months)

- **Feature scope clarity for 7.0**: The schedule implies feature freeze roughly one month before release (early March 2026), so the release squad’s decisions will define which projects land in 7.0. (Source: WordPress Roadmap)
- **AI Experiments plugin maturity**: The AI team has already outlined near‑term expansions (excerpt generation, image generation, Abilities Explorer, AI Playground); cadence and uptake will indicate readiness. (Source: Six Months of Core AI)
- **Abilities API and MCP adoption**: Growth of adapters and plugins built on these building blocks will reveal whether they are becoming de facto integration standards. (Source: AI Building Blocks)

## Risks and Uncertainties

- **Scope volatility**: the roadmap is timeline‑first, so late‑cycle feature inclusion can change quickly based on readiness.
- **AI standards churn and cost**: adapters (like MCP) reduce lock‑in, but AI providers and pricing vary, and the AI Experiments plugin requires external API keys. (Source: AI Experiments Plugin)

## Sources

- WordPress Roadmap: https://wordpress.org/about/roadmap/
- WordPress 7.0 Call for Volunteers: https://make.wordpress.org/test/2026/01/09/xpost-wordpress-7-0-call-for-volunteers/
- Proposal: 2026 Major Release Schedule: https://make.wordpress.org/project/2025/12/18/proposal-2026-major-release-schedule/
- Announcing the Formation of the WordPress AI Team: https://wordpress.org/news/2025/05/announcing-the-formation-of-the-wordpress-ai-team/
- AI Building Blocks for WordPress: https://make.wordpress.org/ai/2025/07/17/ai-building-blocks/
- AI Experiments Plugin: https://wordpress.org/plugins/ai/
- Six Months of Core AI: https://make.wordpress.org/ai/2025/12/03/six-months-of-core-ai/
