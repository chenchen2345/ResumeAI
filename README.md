# ResumeAI

ResumeAI is a Multi-Agent system for generating resumes, featuring resume modification assessment, resume generation, and job advice.

## Features

1. **Resume Modification Assessment**: Determines if the resume needs modification based on user input.
2. **Resume Generation**: Fills resume information into a LaTex template to generate a standard format resume.
3. **Job Advice**: Provides few-shot job recommendations by scraping job information.

## Project Structure

```
ResumeAI/
├── README.md
├── data/
│   ├── raw/                # 原始数据
│   ├── processed/          # 处理后的数据
├── docs/                   # 文档
│   ├── api/                # API 文档
│   ├── user_guide/         # 用户指南
├── src/                    # 源代码
│   ├── agents/             # 各种智能体
│   │   ├── resume_assessment_agent.py
│   │   ├── resume_generation_agent.py
│   │   ├── job_advice_agent.py
│   ├── utils/              # 工具函数
│   │   ├── data_processing.py
│   │   ├── latex_template.py
│   ├── main.py             # 主程序入口
├── tests/                  # 测试代码
│   ├── test_resume_assessment.py
│   ├── test_resume_generation.py
│   ├── test_job_advice.py
├── requirements.txt        # 依赖包列表
├── .gitignore              # Git 忽略文件
```