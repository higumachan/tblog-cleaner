import shutil
from pathlib import Path

import click
from tbparser.summary_reader import SummaryReader
import argparse


def list_log_dir(logs_dir: Path):
    return [log_dir for log_dir in logs_dir.glob("*") if log_dir.is_dir()]


def log_entries(log_dir: Path, tag: str):
    reader = SummaryReader(str(log_dir), tag_filter=[tag])
    entries = [it for it in reader]
    return entries


def is_all_logs_empty(logs_dir: Path, tag: str):
    return all([log_entries(log_dir, tag) == 0 for log_dir in list_log_dir(logs_dir)])


def check_and_remove_logs(logs_dir: Path, threshold: int, tag: str, force: bool):
    for log_dir in logs_dir.glob("*"):
        if not log_dir.is_dir():
            continue
        reader = SummaryReader(str(log_dir), tag_filter=[tag])
        entries = [it for it in reader]
        if len(entries) < threshold:
            if force or click.confirm(f"Do you want to remove {log_dir}({len(entries)} entries)"):
                print(f"remove {log_dir}")
                shutil.rmtree(log_dir)

def main():
    parser = argparse.ArgumentParser("tblog-cleaner", description="tblog-cleaner is removing small tensorboard logs.")
    parser.add_argument("--logsdir", default="logs", help="Directory of tensorboard log dirs")
    parser.add_argument("--tag", default="loss", help="check scalar name")
    parser.add_argument("--threshold", default=10)
    parser.add_argument("-f", dest="force", action="store_true", help="force mode. Do not check when a logdir is removed")
    args = parser.parse_args()

    logs_dir = Path(args.logsdir)

    if is_all_logs_empty(logs_dir, args.tag):
        print(f"all logs are empty. please check tag setting \"{args.tag}\"")

    check_and_remove_logs(logs_dir, args.threshold, args.tag, args.force)


if __name__ == '__main__':
    main()
