import sys

try:
    import pandas as pd
except ModuleNotFoundError:
    print("❌ 还没安装 pandas。请先运行：pip3 install pandas")
    sys.exit(1)

def explore(path):
    df = pd.read_csv(path)
    print(f"已读取：{path}")
    print(f"规模：{df.shape[0]} 行 × {df.shape[1]} 列\n")

    print("=== 前 5 行 ===")
    print(df.head(5).to_string(index=False))

    print("\n=== 各列类型与缺失值 ===")
    for col in df.columns:
        print(f"  {col:8s} 类型={str(df[col].dtype):8s} 缺失={int(df[col].isnull().sum())}")

    print("\n=== 数值列基本统计 ===")
    print(df.describe().to_string())

if __name__ == "__main__":
    # 默认读同目录下的 sample.csv；也可传参：python explore.py 你的文件.csv
    path = sys.argv[1] if len(sys.argv) > 1 else "sample.csv"
    try:
        explore(path)
    except FileNotFoundError:
        print(f"❌ 找不到文件：{path}")
        print("请确认：")
        print("  1) 在 explore.py / sample.csv 所在目录运行此程序；")
        print("  2) 文件名拼写正确；")
        print("  或指定完整路径，例如：python3 explore.py /Users/你的用户名/Desktop/sample.csv")
