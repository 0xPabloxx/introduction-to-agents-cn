# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **bilingual Chinese-English translation project** of "Introduction to Agents: From Predictive AI to Autonomous Agents". The book provides a comprehensive introduction to AI agents, covering the evolution from predictive AI to autonomous agents.

**Key Characteristics:**
- Pure documentation/translation project (no code to build, test, or run)
- All content is in Markdown format
- Uses HTML `<mark>` tags for Chinese text highlighting
- Follows strict bilingual format with English and Chinese side-by-side
- Original book has 54 pages across 7 chapters (including Endnotes)
- Contains 11 images and diagrams that need proper positioning

## File Structure

```
01-From-Predictive-AI-to-Autonomous-Agents.md
02-Introduction-to-AI-Agents.md
03-A-Taxonomy-of-Agentic-Systems.md
04-Core-Agent-Architecture.md
05-Examples-of-Advanced-Agents.md
06-Conclusion.md
07-Endnotes.md

images/
  ├── image_001_page_12_1.png
  ├── image_002_page_14_1.png
  └── ... (11 images total)

chapters/                  # Extracted source text
  ├── chapter01_From_Predictive_AI_to_Autonomous_Agents.txt
  ├── chapter02_Introduction_to_AI_Agents.txt
  ├── ...
  └── image_index.md      # Image location index

scripts/
  └── extract_text_and_images.py

README.md
CLAUDE.md
.gitignore
```

## Translation Format and Rules

### Mandatory Highlighting System

**All Chinese translations MUST use HTML `<mark>` tags:**
```markdown
English text here.

<mark>中文翻译在这里。</mark>
```

This creates yellow highlighting for Chinese content on GitHub, making it easy to distinguish between languages.

### Layout Format

**Bilingual paragraph-by-paragraph:**
```markdown
[English paragraph 1]

<mark>[中文翻译段落 1]</mark>

[English paragraph 2]

<mark>[中文翻译段落 2]</mark>
```

### Image Handling

**Critical Requirement**: Images must be positioned exactly where they appear in the original text.

**Format for images:**
```markdown
[IMAGE_001: image_001_page_12_1.png - 位于第 12 页]

![Agent Architecture Diagram](images/image_001_page_12_1.png)

<mark>[图片_001：智能体架构图 - 第 12 页]</mark>

[Continue with text that follows the image]
```

**Image reference format in extracted text:**
```
[IMAGE_1: image_001_page_12_1.png - 位于第 12 页]
```

When translating, replace this marker with the proper Markdown image syntax shown above.

### Technical Term Conventions

Keep important terms in English with Chinese in parentheses on first use:
- Agent → 智能体 (Agent)
- Agentic System → 智能体系统 (Agentic System)
- Autonomous Agent → 自主智能体 (Autonomous Agent)
- Predictive AI → 预测性 AI (Predictive AI)
- Model → 模型 (Model)
- Tools → 工具 (Tools)
- Orchestration → 编排 (Orchestration)
- LLM → 大语言模型 (LLM)
- Reasoning → 推理 (Reasoning)
- Planning → 规划 (Planning)
- Memory → 记忆 (Memory)
- Reflection → 反思 (Reflection)
- Tool Use → 工具使用 (Tool Use)

Reference the technical term dictionary in README.md for consistent translations.

### Spacing Rules

- Add space between Chinese and English: `AI 系统`
- Add space between Chinese and numbers: `7 个章节`
- Use Chinese punctuation in Chinese context
- Use English punctuation in English context

### Format Requirements

- Use horizontal rules (`---`) to separate major sections
- Preserve all original formatting
- Maintain exact Markdown formatting from original
- Use proper Chinese quotation marks: 「」 or ""

## Translation Quality Standards

