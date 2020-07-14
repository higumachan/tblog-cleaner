import shutil
from pathlib import Path

import click
from tbparser.summary_reader import SummaryReader
import argparse


def main():
    parser = argparse.ArgumentParser("tblog-cleaner", description="tblog-cleaner is removing small tensorboard logs.")
    parser.add_argument("--logsdir", default="logs", help="Directory of tensorboard log dirs")
    parser.add_argument("--tag", default="loss", help="check scalar name")
    parser.add_argument("--threshold", default=10)
    parser.add_argument("-f", dest="force", action="store_true", help="force mode. Do not check when a logdir is removed")
    args = parser.parse_args()

    logs_dir = Path(args.logsdir)
    for log_dir in logs_dir.glob("*"):
        if not log_dir.is_dir():
            continue
        reader = SummaryReader(str(log_dir), tag_filter=[args.tag])
        entries = [it for it in reader]
        if len(entries) < args.threshold:
            if args.force or click.confirm(f"Do you want to remove {log_dir}({len(entries)} entries)"):
                print(f"remove {log_dir}")
                shutil.rmtree(log_dir)


if __name__ == '__main__':
    main()
