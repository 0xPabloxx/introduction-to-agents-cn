#!/usr/bin/env python3
"""
Introduction to Agents - PDF 文本和图片提取工具
提取文本内容和图片，并记录图片位置
"""

import os
import sys
from pathlib import Path
import re

try:
    import pymupdf
except ImportError:
    print("错误: 需要安装 PyMuPDF")
    print("请运行: pip install pymupdf")
    sys.exit(1)


def extract_chapters_with_images(pdf_path, output_dir, images_dir):
    """提取章节文本和图片，记录图片位置"""

    doc = pymupdf.open(pdf_path)
    toc = doc.get_toc()

    print(f"PDF 文件: {pdf_path}")
    print(f"总页数: {len(doc)}")
    print(f"TOC 条目数: {len(toc)}\n")

    if not toc:
        print("警告: PDF 没有目录信息，将处理全部页面...")
        chapters = [{'title': 'Full Document', 'start_page': 1, 'end_page': len(doc), 'level': 1}]
    else:
        chapters = []
        for i, (level, title, page_num) in enumerate(toc):
            if level == 1 or re.search(r'chapter\s+\d+', title, re.IGNORECASE):
                end_page = len(doc)
                for j in range(i + 1, len(toc)):
                    next_level, next_title, next_page = toc[j]
                    if next_level <= level:
                        end_page = next_page - 1
                        break

                chapters.append({
                    'title': title.strip(),
                    'start_page': page_num,
                    'end_page': end_page,
                    'level': level
                })
                print(f"发现章节: {title} (页 {page_num}-{end_page})")

    # 确保输出目录存在
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    Path(images_dir).mkdir(parents=True, exist_ok=True)

    # 提取每个章节
    chapter_data = []
    image_counter = 1

    for idx, chapter in enumerate(chapters):
        print(f"\n提取章节 {idx + 1}/{len(chapters)}: {chapter['title']}")

        content_parts = []
        chapter_images = []

        for page_num in range(chapter['start_page'] - 1, min(chapter['end_page'], len(doc))):
            page = doc[page_num]

            # 提取文本
            text = page.get_text()

            # 提取图片
            image_list = page.get_images()

            if image_list:
                print(f"  页 {page_num + 1}: 发现 {len(image_list)} 个图片")

                for img_index, img in enumerate(image_list):
                    xref = img[0]

                    try:
                        # 提取图片
                        base_image = doc.extract_image(xref)
                        image_bytes = base_image["image"]
                        image_ext = base_image["ext"]

                        # 保存图片
                        image_filename = f"image_{image_counter:03d}_page_{page_num + 1}_{img_index + 1}.{image_ext}"
                        image_path = Path(images_dir) / image_filename

                        with open(image_path, "wb") as img_file:
                            img_file.write(image_bytes)

                        # 记录图片信息
                        chapter_images.append({
                            'filename': image_filename,
                            'page': page_num + 1,
                            'position_in_chapter': len(content_parts)
                        })

                        # 在文本中标记图片位置
                        text = text + f"\n\n[IMAGE_{image_counter}: {image_filename} - 位于第 {page_num + 1} 页]\n\n"

                        image_counter += 1

                    except Exception as e:
                        print(f"  警告: 无法提取图片 {xref}: {e}")

            content_parts.append(text)

            if (page_num + 1) % 10 == 0:
                print(f"  已处理 {page_num + 1 - (chapter['start_page'] - 1)} 页...")

        chapter_data.append({
            'number': idx + 1,
            'title': chapter['title'],
            'start_page': chapter['start_page'],
            'end_page': chapter['end_page'],
            'content': '\n'.join(content_parts),
            'images': chapter_images
        })

    doc.close()
    return chapter_data


def save_chapters(chapters, output_dir):
    """保存章节到文件"""
    output_path = Path(output_dir)

    print(f"\n{'='*80}")
    print(f"共提取 {len(chapters)} 个章节")
    print(f"保存到: {output_dir}")
    print(f"{'='*80}\n")

    # 保存图片索引文件
    image_index_path = output_path / "image_index.md"
    with open(image_index_path, 'w', encoding='utf-8') as f:
        f.write("# Introduction to Agents - 图片索引\n\n")

        for chapter in chapters:
            if chapter['images']:
                f.write(f"\n## {chapter['title']}\n\n")
                for img in chapter['images']:
                    f.write(f"- **{img['filename']}**\n")
                    f.write(f"  - 页码: {img['page']}\n")
                    f.write(f"  - 章节位置: 第 {img['position_in_chapter']} 部分\n\n")

    print(f"✓ 图片索引已保存: {image_index_path}\n")

    # 保存每个章节
    for chapter in chapters:
        safe_title = re.sub(r'[^\w\s-]', '', chapter['title'])
        safe_title = re.sub(r'\s+', '_', safe_title)[:80]

        filename = f"chapter{chapter['number']:02d}_{safe_title}.txt"
        filepath = output_path / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"{'='*80}\n")
            f.write(f"{chapter['title']}\n")
            f.write(f"{'='*80}\n")
            f.write(f"页码: {chapter['start_page']} - {chapter['end_page']}\n")
            f.write(f"图片数量: {len(chapter['images'])}\n")
            f.write(f"{'='*80}\n\n")
            f.write(chapter['content'])

        word_count = len(chapter['content'].split())
        image_count = len(chapter['images'])
        print(f"✓ {filename}")
        print(f"  页数: {chapter['end_page'] - chapter['start_page'] + 1}, "
              f"字符: {len(chapter['content'])}, "
              f"单词: {word_count}, "
              f"图片: {image_count}\n")


def main():
    # 设置路径
    base_dir = Path("/home/pablo/projects/translation/Introduction to agents")
    pdf_path = base_dir / "Introduction to Agents.pdf"
    output_dir = base_dir / "chapters"
    images_dir = base_dir / "images"

    if not pdf_path.exists():
        print(f"错误: 未找到 PDF 文件: {pdf_path}")
        return

    print(f"开始处理: {pdf_path}\n")

    try:
        # 提取章节和图片
        chapters = extract_chapters_with_images(pdf_path, output_dir, images_dir)

        if not chapters:
            print("\n未找到章节")
            return

        # 保存章节
        save_chapters(chapters, output_dir)

        total_images = sum(len(ch['images']) for ch in chapters)
        print(f"\n{'='*80}")
        print(f"✓ 提取完成!")
        print(f"  章节数: {len(chapters)}")
        print(f"  图片数: {total_images}")
        print(f"{'='*80}\n")

    except Exception as e:
        print(f"\n✗ 处理失败: {e}\n")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