1. **Accuracy**: 100% faithful to original meaning
2. **Fluency**: Natural Chinese expression that follows local conventions
3. **Technical Precision**: Maintain technical document rigor
4. **Consistency**: Uniform terminology throughout
5. **Format Compliance**: 100% correct Markdown syntax
6. **Image Positioning**: All images in correct locations matching original

## Image Tracking

The project has extracted 11 images:
- Chapter 2 (Introduction to AI Agents): 1 image
- Chapter 3 (A Taxonomy of Agentic Systems): 1 image
- Chapter 4 (Core Agent Architecture): 5 images
- Chapter 5 (Examples of Advanced Agents): 4 images

Reference `chapters/image_index.md` for complete image location mapping.

## Project Status

Translation progress:
- ✅ Extraction Complete: All text and images extracted
- ⏳ In Progress: None
- ❌ Pending: All 7 chapters (0/7, 0%)

Check README.md for detailed progress tracking.

## Common Tasks

### Starting a New Chapter Translation

1. Read the corresponding source file from `chapters/chapter0X_*.txt`
2. Check `chapters/image_index.md` for any images in this chapter
3. Create new translation file following naming convention: `0X-Title.md`
4. Apply `<mark>` tags to ALL Chinese text
5. Position images exactly where marked in source text
6. Translate image captions in both English and Chinese
7. Update README.md progress table when complete

### Handling Images in Translation

1. Locate image markers in source text: `[IMAGE_X: filename - 位于第 Y 页]`
2. Find the actual image file in `images/` directory
3. Insert proper Markdown image syntax at exact marker location
4. Provide bilingual caption
5. Ensure image renders correctly in Markdown preview

### Translating Endnotes

The Endnotes chapter (Chapter 7) contains references and citations. When translating:
1. Keep all URLs and links intact
2. Translate descriptive text while preserving technical references
3. Maintain citation format and numbering
4. Use `<mark>` tags for Chinese translations

### Reviewing Translations

Check for:
- `<mark>` tags around all Chinese content
- Consistent technical term usage (check README.md dictionary)
- Proper spacing between Chinese/English and numbers
- Horizontal rules between major sections
- All images present and correctly positioned
- Image captions in both languages
- Correct Markdown syntax rendering

## Important Notes

- **No build/test/run commands**: This is a pure documentation project
- **All files are Markdown**: No code compilation or execution needed
- **GitHub is the primary viewing platform**: Format optimized for GitHub rendering
- **Yellow highlighting is essential**: `<mark>` tags are mandatory for all Chinese text
- **Image positioning is critical**: Must match original PDF layout
- **Endnotes must be translated**: Complete coverage required
- **License**: Translation released under CC BY-NC 4.0
- **Purpose**: Educational and community contribution only

## Book Structure Summary

The book covers:

**Chapter 1: From Predictive AI to Autonomous Agents (2 pages)**
- Introduction to the evolution from traditional AI to agents

**Chapter 2: Introduction to AI Agents (6 pages, 1 image)**
- Core concepts and definitions
- Basic agent characteristics

**Chapter 3: A Taxonomy of Agentic Systems (5 pages, 1 image)**
- Classification of different agent types
- System categorization

**Chapter 4: Core Agent Architecture (28 pages, 5 images)**
- Model component
- Tools component
- Orchestration component
- Largest and most technical chapter

**Chapter 5: Examples of Advanced Agents (4 pages, 4 images)**
- Real-world agent implementations
- Case studies

**Chapter 6: Conclusion (1 page)**
- Summary and future directions

**Chapter 7: Endnotes (3 pages)**
- References and citations
- Additional resources

## Resources

- **GitHub Repository**: https://github.com/0xPabloxx/introduction-to-agents-cn
- **Related Project - AI Agents in Action**: https://github.com/0xPabloxx/ai-agents-in-action-cn
- **Related Project - Agentic Design Patterns**: https://github.com/ginobefun/agentic-design-patterns-cn
- **Image Index**: chapters/image_index.md
- **Progress Tracking**: README.md
