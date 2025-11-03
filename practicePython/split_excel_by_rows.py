"""按固定行数拆分 Excel 的实用脚本
用法示例（在 PowerShell）：
python split_excel_by_rows.py -i data.xlsx -n 1000 -o out_dir --format xlsx --keep-header

功能：
- 支持 xlsx/xls/csv 输入（会自动根据后缀选择读取方式）
- 每 n 行拆分为一个文件，支持保留表头
- 支持输出为 xlsx 或 csv
- 输出文件会按序号命名：basename_part_1.xlsx
"""
import os
import argparse
import math
import pandas as pd


def split_excel(input_path: str, rows_per_file: int, out_dir: str, out_format: str = 'xlsx', keep_header: bool = True):
    """将输入表格按固定行数拆分并写出多个文件。

    输入：
      input_path: 输入文件路径（支持 .xlsx/.xls/.csv）
      rows_per_file: 每个输出文件包含的数据行数（不计表头）
      out_dir: 输出目录（会自动创建）
      out_format: 'xlsx' 或 'csv'
      keep_header: 是否在每个输出文件中保留表头
    """
    if rows_per_file <= 0:
        raise ValueError('rows_per_file must be > 0')

    os.makedirs(out_dir, exist_ok=True)

    # 读取文件
    ext = os.path.splitext(input_path)[1].lower()
    if ext in ('.xlsx', '.xls'):
        df = pd.read_excel(input_path)
    elif ext == '.csv':
        df = pd.read_csv(input_path)
    else:
        raise ValueError('Unsupported input file type: ' + ext)

    total_rows = len(df)
    if total_rows == 0:
        print('Input file has no rows. Nothing to do.')
        return []

    parts = math.ceil(total_rows / rows_per_file)
    base = os.path.splitext(os.path.basename(input_path))[0]
    out_paths = []

    for i in range(parts):
        start = i * rows_per_file
        end = min(start + rows_per_file, total_rows)
        chunk = df.iloc[start:end]
        if keep_header:
            out_df = chunk
        else:
            # If not keeping header, write without header when saving
            out_df = chunk

        out_name = f"{base}_part_{i+1}.{out_format}"
        out_path = os.path.join(out_dir, out_name)
        if out_format == 'xlsx':
            # 使用 index=False 通常更直观
            out_df.to_excel(out_path, index=False)
        elif out_format == 'csv':
            out_df.to_csv(out_path, index=False)
        else:
            raise ValueError('Unsupported output format: ' + out_format)
        out_paths.append(out_path)
        print(f'Wrote {out_path} with rows {start}..{end-1}')

    return out_paths


def main():
    parser = argparse.ArgumentParser(description='Split Excel/CSV into multiple files by row count')
    parser.add_argument('-i', '--input', required=True, help='Input Excel/CSV file')
    parser.add_argument('-n', '--rows', required=True, type=int, help='Rows per output file')
    parser.add_argument('-o', '--outdir', default='out', help='Output directory')
    parser.add_argument('-f', '--format', default='xlsx', choices=['xlsx', 'csv'], help='Output format')
    parser.add_argument('--no-header', action='store_true', help="Don't write header to each output file")

    args = parser.parse_args()
    keep_header = not args.no_header

    paths = split_excel(args.input, args.rows, args.outdir, args.format, keep_header)
    print('\nDone. Created files:')
    for p in paths:
        print(' -', p)


if __name__ == '__main__':
    main()
