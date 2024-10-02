import os
import subprocess

def generate_resume(user_info, template_path, output_path):
    """
    根据用户信息填充LaTeX模板并生成PDF文件。

    :param user_info: 用户信息列表
    :param template_path: LaTeX模板路径
    :param output_path: 输出PDF文件路径
    """
    # 解析用户信息
    personal_info = user_info[0]
    education_info = user_info[1]
    work_experience = user_info[2]
    projects = user_info[3]
    skills = user_info[4]

    # 读取LaTeX模板
    with open(template_path, 'r', encoding='utf-8') as file:
        template = file.read()

    # 填充个人信息
    template = template.replace("{{name}}", personal_info["name"])
    template = template.replace("{{age}}", str(personal_info["age"]))
    template = template.replace("{{gender}}", personal_info["gender"])
    template = template.replace("{{phone_number}}", personal_info["phone_number"])
    template = template.replace("{{email}}", personal_info["email"])

    # 填充教育背景
    education_str = "\n".join([f"\\makebox[0.25\\textwidth][l]{{\\textbf{{{edu['school']}}}}} \\makebox[0.25\\textwidth][l]{{{edu['major']}}} \\makebox[0.25\\textwidth][l]{{{edu['education']}}} \\makebox[0.22\\textwidth][r]{{{edu['education_time']}}} \n" for edu in education_info])
    template = template.replace("{{education}}", education_str)

    # 填充工作经历
    work_experience_str = "\n".join([f"\\item \\textbf{{{exp['company']}}} \\quad {exp['title']} \\quad {exp['time']} \n\\begin{{itemize}}[leftmargin=*]\n" + "\n".join([f"\\item {detail}" for detail in exp['details']]) + "\n\\end{itemize}" for exp in work_experience])
    template = template.replace("{{work_experience}}", work_experience_str)

    # 填充项目经历
    projects_str = "\n".join([f"\\item \\textbf{{{proj['name']}}} \\quad {proj['time']} \n\\begin{{itemize}}[leftmargin=*]\n" + "\n".join([f"\\item {detail}" for detail in proj['details']]) + "\n\\end{itemize}" for proj in projects])
    template = template.replace("{{projects}}", projects_str)

    # 填充技能
    skills_str = "\n".join([f"\\item {skill}" for skill in skills])
    template = template.replace("{{skills}}", skills_str)

    # 将填充后的内容写入临时文件
    temp_tex_path = "temp_resume.tex"
    with open(temp_tex_path, 'w', encoding='utf-8') as file:
        file.write(template)

    # 使用xelatex编译LaTeX文件生成PDF
    try:
        subprocess.run(["xelatex", temp_tex_path], check=True)
        # 移动生成的PDF文件到指定输出路径
        os.rename("temp_resume.pdf", output_path)
    except subprocess.CalledProcessError as e:
        print(f"Error compiling LaTeX: {e}")
    except FileNotFoundError as e:
        print(f"xelatex not found: {e}")
    finally:
        # 清理临时文件
        if os.path.exists(temp_tex_path):
            os.remove(temp_tex_path)
        if os.path.exists("temp_resume.aux"):
            os.remove("temp_resume.aux")
        if os.path.exists("temp_resume.log"):
            os.remove("temp_resume.log")

# 示例用法
if __name__ == "__main__":
    user_info = [
        {"name": "Cris", "age": 22, "gender": "男", "phone_number": "66667777", "email": "ilovenlp@qq.com"},
        [
            {"school": "香港大学", "major": "计算机科学", "education": "硕士", "education_time": "2024.09 - 2025.12"},
            {"school": "清华大学", "major": "软件工程", "education": "学士", "education_time": "2020.09 - 2024.06"}
        ],
        [
            {"company": "阿里巴巴", "title": "Java开发工程师", "time": "2018.07 - 2020.06", "details": ["负责后端开发", "参与系统设计"]},
            {"company": "华为", "title": "数据分析师", "time": "2020.07 - 2022.06", "details": ["负责数据清洗和建模", "进行数据分析"]}
        ],
        [
            {"name": "电子商务平台开发", "time": "2019.01 - 2019.12", "details": ["使用Java进行后端开发", "设计数据库"]},
            {"name": "数据分析项目", "time": "2021.01 - 2021.12", "details": ["使用Python进行数据处理和建模", "生成分析报告"]}
        ],
        ["Java", "Python", "数据分析"]
    ]
    template_path = os.path.join(os.path.dirname(__file__), "../../templates/latex_template.tex")
    output_path = os.path.join(os.path.dirname(__file__), "../../output/output_resume.pdf")
    generate_resume(user_info, template_path, output_path)