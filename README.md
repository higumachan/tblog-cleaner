# tblog-cleaner

This is a tool that makes it easy to delete a small amount of tensorboard logdir.

# Install

```bash
pip install git+https://github.com/higumachan/tblog-cleaner.git
```

# Usage

```
logs/
├── big_log
└── small_log
```

```
tblog-cleaner --logsdir logs --tag loss  
```

